### List Function:
1) Help - you can get help about the program;
2) Read file - you can read file;
3) Filter by row - you can specify the ranges of rows with which you want to work;
4) Filter by column - you can specify the ranges of columns with which you want to work;
5) Filter by pattern - you can specify the column number and the pattern by which the rows will be filtered;
6) Work with the header - you can choose whether the header is in the file or not;
7) Export to json - you can export to json file.
## Function ONE - Help:
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
## Function TWO - Read file:
```
C:\Users\Oleksandr_Frolov\PycharmProjects\Task5\venv\Scripts\python.exe C:/Users/Oleksandr_Frolov/PycharmProjects/Task5/Task5.py -f log.csv -d ,
['MAC', 'hostname', 'IPv4', 'IPv6', 'netmask', 'login', 'full_user_name', 'email', 'ssh', 'description_host', 'installed_app', 'UUID']
['00:0a:95:9d:68:12', 'EPUAKHAW011D', '255.255.254.0', '0:0:0:0:0:ffff:c0a8:32', '255.255.255.0', 'Oleksandr_Frolov', 'Oleksandr Frolov', 'Oleksandr_Frolov@epam.com', 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDMFY85GBlB1boQSJ5Sp+a36QUlEtqFIVryz+328ELMhQcdPbg9G7aUH+v1t9EH1PLAmyYCauzOp7I5HFjceFMuisbbxotFuePnbKsYH1/rBMe8yQyFq0BOstMCGdExXQpDGryDVIKTqy3/nRDuVKLPy3x7tTpiMXdVFeTqIOkU19ePihhTViUrLJnbeMmAVrLPqOHz9LLpSPGZ5nljOlv4W0CSNtBT9yOsRAaWAU9ipz+20yfYz6MjbFjneSHpYXgHlW/gxgNJReQYRbJgRobKTvt5oUTKkpmYvBtyDxagLcUb6SCXxfZGhaSAEWCbEN9ETEFaJycVtSaxUG3SKAOBrd0+YxhAwiHjfRKgLPY2pzUK2F31HXY5yO3/9fSeTOmOkg2lHVEeEV0/XFk0yJdD8cnz7QEGQCFFJuZrKreJ76ubzWZggA64qoCsCq3Zm+bvMCIs2WZQukoTg3GqCFGIxwxeGR9T5LcGiV2tPffUtj1JIkohip2NfgIgAZ6UOOlXp66d9JubpoZzrKucdLQCnZlt7tss/RyHoMhal4Ojc6cnBtukoE434PD1Bh/P8doRcrsFYNPzbp5LoTZ9W4m8pY5CZI9Tzaduo5hx9sJ9745xWzl67VEqp8xsjGahUU1YiH0rJDcnpUwnEVNTjVOlXDkc4bNhcwXdIiT9udhG9w== Oleksandr_Frolov@EPUAKHAW013D', 'user-pc', '"Skype, Viber"', '48c1e088-48c1-11ea-b77f-2e728ce88125']
['00:0a:95:9d:68:13', 'EPUAKHAW012D', '192.168.0.50', '0:0:0:0:0:ffff:c0a8:33', '255.255.128.0', 'Vasia_Pupkin', 'Vasia Pupkin', 'Vasia_Pupkin@epam.com', 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDMFY85GBlB1boQSJ5Sp+a36QUlEtqFIVryz+328ELMhQcdPbg9G7aUH+v1t9EH1PLAmyYCauzOp7I5HFjceFMuisbbxotFuePnbKsYH1/rBMe8yQyFq0BOstMCGdExXQpDGryDVIKTqy3/nRDuVKLPy3x7tTpiMXdVFeTqIOkU19ePihhTViUrLJnbeMmAVrLPqOHz9LLpSPGZ5nljOlv4W0CSNtBT9yOsRAaWAU9ipz+20yfYz6MjbFjneSHpYXgHlW/gxgNJReQYRbJgRobKTvt5oUTKkpmYvBtyDxagLcUb6SCXxfZGhaSAEWCbEN9ETEFaJycVtSaxUG3SKAOBrd0+YxhAwiHjfRKgLPY2pzUK2F31HXY5yO3/9fSeTOmOkg2lHVEeEV0/XFk0yJdD8cnz7QEGQCFFJuZrKreJ76ubzWZggA64qoCsCq3Zm+bvMCIs2WZQukoTg3GqCFGIxwxeGR9T5LcGiV2tPffUtj1JIkohip2NfgIgAZ6UOOlXp66d9JubpoZzrKucdLQCnZlt7tss/RyHoMhal4Ojc6cnBtukoE434PD1Bh/P8doRcrsFYNPzbp5LoTZ9W4m8pY5CZI9Tzaduo5hx9sJ9745xWzl67VEqp8xsjGahUU1YiH0rJDcnpUwnEVNTjVOlXDkc4bNhcwXdIiT9udhG9w== Vasia_Pupkin@EPUAKHAW013D', 'user-pc', '"Skype, PyCharm, Chrome"', '48c1e088-48c1-11ea-b77f-2e728ce88126']
['00:0a:95:9d:68:14', 'EPUAKHAW013D', '192.168.0.57', '0:0:0:0:0:ffff:c0a8:34', '255.255.0.0', 'Ivan_Ivanov', 'Ivan Ivanov', 'Ivan_Ivanov@epam.com', 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDMFY85GBlB1boQSJ5Sp+a36QUlEtqFIVryz+328ELMhQcdPbg9G7aUH+v1t9EH1PLAmyYCauzOp7I5HFjceFMuisbbxotFuePnbKsYH1/rBMe8yQyFq0BOstMCGdExXQpDGryDVIKTqy3/nRDuVKLPy3x7tTpiMXdVFeTqIOkU19ePihhTViUrLJnbeMmAVrLPqOHz9LLpSPGZ5nljOlv4W0CSNtBT9yOsRAaWAU9ipz+20yfYz6MjbFjneSHpYXgHlW/gxgNJReQYRbJgRobKTvt5oUTKkpmYvBtyDxagLcUb6SCXxfZGhaSAEWCbEN9ETEFaJycVtSaxUG3SKAOBrd0+YxhAwiHjfRKgLPY2pzUK2F31HXY5yO3/9fSeTOmOkg2lHVEeEV0/XFk0yJdD8cnz7QEGQCFFJuZrKreJ76ubzWZggA64qoCsCq3Zm+bvMCIs2WZQukoTg3GqCFGIxwxeGR9T5LcGiV2tPffUtj1JIkohip2NfgIgAZ6UOOlXp66d9JubpoZzrKucdLQCnZlt7tss/RyHoMhal4Ojc6cnBtukoE434PD1Bh/P8doRcrsFYNPzbp5LoTZ9W4m8pY5CZI9Tzaduo5hx9sJ9745xWzl67VEqp8xsjGahUU1YiH0rJDcnpUwnEVNTjVOlXDkc4bNhcwXdIiT9udhG9w== Ivan_Ivanov@EPUAKHAW013D', 'user-pc', '"Skype, Viber, Teams"', '48c1e088-48c1-11ea-b77f-2e728ce88127']
['00:0a:95:9d:68:15', 'EPUAKHAW014D', '192.168.0.54', '0:0:0:0:0:ffff:c0a8:35', '255.0.0.0', 'Daria_Pupkin', 'Daria Pupkin', 'Daria_Pupkin@epam.com', 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDMFY85GBlB1boQSJ5Sp+a36QUlEtqFIVryz+328ELMhQcdPbg9G7aUH+v1t9EH1PLAmyYCauzOp7I5HFjceFMuisbbxotFuePnbKsYH1/rBMe8yQyFq0BOstMCGdExXQpDGryDVIKTqy3/nRDuVKLPy3x7tTpiMXdVFeTqIOkU19ePihhTViUrLJnbeMmAVrLPqOHz9LLpSPGZ5nljOlv4W0CSNtBT9yOsRAaWAU9ipz+20yfYz6MjbFjneSHpYXgHlW/gxgNJReQYRbJgRobKTvt5oUTKkpmYvBtyDxagLcUb6SCXxfZGhaSAEWCbEN9ETEFaJycVtSaxUG3SKAOBrd0+YxhAwiHjfRKgLPY2pzUK2F31HXY5yO3/9fSeTOmOkg2lHVEeEV0/XFk0yJdD8cnz7QEGQCFFJuZrKreJ76ubzWZggA64qoCsCq3Zm+bvMCIs2WZQukoTg3GqCFGIxwxeGR9T5LcGiV2tPffUtj1JIkohip2NfgIgAZ6UOOlXp66d9JubpoZzrKucdLQCnZlt7tss/RyHoMhal4Ojc6cnBtukoE434PD1Bh/P8doRcrsFYNPzbp5LoTZ9W4m8pY5CZI9Tzaduo5hx9sJ9745xWzl67VEqp8xsjGahUU1YiH0rJDcnpUwnEVNTjVOlXDkc4bNhcwXdIiT9udhG9w== Daria_Pupkin@EPUAKHAW013D', 'user-pc', '"VirtualBox, Vagrant"', '48c1e088-48c1-11ea-b77f-2e728ce88128']
['1a:0a:95:9d:68:15', 'EPUADNAW010D', '74.42.5.54', '0:0:0:0:0:faff:c0a8:36', '255.128.0.0', 'Jacque_Fresco', 'Jacque Fresco', 'Jacque_Fresco@epam.com', 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDMFY85GBlB1boQSJ5Sp+a36QUlEtqFIVryz+328ELMhQcdPbg9G7aUH+v1t9EH1PLAmyYCauzOp7I5HFjceFMuisbbxotFuePnbKsYH1/rBMe8yQyFq0BOstMCGdExXQpDGryDVIKTqy3/nRDuVKLPy3x7tTpiMXdVFeTqIOkU19ePihhTViUrLJnbeMmAVrLPqOHz9LLpSPGZ5nljOlv4W0CSNtBT9yOsRAaWAU9ipz+20yfYz6MjbFjneSHpYXgHlW/gxgNJReQYRbJgRobKTvt5oUTKkpmYvBtyDxagLcUb6SCXxfZGhaSAEWCbEN9ETEFaJycVtSaxUG3SKAOBrd0+YxhAwiHjfRKgLPY2pzUK2F31HXY5yO3/9fSeTOmOkg2lHVEeEV0/XFk0yJdD8cnz7QEGQCFFJuZrKreJ76ubzWZggA64qoCsCq3Zm+bvMCIs2WZQukoTg3GqCFGIxwxeGR9T5LcGiV2tPffUtj1JIkohip2NfgIgAZ6UOOlXp66d9JubpoZzrKucdLQCnZlt7tss/RyHoMhal4Ojc6cnBtukoE434PD1Bh/P8doRcrsFYNPzbp5LoTZ9W4m8pY5CZI9Tzaduo5hx9sJ9745xWzl67VEqp8xsjGahUU1YiH0rJDcnpUwnEVNTjVOlXDkc4bNhcwXdIiT9udhG9w== Jacque_Fresco@EPUAKHAW013D', 'user-pc', '"Chrome, Vagrant"', '48c1e088-48c1-11ea-b77f-2e728ce88128']
```
## Function TREE - Filter by row:
```
C:\Users\Oleksandr_Frolov\PycharmProjects\Task5\venv\Scripts\python.exe C:/Users/Oleksandr_Frolov/PycharmProjects/Task5/Task5.py -f log.csv -d , -r 1-3
['MAC', 'hostname', 'IPv4', 'IPv6', 'netmask', 'login', 'full_user_name', 'email', 'ssh', 'description_host', 'installed_app', 'UUID']
['00:0a:95:9d:68:13', 'EPUAKHAW012D', '192.168.0.50', '0:0:0:0:0:ffff:c0a8:33', '255.255.128.0', 'Vasia_Pupkin', 'Vasia Pupkin', 'Vasia_Pupkin@epam.com', 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDMFY85GBlB1boQSJ5Sp+a36QUlEtqFIVryz+328ELMhQcdPbg9G7aUH+v1t9EH1PLAmyYCauzOp7I5HFjceFMuisbbxotFuePnbKsYH1/rBMe8yQyFq0BOstMCGdExXQpDGryDVIKTqy3/nRDuVKLPy3x7tTpiMXdVFeTqIOkU19ePihhTViUrLJnbeMmAVrLPqOHz9LLpSPGZ5nljOlv4W0CSNtBT9yOsRAaWAU9ipz+20yfYz6MjbFjneSHpYXgHlW/gxgNJReQYRbJgRobKTvt5oUTKkpmYvBtyDxagLcUb6SCXxfZGhaSAEWCbEN9ETEFaJycVtSaxUG3SKAOBrd0+YxhAwiHjfRKgLPY2pzUK2F31HXY5yO3/9fSeTOmOkg2lHVEeEV0/XFk0yJdD8cnz7QEGQCFFJuZrKreJ76ubzWZggA64qoCsCq3Zm+bvMCIs2WZQukoTg3GqCFGIxwxeGR9T5LcGiV2tPffUtj1JIkohip2NfgIgAZ6UOOlXp66d9JubpoZzrKucdLQCnZlt7tss/RyHoMhal4Ojc6cnBtukoE434PD1Bh/P8doRcrsFYNPzbp5LoTZ9W4m8pY5CZI9Tzaduo5hx9sJ9745xWzl67VEqp8xsjGahUU1YiH0rJDcnpUwnEVNTjVOlXDkc4bNhcwXdIiT9udhG9w== Vasia_Pupkin@EPUAKHAW013D', 'user-pc', '"Skype, PyCharm, Chrome"', '48c1e088-48c1-11ea-b77f-2e728ce88126']
['00:0a:95:9d:68:14', 'EPUAKHAW013D', '192.168.0.57', '0:0:0:0:0:ffff:c0a8:34', '255.255.0.0', 'Ivan_Ivanov', 'Ivan Ivanov', 'Ivan_Ivanov@epam.com', 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDMFY85GBlB1boQSJ5Sp+a36QUlEtqFIVryz+328ELMhQcdPbg9G7aUH+v1t9EH1PLAmyYCauzOp7I5HFjceFMuisbbxotFuePnbKsYH1/rBMe8yQyFq0BOstMCGdExXQpDGryDVIKTqy3/nRDuVKLPy3x7tTpiMXdVFeTqIOkU19ePihhTViUrLJnbeMmAVrLPqOHz9LLpSPGZ5nljOlv4W0CSNtBT9yOsRAaWAU9ipz+20yfYz6MjbFjneSHpYXgHlW/gxgNJReQYRbJgRobKTvt5oUTKkpmYvBtyDxagLcUb6SCXxfZGhaSAEWCbEN9ETEFaJycVtSaxUG3SKAOBrd0+YxhAwiHjfRKgLPY2pzUK2F31HXY5yO3/9fSeTOmOkg2lHVEeEV0/XFk0yJdD8cnz7QEGQCFFJuZrKreJ76ubzWZggA64qoCsCq3Zm+bvMCIs2WZQukoTg3GqCFGIxwxeGR9T5LcGiV2tPffUtj1JIkohip2NfgIgAZ6UOOlXp66d9JubpoZzrKucdLQCnZlt7tss/RyHoMhal4Ojc6cnBtukoE434PD1Bh/P8doRcrsFYNPzbp5LoTZ9W4m8pY5CZI9Tzaduo5hx9sJ9745xWzl67VEqp8xsjGahUU1YiH0rJDcnpUwnEVNTjVOlXDkc4bNhcwXdIiT9udhG9w== Ivan_Ivanov@EPUAKHAW013D', 'user-pc', '"Skype, Viber, Teams"', '48c1e088-48c1-11ea-b77f-2e728ce88127']
['00:0a:95:9d:68:15', 'EPUAKHAW014D', '192.168.0.54', '0:0:0:0:0:ffff:c0a8:35', '255.0.0.0', 'Daria_Pupkin', 'Daria Pupkin', 'Daria_Pupkin@epam.com', 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDMFY85GBlB1boQSJ5Sp+a36QUlEtqFIVryz+328ELMhQcdPbg9G7aUH+v1t9EH1PLAmyYCauzOp7I5HFjceFMuisbbxotFuePnbKsYH1/rBMe8yQyFq0BOstMCGdExXQpDGryDVIKTqy3/nRDuVKLPy3x7tTpiMXdVFeTqIOkU19ePihhTViUrLJnbeMmAVrLPqOHz9LLpSPGZ5nljOlv4W0CSNtBT9yOsRAaWAU9ipz+20yfYz6MjbFjneSHpYXgHlW/gxgNJReQYRbJgRobKTvt5oUTKkpmYvBtyDxagLcUb6SCXxfZGhaSAEWCbEN9ETEFaJycVtSaxUG3SKAOBrd0+YxhAwiHjfRKgLPY2pzUK2F31HXY5yO3/9fSeTOmOkg2lHVEeEV0/XFk0yJdD8cnz7QEGQCFFJuZrKreJ76ubzWZggA64qoCsCq3Zm+bvMCIs2WZQukoTg3GqCFGIxwxeGR9T5LcGiV2tPffUtj1JIkohip2NfgIgAZ6UOOlXp66d9JubpoZzrKucdLQCnZlt7tss/RyHoMhal4Ojc6cnBtukoE434PD1Bh/P8doRcrsFYNPzbp5LoTZ9W4m8pY5CZI9Tzaduo5hx9sJ9745xWzl67VEqp8xsjGahUU1YiH0rJDcnpUwnEVNTjVOlXDkc4bNhcwXdIiT9udhG9w== Daria_Pupkin@EPUAKHAW013D', 'user-pc', '"VirtualBox, Vagrant"', '48c1e088-48c1-11ea-b77f-2e728ce88128']
```
## Function FOUR - Filter by column:
```
C:\Users\Oleksandr_Frolov\PycharmProjects\Task5\venv\Scripts\python.exe C:/Users/Oleksandr_Frolov/PycharmProjects/Task5/Task5.py -f log.csv -d , -C 1-3 -C 5-6
['hostname', 'IPv4', 'IPv6', 'login', 'full_user_name']
['EPUAKHAW011D', '255.255.254.0', '0:0:0:0:0:ffff:c0a8:32', 'Oleksandr_Frolov', 'Oleksandr Frolov']
['EPUAKHAW012D', '192.168.0.50', '0:0:0:0:0:ffff:c0a8:33', 'Vasia_Pupkin', 'Vasia Pupkin']
['EPUAKHAW013D', '192.168.0.57', '0:0:0:0:0:ffff:c0a8:34', 'Ivan_Ivanov', 'Ivan Ivanov']
['EPUAKHAW014D', '192.168.0.54', '0:0:0:0:0:ffff:c0a8:35', 'Daria_Pupkin', 'Daria Pupkin']
['EPUADNAW010D', '74.42.5.54', '0:0:0:0:0:faff:c0a8:36', 'Jacque_Fresco', 'Jacque Fresco']
```
## Function FIVE - Filter by pattern:
```
C:\Users\Oleksandr_Frolov\PycharmProjects\Task5\venv\Scripts\python.exe C:/Users/Oleksandr_Frolov/PycharmProjects/Task5/Task5.py -f log.csv -d , -c 6 -F *Pupkin
['MAC', 'hostname', 'IPv4', 'IPv6', 'netmask', 'login', 'full_user_name', 'email', 'ssh', 'description_host', 'installed_app', 'UUID']
['00:0a:95:9d:68:13', 'EPUAKHAW012D', '192.168.0.50', '0:0:0:0:0:ffff:c0a8:33', '255.255.128.0', 'Vasia_Pupkin', 'Vasia Pupkin', 'Vasia_Pupkin@epam.com', 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDMFY85GBlB1boQSJ5Sp+a36QUlEtqFIVryz+328ELMhQcdPbg9G7aUH+v1t9EH1PLAmyYCauzOp7I5HFjceFMuisbbxotFuePnbKsYH1/rBMe8yQyFq0BOstMCGdExXQpDGryDVIKTqy3/nRDuVKLPy3x7tTpiMXdVFeTqIOkU19ePihhTViUrLJnbeMmAVrLPqOHz9LLpSPGZ5nljOlv4W0CSNtBT9yOsRAaWAU9ipz+20yfYz6MjbFjneSHpYXgHlW/gxgNJReQYRbJgRobKTvt5oUTKkpmYvBtyDxagLcUb6SCXxfZGhaSAEWCbEN9ETEFaJycVtSaxUG3SKAOBrd0+YxhAwiHjfRKgLPY2pzUK2F31HXY5yO3/9fSeTOmOkg2lHVEeEV0/XFk0yJdD8cnz7QEGQCFFJuZrKreJ76ubzWZggA64qoCsCq3Zm+bvMCIs2WZQukoTg3GqCFGIxwxeGR9T5LcGiV2tPffUtj1JIkohip2NfgIgAZ6UOOlXp66d9JubpoZzrKucdLQCnZlt7tss/RyHoMhal4Ojc6cnBtukoE434PD1Bh/P8doRcrsFYNPzbp5LoTZ9W4m8pY5CZI9Tzaduo5hx9sJ9745xWzl67VEqp8xsjGahUU1YiH0rJDcnpUwnEVNTjVOlXDkc4bNhcwXdIiT9udhG9w== Vasia_Pupkin@EPUAKHAW013D', 'user-pc', '"Skype, PyCharm, Chrome"', '48c1e088-48c1-11ea-b77f-2e728ce88126']
['00:0a:95:9d:68:15', 'EPUAKHAW014D', '192.168.0.54', '0:0:0:0:0:ffff:c0a8:35', '255.0.0.0', 'Daria_Pupkin', 'Daria Pupkin', 'Daria_Pupkin@epam.com', 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDMFY85GBlB1boQSJ5Sp+a36QUlEtqFIVryz+328ELMhQcdPbg9G7aUH+v1t9EH1PLAmyYCauzOp7I5HFjceFMuisbbxotFuePnbKsYH1/rBMe8yQyFq0BOstMCGdExXQpDGryDVIKTqy3/nRDuVKLPy3x7tTpiMXdVFeTqIOkU19ePihhTViUrLJnbeMmAVrLPqOHz9LLpSPGZ5nljOlv4W0CSNtBT9yOsRAaWAU9ipz+20yfYz6MjbFjneSHpYXgHlW/gxgNJReQYRbJgRobKTvt5oUTKkpmYvBtyDxagLcUb6SCXxfZGhaSAEWCbEN9ETEFaJycVtSaxUG3SKAOBrd0+YxhAwiHjfRKgLPY2pzUK2F31HXY5yO3/9fSeTOmOkg2lHVEeEV0/XFk0yJdD8cnz7QEGQCFFJuZrKreJ76ubzWZggA64qoCsCq3Zm+bvMCIs2WZQukoTg3GqCFGIxwxeGR9T5LcGiV2tPffUtj1JIkohip2NfgIgAZ6UOOlXp66d9JubpoZzrKucdLQCnZlt7tss/RyHoMhal4Ojc6cnBtukoE434PD1Bh/P8doRcrsFYNPzbp5LoTZ9W4m8pY5CZI9Tzaduo5hx9sJ9745xWzl67VEqp8xsjGahUU1YiH0rJDcnpUwnEVNTjVOlXDkc4bNhcwXdIiT9udhG9w== Daria_Pupkin@EPUAKHAW013D', 'user-pc', '"VirtualBox, Vagrant"', '48c1e088-48c1-11ea-b77f-2e728ce88128']
```
## Function SIX - Work with the header:
```
C:\Users\Oleksandr_Frolov\PycharmProjects\Task5\venv\Scripts\python.exe C:/Users/Oleksandr_Frolov/PycharmProjects/Task5/Task5.py -f log.csv -d , -H

['00:0a:95:9d:68:12', 'EPUAKHAW011D', '255.255.254.0', '0:0:0:0:0:ffff:c0a8:32', '255.255.255.0', 'Oleksandr_Frolov', 'Oleksandr Frolov', 'Oleksandr_Frolov@epam.com', 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDMFY85GBlB1boQSJ5Sp+a36QUlEtqFIVryz+328ELMhQcdPbg9G7aUH+v1t9EH1PLAmyYCauzOp7I5HFjceFMuisbbxotFuePnbKsYH1/rBMe8yQyFq0BOstMCGdExXQpDGryDVIKTqy3/nRDuVKLPy3x7tTpiMXdVFeTqIOkU19ePihhTViUrLJnbeMmAVrLPqOHz9LLpSPGZ5nljOlv4W0CSNtBT9yOsRAaWAU9ipz+20yfYz6MjbFjneSHpYXgHlW/gxgNJReQYRbJgRobKTvt5oUTKkpmYvBtyDxagLcUb6SCXxfZGhaSAEWCbEN9ETEFaJycVtSaxUG3SKAOBrd0+YxhAwiHjfRKgLPY2pzUK2F31HXY5yO3/9fSeTOmOkg2lHVEeEV0/XFk0yJdD8cnz7QEGQCFFJuZrKreJ76ubzWZggA64qoCsCq3Zm+bvMCIs2WZQukoTg3GqCFGIxwxeGR9T5LcGiV2tPffUtj1JIkohip2NfgIgAZ6UOOlXp66d9JubpoZzrKucdLQCnZlt7tss/RyHoMhal4Ojc6cnBtukoE434PD1Bh/P8doRcrsFYNPzbp5LoTZ9W4m8pY5CZI9Tzaduo5hx9sJ9745xWzl67VEqp8xsjGahUU1YiH0rJDcnpUwnEVNTjVOlXDkc4bNhcwXdIiT9udhG9w== Oleksandr_Frolov@EPUAKHAW013D', 'user-pc', '"Skype, Viber"', '48c1e088-48c1-11ea-b77f-2e728ce88125']
['00:0a:95:9d:68:13', 'EPUAKHAW012D', '192.168.0.50', '0:0:0:0:0:ffff:c0a8:33', '255.255.128.0', 'Vasia_Pupkin', 'Vasia Pupkin', 'Vasia_Pupkin@epam.com', 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDMFY85GBlB1boQSJ5Sp+a36QUlEtqFIVryz+328ELMhQcdPbg9G7aUH+v1t9EH1PLAmyYCauzOp7I5HFjceFMuisbbxotFuePnbKsYH1/rBMe8yQyFq0BOstMCGdExXQpDGryDVIKTqy3/nRDuVKLPy3x7tTpiMXdVFeTqIOkU19ePihhTViUrLJnbeMmAVrLPqOHz9LLpSPGZ5nljOlv4W0CSNtBT9yOsRAaWAU9ipz+20yfYz6MjbFjneSHpYXgHlW/gxgNJReQYRbJgRobKTvt5oUTKkpmYvBtyDxagLcUb6SCXxfZGhaSAEWCbEN9ETEFaJycVtSaxUG3SKAOBrd0+YxhAwiHjfRKgLPY2pzUK2F31HXY5yO3/9fSeTOmOkg2lHVEeEV0/XFk0yJdD8cnz7QEGQCFFJuZrKreJ76ubzWZggA64qoCsCq3Zm+bvMCIs2WZQukoTg3GqCFGIxwxeGR9T5LcGiV2tPffUtj1JIkohip2NfgIgAZ6UOOlXp66d9JubpoZzrKucdLQCnZlt7tss/RyHoMhal4Ojc6cnBtukoE434PD1Bh/P8doRcrsFYNPzbp5LoTZ9W4m8pY5CZI9Tzaduo5hx9sJ9745xWzl67VEqp8xsjGahUU1YiH0rJDcnpUwnEVNTjVOlXDkc4bNhcwXdIiT9udhG9w== Vasia_Pupkin@EPUAKHAW013D', 'user-pc', '"Skype, PyCharm, Chrome"', '48c1e088-48c1-11ea-b77f-2e728ce88126']
['00:0a:95:9d:68:14', 'EPUAKHAW013D', '192.168.0.57', '0:0:0:0:0:ffff:c0a8:34', '255.255.0.0', 'Ivan_Ivanov', 'Ivan Ivanov', 'Ivan_Ivanov@epam.com', 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDMFY85GBlB1boQSJ5Sp+a36QUlEtqFIVryz+328ELMhQcdPbg9G7aUH+v1t9EH1PLAmyYCauzOp7I5HFjceFMuisbbxotFuePnbKsYH1/rBMe8yQyFq0BOstMCGdExXQpDGryDVIKTqy3/nRDuVKLPy3x7tTpiMXdVFeTqIOkU19ePihhTViUrLJnbeMmAVrLPqOHz9LLpSPGZ5nljOlv4W0CSNtBT9yOsRAaWAU9ipz+20yfYz6MjbFjneSHpYXgHlW/gxgNJReQYRbJgRobKTvt5oUTKkpmYvBtyDxagLcUb6SCXxfZGhaSAEWCbEN9ETEFaJycVtSaxUG3SKAOBrd0+YxhAwiHjfRKgLPY2pzUK2F31HXY5yO3/9fSeTOmOkg2lHVEeEV0/XFk0yJdD8cnz7QEGQCFFJuZrKreJ76ubzWZggA64qoCsCq3Zm+bvMCIs2WZQukoTg3GqCFGIxwxeGR9T5LcGiV2tPffUtj1JIkohip2NfgIgAZ6UOOlXp66d9JubpoZzrKucdLQCnZlt7tss/RyHoMhal4Ojc6cnBtukoE434PD1Bh/P8doRcrsFYNPzbp5LoTZ9W4m8pY5CZI9Tzaduo5hx9sJ9745xWzl67VEqp8xsjGahUU1YiH0rJDcnpUwnEVNTjVOlXDkc4bNhcwXdIiT9udhG9w== Ivan_Ivanov@EPUAKHAW013D', 'user-pc', '"Skype, Viber, Teams"', '48c1e088-48c1-11ea-b77f-2e728ce88127']
['00:0a:95:9d:68:15', 'EPUAKHAW014D', '192.168.0.54', '0:0:0:0:0:ffff:c0a8:35', '255.0.0.0', 'Daria_Pupkin', 'Daria Pupkin', 'Daria_Pupkin@epam.com', 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDMFY85GBlB1boQSJ5Sp+a36QUlEtqFIVryz+328ELMhQcdPbg9G7aUH+v1t9EH1PLAmyYCauzOp7I5HFjceFMuisbbxotFuePnbKsYH1/rBMe8yQyFq0BOstMCGdExXQpDGryDVIKTqy3/nRDuVKLPy3x7tTpiMXdVFeTqIOkU19ePihhTViUrLJnbeMmAVrLPqOHz9LLpSPGZ5nljOlv4W0CSNtBT9yOsRAaWAU9ipz+20yfYz6MjbFjneSHpYXgHlW/gxgNJReQYRbJgRobKTvt5oUTKkpmYvBtyDxagLcUb6SCXxfZGhaSAEWCbEN9ETEFaJycVtSaxUG3SKAOBrd0+YxhAwiHjfRKgLPY2pzUK2F31HXY5yO3/9fSeTOmOkg2lHVEeEV0/XFk0yJdD8cnz7QEGQCFFJuZrKreJ76ubzWZggA64qoCsCq3Zm+bvMCIs2WZQukoTg3GqCFGIxwxeGR9T5LcGiV2tPffUtj1JIkohip2NfgIgAZ6UOOlXp66d9JubpoZzrKucdLQCnZlt7tss/RyHoMhal4Ojc6cnBtukoE434PD1Bh/P8doRcrsFYNPzbp5LoTZ9W4m8pY5CZI9Tzaduo5hx9sJ9745xWzl67VEqp8xsjGahUU1YiH0rJDcnpUwnEVNTjVOlXDkc4bNhcwXdIiT9udhG9w== Daria_Pupkin@EPUAKHAW013D', 'user-pc', '"VirtualBox, Vagrant"', '48c1e088-48c1-11ea-b77f-2e728ce88128']
['1a:0a:95:9d:68:15', 'EPUADNAW010D', '74.42.5.54', '0:0:0:0:0:faff:c0a8:36', '255.128.0.0', 'Jacque_Fresco', 'Jacque Fresco', 'Jacque_Fresco@epam.com', 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDMFY85GBlB1boQSJ5Sp+a36QUlEtqFIVryz+328ELMhQcdPbg9G7aUH+v1t9EH1PLAmyYCauzOp7I5HFjceFMuisbbxotFuePnbKsYH1/rBMe8yQyFq0BOstMCGdExXQpDGryDVIKTqy3/nRDuVKLPy3x7tTpiMXdVFeTqIOkU19ePihhTViUrLJnbeMmAVrLPqOHz9LLpSPGZ5nljOlv4W0CSNtBT9yOsRAaWAU9ipz+20yfYz6MjbFjneSHpYXgHlW/gxgNJReQYRbJgRobKTvt5oUTKkpmYvBtyDxagLcUb6SCXxfZGhaSAEWCbEN9ETEFaJycVtSaxUG3SKAOBrd0+YxhAwiHjfRKgLPY2pzUK2F31HXY5yO3/9fSeTOmOkg2lHVEeEV0/XFk0yJdD8cnz7QEGQCFFJuZrKreJ76ubzWZggA64qoCsCq3Zm+bvMCIs2WZQukoTg3GqCFGIxwxeGR9T5LcGiV2tPffUtj1JIkohip2NfgIgAZ6UOOlXp66d9JubpoZzrKucdLQCnZlt7tss/RyHoMhal4Ojc6cnBtukoE434PD1Bh/P8doRcrsFYNPzbp5LoTZ9W4m8pY5CZI9Tzaduo5hx9sJ9745xWzl67VEqp8xsjGahUU1YiH0rJDcnpUwnEVNTjVOlXDkc4bNhcwXdIiT9udhG9w== Jacque_Fresco@EPUAKHAW013D', 'user-pc', '"Chrome, Vagrant"', '48c1e088-48c1-11ea-b77f-2e728ce88128']
```
## Function SEVEN - Export to json:
```
C:\Users\Oleksandr_Frolov\PycharmProjects\Task5\venv\Scripts\python.exe C:/Users/Oleksandr_Frolov/PycharmProjects/Task5/Task5.py -f log.csv -d , -o out.json
```
```yaml
```json
{
    "one": 2,
    "three": {
        "point_1": "point_2",
        "point_3": 3.4
    },
    "list": [
        "one",
        "two",
        "three"
    ]
}
```
```
