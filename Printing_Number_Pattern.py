
# Program 1:
"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
user_input = int(input("Enter the no of rows: "))
for i in range(1,user_input+1):
    for j in range(1,i+1):
        print(i, end=' ')
    print()

# Program 2: --- Pyramid Patten of Numbers
"""
1
12
123
1234
12345
"""
user_input = int(input("Enter the no of rows: "))
for i in range(1,user_input+1):
    for j in range(1,i+1):
        print(j, end= '')
    print()

# Program 3: --- Inverted Pyramid Pattern of Numbers
"""
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 
"""
user_input = int(input("Enter the no of rows: "))
for i in range(user_input,0,-1):
    for j in range(1,i+1):
        print(i, end=' ')
    print()

# Program 4: ---Inverted Pyramid Pattern with same digit
"""
5 5 5 5 5 
5 5 5 5 
5 5 5 
5 5 
5
"""
user_input = int(input("Enter the no of rows: "))
for i in range(user_input,0,-1):
    for j in range(1, i+1):
        print(user_input, end=' ')
    print()

# Program 5: ---Inverted half pyramid pattern with number
"""
0 1 2 3 4 5 
0 1 2 3 4 
0 1 2 3 
0 1 2 
0 1
"""
user_input = int(input("Enter the no of rows: "))
for i in range(user_input,1,-1):
    for j in range(0,i):
        print(j, end='')
    print()

# Program 6: ---Printing alternate numbers
"""
1 
3 3 
5 5 5 
7 7 7 7 
9 9 9 9 9
"""
user_input = int(input("Enter the no of rows: "))
for i in range(1,user_input+1):
    for j in range(1, i+1):
        print((i*2-1), end='')
    print()

# Program 7: ---Printing reverse number pattern
"""
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1
"""
user_input = int(input("Enter the no of rows: "))
for i in range(user_input, 0,-1):
    for j in range(1, i+1):
        print(i, end='')
    print()

# Program 8: ---Printing reverse number pattern
"""
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1
"""
user_input = int(input("Enter the no of rows: "))
for i in range(1,user_input+1):
    for j in range(i,0,-1):
        print(j, end='')
    print()

# Program 9: ---Printing reverse number pattern
"""
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
"""
user_input = int(input("Enter the no of rows: "))
for i in range(user_input,0,-1):
    for j in range(i,0,-1):
        print(j, end='')
    print()
