def graph_gen(N=3, M=3, d=1, forbidden=[]):
    graph = {}

    for i in range(N):
        for j in range(M):
            graph[(i, j)] = []

    for i in range(N):
        for j in range(M):
            if (i, j) not in forbidden:
                if i-1 != -1 and j-1 != -1 and (i-1, j-1) not in forbidden:
                    graph[(i, j)].append((d*1.41, (i-1, j-1)))  # 1 - ая ячейка
                if i-1 != -1 and 0 <= j < M and (i-1, j) not in forbidden:
                    graph[(i, j)].append((d, (i-1, j)))        # 2 - ая ячейка
                if i-1 != -1 and j+1 != M and (i-1, j+1) not in forbidden:
                    graph[(i, j)].append((d*1.41, (i-1, j+1)))  # 3 - ая ячейка
                if 0 <= i <= N and j+1 != M and (i, j+1) not in forbidden:
                    graph[(i, j)].append((d, (i, j+1)))        # 4 - ая ячейка
                if i+1 != N and j+1 != M and (i+1, j+1) not in forbidden:
                    graph[(i, j)].append((d*1.41, (i+1, j+1)))  # 5 - ая ячейка
                if i+1 != N and 0 <= j < M and (i+1, j) not in forbidden:
                    graph[(i, j)].append((d, (i+1, j)))        # 6 - ая ячейка
                if i+1 != N and j-1 != -1 and (i+1, j-1) not in forbidden:
                    graph[(i, j)].append((d*1.41, (i+1, j-1)))  # 7 - ая ячейка
                if 0 <= i < N and j-1 != -1 and (i, j-1) not in forbidden:
                    graph[(i, j)].append((d, (i, j-1)))        # 8 - ая ячейка
    return graph