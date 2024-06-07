from sympy import symbols, simplify, summation, sympify

# Colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def not_p(p):
  print(f"{bcolors.OKCYAN}p | ¬p{bcolors.ENDC}")
  print(f"{bcolors.OKCYAN}------{bcolors.ENDC}")
  print(f"{bcolors.OKCYAN}T | F{bcolors.ENDC}")
  print(f"{bcolors.OKCYAN}F | T{bcolors.ENDC}")

  if p == "F" or p == "f":
    return "T"
  else:
     return "F"
  
########################################################################

def p_OR_q(p, q):
  print(f"{bcolors.OKCYAN}p | q | p v q{bcolors.ENDC}")
  print(f"{bcolors.OKCYAN}-------------{bcolors.ENDC}")
  print(f"{bcolors.OKCYAN}F | F |   F{bcolors.ENDC}")
  print(f"{bcolors.OKCYAN}T | F |   T{bcolors.ENDC}")
  print(f"{bcolors.OKCYAN}F | T |   T{bcolors.ENDC}")
  print(f"{bcolors.OKCYAN}T | T |   T{bcolors.ENDC}")
  print()


  print(f"{bcolors.OKCYAN}p | q | p v q{bcolors.ENDC}")
  print(f"{bcolors.OKCYAN}-------------{bcolors.ENDC}")
  return (f"{p} | {q} |   {p or q}")

########################################################################


def p_AND_q(p, q):
  print(f"{bcolors.OKCYAN}p | q | p ^ q{bcolors.ENDC}")
  print(f"{bcolors.OKCYAN}-------------{bcolors.ENDC}")
  print(f"{bcolors.OKCYAN}F | F |   F{bcolors.ENDC}")
  print(f"{bcolors.OKCYAN}T | F |   F{bcolors.ENDC}")
  print(f"{bcolors.OKCYAN}F | T |   F{bcolors.ENDC}")
  print(f"{bcolors.OKCYAN}T | T |   T{bcolors.ENDC}")
  print()

  print(f"{bcolors.OKCYAN}p | q | p ^ q{bcolors.ENDC}")
  print(f"{bcolors.OKCYAN}-------------{bcolors.ENDC}")
  return (f"{p} | {q} |   {p and q}")

########################################################################


def p_SO_q(p, q):
  print(f"{bcolors.OKCYAN}p | q | p → q{bcolors.ENDC}")
  print(f"{bcolors.OKCYAN}-------------{bcolors.ENDC}")
  print(f"{bcolors.OKCYAN}F | F |   T{bcolors.ENDC}")
  print(f"{bcolors.OKCYAN}T | F |   F{bcolors.ENDC}")
  print(f"{bcolors.OKCYAN}F | T |   T{bcolors.ENDC}")
  print(f"{bcolors.OKCYAN}T | T |   T{bcolors.ENDC}")
  print()

  print(f"{bcolors.OKCYAN}p | q | p → q{bcolors.ENDC}")
  print(f"{bcolors.OKCYAN}-------------{bcolors.ENDC}")
  if (p == "T" or p == "t") and (q == "F" or q == 'f'):
    return (f"{p} | {q} |   F")
  else:
     return (f"{p} | {q} |   T")


########################################################################


def p_biimplication_q(p, q):
  print(f"{bcolors.OKCYAN}p | q | p ↔ q{bcolors.ENDC}")
  print(f"{bcolors.OKCYAN}-------------{bcolors.ENDC}")
  print(f"{bcolors.OKCYAN}F | F |   T{bcolors.ENDC}")
  print(f"{bcolors.OKCYAN}T | F |   F{bcolors.ENDC}")
  print(f"{bcolors.OKCYAN}F | T |   F{bcolors.ENDC}")
  print(f"{bcolors.OKCYAN}T | T |   T{bcolors.ENDC}")
  print()

  print(f"{bcolors.OKCYAN}p | q | p ↔ q{bcolors.ENDC}")
  print(f"{bcolors.OKCYAN}-------------{bcolors.ENDC}") 
  if p == q :
    return (f"{p} | {q} |   T")
  else:
     return (f"{p} | {q} |   F")
  
########################################################################

def Cardinality(setA):
  return len(setA)

########################################################################

