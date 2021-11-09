from random import randint

def forbidden_gen_rectangle(start, goal):
    forbidden = []
    for i in range(start[0], goal[0] + 1):
        for j in range(start[1], goal[1] + 1):
            forbidden.append((i,j))
    return set(forbidden)

def forbidden_random(N, M, k=0):
    forbidden = set()
    for _ in range(k):
        f1 = randint(0, N-1)
        f2 = randint(0, M-1)
        forbidden.add((f1,f2))
    return forbidden