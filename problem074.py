
factorials = [1,1,2,6,24,120,720,5040,40320,362880]

def facSum(n):
    """Returns the sum of the factorials of the digits of a number."""
    return sum([factorials[int(x)] for x in str(n)])

if __name__ == "__main__":
    numTerms = {169:3, 363601:3, 1454:3, 871:2, 45361:2, 872:2, 45362:2}
    result = 0
    for i in range(1, 10**6+1):
        n = i
        count = 0
        seq = [0]

        while(seq[-1] != n):
            seq.append(n)
            n = facSum(n)
            count += 1

            if (n <= 10**6 and (n in numTerms)):
                count += numTerms[n]
                break

        if (count == 60):
            result += 1

        for j in range(1, len(seq)):
            if (seq[j] <= 10**6):
                numTerms[seq[j]] = count
            count -= 1
        
    print(result) # 402
