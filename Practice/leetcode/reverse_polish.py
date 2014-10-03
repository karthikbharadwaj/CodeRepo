__author__ = 'karthikb'
'''
Program to evaluate reverse polish expression
'''
input = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
failed_input = ["-3","9","*"]

def reverse_polish(input):
    stack = []
    symbols = ["/","*","-","+"]
    for item in input:
        print item, stack
        if item not in symbols:
            stack.append(item)
        elif len(stack) >= 2 and item in symbols:
            a = int(stack.pop())
            b = int(stack.pop())
            if item == '/' and a != 0:
                result = float(b) / float(a)
                result = int(result)
            elif item == '*':
                result = a * b
            elif item == '+':
                result = a + b
            elif item == '-':
                result = b - a
            else:
                result = 0
            stack.append(result)
        else:
            return -1

    return stack.pop()


output = reverse_polish(input)
print output




