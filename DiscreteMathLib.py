<<<<<<< HEAD
########################################################################
=======
#test01
#test02
#test03
>>>>>>> 6bb829aa8b7758188271b2ede8759065777e8538

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
def IsElement(x, set):
  if x in set:
    return True
  else:
    return False
    
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
  setComplement = []

  for i in range(0, len(setUniversal)):
    if setUniversal[i] not in setA:
      setComplement.append(setUniversal[i])

  setComplement = sorted(setComplement)
  return setComplement


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
def partition(setPartition):
  if len(setPartition) == 1:
    yield [setPartition]
    return

  first = setPartition[0]
  for smaller in partition(setPartition[1:]):
    # insert `first` in each of the subpartition's subsets
    for n, subset in enumerate(smaller):
      yield smaller[:n] + [[first] + subset] + smaller[n + 1:]
    # put `first` in its own subset
    yield [[first]] + smaller


'''setPartition = [1, 2, 3, 4]
print(setPartition)
print("")

print("1 [NULL]")
for n, p in enumerate(partition(setPartition), 2):
    print(n, sorted(p))'''

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

def p_implication_q(p,q):
  if p and not q:
    return False
  else:
    return True

def p_biimplication_q(p,q):
  if p == q:
    return True
  else:
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

def Transpose(mat, N):
  tr = [ [0 for j in range(len(mat[0])) ] for i in range(len(mat)) ]  
  for i in range(N):
    for j in range(N):
      tr[i][j] = mat[j][i]
      print(tr[i][j],end='  ')
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
