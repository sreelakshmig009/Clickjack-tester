# Clickjacking Tester

A python script designed to check if the website is vulnerable of clickjacking and saves the result into Vulnerable.txt file.

### Usage

```
python clickjack.py <file_name>
#python3 in case of Linux environment
```

### Example

##### Input

```
python clickjack.py sites.txt
```

##### sites.txt

```
www.bugcrowd.com
www.srsecure.xyz
www.developer.pubg.com
```

##### Output

```
[-] www.bugcrowd.com is not Vulnerable
[+] www.srsecure.xyz is Vulnerable
[+] www.developer.pubg.com is Vulnerable
```
