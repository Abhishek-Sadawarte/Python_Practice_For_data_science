#Solving Hacker Rank problem 
#list Comprehension 
# Python List are most versatile function you can almost add anything to list 
'''list can contain 1. integers, 2.strings, 3. even lists'''
# Q1. Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

N = int(input())
output = []
for i in range(N):
    command = input().split(' ')
    if command[0] == 'insert':
        output.insert(int(output[0]), int(output[1]))
    elif command[0] == 'remove':
        output.remove(int(command[1]))
    elif command[0] == 'append':
        output.append(int(command[1]))
    elif command[0] == 'sort':
        output.sort()
    elif command[0] == 'pop':
        output.pop()
    elif command[0] == 'reverse':
        output.reverse()
    elif command[0] == 'print':
        print(output)

