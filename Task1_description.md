### task_1_1():
Обработать строку nat таким образом, чтобы в имени интерфейса вместо FastEthernet было GigabitEthernet.
```
ip nat inside source list ACL interface GigabitEthernet0/1 over
```
### task_1_2():
Преобразовать строку mac из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX.
```
AAAA.BBBB.CCCC
```
### task_1_3():
Получить из строки config список VLAN-ов вида: ['1', '3', '10', '20', '30', '100'].
```
['1', '3', '10', '20', '30', '100']
```
### task_1_4():
Список vlans это список VLANов, собранных со всех устройств сети, поэтому в списке есть повторяющиеся номера VLAN. Из списка нужно получить уникальный список VLAN-ов, отсортированный по возрастанию номеров.
```
[1, 2, 3, 4, 10, 20, 30, 100]
```
### task_1_5():
Из строк command1 и command2 получить список VLAN-ов, которые есть и в команде command1 и в команде command2.
```
['1', '3', '8']
```
### task_1_6():
Обработать строку ospf_route и вывести информацию на стандартный поток вывода.
```
Protocol:            OSPF
Prefix:              10.0.24.0/24
AD/Metric:           110/41
Next-Hop:            10.0.13.3
Last update:         3d18h
Outbound Interface:  FastEthernet0/0
```
### task_1_7():
Преобразовать MAC-адрес mac в двоичную строку такого вида: 101010101010101010111011101110111100110011001100.
```
101010101010101010111011101110111100110011001100
```
### task_1_8():
Преобразовать IP-адрес в двоичный формат и вывести на стандартный поток вывода вывод столбцами, таким образом:<br>
• первой строкой должны идти десятичные значения байтов<br>
• второй строкой двоичные значения<br>
Вывод должен быть упорядочен также, как в примере:<br>
• столбцами<br>
• ширина столбца 10 символов<br>
```
192        168        3          1
11000000   10101000   00000011   00000001
```
