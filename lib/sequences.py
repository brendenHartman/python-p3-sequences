#!/usr/bin/env python3

def print_fibonacci(length):
    fib_list = []
    if length > 0:
        if length == 1:
            fib_list = [0]
        elif length == 2:
            fib_list = [0,1]
        else:
            fib_list = [0,1]
            i = 0
            for i in range(length - 2):
                fib_list.append(fib_list[i] + fib_list[i + 1])
    print(fib_list)