def Union(setA, setB):
  setAB =  setA | setB
    
  # Will put the set in ascending order
  setAB = sorted(setAB)
  return setAB

'''
setA = {1, 2, 3, 6}
setB = {1, 2, 6, 9}

setAB = Union(setA, setB)
print(setAB)

'''

#########################################################################

def Intersection(setA, setB):
  setAB =  setA & setB
  
  # Will put the set in ascending order
  setAB = sorted(setAB)
  return setAB

'''
setA = {1, 2, 3, 6}
setB = {1, 2, 6, 9}

setAB = Intersection(setA, setB)
print(setAB)
'''
#########################################################################


# Subset(or equal)/check_if_is_contained( or equal ) of two sets
def Contained_or_IsSubset(setA, setB):
  print(f"{bcolors.OKCYAN}A subset relation between two sets exists when all elements of one set are also elements of the other set, defining a contained or subset relationship.{bcolors.ENDC}")
  setAB =  setA.issubset(setB)
  return setAB

'''
setA = {1, 2, 69}
setB = {1, 2, 6, 9, 8, 2, 69, 50135}

setAB = Contained_or_IsSubset(setA, setB)
print(setAB)
'''
#########################################################################

# Check if x is a element in set
def IsElement(x, user_setB):
  return x in user_setB
    
'''
x = 1
set = {1, 2, 3}

element = IsElement(x, set)
print(element)
'''

#########################################################################

# Subtraction of two sets
def Subtraction(setA, setB):
  setAB = setA.difference(setB)
  return setAB

'''
setA = {4, 2, 6}
setB = {1, 2, 3}

setAB = Subtraction(setA, setB)
print(setAB)
'''

#########################################################################


# Complement of setA = A' or A^c
def Complement(setUniversal, setA):
  setComplement = setUniversal - setA
  return sorted(setComplement)

'''
setUniversal = [1, 2, 3, 4, 5, 6]
setA = [1, 2, 3]

setComplement = Complement(setUniversal, setA)
print(setComplement)
'''

#########################################################################


# Cartesian Product of two sets
def CrtProd(setA, setB):
  setAB = [(x, y) for x in setA for y in setB]
  return setAB


'''
setA = [4, 2, 6]
setB = [1, 2, 3]

setAB = CrtProd(setA, setB)
print(setAB)
'''

#########################################################################


# Partition of a set = P(a)
def Partition(setPartition):
    setPartition = set(setPartition)  # Convert to set for set operations
    if len(setPartition) == 1:
        yield [setPartition]
        return

    first = next(iter(setPartition))
    for smaller in Partition(setPartition - {first}):
        # Convert each subset in smaller to sets for set operations
        smaller_sets = [set(subset) for subset in smaller]
        
        # insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller_sets):
            yield smaller[:n] + [[first] + list(subset)] + smaller[n + 1:]
        # put `first` in its own subset
        yield [[first]] + smaller

# Function to print partitions
def print_partitions(partitions):
    for partition in partitions:
        print(f"          {bcolors.FAIL}{partition}{bcolors.ENDC}")

'''setPartition = [1, 2, 3, 4]
print(setPartition)
print("")

print("1 [NULL]")
for n, p in enumerate(partition(setPartition), 2):
    print(n, sorted(p))'''

#########################################################################

# Simetric Difference A△B=(A∪B)−(A∩B)
def SimetricDifference(setA, setB):
  setAB = setA.symmetric_difference(setB)
  return sorted(setAB)

#########################################################################


# Logical Operators (p->q, p<->q, ¬p...) 
def p(p1):
  res = str(input(p1 + "?(T/F) "))
  if res == 'T' or res == 't':
      return True
  elif res == 'F' or res == 'f':
      return False
        
def q(q1):
  res = str(input(q1 + "?(T/F) "))
  if res == 'T' or res ==  't':
      return True
  elif res == 'F' or res ==  'f':
      return False
    

#########################################################################
# for all elements on set, will evaluate if the each Xi is true in Px

# Universal Quantifier 
def For_all_x(setA):
    for x in setA:
        if not (x%2 == 0):# Put your Px here
            return False
        else:
            pass
    return True
    
'''
Read as ´There is at least one value x in the set A, where Px is valid´
Mental Note: with lambda and functional programming i can pass another function as parameter: For_all_x(setA,Px(setA[i]))
setA=[2,4,6,8]
print(For_all_x(setA))'''


