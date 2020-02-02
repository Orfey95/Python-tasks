### task_2_1():
Список mac содержит MAC-адреса в формате XXXX:XXXX:XXXX. Однако, в оборудовании cisco MAC-адреса используются в формате XXXX.XXXX.XXXX. Создать скрипт, который преобразует MAC-адреса в формат cisco и добавляет их в новый список mac_cisco.
```
['aabb.cc80.7000', 'aabb.dd80.7340', 'aabb.ee80.7000', 'aabb.ff80.7000']
```
### task_2_2():
1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1<br>
2. Определить тип IP-адреса.<br>
3. В зависимости от типа адреса, вывести на стандартный поток вывода:<br>
• „unicast“ - если первый байт в диапазоне 1-223<br>
• „multicast“ - если первый байт в диапазоне 224-239<br>
• „local broadcast“ - если IP-адрес равен 255.255.255.255<br>
• „unassigned“ - если IP-адрес равен 0.0.0.0<br>
• „unused“ - во всех остальных случаях<br>
```
Input ip address (example: 192.168.0.1):
10.20.30.40
unicast
Input ip address (example: 192.168.0.1):
230.20.30.40
multicast
Input ip address (example: 192.168.0.1):
255.255.255.255
local broadcast
Input ip address (example: 192.168.0.1):
0.0.0.0
unassigned
Input ip address (example: 192.168.0.1):
250.20.30.40
unused
```
### task_2_3():
Сделать копию скрипта задания task_2_2.<br>
Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:<br>
• состоит из 4 чисел разделенных точкой,<br>
• каждое число в диапазоне от 0 до 255.<br>
Если адрес задан неправильно, выводить сообщение: „Неправильный IP-адрес“.<br>
```
Input ip address (example: 192.168.0.1):
500.20.30.40
Invalid IP Address
```
### task_2_4():
Сделать копию скрипта задания task_2_2.<br>
Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.<br>
```
Input ip address (example: 192.168.0.1):
500.20.30.40
Invalid IP Address. Input again.
400.20.30.40
Invalid IP Address. Input again.
255.20.30.40
unused
```
### task_2_5():
В скрипте сделан генератор конфигурации для access-портов.<br>
Сделать аналогичный генератор конфигурации для портов trunk.<br>
В транках ситуация усложняется тем, что VLANов может быть много, и надо понимать, что с ним делать.<br>
Поэтому в соответствии каждому порту стоит список и первый (нулевой) элемент списка указывает как воспринимать номера VLAN, которые идут дальше:<br>
• add - VLANы надо будет добавить (команда switchport trunk allowed vlan add 10,20)<br>
• del - VLANы надо удалить из списка разрешенных (команда switchport trunk allowed vlan remove 17)<br>
• only - на интерфейсе должны остаться разрешенными только указанные VLANы (команда switchport trunk allowed vlan 11,30)<br>
Задача для портов 0/1, 0/2, 0/4:<br>
• сгенерировать конфигурацию на основе шаблона trunk_template<br>
• с учетом ключевых слов add, del, only<br>
Код не должен привязываться к конкретным номерам портов. То есть, если в словаре trunk будут другие номера интерфейсов, код должен работать.<br>
```
interface FastEthernet0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan add 10,20
interface FastEthernet0/2
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 11,30
interface FastEthernet0/4
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan remove 17
```
