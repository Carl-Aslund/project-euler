from math import factorial

def permuter(L, n):
    """Computes the nth lexographic permutation of the elements in L."""
    if len(L) == 1:
        return [L[0]]
    else:
        index = 0
        miniPermute = factorial( len(L)-1 ) # Permutations per starting point
        while(n > miniPermute):
            index += 1
            n -= miniPermute
            if index >= len(L):
                print("ERROR")
                return
        indexElement = L[index]
        leftoverList = L[:index]+L[index+1:]
        return [indexElement] + permuter(leftoverList, n)

permuterList = permuter(list(range(10)), 1000000)
print(''.join([str(x) for x in permuterList])) # 2783915460
