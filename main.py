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
from DiscreteMathLib import not_p
from DiscreteMathLib import p_OR_q
from DiscreteMathLib import p_AND_q
from DiscreteMathLib import p_SO_q
from DiscreteMathLib import p_biimplication_q
from DiscreteMathLib import Transpose
from DiscreteMathLib import isSymmetric
from DiscreteMathLib import Sum_of_Matrix
from DiscreteMathLib import Sub_of_Matrix
from DiscreteMathLib import Mult_of_Matrix
from DiscreteMathLib import Summation
from DiscreteMathLib import ProductionNotation
from DiscreteMathLib import BasicTrueTable

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

# Logo Display
print(rf"""{bcolors.WARNING}
  _____  _                   _       __  __       _   _     _      _ _     
 |  __ \(_)                 | |     |  \/  |     | | | |   | |    (_) |    
 | |  | |_ ___  ___ _ __ ___| |_ ___| \  / | __ _| |_| |__ | |     _| |__  
 | |  | | / __|/ __| '__/ _ \ __/ _ \ |\/| |/ _` | __| '_ \| |    | | '_ \ 
 | |__| | \__ \ (__| | |  __/ ||  __/ |  | | (_| | |_| | | | |____| | |_) |
 |_____/|_|___/\___|_|  \___|\__\___|_|  |_|\__,_|\__|_| |_|______|_|_.__/ {bcolors.ENDC}
      
                                                    {bcolors.OKCYAN}by @joaoguilhermemendes{bcolors.ENDC}                        
        """)

# Menu
print(f"     {bcolors.UNDERLINE}LOGICAL OPERATIONS{bcolors.ENDC}      ")
print()
print(f"{bcolors.WARNING} [ 01 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} ¬x {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 02 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} p ∨ q {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 03 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} p ∧ q {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 04 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} p -> q (implication) {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 05 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} p <-> q (biimplication) {bcolors.ENDC}")
print()
print()
print(f"     {bcolors.UNDERLINE}OPERATION WITH SETS{bcolors.ENDC}      ")
print()
print(f"{bcolors.WARNING} [ 06 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} Cardinality {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 07 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} Union {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 08 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} Intersection {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 09 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} Contained/IsSubset? {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 10 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} IsElement? {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 11 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} Subtraction {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 12 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} Complement {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 13 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} Cartesian product {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 14 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} Partition {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 15 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} Simetric Diference {bcolors.ENDC}")
print()
print()
print(f"     {bcolors.UNDERLINE}MATRIX OPERATIONS{bcolors.ENDC}      ")
print()
print(f"{bcolors.WARNING} [ 16 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} Sum of Matrix {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 17 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} Subtration of Matrix {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 18 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} Multiplication of Matrix {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 19 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} Transpose Matrix {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 20 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} Matrix is Simetric {bcolors.ENDC}")
print()
print()
print(f"     {bcolors.UNDERLINE}SUMMATION AND PRODUCTION NOTATION{bcolors.ENDC}      ")
print()
print(f"{bcolors.WARNING} [ 21 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} Summation {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 22 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} Production Notation {bcolors.ENDC}")
print()
print()
print(f"     {bcolors.UNDERLINE}TRUE TABLES{bcolors.ENDC}      ")
print()
print(f"{bcolors.WARNING} [ 23 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} (Basics) |p |q |¬p |¬q |pvq |p∧q |p->q |p<->q| {bcolors.ENDC}")
print(f"{bcolors.WARNING} [ 24 ] {bcolors.ENDC}" + " " + f"{bcolors.BOLD} (Create) e.g. (p ^ q -> -r) {bcolors.ENDC}")
print()
print("---------------------------------------------")

