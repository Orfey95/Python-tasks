import getopt
import sys
import re


__ERROR_ARGUMENT = 2
__SUCCESSFUL = 0
__COL_NUMBERS = 12  # number of columns of csv file


def get_delimiter(file_name, f_head):
    file = open(file_name)
    line = file.readlines()
    if f_head:
        delimiter = re.findall(r'[0-9a-f]{2}(?::[0-9a-f]{2}){5}(.1?)', line[1])
    else:
        delimiter = re.findall(r'[0-9a-f]{2}(?::[0-9a-f]{2}){5}(.1?)', line[0])
    return delimiter[0]


def read_CSV(file_name, f_head):
    csv_head = list()
    csv_body = list()
    start_element_of_list_app = list()
    end_element_of_list_app = list()
    with open(file_name, "r") as record:
        if f_head:
            csv_head.append(record.readline().replace("\n", "").split(get_delimiter(file_name, f_head)))
        for line in record:
            while True:
                if len(line.split(get_delimiter(file_name, f_head))) < __COL_NUMBERS:
                    line = str(line).replace("\n", "") + next(record).replace("\n", "")
                else:
                    break
            csv_body.append(line.replace("\n", "").split(get_delimiter(file_name, f_head)))
    # Convert list of apps to list element
    for x in csv_body:
        start_element_of_list_app.append([i for i, word in enumerate(x) if word.startswith('"')])
        end_element_of_list_app.append([i for i, word in enumerate(x) if word.endswith('"')])
    for x in range(len(csv_body)):
        csv_body[x][int(start_element_of_list_app[x][0]): int(end_element_of_list_app[x][0]) + 1] = [
            get_delimiter(file_name, f_head).join(csv_body[x][int(start_element_of_list_app[x][0]): int(end_element_of_list_app[x][0]) + 1])]
    return csv_head, csv_body


def write_csv(out_file, csv_head, csv_body):
    with open(out_file, "w") as out:
        for rec in csv_head:
            out.writelines(",".join(rec))
        for rec in csv_body:
            out.writelines(",".join(rec))


def filter_csv(csv_body, column_regex, filter_regex):
    regex_list = list()
    for regex_element in filter_regex:
        regex_list.append(str(regex_element).replace("*", ".+?"))
    for x in range(len(regex_list)):
        for csv_body_element in csv_body[:]:
            if not re.match(regex_list[x], csv_body_element[int(column_regex[x])]):
                csv_body.remove(csv_body_element)


def range_rows(csv_body, range_rows):
    matching_rows = list()
    for range_rows_element in range_rows:
        start_number = int(str(range_rows_element).split("-")[0])
        end_number = int(str(range_rows_element).split("-")[1])
        for x in range(start_number, end_number+1):
            matching_rows.append(x)
    for index, csv_body_element in enumerate(csv_body[:]):
        if index not in matching_rows:
            csv_body.remove(csv_body_element)


def range_columns(csv_head, csv_body, range_columns, f_head):
    matching_columns = list()
    for range_columns_element in range_columns:
        start_number = int(str(range_columns_element).split("-")[0])
        end_number = int(str(range_columns_element).split("-")[1])
        for x in range(start_number, end_number+1):
            matching_columns.append(x)
    for csv_body_element in csv_body[:]:
        del csv_body_element[matching_columns[0]:matching_columns[-1]+1]
    if f_head:
        del csv_head[0][matching_columns[0]:matching_columns[-1]]


def manual():
    print('DESCRIPTION')
    print('\tA program for filtering csv files.\n')
    print('\t-f, --file <input_file> \n\t\t specifying the path to the csv file')
    print('\t-h, --help \n\t\t get help about the program')
    print('\t-H, --head \n\t\t specify this parameter if the csv file contains a header')
    print('\t-c, --col <col_number> \n\t\t specify the column number to which you want to apply a filter')
    print('\t-F, --filter <filter_regex> \n\t\t specify a filtering rule, example: -F *KH*')
    print('\t-o, --out <output_file> \n\t\t specify the path where the csv file will be written')
    print('\t-r, --row_range <range> \n\t\t specify the range of rows you need, example: -r 1-3')
    print('\t-C, --column_range <range> \n\t\t specify the range of columns you need, example: -C 1-3')
    print('\n\tThe -c and -F options work only together, and cannot be alone.\n')
    print('  Exit status:')
    print('\t0\t-\tif OK,')
    print('\t1\t-\tif critical error,')
    print('\t2\t-\tif problem with arguments.')
    print('\nAUTHOR')
    print('\tWritten by Oleksandr Frolov.')


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hf:Ho:c:F:r:C:", ["help", "file=", "head", "out=", "col=", "filter=", "row_range=", "column_range="])
    except getopt.GetoptError:
        print("An error occurred while specifying program parameters. "
              "To specify the correctness, specify the -h or --help option")
        sys.exit(__ERROR_ARGUMENT)
    # print(opts)
    csv_opt = dict()
    csv_opt["head"] = True
    csv_opt["column_regex"] = list()
    csv_opt["filter_regex"] = list()
    csv_opt["range_rows"] = list()
    csv_opt["range_columns"] = list()
    csv_opt["check_filter"] = False
    csv_opt["check_read"] = False
    csv_opt["check_write"] = False
    csv_opt["check_range_row"] = False
    csv_opt["check_range_column"] = False
    for opt, arg in opts:
        if opt in ('-h', "--help"):
            manual()
            sys.exit(__SUCCESSFUL)
        elif opt in ("-f", "--file"):
            csv_opt["check_read"] = True
            csv_opt["file"] = arg
        elif opt in ("-H", "--head"):
            csv_opt["head"] = False
        elif opt in ("-o", "--out"):
            csv_opt["output_file"] = arg
            csv_opt["check_write"] = True
        elif opt in ("-c", "--col"):
            csv_opt["column_regex"].append(arg)
            csv_opt["check_filter"] = True
        elif opt in ("-F", "--filter"):
            csv_opt["filter_regex"].append(arg)
        elif opt in ("-r", "--row_range"):
            csv_opt["range_rows"].append(arg)
            csv_opt["check_range_row"] = True
        elif opt in ("-C", "--column_range"):
            csv_opt["range_columns"].append(arg)
            csv_opt["check_range_column"] = True

    if csv_opt["check_read"]:
        csv_head, csv_body = read_CSV(csv_opt["file"], csv_opt["head"])
    if csv_opt["check_range_row"]:
        range_rows(csv_body, csv_opt["range_rows"])
    if csv_opt["check_range_column"]:
        range_columns(csv_head, csv_body, csv_opt["range_columns"], csv_opt["head"])
    if csv_opt["check_filter"]:
        filter_csv(csv_body, csv_opt["column_regex"], csv_opt["filter_regex"])
    if csv_opt["check_read"]:
        print(*csv_head, sep="\n")
        print(*csv_body, sep="\n")
    if csv_opt["check_write"]:
        write_csv(csv_opt["output_file"], csv_head, csv_body)


if __name__ == "__main__":
    main(sys.argv[1:])
