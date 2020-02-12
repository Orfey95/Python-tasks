### Help:
```
C:\Users\Oleksandr_Frolov\PycharmProjects\Task5\venv\Scripts\python.exe C:/Users/Oleksandr_Frolov/PycharmProjects/Task5/Task5_csv_mode.py -h
DESCRIPTION
	A program for filtering csv files.

	-f, --file <input_file> 
		 specifying the path to the csv file
	-d, --delimiter <delimiter> 
		 specifying the column delimiter, example: -d ","
	-h, --help 
		 get help about the program
	-H, --head 
		 specify this parameter if the csv file contains a header
	-c, --col <col_number> 
		 specify the column number to which you want to apply a filter
	-F, --filter <filter_regex> 
		 specify a filtering rule, example: -F *KH*
	-o, --out <output_file> 
		 specify the path where the csv file will be written
	-r, --row_range <range> 
		 specify the range of rows you need, example: -r 1-3
	-C, --column_range <range> 
		 specify the range of columns you need, example: -C 1-3

	The -c and -F options work only together, and cannot be alone.
	The -f and -d options work only together, and cannot be alone.

  Exit status:
	0	-	if OK,
	1	-	if critical error,
	2	-	if problem with arguments.

AUTHOR
	Written by Oleksandr Frolov.

```
