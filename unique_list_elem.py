#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 17:41:53 2022
@author: parisbg

Given an array of integers, where all elements but one occur twice, find the unique element.
"""

#Create hashmap (dictionary)
#Traverse the array
#key = list element (num)
#value = # of occurences
#Find highest value in hashmap (val = # of occurences) and return that key (unique)

a = [1,0,0,9,6,9,1,6,7]
    
unique_dict = {}
for i in a:
    if i not in unique_dict.keys():   
        unique_dict[i] = 1
    else:
        unique_dict[i] += 1
        
unique = [x for x in unique_dict if unique_dict[x] == min(unique_dict.values())]
print(unique[0])
    