option=1
while option != 0:
    option = int(input("Choose an option (0 to exit): "))
    print("---------------------------------------------")
    print()

    # ¬p / Not p
    if option == 1:
        print(f"{bcolors.OKGREEN}----> [ ¬p | NOT p]{bcolors.ENDC}")
        print()
        p = str(input("Enter the (p) value (T/F): "))
        print()
        notp = not_p(p)
        print()
        print(f"{bcolors.OKCYAN}The inverse value for [{p.upper()}] is --> {bcolors.ENDC}", end=" ")
        print(f"{bcolors.FAIL}[{notp}]{bcolors.ENDC}")
        print()
        print("---------------------------------------------")
    
    # OR
    if option == 2:
        print(f"{bcolors.OKGREEN}----> [ p v q | p OR q]{bcolors.ENDC}")
        print()
        p = str(input("Enter the (p) value (T/F): "))
        q = str(input("Enter the (p) value (T/F): "))
        print()
        print(f"{bcolors.FAIL}{p_OR_q(p, q)}{bcolors.ENDC}")
        print()
        print("---------------------------------------------")

    # AND
    if option == 3:
        print(f"{bcolors.OKGREEN}----> [ p ^ q | p AND q]{bcolors.ENDC}")
        print()
        p = str(input("Enter the (p) value (T/F): "))
        q = str(input("Enter the (p) value (T/F): "))
        print()
        print(f"{bcolors.FAIL}{p_AND_q(p, q)}{bcolors.ENDC}")
        print()
        print("---------------------------------------------")

    # Implication
    if option == 4 or option == "4":
        print(f"{bcolors.OKGREEN}----> [ p → q ] IMPLICATION{bcolors.ENDC}")
        print()
        p = str(input("Enter the (p) value (T/F): "))
        q = str(input("Enter the (p) value (T/F): "))
        print()
        print(f"{bcolors.FAIL}{p_SO_q(p, q)}{bcolors.ENDC}")
        print()
        print("---------------------------------------------")

    # BI-Implication
    if option == 5 or option == "5":
        print(f"{bcolors.OKGREEN}----> [ p ↔ q ] BI-IMPLICATION{bcolors.ENDC}")
        print()
        p = str(input("Enter the (p) value (T/F): "))
        q = str(input("Enter the (p) value (T/F): "))
        print()
        print(f"{bcolors.FAIL}{p_biimplication_q(p, q)}{bcolors.ENDC}")
        print()
        print("---------------------------------------------")

    # Cardinality
    if option == 6 or option == "06": 
        print(f"{bcolors.OKGREEN}----> [|A|] CARDINALITY{bcolors.ENDC}")
        print()
        print(f"{bcolors.OKCYAN}The number of elements in the set. For example...{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}A = {1,2,3,4,5}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}∣A∣ = 5{bcolors.ENDC}")
        print()
        setA = input("Enter a set (e.g. 1,2,3,4): ")
        setA = set(map(int, setA.split(',')))
        print()
        print(f"{bcolors.FAIL}|A| = {Cardinality(setA)}{bcolors.ENDC}")
        print()
        print("---------------------------------------------")

    # Union
    if option == 7:
        print(f"{bcolors.OKGREEN}----> [ A ∪ B ] UNION{bcolors.ENDC}")
        print()
        setA = input("Enter a setA (e.g. 1,2,3,4): ")
        setA = set(map(int, setA.split(',')))
        setB = input("Enter a setA (e.g. 1,2,3,4): ")
        setB = set(map(int, setB.split(',')))
        print()

        print(f"{bcolors.OKCYAN}{setA} ∪ {setB}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}A ∪ B: {bcolors.ENDC}", end=" ")
        print(f"{bcolors.FAIL}{Union(setA, setB)}{bcolors.ENDC}")
        print()
        print("---------------------------------------------")

    # Intersection
    if option == 8:
        print(f"{bcolors.OKGREEN}----> [ A ∩ B ] INTERSECTION{bcolors.ENDC}")
        print()
        setA = input("Enter a setA (e.g. 1,2,3,4): ")
        setA = set(map(int, setA.split(',')))

        setB = input("Enter a setA (e.g. 1,2,3,4): ")
        setB = set(map(int, setB.split(',')))
        print()

        print(f"{bcolors.OKCYAN}{setA} ∩ {setB}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}A ∩ B: {bcolors.ENDC}", end=" ")
        print(f"{bcolors.FAIL}{Intersection(setA, setB)}{bcolors.ENDC}")
        print()
        print("---------------------------------------------")

    # Contained/IsSubset
    if option == 9:
        print(f"{bcolors.OKGREEN}----> [ A ⊆ B ] CONTAINED/IS SUBSET{bcolors.ENDC}")
        print()
        setA = input("Enter a setA (e.g. 1,2,3,4): ")
        setA = set(map(int, setA.split(',')))

        setB = input("Enter a setA (e.g. 1,2,3,4): ")
        setB = set(map(int, setB.split(',')))
        print()

        print(f"{bcolors.OKCYAN}{setA} ⊆ {setB}? {bcolors.ENDC}", end=" ")
        print(f"{bcolors.FAIL}{Contained_or_IsSubset(setA, setB)}{bcolors.ENDC}")
        print()
        print("---------------------------------------------")

    # IsElement?
    if option == 10:
        print(f"{bcolors.OKGREEN}----> [ x ∈ A ] IS ELEMENT?{bcolors.ENDC}")
        print()
        x = int(input("Enter a element (e.g. 5): "))

        setA = input("Enter a setA (e.g. 1,2,3,4): ")
        setA = set(map(int, setA.split(',')))
        print()

        print(f"{bcolors.OKCYAN}{x} ∈ {setA}? {bcolors.ENDC}", end=" ")
        print(f"{bcolors.FAIL}{IsElement(x, setA)}{bcolors.ENDC}")
        print()
        print("---------------------------------------------")
        
    # Subtraction?
    if option == 11:
        print(f"{bcolors.OKGREEN}----> [ A - B ] SUBTRATION{bcolors.ENDC}")
        print()
        setA = input("Enter a setA (e.g. 1,2,3,4): ")
        setA = set(map(int, setA.split(',')))

        setB = input("Enter a setA (e.g. 1,2,3,4): ")
        setB = set(map(int, setB.split(',')))

        print(f"{bcolors.OKCYAN}{setA} - {setB} = {bcolors.ENDC}", end=" ")
        print(Subtraction(setA, setB))
        print()
        print("---------------------------------------------")

    # Complement?
    if option == 12:
        print(f"{bcolors.OKGREEN}----> [ Aˉ ] COMPLEMENT{bcolors.ENDC}")
        print()
        setA = input("Enter a set Universal (e.g. 1,2,3,4): ")
        setA = set(map(int, setA.split(',')))

        setB = input("Enter a set (e.g. 1,2,3,4): ")
        setB = set(map(int, setB.split(',')))

        print(f"{bcolors.OKCYAN}{setA}' ou ({setA} - {setB}) = {bcolors.ENDC}", end=" ")
        print(Complement(setA, setB))
        print()
        print("---------------------------------------------")

    # CrtProd
    if option == 13:
        print(f"{bcolors.OKGREEN}----> [ A × B ] CARTESIAN PRODUCT{bcolors.ENDC}")
        print()
        setA = input("Enter a set Universal (e.g. 1,2,3,4): ")
        setA = set(map(int, setA.split(',')))

        setB = input("Enter a set (e.g. 1,2,3,4): ")
        setB = set(map(int, setB.split(',')))

        print(f"{bcolors.OKCYAN}{setA} x {setB} = {bcolors.ENDC}", end=" ")
        print(CrtProd(setA, setB))
        print()
        print("---------------------------------------------")

    # Partition
    if option == 14:
        print(f"{bcolors.OKGREEN}----> [ P=(A1​,A2​,…,An​) ] PARTITION{bcolors.ENDC}")
        print()
        setA = input("Enter a set Universal (e.g. 1,2,3,4): ")
        setA = set(map(int, setA.split(',')))

        print(f"P({setA}) = ", end=" ")
        partitions = Partition(list(setA))
        print_partitions(partitions)
        print()
        print("---------------------------------------------")

    # Symmetric Difference
    if option == 15:
        print(f"{bcolors.OKGREEN}----> [ A△B ] SYMMETRIC DIFFERENCE {bcolors.ENDC}")
        print()
        setA = input("Enter a setA (e.g. 1,2,3,4): ")
        setA = set(map(int, setA.split(',')))

        setB = input("Enter a setB (e.g. 1,2,3,4): ")
        setB = set(map(int, setB.split(',')))

        print(f"{bcolors.OKCYAN}{setA} △ {setB} = {bcolors.ENDC}", end=" ")
        print(SimetricDifference(setA, setB))
        print()
        print("---------------------------------------------")
    
    # Sum of Matrix
    if option == 16:
        print(f"{bcolors.OKGREEN}----> [ A + B ] SUM OF MATRIX {bcolors.ENDC}")
        print()
        sizeA = int(input("Enter the matrix A size: "))

        cont = 0
        matA = []
        while cont < sizeA:
            row = input(f"Enter row {cont + 1} of the matrix (e.g. 1,2,3,4): ")
            row = list(map(int, row.split(',')))
            matA.append(row)
            cont += 1
        
        print()

        sizeB = int(input("Enter the matrix B size: "))

        cont = 0
        matB = []
        while cont < sizeB:
            row = input(f"Enter row {cont + 1} of the matrix (e.g. 1,2,3,4): ")
            row = list(map(int, row.split(',')))
            matB.append(row)
            cont += 1
        
        print()

        print(f"{bcolors.OKCYAN}{matA} + {matB}{bcolors.ENDC} = {Sum_of_Matrix(matA, matB)}")
        print()
        print("---------------------------------------------")


    # Sub of Matrix
    if option == 17:
        print(f"{bcolors.OKGREEN}----> [ A - B ] SUB OF MATRIX {bcolors.ENDC}")
        print()
        sizeA = int(input("Enter the matrix A size: "))

        cont = 0
        matA = []
        while cont < sizeA:
            row = input(f"Enter row {cont + 1} of the matrix (e.g. 1,2,3,4): ")
            row = list(map(int, row.split(',')))
            matA.append(row)
            cont += 1
        
        print()

        sizeB = int(input("Enter the matrix B size: "))

        cont = 0
        matB = []
        while cont < sizeB:
            row = input(f"Enter row {cont + 1} of the matrix (e.g. 1,2,3,4): ")
            row = list(map(int, row.split(',')))
            matB.append(row)
            cont += 1

        print()

        print(f"{bcolors.OKCYAN}{matA} + {matB}{bcolors.ENDC} = {Sub_of_Matrix(matA, matB)}")
        print()
        print("---------------------------------------------")


    # Mult of Matrix
    if option == 18:
        print(f"{bcolors.OKGREEN}----> [ A * B ] MULT OF MATRIX {bcolors.ENDC}")
        print()
        sizeA = int(input("Enter the matrix A size: "))

        cont = 0
        matA = []
        while cont < sizeA:
            row = input(f"Enter row {cont + 1} of the matrix (e.g. 1,2,3,4): ")
            row = list(map(int, row.split(',')))
            matA.append(row)
            cont += 1
        
        print()

        sizeB = int(input("Enter the matrix B size: "))

        cont = 0
        matB = []
        while cont < sizeB:
            row = input(f"Enter row {cont + 1} of the matrix (e.g. 1,2,3,4): ")
            row = list(map(int, row.split(',')))
            matB.append(row)
            cont += 1

        print()

        print(f"{bcolors.OKCYAN}{matA} + {matB}{bcolors.ENDC} = {Mult_of_Matrix(matA, matB)}")
        print()
        print("---------------------------------------------")

    # Transpose Matrix
    if option == 19:
        print(f"{bcolors.OKGREEN}----> [ A^T ] TRANSPOSE MATRIX {bcolors.ENDC}")
        print()
        size = int(input("Enter the matrix size: "))

        cont = 0
        mat = []
        while cont < size:
            row = input(f"Enter row {cont + 1} of the matrix (e.g. 1,2,3,4): ")
            row = list(map(int, row.split(',')))
            mat.append(row)
            cont += 1

        print(f"{bcolors.OKCYAN}{Transpose(mat, size)}{bcolors.ENDC}")
        print()
        print("---------------------------------------------")

    # Matrix is symmetric
    if option == 20:
        print(f"{bcolors.OKGREEN}----> [ A△B ?] MATRIX IS SYMMETRIC? {bcolors.ENDC}")
        print()
        size = int(input("Enter the matrix size: "))

        cont = 0
        mat = []
        while cont < size:
            row = input(f"Enter row {cont + 1} of the matrix (e.g. 1,2,3,4): ")
            row = list(map(int, row.split(',')))
            mat.append(row)
            cont += 1

        print(f"{bcolors.OKCYAN}{mat}{bcolors.ENDC} is symmetric? = {isSymmetric(mat, size)}")
        print()
        print("---------------------------------------------")

    # Summation
    if option == 21:
        print(f"{bcolors.OKGREEN}----> [ Σ (i=a; n) f(i) ] SUMMATION? {bcolors.ENDC}")
        print()
        exp = str(input("Enter the expression - e.g. (4*x ** 2) - 1 ---- "))
        i = int(input("Enter the initial index: "))
        n = int(input("Enter the final index: "))

        print(f"{bcolors.OKCYAN}Σ (i={i} to {n}) = {exp}{bcolors.ENDC}")
        print()
        print("Σ = ", end="")
        print(Summation(exp, i, n))
        print()
        print("---------------------------------------------")

    # Production Notation
    if option == 22:
        print(f"{bcolors.OKGREEN}----> [ ∏ (i=a; n) f(i) ] PRODUCTION NOTATION? {bcolors.ENDC}")
        print()
        exp = str(input("Enter the expression - e.g. (4*x ** 2) - 1 ---- "))
        i = int(input("Enter the initial index: "))
        n = int(input("Enter the final index: "))

        print(f"{bcolors.OKCYAN}Production Notation: {bcolors.ENDC}")
        print()
        print(ProductionNotation(exp, i, n))
        print()
        print("---------------------------------------------")

    # Basic True Table
    if option == 23:
        print(f"{bcolors.OKGREEN}----> (Basic) TRUE TABLE {bcolors.ENDC}")
        print()
        p = str(input("Enter the (p) value (T for True / F for false): "))
        q = str(input("Enter the (q) value (T for True / F for false): "))
        print()
        print(f"{bcolors.OKCYAN}{BasicTrueTable(p,q)}{bcolors.ENDC}", end=" ")
        print()
        print("---------------------------------------------")



print()
print()