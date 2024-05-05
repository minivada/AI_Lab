class DisjointSetUnionFind:
    def __init__(self, size):
        self.parent = [-1] * size
        self.rank = [0] * size

    def find(self, v):
        if self.parent[v] == -1:
            return v
        self.parent[v] = self.find(self.parent[v])  # Path compression
        return self.parent[v]

    def union(self, fromP, toP):
        if self.rank[fromP] > self.rank[toP]:
            self.parent[toP] = fromP
        elif self.rank[fromP] < self.rank[toP]:
            self.parent[fromP] = toP
        else:
            self.parent[fromP] = toP
            self.rank[toP] += 1


def kruskal(edges, vertices):
    edges.sort(key=lambda x: x[2])  # Sort edges based on weights
    mst = []
    dsuf = DisjointSetUnionFind(vertices)
    for edge in edges:
        src, dest, wt = edge
        fromP = dsuf.find(src)
        toP = dsuf.find(dest)
        if fromP != toP:  # If including this edge doesn't create a cycle
            mst.append(edge)
            dsuf.union(fromP, toP)
    return mst


# Example usage
if __name__ == "__main__":
    edges = [
        (0, 1, 4),
        (0, 7, 8),
        (7, 1, 11),
        (1, 2, 8),
        (7, 8, 7)
    ]
    vertices = 9  # Number of vertices assuming the vertices are numbered from 0 to 8
    minimum_spanning_tree = kruskal(edges, vertices)
    print("Minimum Spanning Tree:")
    for edge in minimum_spanning_tree:
        print(edge)
