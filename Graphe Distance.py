graph = {'A': {'B': 1, 'C':2},
         'B': {'C': 3, 'D':4},
         'C': {'D': 5},
         'D': {'C': 6},
         'E': {'F': 7},
         'F': {'C': 8}}

from pprint import pprint
pprint(graph)


def find_all_paths(graph, start, end, path=None):
    if not path:
        path = []
    path = path + [start]

    if start == end:
        return [path]

    if start not in graph:
        return []

    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


all_paths = find_all_paths(graph, 'A', 'D')


def fina_path_distance(paths, graph):
    l = []
    buff_dict = {}
    for i in all_paths:
        distance = 0
        for k, v in enumerate(i[:-1]):
            distance += graph[v][i[k + 1]]
        l.append(distance)
        buff_dict[distance] = i
    return l, buff_dict


l, buff_dict = fina_path_distance(all_paths, graph)
for i in sorted(l):
    print(buff_dict[i])