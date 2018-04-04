
if __name__ == "__main__":
    limit = 10**6
    d = [1]*limit
    for i in range(2, limit//2):
        for j in range(2*i, limit, i):
            d[j] += i
    max_cl = 0
    for i in range(2, limit):
        n, chain = i, []
        while d[n] < limit:
            d[n], n = limit+1, d[n]
            try: k = chain.index(n)
            except ValueError: chain.append(n)
            else:
                if len(chain[k:]) > max_cl:
                    max_cl, min_link = len(chain[k:]), min(chain[k:])
    print(min_link) # 14316
