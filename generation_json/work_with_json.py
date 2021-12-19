def DATA2JSON(X, Y, filename, str_format = '05d', digits = 3):
    n = len(X)
    data = dict()
    for i in range(n):
        data[format(i, str_format)] = {'X':round(X[i], digits), 'Y':round(Y[i], digits)}
    with open(filename, "w") as outfile:
        json.dump(data, outfile, indent=4)
        
def JSON2DATA(filename, str_format = '05d', digits = 3):
    with open(filename) as infile:
        data = load(infile)
    N = len(data)
    X = np.zeros(N)
    Y = np.zeros(N)

    for i in range(N):
        X[i] = data[format(i, str_format)]['X']
        Y[i] = data[format(i, str_format)]['Y']
    return X,Y