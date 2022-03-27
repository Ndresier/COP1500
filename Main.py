#Nathan Dreiser
#Integration Project Step 1
#The first sprint is set up as a basic calculator, along with a modular arithmetic calculator

print('==============================')
print('WELCOME TO THE CRAPULATOR 4000')
print('============================== \n')

def main():
    print("1. List of math operations")
    print("2. Standerd calculator mode")
    print("3. Modular arithemtic calculator mode")
    print('4. Factorial')
    print('5. Inequalities')
    print("6. String operations and 'end=' argument") #this mode is just here for requirements that don't fit elsewhere
    print("7. End program")
    mode = input("Type the number of the mode you choose. ")
    if mode == "1":
        print("add", "subtract", "multiply", "divide", "divide w/ remainder", "exponentiate", sep=", ")
    elif mode == "2":
        StandardCalculator()
    elif mode == '3':
        ModularArithmeticCalculator()
    elif mode == '4':
        factorial()
    elif mode == '5':
        inequalities()
    elif mode == '6':
        stringOperations()
    elif mode == '7':
        print('Goodbye.')
    else:
        print('Invalid menu selection.')
        main()

def addition(num1, num2):
    sum = num1 + num2
    return sum

def subtraction(num1, num2):
    difference = num1 - num2
    return difference

def multiplication(num1,num2):
    product = num1*num2
    return product

def division(num1, num2):
    quotient = num1/num2
    return quotient

def divisionWithRemainder(num1, num2): #gives quotient in the form of an integer part and remainder part
    integerPart = int(num1 // num2)
    remainder = int(num1 % num2)
    print(integerPart, 'r', remainder)

def exponential(num1, num2):
    power = num1**num2
    return power

def factorial():
    fact = 1
    try:
        num = float(input('Enter number: ')) #I can't use int() instead of float() because I want it to return an error
        decimal = num - int(num)             #if the user inputs a decimal
        if num >= 1 and decimal == 0:
            num = int(num)
            for i in range(1, num+1):
                fact *= i
        elif num == 0:
            fact = 1
        else:
            print("Invalid number.")
            factorial()
    except:
        print("Invalid input.")
        factorial()
    print(str(num) + '! =', fact)
    main()

def StandardCalculator():
    n = 'y'
    while n == 'y':
        print("1. Add")
        print('2. Subtract')
        print('3. Multiply')
        print('4. Divide')
        print('5. Divide w/ remainder')
        print('6. Exponentiate')
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter number of desired operation ")
        if operation == '1':
            print(addition(num1, num2))
        elif operation == '2':
            print(subtraction(num1, num2))
        elif operation == '3':
            print(multiplication(num1, num2))
        elif operation == '4':
            print(division(num1, num2))
        elif operation == '5':
            divisionWithRemainder(num1, num2)
        elif operation == '6':
            print(exponential(num1, num2))
        else:
            print('Invalid operation.')
            StandardCalculator()
        n = input('Continue? (y/n): ')
    main()

def ModularArithmeticCalculator(): #Modular arithmetic does not traditionally use division, so it is excluded
    n = 'y'
    mod = int(input('Enter modulus: '))
    while n == 'y':
        print("1. Add")
        print('2. Subtract')
        print('3. Multiply')
        print('4. Exponentiate')
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        operation = input("Enter number of desired operation. ")
        if operation == '1':
            print(addition(num1, num2)%mod)
        elif operation == '2':
            print(subtraction(num1, num2)%mod)
        elif operation == '3':
            print(multiplication(num1, num2)%mod)
        elif operation == '4':
            print(exponential(num1, num2)%mod)
        else:
            print('Invalid operation.')
            ModularArithmeticCalculator()
        n = input('Continue? (y/n): ')
    main()

def inequalities():
    n = 'y'
    while n == 'y':
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        if num1 == num2:
            print(num1, '=', num2)
        elif num1 > num2:
            print(num1, '>', num2)
        elif num1 < num2:
            print(num1, '<', num2)
        n = input('Continue? (y/n): ')
    main()

def stringOperations():
    print('1. Concatenate strings')
    print('2. Repeat string')
    print('3. Check for capital letters')
    print('4. Check for all caps or all lowercase letters')
    print('5. Random crap that uses "end="')
    operation = input("Enter number of the operation to be performed: ")
    word1 = input('Enter first word: ')
    if operation == "1":
        word2= input("Enter second word: ")
        print(word1+word2)
    elif operation == "2":
        num_repetitions= int(input("Enter the number of times you would like the word repeated: "))
        print(word1*num_repetitions)
    elif operation == '3':
        capital = False
        for letter in word1:
            if not (letter >= 'a') and letter >='A': #This is only here to include a 'not' statement
                capital = True
        if capital == True:
            print('This string contains at least one capital letter.')
        else:
            print('This string does not contain capital letters.')
    elif operation == '4':
        if word1 == word1.isupper() or word1.islower(): #This is only here for the 'or' statement requirement
            print('This word is either all uppercase or all lowercase.')
            print("I cannot tell you which, because because I would lose the 'or' statement in my code.")
            print('You can probably tell by looking at it, so who cares?')
        else:
            print('This word is not all uppercase or lowercase (or you put numbers in it and broke my code).')
    elif operation == "5":
        print(word1, "fart", end="!")#this really is just here to include the 'end=' argument
    else:
        print("Invalid operation.")
        stringOperations()
    main()

main()