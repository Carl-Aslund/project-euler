
def uniquePowers(n):
    """Find the number of unique values of a**b for 2 <= a,b <= n."""
    powers = set()
    for a in range(2,n+1):
        for b in range(2,n+1):
            powers.add(a**b)
    return len(powers)

print(uniquePowers(100)) # 9183
