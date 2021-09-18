```python
A = "abel"
B = "nenny"
numberA = "010-1234-5678" #phone number of A
numberB = "010-9876-5432" #phone number of B

print(f"{A} {numberA} --> {A[0].upper()}{A[1:]} {numberA.replace('-', '')}")
print(f"{B} {numberB} --> {A[0].upper()}{B[1:]} {numberB.replace('-', '')}")
```

    abel 010-1234-5678 --> Abel 01012345678
    nenny 010-9876-5432 --> Aenny 01098765432
    


```python
list1 = []
list2 = []

for i in range(1, 11):
    if i % 2 == 1: # i is odd
        list1.append(i)
    else :         # i is even
        list2.append(i)
print("list1: {0}".format(list1))
print("list2: {0}".format(list2))

result = list1+list2
result.sort(reverse=True)
print("result: {0}".format(result))
```

    list1: [1, 3, 5, 7, 9]
    list2: [2, 4, 6, 8, 10]
    result: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    


```python
x = (1, 2, 3)
y = ('a', 'b')
new = x+y

print(f"x: {x}")
print(f"y: {y}")
print(f"drop 'b': {new[0:-1]}")
```

    x: (1, 2, 3)
    y: ('a', 'b')
    drop 'b': (1, 2, 3, 'a')
    


```python
dic = { 
       "Kim" : "Math", 
       "Lee" : "English", 
       "Han" : "Art",
        "Ahn" : "Physics"}
print(f"dic = {dic}")
del dic["Lee"]
print(dic.keys())
print(dic.values())
```

    dic = {'Kim': 'Math', 'Lee': 'English', 'Han': 'Art', 'Ahn': 'Physics'}
    dict_keys(['Kim', 'Han', 'Ahn'])
    dict_values(['Math', 'Art', 'Physics'])
    


```python

```
