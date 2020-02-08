import getopt
import sys
import re


__ERROR_ARGUMENT = 2
__SUCCESSFUL = 1


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


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hf:Ho:c:F:", ["help="])
    except getopt.GetoptError:
        print("demo_parse.py -f <file_name>")
        sys.exit(__ERROR_ARGUMENT)
    print(opts)
    csv_opt = dict()
    csv_opt["head"] = 1
    csv_opt["column_regex"] = list()
    csv_opt["filter_regex"] = list()
    csv_opt["check_filter"] = False
    csv_opt["check_write"] = False
    for opt, arg in opts:
        if opt == ('-h', "--help"):
            print('demo_getopt.py.py -f | --file <input_file>')
            print('demo_getopt.py.py -h | -- help')
            sys.exit(__SUCCESSFUL)
        elif opt in ("-f"):
            csv_opt["file"] = arg
        elif opt in ("-H"):
            csv_opt["head"] = 0
        elif opt in ("-o"):
            csv_opt["output_file"] = arg
            csv_opt["check_write"] = True
        elif opt in ("-c"):
            csv_opt["column_regex"].append(arg)
            csv_opt["check_filter"] = True
        elif opt in ("-F"):
            csv_opt["filter_regex"].append(arg)

    csv_head, csv_body = read_CSV(csv_opt["file"], csv_opt["head"])
    if csv_opt["check_filter"]:
        filter_csv(csv_body, csv_opt["column_regex"], csv_opt["filter_regex"])
    print(*csv_head, sep="\n")
    print(*csv_body, sep="\n")
    if csv_opt["check_write"]:
        write_csv(csv_opt["output_file"], csv_head, csv_body)


if __name__ == "__main__":
    main(sys.argv[1:])
