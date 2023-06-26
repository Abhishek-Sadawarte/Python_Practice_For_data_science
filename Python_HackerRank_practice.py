#Solving Hacker Rank problem 
#list Comprehension 
# Python List are most versatile function you can almost add anything to list 
'''list can contain 1. integers, 2.strings, 3. even lists'''
# Q1. Initialize your list and read in the value of  followed by  lines of commands where each 
# command will be of the  types listed above. Iterate through each command in order and perform 
# the corresponding operation on your list.

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

# Q2 In this challenge, the user enters a string and a substring. 
# You have to print the number of times that the substring occurs in the given string. 
# String traversal will take place from left to right, not from right to left.
string = "ABCDCDC"
sub_string = "CDC"
def count_substring(string, sub_string):
    count = 0 
    n = len(string)
    m = len(sub_string)
    for i in range(n-m+1):
        if string[i:i+m] == sub_string:
            count += 1
    return count

count_substring(string,sub_string)

'''SwapCase
Q3. swap given string, if string contain Upeprcase char then to lower or vice versa
input = Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  '''

def SwapCase(s):
    output = ""
    for i in s:
        if i.islower():
            output += i.upper()
        else:
            output += i.lower()
    return output