#########################################################################
# will look for one element on set that makes Px be true

# Existencial Quantifier 
def Exist_x(setA):
    for x in setA:
        if (x%2 == 0):# Put your Px here
            return True
        else:
            pass
    return False
    
'''setA=[1,3,5,9]

Exist_x(setA) 
print(Exist_x(setA))'''

#########################################################################

def Sum_of_Matrix(matA, matB):
    if len(matA) != len(matB) or len(matA[0]) != len(matB[0]):
        return "Matrices must have the same dimensions for addition."
    
    result = [[0 for _ in range(len(matA[0]))] for _ in range(len(matA))]
    
    for i in range(len(matA)):
        for j in range(len(matA[0])):
            result[i][j] = matA[i][j] + matB[i][j]
    
    return result

#########################################################################

def Sub_of_Matrix(matA, matB):
    if len(matA) != len(matB) or len(matA[0]) != len(matB[0]):
        return "Matrices must have the same dimensions for addition."
    
    result = [[0 for _ in range(len(matA[0]))] for _ in range(len(matA))]
    
    for i in range(len(matA)):
        for j in range(len(matA[0])):
            result[i][j] = matA[i][j] - matB[i][j]
    
    return result

#########################################################################

def Mult_of_Matrix(matA, matB):
    if len(matA) != len(matB) or len(matA[0]) != len(matB[0]):
        return "Matrices must have the same dimensions for addition."
    
    result = [[0 for _ in range(len(matA[0]))] for _ in range(len(matA))]
    
    for i in range(len(matA)):
        for j in range(len(matA[0])):
            result[i][j] = matA[i][j] * matB[i][j]
    
    return result

#########################################################################

def Transpose(mat, N):
  tr = [ [0 for j in range(len(mat[0])) ] for i in range(len(mat)) ]  
  for i in range(N):
    for j in range(N):
      tr[i][j] = mat[j][i]
      print(f"{bcolors.FAIL}{tr[i][j]}{bcolors.ENDC}",end='  ')
    print()

'''
mat = [ [ 1, 2, 3 ], 
        [ 4, 5, 6 ], 
        [ 7, 8, 9 ] ]

transpose(mat,3)
'''

#########################################################################

def isSymmetric(mat, N):
    for i in range(N):
        for j in range(N):
            if (mat[i][j] != mat[j][i]):
                return False
    return True
   
'''
mat = [ [ 1, 3, 5 ], 
        [ 3, 2, 4 ], 
        [ 5, 4, 1 ] ]

if (isSymmetric(mat, 3)):
    print("Yes")
else:
  print("No")
'''

#########################################################################


def Summation(exp,i,n):
    j=i
    parts=[]
    while j<=n:
        x=j
        res = eval(exp)
        parts.append(res)
        j=j+1
    print(f"{bcolors.FAIL}{parts}{bcolors.ENDC}")
    print(f"{bcolors.FAIL}Σ = {bcolors.ENDC}", end="")
    return sum(parts)

'''
exp = (4*x ** 2)/2*x
i = 0
n = 2

print(Summation(exp, i, n))
'''

##########################################################################

def ProductionNotation(exp, i, n):
    j = i
    parts = []
    while j <= n:
        x = j
        res = eval(exp)
        parts.append(res)
        j = j + 1

    print(f"{bcolors.FAIL}∏ = {parts}{bcolors.ENDC}")
    prod = parts[0]
    for aux in range(0, len(parts) - 1):
        if (aux + 1) <= len(parts) - 1:
            prod = prod * parts[aux + 1]
    return prod

##########################################################################

def BasicTrueTable(p,q):
  print(f"{bcolors.OKCYAN}p | q | ¬p | ¬q | pvq |p∧q |p->q |p<->q|{bcolors.ENDC}")
  print(f"{bcolors.OKCYAN}----------------------------------------{bcolors.ENDC}")
  if (p == "T" or p == "t") and (q == "F" or q == 'f'):
    impl = "F"
  else:
    impl = "T"
     
  return (f"{p} | {q} |  {not p} |  {not q} |  {p or q}  |  {p and q} |  {impl}  |  {p == q}").replace("True", "T").replace("False", "F").replace("t", "T").replace("f", "F")