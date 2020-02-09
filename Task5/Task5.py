import getopt
import sys
import re


__ERROR_ARGUMENT = 2
__SUCCESSFUL = 0


def read_CSV(file_name, f_head):
    csv_head = list()
    csv_body = list()
    start_element_of_list_app = list()
    end_element_of_list_app = list()
    with open(file_name, "r") as record:
        if f_head == 1:
            csv_head.append(record.readline().replace("\n", "").split(","))
        for line in record:
            csv_body.append(line.replace("\n", "").split(","))
    for x in csv_body:
        start_element_of_list_app.append([i for i, word in enumerate(x) if word.startswith('"')])
        end_element_of_list_app.append([i for i, word in enumerate(x) if word.endswith('"')])
    for x in range(len(csv_body)):
        csv_body[x][int(start_element_of_list_app[x][0]): int(end_element_of_list_app[x][0]) + 1] = [
            ','.join(csv_body[x][int(start_element_of_list_app[x][0]): int(end_element_of_list_app[x][0]) + 1])]
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


def manual():
    print('DESCRIPTION')
    print('\tA program for filtering csv files.\n')
    print('\t-f, --file <input_file> \n\t specifying the path to the csv file')
    print('\t-h, --help \n\t get help about the program')
    print('\t-H, --head \n\t specify this parameter if the csv file contains a header')
    print('\t-c, --col <col_number> \n\t specify the column number to which you want to apply a filter')
    print('\t-F, --filter <filter_regex> \n\t specify a filtering rule, example: *KH*')
    print('\t-o, --out <output_file> \n\t specify the path where the csv file will be written')
    print('\n\tThe -c and -F options work only together, and cannot be alone.\n')
    print('  Exit status:')
    print('\t0\t-\tif OK,')
    print('\t1\t-\tif critical error,')
    print('\t2\t-\tif problem with arguments.')
    print('\nAUTHOR')
    print('\tWritten by Oleksandr Frolov.')


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hf:Ho:c:F:", ["help", "file=", "head", "out=", "col=", "filter="])
    except getopt.GetoptError:
        print("An error occurred while specifying program parameters. "
              "To specify the correctness, specify the -h or --help option")
        sys.exit(__ERROR_ARGUMENT)
    print(opts)
    csv_opt = dict()
    csv_opt["head"] = 1
    csv_opt["column_regex"] = list()
    csv_opt["filter_regex"] = list()
    csv_opt["check_filter"] = False
    csv_opt["check_read"] = False
    csv_opt["check_write"] = False
    for opt, arg in opts:
        if opt in ('-h', "--help"):
            manual()
            sys.exit(__SUCCESSFUL)
        elif opt in ("-f", "--file"):
            csv_opt["check_read"] = True
            csv_opt["file"] = arg
        elif opt in ("-H", "--head"):
            csv_opt["head"] = 0
        elif opt in ("-o", "--out"):
            csv_opt["output_file"] = arg
            csv_opt["check_write"] = True
        elif opt in ("-c", "--col"):
            csv_opt["column_regex"].append(arg)
            csv_opt["check_filter"] = True
        elif opt in ("-F", "--filter"):
            csv_opt["filter_regex"].append(arg)

    if csv_opt["check_read"]:
        csv_head, csv_body = read_CSV(csv_opt["file"], csv_opt["head"])
    if csv_opt["check_filter"]:
        filter_csv(csv_body, csv_opt["column_regex"], csv_opt["filter_regex"])
    if csv_opt["check_read"] or csv_opt["check_filter"]:
        print(*csv_head, sep="\n")
        print(*csv_body, sep="\n")
    if csv_opt["check_write"]:
        write_csv(csv_opt["output_file"], csv_head, csv_body)


if __name__ == "__main__":
    main(sys.argv[1:])
