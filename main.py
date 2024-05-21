from DiscreteMathLib import Cardinality
from DiscreteMathLib import Union
from DiscreteMathLib import Intersection
from DiscreteMathLib import Contained_or_IsSubset
from DiscreteMathLib import IsElement
from DiscreteMathLib import Subtraction
from DiscreteMathLib import Complement
from DiscreteMathLib import CrtProd
from DiscreteMathLib import partition
from DiscreteMathLib import p
from DiscreteMathLib import q
from DiscreteMathLib import p_implication_q
from DiscreteMathLib import p_biimplication_q
from DiscreteMathLib import For_all_x
from DiscreteMathLib import Exist_x
from DiscreteMathLib import Transpose
from DiscreteMathLib import isSymmetric


# Menu
print()
print()
print("-=-=- Logical Operations =-=-=")
print("1 - x is true or false?")
print("2 - ¬x")
print("3 - p ∨ q")
print("4 - p ∧ q")
print("5 - p -> q (implication)")
print("6 - p <-> q (biimplication)")
print()
print("-=-=- Quantifier =-=-=")
print("23 - Existencial Quantifier")
print("24 - Universal Quantifier ")
print()
print("-=-=- Operations with Sets =-=-=")
print("7  - Cardinality")
print("8  - Union")
print("9  - Intersection")
print("10 - Contained/IsSubset?")
print("11 - IsElement?")
print("12 - Subtraction")
print("13 - Complement")
print("14 - Cartesian product")
print("15 - Partition")
print("16 - Simetric Diference")
print()
print("-=-=- Matrix Operations =-=-=")
print("17 - Sum of Matrix ")
print("18 - Subtration of Matrix")
print("19 - Multiplication of Matrix")
print("20 - Transpose Matrix")
print("21 - Matrix is Simetric")
print()
print("-=-=- Summation and Production Notation =-=-=")
print("22 - Summation")
print("23 - Production Notation")
print()
print("-=-=- True Tables =-=-=")
print("24 - (Basics) |p |q |¬p |¬q |p∨q |p∧q |p->q |p<->q| ")
print()
print("---------------------------------------------")
print()

option = int(input("Choose an option: "))

if option == 1:
    setA = {1, 2, 3, 6}
    setB = {1, 2, 6, 9}

    setAB = Union(setA, setB)
    print(setAB)
    print()
    print("---------------------------------------------")
    print()    
    
print()
print()