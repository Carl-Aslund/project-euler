
def spiralSum(n):
    """Calculates the sum of an nxn spiral."""
    N = n//2
    return (int) (16*N**3/3 + 10*N**2 + 26*N/3 + 1.5)

print(spiralSum(1001)) # 669171001
