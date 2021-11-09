def draw_graph(N, M, result, start, goal, forbidden=[]):
    for i in range(N):
        for j in range(M):
            if (i, j) in forbidden:
                print('X', end='')
            elif i == start[0] and j == start[1]:
                print('S', end='')
            elif (i, j) in result:
                print('#', end='')
            elif i == goal[0] and j == goal[1]:
                print('F', end='')
            else:
                print('.', end='')
        print('\n', end='')
        
def draw_graph_pathless(N, M, start, goal, forbidden=[]):
    for i in range(N):
        for j in range(M):
            if (i, j) in forbidden:
                print('X', end='')
            elif i == start[0] and j == start[1]:
                print('S', end='')
            elif i == goal[0] and j == goal[1]:
                print('F', end='')
            else:
                print('.', end='')
        print('\n', end='')