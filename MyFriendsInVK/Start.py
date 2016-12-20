#!/usr/bin/env python
# -*- coding: utf-8 -*-


import networkx as nx
import matplotlib.pyplot as plt


ID_APP = 5786550





params = {
    "access_token": KEY,
    "v": VERSION
}

response = requests.get("https://api.vk.com/method/freinds.getOnline", params)

for user_id in response.json()['response']:
    response = requests.get("https://api.vk.com/method/users.get", {"user_id": user_id})
    print(user_id)

exit()

my_graph = nx.Graph()




my_graph.add_node(1, name="Nick")
my_graph.add_node(2, name="Jack")
my_graph.add_edge(1, 2)

nx.draw(my_graph)
plt.show()

# print(my_graph.)

