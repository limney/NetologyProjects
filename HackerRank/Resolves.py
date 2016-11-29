#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import Counter


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

