
#예제 1

list_variable = [0, 1, 2, 3, 4, 5, 6]
list_variable.pop()
list_variable.append(7)
list_variable.append(8)

for element in list_variable[2:]:
    print(element, end=" ")
    
"""
예측을 작성하세요.
1 6
2 [0,1,2,3,4,5,7]
3 [0,1,2,3,4,5,7,8]
4 2 3 4 5 6 7 8

"""

#예제 2

for element in range(-2, 10, 2):
    print(element, end=" ")
    
"""
예측을 작성하세요.
1 -2 0 2 4 6 7 8 
"""

#예제 3

a, b, c, d = 0, 0, 0, 0
n = 10

for number in range(n):
    if number % 2 == 0: 
        a = a + 1 # 이거 몇개야 -> 짝수면 한번 올려 0 2 4 6 8  -> 5
        
    if number % 3 == 0:
        b = b + 1 # 3으로 나눠 떨어지면 한번 올려 0 3 6 9-> 4
        
    if number % 4 == 0:
        c = c + 1 # 4로 나눠 떨어지면 한번올려 0 4 8 -> 3
        
    if number % 5 == 0:
        d = d + 1 # 5로 나눠 떨어지면 한번 올려 0 5 -> 2

print(a, b, c, d) # 5 4 3 2

#예제 4

i = 0
while i <= 10:
    print(i)
    i = i + 1
"""
예측을 작성하세요.
1 0
2 1
3 2
4 3
5 4
6 5
7 6
8 7
9 8
10 9
11 10
"""

#예제 5

while i <= 10:
    i = i + 1
    print(i)
"""
예측을 작성하세요.
i에 대한 초기화를 안했기 때문에 출력 안됨
"""

#예제 6

i = 0
while i <= 10:
    i = i + 2
    print(i)
"""
예측을 작성하세요.
1 2
2 4
3 6
4 8
5 10
6 12
"""

#예제 7
# while True는 특별한 일이 없는 한 계속해서 반복문을 진행하겠다는 무한반복문의 의미를 지니게 됨
while True:
    print(i) 
    i = i + 1
    if i > 10:
        break
"""
예측을 작성하세요.
1 0
2 1
3 2
4 3
5 4
6 5
7 6 
8 7
9 8
10 9
11 10
"""

#예제 8

i = 0
while True:
    print(i) 
    if i > 10:
        break
    i = i + 1
    
"""
예측을 작성하세요.
1 0
2 1
3 2
4 3
5 4
6 5
7 6 
8 7
9 8
10 9
11 10
12 11
"""

#예제 9

list_variable = [0, 1, 2, 3, 4, 5, 6]
print(len(list_variable)) # 7

#예제 10

list_variable = [0, 1, 2, 3, 4, 5, 6]
print(sum(list_variable)) # 21

#예제 11

list_variable = [3, 1, 4, -3, 9, 7]
print(min(list_variable) - max(list_variable)) # 6(?)