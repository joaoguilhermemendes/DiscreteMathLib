from DiscreteMathLib import Cardinality
from DiscreteMathLib import Union
from DiscreteMathLib import Intersection
from DiscreteMathLib import Contained_or_IsSubset
from DiscreteMathLib import IsElement
from DiscreteMathLib import Subtraction
from DiscreteMathLib import Complement
from DiscreteMathLib import CrtProd
from DiscreteMathLib import Partition
from DiscreteMathLib import print_partitions
from DiscreteMathLib import SimetricDifference
from DiscreteMathLib import p
from DiscreteMathLib import q
from DiscreteMathLib import p_implication_q
from DiscreteMathLib import p_biimplication_q
from DiscreteMathLib import For_all_x
from DiscreteMathLib import Exist_x
from DiscreteMathLib import Transpose
from DiscreteMathLib import isSymmetric

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

# Menu
print()
print()
print(f"     {bcolors.UNDERLINE}LOGICAL OPERATIONS{bcolors.ENDC}      ")
print()
print(f"{bcolors.WARNING} [ 01 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} x is TRUE or FALSE? {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 02 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} ¬x {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 03 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} p ∨ q {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 04 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} p ∧ q {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 05 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} p -> q (implication) {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 06 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} p <-> q (biimplication) {bcolors.ENDC}")
print()
print()
print(f"     {bcolors.UNDERLINE}QUANTIFIER{bcolors.ENDC}      ")
print()
print(f"{bcolors.WARNING} [ 07 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} Existencial Quantifier {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 08 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} Universal Quantifier {bcolors.ENDC}")
print()
print()
print(f"     {bcolors.UNDERLINE}OPERATION WITH SETS{bcolors.ENDC}      ")
print()
print(f"{bcolors.WARNING} [ 09 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} Cardinality {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 10 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} Union {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 11 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} Intersection {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 12 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} Contained/IsSubset? {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 13 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} IsElement? {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 14 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} Subtraction {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 15 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} Complement {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 16 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} Cartesian product {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 17 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} Partition {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 18 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} Simetric Diference {bcolors.ENDC}")
print()
print()
print(f"     {bcolors.UNDERLINE}MATRIX OPERATIONS{bcolors.ENDC}      ")
print()
print(f"{bcolors.WARNING} [ 19 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} Sum of Matrix {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 20 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} Subtration of Matrix {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 21 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} Multiplication of Matrix {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 22 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} Transpose Matrix {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 23 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} Matrix is Simetric {bcolors.ENDC}")
print()
print()
print(f"     {bcolors.UNDERLINE}SUMMATION AND PRODUCTION NOTATION{bcolors.ENDC}      ")
print()
print(f"{bcolors.WARNING} [ 24 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} Summation {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 25 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} Production Notation {bcolors.ENDC}")
print()
print()
print(f"     {bcolors.UNDERLINE}TRUE TABLES{bcolors.ENDC}      ")
print()
print(f"{bcolors.WARNING} [ 25 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} (Basics) |p |q |¬p |¬q |pvq |p∧q |p->q |p<->q| {bcolors.ENDC}")
print()
print("---------------------------------------------")
print()

option = int(input("Choose an option (0 to exit): "))
print()

# Cardinality
if option == 9 or option == "09": 
    setA = input("Enter a set (e.g. 1,2,3,4): ")
    setA = set(map(int, setA.split(',')))

    print(f"{bcolors.OKCYAN}CARDINALITY: {bcolors.ENDC}", end=" ")
    print(Cardinality(setA))
    print()
    print("---------------------------------------------")
    print()    

# Union
if option == 10:
    setA = input("Enter a setA (e.g. 1,2,3,4): ")
    setA = set(map(int, setA.split(',')))

    setB = input("Enter a setA (e.g. 1,2,3,4): ")
    setB = set(map(int, setB.split(',')))

    print(f"{bcolors.OKCYAN}UNION: {bcolors.ENDC}", end=" ")
    print(Union(setA, setB))
    print()
    print("---------------------------------------------")
    print()

