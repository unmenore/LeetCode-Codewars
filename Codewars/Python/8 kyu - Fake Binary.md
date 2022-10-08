## 
Fake Binary

Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. 
Return the resulting string.

### Solution
```python
def count_positives_sum_negatives(arr):
    return [len([i for i in arr if i > 0]), sum([i for i in arr if i < 0])] if len(arr) !=0 else []
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