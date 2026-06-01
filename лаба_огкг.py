import numpy as np
import matplotlib.pyplot as plt

class EuclideanMST:
    def __init__(self, points):
        self.points = np.array(points)
        self.num_points = len(points)
        
    def compute_distance_matrix(self):
        #обчисл матриці евклідових відстаней
        matrix = np.zeros((self.num_points, self.num_points))
        for i in range(self.num_points):
            for j in range(i + 1, self.num_points):
                #формула Евклідової відстані
                dist = np.linalg.norm(self.points[i] - self.points[j])
                matrix[i][j] = dist
                matrix[j][i] = dist
        return matrix

    def find_mst_prim(self):
        #алгоритм Прима
        dist_matrix = self.compute_distance_matrix()
        
        selected_nodes = np.zeros(self.num_points, dtype=bool)
        selected_nodes[0] = True  
        
        mst_edges = []
        total_weight = 0

        
        for _ in range(self.num_points - 1):
            minimum = float('inf')
            u, v = -1, -1
            
            for i in range(self.num_points):
                if selected_nodes[i]:
                    for j in range(self.num_points):
                        if not selected_nodes[j] and dist_matrix[i][j] > 0:
                            if minimum > dist_matrix[i][j]:
                                minimum = dist_matrix[i][j]
                                u, v = i, j
            
            selected_nodes[v] = True
            mst_edges.append((u, v))
            total_weight += minimum
            
        return mst_edges, total_weight

num_points = 100

np.random.seed(22)  #кількість точок
points = np.random.rand(num_points, 2) * 100  #площина 100*100

mst_solver = EuclideanMST(points)
edges, total_length = mst_solver.find_mst_prim()

print(f"Побудовано дерево! Сумарна довжина ребер: {total_length:.2f}")

plt.figure(figsize=(8, 8))

#ребра
for u, v in edges:
    p1 = points[u]
    p2 = points[v]
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], color='red', linewidth=2.5, zorder=1)

#точки
plt.scatter(points[:, 0], points[:, 1], color='blue', edgecolors='black', s=80, zorder=2, label='Точки множини')

plt.title("Евклідове мінімальне кістякове дерево (EMST)", fontsize=14)
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()