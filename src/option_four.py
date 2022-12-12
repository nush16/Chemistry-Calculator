from chempy.util import periodic as prd

# Number of elements from user  
x = input("Enter the Element from the periodic table that you want information on: ")
print("Printing information on", x, "from the periodic table")
print()
# Displaying the periodic element information  
print("Atomic No.\tName\t\tSymbol\t\tMass")  
# Using for loop to loop over periodic table  
for a in range(1, 2):  
    # Printing the atomic number of elements  
    find_atomic_number = prd.atomic_number(x) 
    print(find_atomic_number, end = "\t\t") 
    # Displaying the names of elements
    # 
    y = prd.names.index(x)  
    if len(prd.names[y]) > 7:  
        print(prd.names[y], end = "\t")  
    else:  
        print(prd.names[y], end = "\t\t")  
    # # Printing the element symbol  
    
    print(prd.symbols[y], end = "\t\t")  
  
    # # Displaying the atomic mass of element  
    print(prd.relative_atomic_masses[y])  
print("Result for periodic elements is printed according to number you provided")  
