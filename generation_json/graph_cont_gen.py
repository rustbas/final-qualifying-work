
    Y_sort = np.sort(Y)

    for i in tqdm(range(N)):
        for j in range(N):
            i_t = np.where(X_sort == X[i])[0][0]
            j_t = np.where(Y_sort == Y[j])[0][0]
            if i_t == 0 and j_t == 0:
    #             print(X_sort, X, X_sort[i_t], Y[j_t], sep='\n')
                graph[(X[i], Y[j])] = {(X_sort[i_t], Y_sort[j_t + 1]): 
                                       ((X_sort[i_t] - X[i])**2 + ((Y_sort[j_t + 1] - Y[j])**2)**0.5),

                                       (X_sort[i_t+1], Y_sort[j_t + 1]): 
                                       ((X_sort[i_t+1] - X[i])**2 + ((Y_sort[j_t + 1] - Y[j])**2)**0.5),

                                      (X_sort[i_t+1], Y_sort[j_t]): 
                                       ((X_sort[i_t+1] - X[i])**2 + ((Y_sort[j_t] - Y[j])**2)**0.5)}
            elif i_t == 0 and 0 < j_t < N-1:
                graph[(X[i], Y[j])] = {(X_sort[i_t], Y_sort[j_t + 1]): 
                                       ((X_sort[i_t] - X[i])**2 + ((Y_sort[j_t + 1] - Y[j])**2)**0.5),

                                       (X_sort[i_t+1], Y_sort[j_t + 1]): 
                                       ((X_sort[i_t+1] - X[i])**2 + ((Y_sort[j_t + 1] - Y[j])**2)**0.5),

                                       (X_sort[i_t+1], Y_sort[j_t]): 
                                       ((X_sort[i_t+1] - X[i])**2 + ((Y_sort[j_t] - Y[j])**2)**0.5),

                                       (X_sort[i_t], Y_sort[j_t - 1]): 
                                       ((X_sort[i_t] - X[i])**2 + ((Y_sort[j_t - 1] - Y[j])**2)**0.5),

                                       (X_sort[i_t+1], Y_sort[j_t - 1]): 
                                       ((X_sort[i_t+1] - X[i])**2 + ((Y_sort[j_t - 1] - Y[j])**2)**0.5)}

            elif i_t == 0 and j_t == N-1:
                graph[(X[i], Y[j])] = {(X_sort[i_t], Y_sort[j_t-1]): 
                                       ((X_sort[i_t] - X[i])**2 + ((Y_sort[j_t-1] - Y[j])**2)**0.5),

                                       (X_sort[i_t+1], Y_sort[j_t-1]): 
                                       ((X_sort[i_t+1] - X[i])**2 + ((Y_sort[j_t-1] - Y[j])**2)**0.5),

                                       (X_sort[i_t+1], Y_sort[j_t]): 
                                       ((X_sort[i_t+1] - X[i])**2 + ((Y_sort[j_t] - Y[j])**2)**0.5)}

            elif 0 < i_t < N-1 and 0 < j_t < N-1:
                graph[(X[i], Y[j])] = {(X_sort[i_t-1], Y_sort[j_t]): 
                                       ((X_sort[i_t-1] - X[i])**2 + ((Y_sort[j_t] - Y[j])**2)**0.5),

                                       (X_sort[i_t-1], Y_sort[j_t-1]): 
                                       ((X_sort[i_t-1] - X[i])**2 + ((Y_sort[j_t-1] - Y[j])**2)**0.5),

                                       (X_sort[i_t], Y_sort[j_t-1]): 
                                       ((X_sort[i_t] - X[i])**2 + ((Y_sort[j_t-1] - Y[j])**2)**0.5),

                                       (X_sort[i_t+1], Y_sort[j_t-1]): 
                                       ((X_sort[i_t+1] - X[i])**2 + ((Y_sort[j_t-1] - Y[j])**2)**0.5),

                                       (X_sort[i_t], Y_sort[j_t]): 
                                       ((X_sort[i_t] - X[i])**2 + ((Y_sort[j_t] - Y[j])**2)**0.5)}

            elif i_t == N-1 and j_t == N-1:
                graph[(X[i], Y[j])] = {(X_sort[i_t-1], Y_sort[j_t]): 
                                       ((X_sort[i_t-1] - X[i])**2 + ((Y_sort[j_t] - Y[j])**2)**0.5),

                                       (X_sort[i_t-1], Y_sort[j_t-1]): 
                                       ((X_sort[i_t-1] - X[i])**2 + ((Y_sort[j_t-1] - Y[j])**2)**0.5),

                                       (X_sort[i_t], Y_sort[j_t-1]): 
                                       ((X_sort[i_t] - X[i])**2 + ((Y_sort[j_t-1] - Y[j])**2)**0.5)}

            elif i_t == N-1 and 0 < j_t < N-1:
                graph[(X[i], Y[j])] = {(X_sort[i_t], Y_sort[j_t+1]): 
                                       ((X_sort[i_t] - X[i])**2 + ((Y_sort[j_t+1] - Y[j])**2)**0.5),

                                       (X_sort[i_t-1], Y_sort[j_t+1]): 
                                       ((X_sort[i_t-1] - X[i])**2 + ((Y_sort[j_t+1] - Y[j])**2)**0.5),

                                       (X_sort[i_t-1], Y_sort[j_t]): 
                                       ((X_sort[i_t-1] - X[i])**2 + ((Y_sort[j_t] - Y[j])**2)**0.5),

                                       (X_sort[i_t-1], Y_sort[j_t-1]): 
                                       ((X_sort[i_t-1] - X[i])**2 + ((Y_sort[j_t-1] - Y[j])**2)**0.5),

                                       (X_sort[i_t], Y_sort[j_t-1]): 
                                       ((X_sort[i_t] - X[i])**2 + ((Y_sort[j_t-1] - Y[j])**2)**0.5)}

            elif i_t == N-1 and j_t == 0:
                graph[(X[i], Y[j])] = {(X_sort[i_t], Y_sort[j_t+1]): 
                                       ((X_sort[i_t] - X[i])**2 + ((Y_sort[j_t+1] - Y[j])**2)**0.5),

                                       (X_sort[i_t-1], Y_sort[j_t+1]): 
                                       ((X_sort[i_t-1] - X[i])**2 + ((Y_sort[j_t+1] - Y[j])**2)**0.5),

                                       (X_sort[i_t-1], Y_sort[j_t]): 
                                       ((X_sort[i_t-1] - X[i])**2 + ((Y_sort[j_t] - Y[j])**2)**0.5)}

            elif 0 < i_t < N-1 and j_t == 0:
                graph[(X[i], Y[j])] = {(X_sort[i_t+1], Y_sort[j_t]): 
                                       ((X_sort[i_t+1] - X[i])**2 + ((Y_sort[j_t] - Y[j])**2)**0.5),

                                       (X_sort[i_t+1], Y_sort[j_t+1]): 
                                       ((X_sort[i_t+1] - X[i])**2 + ((Y_sort[j_t+1] - Y[j])**2)**0.5),

                                       (X_sort[i_t], Y_sort[j_t+1]): 
                                       ((X_sort[i_t] - X[i])**2 + ((Y_sort[j_t+1] - Y[j])**2)**0.5),

                                       (X_sort[i_t-1], Y_sort[j_t+1]): 
                                       ((X_sort[i_t-1] - X[i])**2 + ((Y_sort[j_t+1] - Y[j])**2)**0.5),

                                       (X_sort[i_t-1], Y_sort[j_t]): 
                                       ((X_sort[i_t-1] - X[i])**2 + ((Y_sort[j_t] - Y[j])**2)**0.5)}
                
            elif 0 < i_t < N-1 and j_t == N-1:
                graph[(X[i], Y[j])] = {(X_sort[i_t-1], Y_sort[j_t]): 
                                       ((X_sort[i_t-1] - X[i])**2 + ((Y_sort[j_t] - Y[j])**2)**0.5),

                                       (X_sort[i_t-1], Y_sort[j_t-1]): 
                                       ((X_sort[i_t-1] - X[i])**2 + ((Y_sort[j_t-1] - Y[j])**2)**0.5),

                                       (X_sort[i_t], Y_sort[j_t-1]): 
                                       ((X_sort[i_t] - X[i])**2 + ((Y_sort[j_t-1] - Y[j])**2)**0.5),

                                       (X_sort[i_t+1], Y_sort[j_t-1]): 
                                       ((X_sort[i_t+1] - X[i])**2 + ((Y_sort[j_t-1] - Y[j])**2)**0.5),

                                       (X_sort[i_t+1], Y_sort[j_t]): 
                                       ((X_sort[i_t+1] - X[i])**2 + ((Y_sort[j_t] - Y[j])**2)**0.5)}
    return graph