## Password generation
Designations:
* A - any capital letter of the Latin alphabet;
* a - any small letter of the Latin alphabet;
* d - any digit;
* S - any special symbol.
Password Pattern:
{N}a{N}A{N}d{N}S
```
Input password pattern (example: 2a11A4d7S):
4a6A3d2S
Your password: 10n+wVSaE#ISMt7
```
Handling error pattern:
Incorrect pattern entered. 
```
Input password pattern (example: 2a11A4d7S):
4a6A3d2
Errors in the password pattern, correct them. Here is an example: 2a11A4d7S
```

## IP address calculator
```
Input ip address with subnet mask (example: 192.168.0.1/24):
192.168.12.14/20
IP address   | (10) 192.168.12.14   | (2) 11000000101010000000110000001110
Subnet mask  | (10) 255.255.240.0   | (2) 11111111111111111111 | (bit) 20
Network size | 4096
Broadcast    | (10) 192.168.15.255  | (2) 11000000101010000000111111111111
Network      | (10) 192.168.0.0     | (2) 11000000101010000000000000000000
Host minimal | (10) 192.168.0.1     | (2) 11000000101010000000000000000001
Host maximal | (10) 192.168.15.254  | (2) 11000000101010000000111111111110
Input host number:
74
IP address of your host number is:  192.168.0.74
```
Handling error pattern:
1) Incorrect pattern entered.
```
Input ip address with subnet mask (example: 192.168.0.1/24):
192.168.0.1//24
IP address or subnet mask is not correct, example: 192.168.0.1/24
```
2) Incorrect pattern entered. IP address octet more than 255.
```
Input ip address with subnet mask (example: 192.168.0.1/24):
392.168.0.1/24
IP address octet cannot be more than 255
```
3) Incorrect pattern entered. Subnet mask more than 32.
```
Input ip address with subnet mask (example: 192.168.0.1/24):
192.168.0.1/33
Subnet mask cannot be more than 32
```
4) Incorrect host number entered. Host number more than network size.
```
Input ip address with subnet mask (example: 192.168.0.1/24):
192.168.0.1/28
IP address   | (10) 192.168.0.1     | (2) 11000000101010000000000000000001
Subnet mask  | (10) 255.255.255.240 | (2) 1111111111111111111111111111 | (bit) 28
Network size | 16
Broadcast    | (10) 192.168.0.15    | (2) 11000000101010000000000000001111
Network      | (10) 192.168.0.0     | (2) 11000000101010000000000000000000
Host minimal | (10) 192.168.0.1     | (2) 11000000101010000000000000000001
Host maximal | (10) 192.168.0.14    | (2) 11000000101010000000000000001110
Input host number:
17
Entered host number is outside the network size. Input again.
14
IP address of your host number is:  192.168.0.14
```
