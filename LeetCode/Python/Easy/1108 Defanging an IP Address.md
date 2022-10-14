## 1108 - Defanging an IP Address (string)

Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".

### Examples 1
```
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
```

### Examples 2
```
Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
```

### Solution
```python
class Solution(object):
    def defangIPaddr(self, address):
        return address.replace('.' , '[.]')
        

```