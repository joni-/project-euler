# -*- coding: utf-8 -*-
"""
A palindromic number reads the same both ways. The largest palindrome made from 
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def get_largest_palindrome():
    palindrome = 0
    for first in xrange(100, 1000):
        for second in xrange(100, 1000):
            result = first * second
            if is_palindrome(result) and result > palindrome:
                palindrome = result
    return palindrome

if __name__ == '__main__':
    palindrome = get_largest_palindrome()
    print palindrome
