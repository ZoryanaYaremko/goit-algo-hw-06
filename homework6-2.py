import networkx as nx
from collections import deque

# Використовуємо граф, створений у першому завданні
G = nx.Graph()

# Додавання станцій метро як вершин графа (назви станцій)
stations = [
    "Святошин", "Нивки", "Політехнічний інститут", "Театральна", "Хрещатик", "Арсенальна", "Дарниця", 
    "Лісова", "Академмістечко", "Житомирська", "Берестейська", "Вокзальна", "Університет", 
    "Золоті ворота", "Палац спорту", "Кловська", "Печерська", "Дружби народів", "Видубичі", 
    "Славутич", "Осокорки", "Позняки", "Харківська", "Вирлиця", "Бориспільська", "Червоний хутір",
    "Лук'янівська", "Дорогожичі", "Сирець", "Либідська", "Героїв Дніпра", "Мінська", 
    "Оболонь", "Петрівка", "Тараса Шевченка", "Контрактова площа", "Поштова площа", 
    "Майдан Незалежності"
]

# Додавання ребер графа (лінії метро між станціями)
edges = [
    ("Академмістечко", "Житомирська"), ("Житомирська", "Святошин"), ("Святошин", "Нивки"),
    ("Нивки", "Берестейська"), ("Берестейська", "Політехнічний інститут"),
    ("Політехнічний інститут", "Вокзальна"), ("Вокзальна", "Університет"),
    ("Університет", "Театральна"), ("Театральна", "Хрещатик"), ("Хрещатик", "Арсенальна"),
    ("Арсенальна", "Дарниця"), ("Дарниця", "Лісова"), ("Майдан Незалежності", "Хрещатик"),
    ("Майдан Незалежності", "Поштова площа"), ("Поштова площа", "Контрактова площа"),
    ("Контрактова площа", "Тараса Шевченка"), ("Тараса Шевченка", "Петрівка"),
    ("Петрівка", "Оболонь"), ("Оболонь", "Мінська"), ("Мінська", "Героїв Дніпра"),
    ("Золоті ворота", "Театральна"), ("Золоті ворота", "Лук'янівська"),
    ("Лук'янівська", "Дорогожичі"), ("Дорогожичі", "Сирець"),
    ("Золоті ворота", "Університет"), ("Золоті ворота", "Палац спорту"),
    ("Палац спорту", "Кловська"), ("Кловська", "Печерська"), ("Печерська", "Дружби народів"),
    ("Дружби народів", "Видубичі"), ("Видубичі", "Славутич"), ("Славутич", "Осокорки"),
    ("Осокорки", "Позняки"), ("Позняки", "Харківська"), ("Харківська", "Вирлиця"),
    ("Вирлиця", "Бориспільська"), ("Бориспільська", "Червоний хутір"),
    ("Палац спорту", "Либідська")
]

# Додавання вершин і ребер до графу
G.add_nodes_from(stations)
G.add_edges_from(edges)

# Функція для пошуку всіх шляхів за допомогою DFS
def dfs_all_paths(graph, start, goal, path=[]):
    path = path + [start]
    if start == goal:
        return [path]
    paths = []
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            new_paths = dfs_all_paths(graph, neighbor, goal, path)
            for p in new_paths:
                paths.append(p)
    return paths

# Функція для пошуку всіх шляхів за допомогою BFS
def bfs_all_paths(graph, start, goal):
    queue = deque([(start, [start])])
    all_paths = []
    while queue:
        (vertex, path) = queue.popleft()
        for next in set(graph.neighbors(vertex)) - set(path):
            new_path = path + [next]
            if next == goal:
                all_paths.append(new_path)
            else:
                queue.append((next, new_path))
    return all_paths

# Вибір початкової та кінцевої станцій
start_station = "Академмістечко"
goal_station = "Либідська"

# Знаходження всіх шляхів за допомогою DFS та BFS
dfs_all_results = dfs_all_paths(G, start_station, goal_station)
bfs_all_results = bfs_all_paths(G, start_station, goal_station)

# Виведення всіх шляхів для DFS
print(f"Всі шляхи від {start_station} до {goal_station} за допомогою DFS:")
for i, path in enumerate(dfs_all_results, 1):
    print(f"Шлях {i}: {path}")

# Виведення всіх шляхів для BFS
print(f"\nВсі шляхи від {start_station} до {goal_station} за допомогою BFS:")
for i, path in enumerate(bfs_all_results, 1):
    print(f"Шлях {i}: {path}")


