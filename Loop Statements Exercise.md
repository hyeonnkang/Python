```python
coin = 0 # user money
while True:
    print("""
        1: Insert coin | 2: Item list | 3: Select fruit | 
        4: Change money | Q: exit""")
    select = input("Please select menu: ")
    print()

    if select == "1":
        num = int(input("How much money do y ou want to put in?"))
        coin += num
        print(f"You insert {num} coins")
    elif select == "2":
        print("::::1. Orange: 300:::: ::::2. Shine muscat: 1000::::")
    elif select == "3":
        fruit = int(input("Which fruit do you want?"))
        if fruit == 1 :
            if coin >= 300 :
                coin -= 300
                print("You get an orange")
                print("You have {0} coins".format(coin))
            else: print("I'm sorry. Your coin is not enough")
        elif fruit == 2 :
            if coin >= 1000 :
                coin -= 1000
                print("You get an shine muscat")
                print("You have {0} coins".format(coin))
            else: print("I'm sorry. Your coin is not enough")
    elif select == "4":
        print(f"You get {coin} coins back")
        coin = 0
    else :
        print("End")
        break
```

    
            1: Insert coin | 2: Item list | 3: Select fruit | 
            4: Change money | Q: exit
    Please select menu: 1
    
    How much money do y ou want to put in?500
    You insert 500 coins
    
            1: Insert coin | 2: Item list | 3: Select fruit | 
            4: Change money | Q: exit
    Please select menu: 2
    
    ::::1. Orange: 300:::: ::::2. Shine muscat: 1000::::
    
            1: Insert coin | 2: Item list | 3: Select fruit | 
            4: Change money | Q: exit
    Please select menu: 3
    
    Which fruit do you want?1
    You get an orange
    You have 200 coins
    
            1: Insert coin | 2: Item list | 3: Select fruit | 
            4: Change money | Q: exit
    Please select menu: 4
    
    You get 200 coins back
    
            1: Insert coin | 2: Item list | 3: Select fruit | 
            4: Change money | Q: exit
    Please select menu: Q
    
    End
    


```python
li = [100, 90, 80, 55, 95, 80, 65, 75, 70, 90]

avg = 0
for i in li :
    avg += i
avg /= len(li)

print("Meanse : {0}".format(avg))

variance = 0
for i in li :
    variance += (i - avg)**2
variance /= len(li)

print("Variance : {0}".format(variance))
```

    Meanse : 80.0
    Variance : 180.0
    


```python
students = [55, 90, 89, 76, 37, 100, 67]

for i in range(0, len(students)):
    if students[i] >= 90 : 
        print(f"{i}번 학생은 {students[i]}점으로 A입니다.")
    elif students[i] >= 80 : 
        print(f"{i}번 학생은 {students[i]}점으로 B입니다.")
    elif students[i] >= 70 : 
        print(f"{i}번 학생은 {students[i]}점으로 C입니다.")
    elif students[i] >= 60 : 
        print(f"{i}번 학생은 {students[i]}점으로 D입니다.")
    else :
        print(f"{i}번 학생은 {students[i]}점으로 F입니다.")
```

    0번 학생은 55점으로 F입니다.
    1번 학생은 90점으로 A입니다.
    2번 학생은 89점으로 B입니다.
    3번 학생은 76점으로 C입니다.
    4번 학생은 37점으로 F입니다.
    5번 학생은 100점으로 A입니다.
    6번 학생은 67점으로 D입니다.
    


```python
a = [4, 3, 2, 9, 7, 18, 22, 13, 6, 24, 37, 12]

prime = []
composite = []

for i in a:
    put = 0
    for j in range(2, i):
        if i % j == 0:
            composite.append(i)
            put += 1
            break
    
    if put == 0:
        prime.append(i)

print(f"Prime numbers: {prime} {len(prime)}")
print(f"Composite_numbers: {composite} {len(composite)}")
```

    Prime numbers: [3, 2, 7, 13, 37] 5
    Composite_numbers: [4, 9, 18, 22, 6, 24, 12] 7
    


```python
li = [[1, 2], [5, 4], [6, 6], [7, 8], [9, 10]]

arr = [i for row in li for i in row]
print(arr)
```

    [1, 2, 5, 4, 6, 6, 7, 8, 9, 10]
    


```python

```
