# 백준 문제번호 - 1260

n, m, v = map(int, input().split()) # n:정점의 개수/ m:간선의 개수 / v:탐색을 시작할 정점의 번호

# 정점이 n개일 때, n*n크기의 이차원 배열을 생성한다.
a = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(m):  # m : 간선의 개수
    x, y = map(int, input().split())

    # x와 y가 연결되어있음을 의미함. 양방향이므로 방향은 무의미.
    a[x][y] = a[y][x] = 1

def dfs(start_node, visited_node):
    # 모든 노드를 돌아다니면서 한 노드 다 팔 때 까지
    # stack에 시작노드를 입력하고
    # visited node에 시작노드를 입력하면서 pop
    # visited 하지않은 노드 다 방문
    stack = [start_node]
    while stack:
        current_node = stack.pop()
        visited_node.append(current_node)
        for i in range(len(a[start_node])):
            if a[start_node][i] == 1 and (i not in visited_node):
                dfs(i, visited_node)
    return visited_node

def bfs(start_node, visited_node):
    visited_node = []
    queue = [start_node]  # startnode에서 시작한다
    while queue:
        current_node = queue.pop(0)
        visited_node.append(current_node)
        # 그래프 내의 start node열의 개수만큼(연결가능한?) for문,
        for i in range(len(a[start_node])):
            # 현재노드와 인접한 노드가 연결되어있고, i값을 방문하지않았다면
            if a[current_node][i] == 1 and (i not in visited_node) and (i not in queue):
                queue.append(i)
    return visited_node

print(" ".join(map(str, dfs(v, []))))
print(" ".join(map(str, bfs(v, []))))