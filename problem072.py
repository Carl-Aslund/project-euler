
if __name__ == "__main__":
    phi = list(range(10**6+1))
    for n in range(2, 10**6+1):
        if phi[n] == n:
            for k in range(n, 10**6+1, n):
                phi[k] -= phi[k]//n
    print(sum(phi)-1) # 303963552391
