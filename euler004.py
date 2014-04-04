# -*- coding: utf-8 -*-
"""
A palindromic number reads the same both ways. The largest palindrome made from 
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def get_largest_palindrome(digits=3):
    palindrome = 0
    start = 10 ** (digits-1)
    end = 10 ** digits
    for first in xrange(end-1, start, -1):
        for second in xrange(end-1, start, -1):
            result = first * second
            if result <= palindrome:
                break
            elif (is_palindrome(result) and result > palindrome):
                palindrome = result
    return palindrome

if __name__ == '__main__':
    palindrome = get_largest_palindrome(3)
    print palindrome