# Intersection
if option == 11:
    setA = input("Enter a setA (e.g. 1,2,3,4): ")
    setA = set(map(int, setA.split(',')))

    setB = input("Enter a setA (e.g. 1,2,3,4): ")
    setB = set(map(int, setB.split(',')))

    print(f"{bcolors.OKCYAN}INTERSECTION: {bcolors.ENDC}", end=" ")
    print(Intersection(setA, setB))
    print()
    print("---------------------------------------------")
    print()    

# Contained/IsSubset
if option == 12:
    setA = input("Enter a setA (e.g. 1,2,3,4): ")
    setA = set(map(int, setA.split(',')))

    setB = input("Enter a setA (e.g. 1,2,3,4): ")
    setB = set(map(int, setB.split(',')))

    print(f"{bcolors.OKCYAN}{setA} ⊆ {setB}? {bcolors.ENDC}", end=" ")
    print(Contained_or_IsSubset(setA, setB))
    print()
    print("---------------------------------------------")
    print()

# IsElement?
if option == 13:
    x = int(input("Enter a element (e.g. 5): "))

    setB = input("Enter a set (e.g. 1,2,3,4): ")
    setB = set(map(int, setB.split(',')))

    print(f"{bcolors.OKCYAN}{x} ∈ {setB}? {bcolors.ENDC}", end=" ")
    print(IsElement(x, setB))
    print()
    print("---------------------------------------------")
    print()
    
# Subtraction?
if option == 14:
    setA = input("Enter a setA (e.g. 1,2,3,4): ")
    setA = set(map(int, setA.split(',')))

    setB = input("Enter a setA (e.g. 1,2,3,4): ")
    setB = set(map(int, setB.split(',')))

    print(f"{bcolors.OKCYAN}{setA} - {setB} = {bcolors.ENDC}", end=" ")
    print(Subtraction(setA, setB))
    print()
    print("---------------------------------------------")
    print()

# Complement?
if option == 15:
    setA = input("Enter a set Universal (e.g. 1,2,3,4): ")
    setA = set(map(int, setA.split(',')))

    setB = input("Enter a set (e.g. 1,2,3,4): ")
    setB = set(map(int, setB.split(',')))

    print(f"{bcolors.OKCYAN}{setA}' ou ({setA} - {setB}) = {bcolors.ENDC}", end=" ")
    print(Complement(setA, setB))
    print()
    print("---------------------------------------------")
    print()

# CrtProd
if option == 16:
    setA = input("Enter a set Universal (e.g. 1,2,3,4): ")
    setA = set(map(int, setA.split(',')))

    setB = input("Enter a set (e.g. 1,2,3,4): ")
    setB = set(map(int, setB.split(',')))

    print(f"{bcolors.OKCYAN}{setA} x {setB} = {bcolors.ENDC}", end=" ")
    print(CrtProd(setA, setB))
    print()
    print("---------------------------------------------")
    print()

# Partition
if option == 17:
    setA = input("Enter a set Universal (e.g. 1,2,3,4): ")
    setA = set(map(int, setA.split(',')))

    print(f"P({setA}) = ", end=" ")
    partitions = Partition(list(setA))
    print_partitions(partitions)
    print()
    print("---------------------------------------------")
    print()

# Simetric Difference
if option == 18:
    setA = input("Enter a set Universal (e.g. 1,2,3,4): ")
    setA = set(map(int, setA.split(',')))

    setB = input("Enter a set (e.g. 1,2,3,4): ")
    setB = set(map(int, setB.split(',')))

    print(f"{bcolors.OKCYAN}{setA} △ {setB} = {bcolors.ENDC}", end=" ")
    print(SimetricDifference(setA, setB))
    print()
    print("---------------------------------------------")
    print()

print()
print()