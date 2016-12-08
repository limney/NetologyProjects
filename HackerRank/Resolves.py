#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import Counter

import numpy


array_1 = numpy.array([[1,2,3],[0,0,0]])
array_2 = numpy.array([[0,0,0],[7,8,9]])


print(array_1, array_2)

print(numpy.concatenate((array_1, array_2), axis=0))



exit()


nums = list(map(float, input().split()))

nums.sort(key=lambda x: x**2, reverse=True)
print(nums)

print(numpy.array(nums, float))



exit()












myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
print(Counter(myList))

exit()

count_sizis = int(input())

count_shoes = Counter(map(int, input().split()))

count_purchase = int(input())
purchases = []
for i in range(count_purchase):
    size, price = map(int, input().split())
    if count_shoes[size]:
        purchases += price
        count_shoes[size] -= 1
print(sum(purchases))

