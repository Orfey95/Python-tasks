"""CSV reader
This script allows the user to work with csv, tsv and dsv files.
List Function:
Help - you can get help about the program;
Read file - you can read file;
Filter by row - you can specify the ranges of rows with which you want to work;
Filter by column - you can specify the ranges of columns with which you want to work;
Filter by pattern - you can specify the column number and the pattern by which the rows will be filtered;
Work with the header - you can choose whether the header is in the file or not;
Export to json - you can export to json file.
"""

import getopt
import json
import sys
import re
import os.path


__ERROR_FILE = 3  # problem with filename
__ERROR_ARGUMENT = 2  # problem with arguments
__SUCCESSFUL = 0  # OK
__COL_NUMBERS = 12  # number of columns of csv file


def read_csv(file_name, f_head, delimiter):
    """Function to read csv file
    :param file_name: str
        The name of csv, tsv and dsv files
    :param f_head: bool
        The pointer that indicates whether there is a header in the file
    :param delimiter: str
        The file delimiter
    :return: list, list
        Return header and body of file
    """
    csv_head = list()
    csv_body = list()
    start_element_of_list_app = list()
    end_element_of_list_app = list()
    with open(file_name, "r") as record:
        if f_head:
            csv_head.append(record.readline().replace("\n", "").split(delimiter))
        for line in record:
            while True:
                if len(line.split(delimiter)) < __COL_NUMBERS:
                    line = str(line).replace("\n", "") + next(record).replace("\n", "")
                else:
                    break
            csv_body.append(line.replace("\n", "").split(delimiter))

    # Convert list of apps to list element
    for x in csv_body:
        start_element_of_list_app.append([i for i, word in enumerate(x) if not word.startswith('""') and word.startswith('"')])
        end_element_of_list_app.append([i for i, word in enumerate(x) if not word.endswith('""') and word.endswith('"')])
    for x in range(len(csv_body)):
        csv_body[x][int(start_element_of_list_app[x][0]): int(end_element_of_list_app[x][0]) + 1] = [
            delimiter.join(csv_body[x][int(start_element_of_list_app[x][0]): int(end_element_of_list_app[x][0]) + 1])]
    return csv_head, csv_body


def write_csv(out_file, csv_head, csv_body, f_head, delimiter):
    """Function to write to file
    :param out_file: str
        The name of file to write
    :param csv_head: list
        The header of file
    :param csv_body: list
        The body of file
    :param f_head: bool
        The pointer that indicates whether there is a header in the file
    :param delimiter: str
        The file delimiter
    :return: 0
    """
    dict_of_csv = dict()
    temp_list = []
    list_of_dict_of_csv = list()
    if str(out_file).split(".")[1] == 'json' and not f_head:
        for x in range(len(csv_body[0])):
            temp_list.append('Column' + str(x))
        csv_head.append(temp_list)
    if str(out_file).split(".")[1] == 'json':
        for x in range(len(csv_body)):
            for y in range(len(csv_head[0])):
                dict_of_csv[csv_head[0][y]] = csv_body[x][y]
            list_of_dict_of_csv.append(dict_of_csv)
            dict_of_csv = {}
        with open(out_file, 'w') as fp:
            json.dump(list_of_dict_of_csv, fp)
    else:
        with open(out_file, "w") as out:
            for rec in csv_head:
                out.writelines(delimiter.join(rec) + '\n')
            for rec in csv_body:
                out.writelines(delimiter.join(rec) + '\n')


def filter_csv(csv_body, column_regex, filter_regex):
    """Function to filter csv file by regex
    :param csv_body: list
        The body of file
    :param column_regex: list
        The list of columns for filter
    :param filter_regex: list
        The list of regex for columns
    :return: 0
    """
    regex_list = list()
    for regex_element in filter_regex:
        regex_list.append(str(regex_element).replace("*", ".+?"))
    for x in range(len(regex_list)):
        for csv_body_element in csv_body[:]:
            if not re.match(regex_list[x], csv_body_element[int(column_regex[x])]):
                csv_body.remove(csv_body_element)


def range_rows(csv_body, range_rows):
    """Function to filter csv by row range
    :param csv_body: list
        The body of file
    :param range_rows: list
        The list of rows for filter
    :return: 0
    """
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
    """Function to filter csv by column range
    :param csv_head: list
        The header of file
    :param csv_body: list
        The body of file
    :param range_columns: list
        The list of columns for filter
    :param f_head: bool
        The pointer that indicates whether there is a header in the file
    :return: 0
    """
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
    """Function of help
    :return: 0
    """
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
    """Function for processing script parameters
    :param argv: list
        Arguments of script
    :return: 0
    """
    try:
        opts, args = getopt.getopt(argv, "hf:Ho:c:F:r:C:d:", ["help", "file=", "head", "out=", "column=",
                                                              "filter=", "row_range=", "column_range=", "delimiter="])
    except getopt.GetoptError:
        print("An error occurred while specifying program parameters. "
              "To specify the correctness, specify the -h or --help option")
        sys.exit(__ERROR_ARGUMENT)
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
        if os.path.isfile(csv_opt["file"]):
            csv_head, csv_body = read_csv(csv_opt["file"], csv_opt["head"], csv_opt["delimiter"])
        else:
            print("The specified file does not exist.")
            sys.exit(__ERROR_FILE)
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
