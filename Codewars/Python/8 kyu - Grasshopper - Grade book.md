## Grade book
Complete the function so that it finds the average of the three scores passed to it 
and returns the letter value associated with that grade.

### Examples
```
Numerical Score	        Letter Grade
90 <= score <= 100	        'A'
80 <= score < 90	        'B'
70 <= score < 80	        'C'
60 <= score < 70	        'D'
0 <= score < 60	            'F'

```
### Solution
```python
def get_grade(s1, s2, s3):
    score = (s1+s2+s3)//3
    if (90 <= score and score <=100):
        return "A"
    elif (80 <= score and score < 90):
        return "B"
    elif (70 <= score and score < 80):
        return "C"
    elif (60 <= score and score < 70):
        return "D"
    elif (0 <= score and score < 60):
        return "F"
```