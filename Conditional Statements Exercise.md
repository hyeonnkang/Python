```python
a = (5, 5)
b = (-5, 5)

if a[0]==b[0] & a[1]==b[1] : # same point
    print("same points")
elif a[0]==b[0] & a[1]==-b[1]: # y axis symmetry
    printf("Y-axis symmetry")
elif a[0]==-b[0] & a[1]==b[1]: # x axis symmetry
    print("X-axis symmetry")
elif a[0]==-b[0] & a[1]==-b[1]: # origin symmetry
    print("origin symmetry")
else :
    print("Nothing")
```

    X-axis symmetry
    


```python
time = input("time: ")

# hour, min을 정수로 변환
org_hour = int(time[0:2])
org_min = int(time[3:5])

# 30분 전의 시간을 계산
min = org_min - 30
hour = org_hour

if min < 0 :
    hour -= 1
    min = 60 + min
    
    if hour < 0 :
        hour = 24 + hour

print("time {0} -> {1:02d}:{2:02d}".format(time, hour, min))
```

    time: 03:20
    time 03:20 -> 02:50
    


```python
import random

player1 = input("player1: ")  # user input
player2 = ""                # computer input
i = random.random() % 3
if i == 0: player2 = "가위"
elif i == 1 : player2 = "바위"
else : player2 = "보"

print('player1 = "{0}"'.format(player1))
print('player2 = "{0}"'.format(player2))
if player1 == player2 : # 무승부일 경우
    print("draw")
else :
    if player1 == "가위" :
        if player2 == "바위" : print("player2")
        else : print("player1")
    elif player1 == "바위":
        if player2 == "가위": print("player1")
        else : print("player2")
    elif player1 == "보":
        if player2 == "가위" : print("player2")
        else : print("player1")
```

    player1: 가위
    player1 = "가위"
    player2 = "보"
    player1
    


```python

```
