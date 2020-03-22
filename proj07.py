# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 12:55:27 2020

@author: tjdok
"""

''' Your header goes here '''
    ###########################################################

    #  Computer Project #5

    #

    #  Algorithm

    #    prompt for an integer

    #    input an integer

    #    loop while not end-of-data

    #       call function to count number of digits in integer

    #       output the number of digits

    #       prompt for an integer

    #       input an integer

    #    display closing message

    ###########################################################
import math

def open_file():
    ''' Docstring goes here '''
    while True:
        a = input('file: ')
        try:
            b = open(a,'r')
            return b
            break
        except FileNotFoundError:
            print('fail')
    pass

def calc_multipliers():
    ''' Docstring goes here '''
    n = 2
    C = []
    while n <= 60 :
        c = 1 / (n * (n - 1)) ** (.5)
        C.append(float(c))
        n += 1
    return C
    pass
    
def calc_priorities(s,p,m):
    ''' Docstring goes here '''
    L = []
    for i in range(len(m)) :
        L.append((int(p * m),s))
    return L
    pass

def read_file_make_priorities(fp,multipliers): 
    ''' Docstring goes here '''
    reps = []
    p = []
    count = 1
    pass

def add_to_state(state,states):
    ''' Docstring goes here '''
    pass

def display(states):
    ''' Docstring goes here '''
    pass

def main():
    ''' Docstring goes here '''
    x = open_file()
    c = calc_multipliers()
    pass

if __name__ == "__main__":
    main()