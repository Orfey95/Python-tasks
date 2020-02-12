import getopt
import json
import sys
import re
import csv


__ERROR_ARGUMENT = 2
__SUCCESSFUL = 0
__COL_NUMBERS = 12  # number of columns of csv file


def read_CSV(file_name, f_head, delimiter):
    csv_head = list()
    csv_body = list()
    with open(file_name, 'r') as read_obj:
        csv_reader = csv.reader(read_obj, delimiter=delimiter)
        if f_head:
            csv_head.append(next(csv_reader))
        for row in csv_reader:
            csv_body.append(row)
    return csv_head, csv_body


def write_csv(out_file, csv_head, csv_body, f_head, delimiter):
    dict_of_csv = dict()
    list_of_dict_of_csv = list()
    if str(out_file).split(".")[1] == 'json' and not f_head:
        csv_head = [['Column1', 'Column2', 'Column3', 'Column4', 'Column5', 'Column6', 'Column7', 'Column8',
                     'Column9', 'Column10', 'Column11', 'Column12']]
    if str(out_file).split(".")[1] == 'json':
        for x in range(len(csv_body)):
            for y in range(__COL_NUMBERS):
                dict_of_csv[csv_head[0][y]] = csv_body[x][y]
            list_of_dict_of_csv.append(dict_of_csv)
            dict_of_csv = {}
        with open(out_file, 'w') as fp:
            json.dump(list_of_dict_of_csv, fp)
    else:
        with open(out_file, 'w', newline='') as write_obj:
            csv_writer = csv.writer(write_obj, delimiter=delimiter)
            csv_writer.writerow(csv_head[0])
            for csv_body_element in csv_body:
                csv_writer.writerow(csv_body_element)


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
    if f_head:
        for csv_head_element in csv_head[:]:
            for index, csv_head_element_element in enumerate(csv_head_element[:]):
                if index not in matching_columns:
                    csv_head_element.remove(csv_head_element_element)
    for csv_body_element in csv_body[:]:
        for index, csv_body_element_element in enumerate(csv_body_element[:]):
            if index not in matching_columns:
                csv_body_element.remove(csv_body_element_element)


def manual():
    print('DESCRIPTION')
    print('\tA program for filtering csv files.\n')
    print('\t-f, --file <input_file> \n\t\t specifying the path to the csv file')
    print('\t-d, --delimiter <delimiter> \n\t\t specifying the column delimiter, example: -d ","')
    print('\t-h, --help \n\t\t get help about the program')
    print('\t-H, --head \n\t\t specify this parameter if the csv file contains a header')
    print('\t-c, --column <col_number> \n\t\t specify the column number to which you want to apply a filter')
    print('\t-F, --filter <filter_regex> \n\t\t specify a filtering rule, example: -F *KH*')
    print('\t-o, --out <output_file> \n\t\t specify the path where the csv file will be written')
    print('\t-r, --row_range <range> \n\t\t specify the range of rows you need, example: -r 1-3')
    print('\t-C, --column_range <range> \n\t\t specify the range of columns you need, example: -C 1-3')
    print('\n\tThe -c and -F options work only together, and cannot be alone.')
    print('\tThe -f and -d options work only together, and cannot be alone.\n')
    print('  Exit status:')
    print('\t0\t-\tif OK,')
    print('\t1\t-\tif critical error,')
    print('\t2\t-\tif problem with arguments.')
    print('\nAUTHOR')
    print('\tWritten by Oleksandr Frolov.')


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hf:Ho:c:F:r:C:d:", ["help", "file=", "head", "out=", "column=",
                                                              "filter=", "row_range=", "column_range=", "delimiter="])
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
    csv_opt["delimiter"] = str()
    csv_opt["check_filter"] = False
    csv_opt["check_read"] = False
    csv_opt["check_write"] = False
    csv_opt["check_range_row"] = False
    csv_opt["check_range_column"] = False
    csv_opt["check_delimiter"] = False
    csv_opt["check_filter"] = False
    csv_opt["check_col"] = False
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
        elif opt in ("-c", "--column"):
            csv_opt["column_regex"].append(arg)
            csv_opt["check_col"] = True
        elif opt in ("-F", "--filter"):
            csv_opt["filter_regex"].append(arg)
            csv_opt["check_filter"] = True
        elif opt in ("-r", "--row_range"):
            csv_opt["range_rows"].append(arg)
            csv_opt["check_range_row"] = True
        elif opt in ("-C", "--column_range"):
            csv_opt["range_columns"].append(arg)
            csv_opt["check_range_column"] = True
        elif opt in ("-d", "--delimiter"):
            csv_opt["delimiter"] = arg
            csv_opt["check_delimiter"] = True
    #  Check pair parameters
    if csv_opt["check_read"] and not csv_opt["check_delimiter"]:
        print("The -f and -d options work only together, and cannot be alone.")
        sys.exit(__ERROR_ARGUMENT)
    if not csv_opt["check_read"] and csv_opt["check_delimiter"]:
        print("The -f and -d options work only together, and cannot be alone.")
        sys.exit(__ERROR_ARGUMENT)
    if csv_opt["check_filter"] and not csv_opt["check_col"]:
        print("The -c and -F options work only together, and cannot be alone.")
        sys.exit(__ERROR_ARGUMENT)
    if not csv_opt["check_filter"] and csv_opt["check_col"]:
        print("The -c and -F options work only together, and cannot be alone.")
        sys.exit(__ERROR_ARGUMENT)
    ########
    if csv_opt["check_read"]:
        csv_head, csv_body = read_CSV(csv_opt["file"], csv_opt["head"], csv_opt["delimiter"])
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
        write_csv(csv_opt["output_file"], csv_head, csv_body, csv_opt["head"], csv_opt["delimiter"])


if __name__ == "__main__":
    main(sys.argv[1:])
