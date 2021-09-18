```python
x = int(input("x: "))
y = int(input("y: "))

print(f"add: {x+y} sub: {x-y} mul: {x*y} div: {x/y}")
```

    x: 10
    y: 2
    add: 12 sub: 8 mul: 20 div: 5.0
    


```python
x = int(input("x: "))
y = int(input("y: "))

print(f"{x} x {y} = {x*y}")
```

    x: 31
    y: 38
    31 x 38 = 1178
    


```python
num = int(input("Please enter the number : "))

for i in range(0, num):
    for j in range(0, num-i):
        print("*", end='')
    print()
```

    Please enter the number : 5
    *****
    ****
    ***
    **
    *
    


```python
sum = 0

for i in range(1, 11):
    sum += i
    print(f"{i} --> {sum}")
```

    1 --> 1
    2 --> 3
    3 --> 6
    4 --> 10
    5 --> 15
    6 --> 21
    7 --> 28
    8 --> 36
    9 --> 45
    10 --> 55
    


```python

```
