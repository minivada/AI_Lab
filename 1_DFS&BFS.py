def dfs(visited,graph,node):
    if node not in visited:
        print(node,end=" ")
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)
def bfs(visited,graph,node,queue):
    visited.add(node)
    queue.append(node)
    while queue:
        s=queue.pop(0)
        print(s,end=" ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
def main():
    visited_dfs=set()
    visited_bfs=set()
    queue=[]
    graph={
        1:[2,3],
        2:[4,5],
        3:[6,7],
        4:[],
        5:[],
        6:[],
        7:[]

    }
    print("the following dfs")
    dfs(visited_dfs,graph,1)
    print()
    print("the following Bfs")
    bfs(visited_bfs,graph,1,queue)


if __name__=="__main__":
    main()


    