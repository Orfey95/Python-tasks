### List Function:
1) Help - you can get help about the program;
2) Filter by row - you can specify the ranges of rows with which you want to work;
3) Filter by column - you can specify the ranges of columns with which you want to work;
4) Filter by pattern - you can specify the column number and the pattern by which the rows will be filtered;
5) Work with the header - you can choose whether the header is in the file or not.
## Help:
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
	-c, --column <col_number> 
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
