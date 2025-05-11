#!/usr/bin/env python3

def return_evens(num_list = range(0,10)):
   return [num for num in num_list if num % 2 == 0 ]
print(return_evens())

def make_exclamation(sentence_list):
    return [ sentence + "!" for sentence in sentence_list]