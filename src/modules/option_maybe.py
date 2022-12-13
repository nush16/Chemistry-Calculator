import sys
from modules.molar_weight import *

class CompoundProperties:
    menu_options = (1, 2, 3, 4)
    print()
    print('-------Calculate molar weight, density or number of mols-------')
    print('press 1 : Calculate molar weight')
    print('press 2 : Calculate density')
    print('press 3 : Calculate number of mols')
    print('press 4 : exit')

    print()
    user_input = int(input('Enter an option: '))

    def calculate_molar_weight(cls):
            print('To calculate the molar weight of a compound we need to know the element and how many of each element is in the compound' )
            print()
            user_input1 = int(input('How many elements in the compound: '))
            print()
            if user_input1 == 1:
                MolarWeight.one_element_mw()
            elif user_input1 == 2:
                MolarWeight.two_element_mw()
            elif user_input1 == 3:
                MolarWeight.three_element_mw()
            elif user_input1 == 4:
                MolarWeight.four_element_mw()
            elif user_input1 == 5:
                MolarWeight.five_element_mw()
            elif user_input1 == 6:
                MolarWeight.six_element_mw()
            else:
                print ('You cannot have more than 6 different elements in a compound')
        
     
    def calculate_density(cls):
            print('To calculate the density of a compound we need to the mass(g) and volume(cm3) of the compound' )
            print()
            mass = float(input('-> What is the mass (g)?: '))
            volume = float(input('-> What is the volume (cm3)?: '))
            print()
            # equation to calculate density
            density = mass / volume
            print('--> The density of the compound is', round(density, 2), 'g/cm3')

    def calculate_mols(cls):
            print('To calculate the number of mols of a compound we need to the mass(g) and molecular weight (g/mol) of the compound' )
            print()
            mass = float(input('-> What is the mass (g)?: '))
            molecular_mass = float(input('-> What is the molecular mass (g/mol)?: '))
            print()
            # equation to calculate the number of mols
            mol = mass/molecular_mass
            print('--> The number of mols, when mass is', mass, '(g) and molecular weight is',molecular_mass, '(g/mol) is,', round(mol, 2), '(mol)')


z = CompoundProperties()

if z.user_input == 1:
    z.calculate_molar_weight()
elif z.user_input == 2:
    z.calculate_density()
elif z.user_input == 3:
    z.calculate_mols()
elif z.user_input == 4:
        sys.exit()
else:
    print()
    print('Option not available')




        