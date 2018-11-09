#!/usr/bin/env python3

import operator
import math


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': math.pow,
    '//': operator.floordiv,
    '&': operator.and_,
    '|': operator.or_,
    '~': operator.inv,
    '!': operator.mul,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError: 
            if (token == '%'):
              arg2 = stack.pop()
              arg1 = stack.pop()
              arg3 = arg1 / 100
              arg3 *= arg2
              result = (arg1 + arg3)
              stack.append(result)
            elif (token == '~'):
              function = operators[token]
              arg2 = stack.pop()
              result = function(arg2)
              stack.append(result)
            elif (token == '!'):
              function = operators[token]
              arg2 = stack.pop()
              result = 1
              while (arg2 > 1):
                result = function(result, arg2)
                arg2 = arg2 - 1
              stack.append(result)
            else:
              function = operators[token]	  
              arg2 = stack.pop()
              arg1 = stack.pop()
              result = function(arg1, arg2)
              stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()
