import _pickle as cPickle
import time, copy

def exactcover(X, Y, solution = []):
    if not len(Y):
        yield sorted(solution)
    else:
        minc = None; numr = float('inf')
        for k in Y:
            if len(Y[k]) < numr:
                numr = len(Y[k])
                minc = k
        for r in Y[minc]:
            solution.append(r)
            cache = trim(X, Y, r)
            # The algorithm clones itself into subalgorithms
            for s in exactcover(X, Y, solution):
                yield s
            recover(X, Y, r, cache)
            solution.pop()

def trim(X, Y, r):
    
    cache = {} # Cache columns for recovering the last-stage problem
    for j in X[r]:
        for i in Y[j]:
            for k in X[i]:
                if k != j:
                    Y[k].remove(i) # mask rows
        cache[j] = Y.pop(j) # mask columns
    return cache

def recover(X, Y, r, cache):
    for j in reversed(X[r]): # X remains intact
        Y[j] = cache.pop(j) # recover columns
        for i in Y[j]:
            for k in X[i]:
                if k != j:
                    Y[k].add(i) # recover rows

standard, inverse = cPickle.load(open('constraints.db','rb'))

class sudoku(object):
    
    def __init__(self, ori, X = standard, Y = copy.deepcopy(inverse)):
        # Add additional constraints
        for i in range(len(ori)):
            for j in range(len(ori[i])):
                if ori[i][j] != '0':
                    trim(X, Y, (i,j,ori[i][j]))
        
        self.X = X
        self.Y = Y
        self.ori = ori
    
    def solve(self):
        start = time.time()
        self.solutions = set()
        X = self.X; Y = copy.deepcopy(self.Y)
        gensolution = exactcover(X, Y)
        for s in gensolution:
            self.solutions.add(tuple(s))
        self.elapse = time.time() - start
        self.solutions = list(self.solutions)
    
    def _report(self):
        
        print('Problem:\n')
        self.pretty_print(self.ori)
        print('Solved in %.4gs, found %d solution(s)\n' % (self.elapse,
              len(self.solutions)))
        if len(self.solutions):
            candi = self.solutions[0]
            solution = copy.deepcopy(self.ori)
            for r in candi:
                solution[r[0]][r[1]] = r[2]
            print('Solution view:\n')
            self.pretty_print(solution)
    
    def pretty_print(self, data):
        
        template = ['|','','','','|','','','','|','','','','|']
        mapidx = [1, 2, 3, 5, 6, 7, 9, 10, 11]
        string = '+-----------------------+\n'
        for i in range(len(data)):
            for j, idx in enumerate(mapidx):
                template[idx] = data[i][j]
            string += (' '.join(template)+'\n')
            if (i % 3 == 2) and (i != 8):
                string += '|-------+-------+-------|\n'
        string += '+-----------------------+\n'
        
        print(string)

def readdata(filename):
    
    problems = {}
    with open(filename) as source:
        for line in source:
            if line.startswith('G'):
                key = line.rstrip()
                problems[key] = []
            else:
                tmp = list(line.rstrip())
                if tmp:
                    problems[key].append(tmp)
    
    return problems

if __name__ == '__main__':
    problems = readdata('sudoku.txt')
    start = time.time()
    count = 0
    for p in problems:
        P = sudoku(problems[p], X = standard, Y = copy.deepcopy(inverse))
        P.solve()
        candi = P.solutions[0]
        solution = copy.deepcopy(P.ori)
        for r in candi:
            solution[r[0]][r[1]] = r[2]
        count += int(''.join(solution[0][:3]))
    elapse = time.time() - start
    print(count) # 24702
