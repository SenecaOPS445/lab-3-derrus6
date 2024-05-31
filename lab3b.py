#!/usr/bin/env python3
'''Lab 3 Part 1 script - functions'''
# Author ID: drussell6 

def sum_numbers(number1, number2):
    sum = int(number1) + int(number2)
    return sum

def subtract_numbers(number1, number2):
    diff = int(number1) - int(number2)
    return diff

def multiply_numbers(number1, number2):
    prod = int(number1) * int(number2)
    return prod

if __name__ == '__main__':
    print(sum_numbers(10, 5))
    print(subtract_numbers(10, 5))
    print(multiply_numbers(10, 5))