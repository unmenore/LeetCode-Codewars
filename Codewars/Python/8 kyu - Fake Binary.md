## 
Fake Binary

Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. 
Return the resulting string.

### Solution
```python
def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)
```

### Simple Solution
```python
def fake_bin(x):
    res = ""
    stNum = x
    for num in x:
        if int(num) < 5:
            res += "0"
        if int(num) >= 5:
            res += "1"
    return res
```