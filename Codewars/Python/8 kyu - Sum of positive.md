## Sum of positive
You get an array of numbers, return the sum of all of the positives ones.
### Examples
```
[1,-4,7,12] => 1 + 7 + 12 = 20
```
### Solution
```python
def positive_sum(arr):
    return sum(filter(lambda x: x>0, arr))
```