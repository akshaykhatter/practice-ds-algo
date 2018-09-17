# https://www.hackerrank.com/challenges/balanced-brackets/problem
no_of_test_cases = int(input())

class Stack:
    def __init__(self):
        self.list = []
    
    def __repr__(self):
        return str(self.list)

    def size(self):
        return len(self.list)
    
    def push(self, value: str):
        self.list.append(value)
    
    def pop(self) -> str:
        return self.list.pop()
    
    def peek(self):
        if len(self.list) != 0:
            return self.list[-1]
        else:
            return None

def check_pair(s1, s2):
    if s1 == '{' and s2 == '}':
        return True
    elif s1 == '(' and s2 == ')':
        return True
    elif s1 == '[' and s2 == ']':
        return True
    else:
        return False

def isBalanced(s):
    stack = Stack()

    for char in s:
        if check_pair(stack.peek(), char):
            stack.pop()
        else:
            stack.push(char)

    if stack.size() == 0:
        return 'YES'
    else:
        return 'NO'

for _ in range(no_of_test_cases):
    s = input()
    result = isBalanced(s)
    print(result)