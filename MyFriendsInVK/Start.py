#!/usr/bin/env python
# -*- coding: utf-8 -*-


import networkx as nx
import matplotlib.pyplot as plt
from vk_client import UserVK
import pickle
from collections import Counter

"""
В файле vk_client.py я реализовал загрузки из ВК своих друзей и их друзей.
Загрузка с ВК занимает много времени, поэтому я сохранил результат, и тут работаю с уже сохраненной версией моих друзей.
"""

my_friends = []
# Читаем объект my_friends (JSON сериализация)
with open('my_friends.pickle', 'rb') as f:
    my_friends = pickle.load(f)


# Найдем общих друзей среди моих друзей в ВК
general_friends = Counter()

for my_friend in my_friends:
    general_friends[my_friend.my_name] += 1
    for friend_my_friend in my_friend.friends:
        general_friends[friend_my_friend.my_name] += 1

print(" Общие друзья моих друзей в ВК:")
count_general_friends = 0
for friend, count in general_friends.items():
    if count > 1:
        print(friend, count)
        count_general_friends += 1
print("Общее количество общих друзей: %d" % count_general_friends)

# Сформируем граф моих друзей
my_graph = nx.Graph()
i_am = UserVK({"first_name": "Дмитрий", "last_name": "Климов"})  # это я
my_graph.add_node(0, name=i_am.profile["last_name"])

for index, my_friend in enumerate(my_friends):
    my_graph.add_node(index+1, name=my_friend.profile["last_name"])
    my_graph.add_edge(0, index+1)

# Отрисуем граф
nx.draw(my_graph, node_color='b')
plt.show()

