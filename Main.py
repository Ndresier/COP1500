# Nathan Dreiser
# Integration Project Final Sprint
# This program is a basic calculator that includes functions such as basic
# calculator functions, modular arithmetic, factorials, inequalities, and
# string operations.

print('==============================')
print('WELCOME TO THE CRAPULATOR 4000')
print('==============================')


def main():
    """
    The main function is the function that has the main menu and calls upon
    all other functions available in this calculator.
    """
    validation_main = True
    # This initializes the following loop.
    while validation_main != False:
        # This
        print("\n1. Explanation of math operations")
        print("2. Standard calculator mode")
        print("3. Modular arithmetic calculator mode")
        print('4. Factorial')
        print('5. Inequalities')
        print("6. String operations and 'end=' argument")
        print("7. End program \n")
        mode = input("Type the number of the mode you choose: ")
        if mode == "1":
            print("\nAdd", "Subtract", "Multiply", "Divide",
                  "Divide w/ remainder", "Exponentiate", sep=", ")
            print('All operations take the first number given and perform the'
                  'given operation using the second number.\n')
        elif mode == "2":
            standard_calculator()
        elif mode == '3':
            modular_arithmetic_calculator()
        elif mode == '4':
            factorial()
        elif mode == '5':
            inequalities()
        elif mode == '6':
            string_operations()
        elif mode == '7':
            print('Goodbye.')
            validation_main = False
        else:
            print('Invalid menu selection. \n')


def addition(num1, num2):
    """
    This function takes two inputs and adds them together.
    num1: The number to which addition occurs.
    num2: The number adding to the first number.
    """
    sum = num1 + num2
    return sum


def subtraction(num1, num2):
    """
    This function takes two inputs and subtracts the first number from the
    second.
    num1: The number to which subtraction occurs.
    num2: The number subtracting from the first number.
    """
    difference = num1 - num2
    return difference


def multiplication(num1, num2):
    """
    This function takes two inputs and multiplies them.
    num1: The first number to be multiplied.
    num2: The second number to be multiplied.
    """
    product = num1 * num2
    return product


def division(num1, num2):
    """
    This function takes two inputs and divides the first number by the second
    number. It displays the resulting quotient in decimal form.
    num1: The number to which division occurs.
    num2: The number that divides the second number.
    """
    quotient = num1 / num2
    return quotient


def division_with_remainder(num1, num2):
    """
    This function takes two inputs and divides the first number by the second
    number. It displays the resulting quotient as an integer value with the
    remainder.
    num1: The number to which division occurs.
    num2: The number that divides the second number.
    """
    integer_part = int(num1 // num2)
    remainder = int(num1 % num2)
    print(integer_part, 'r', remainder)


def exponential(num1, num2):
    """
    This function takes the first number and raises it to the power of the
    second number.
    num1: The base.
    num2: The exponent.
    """
    power = num1 ** num2
    return power


def factorial():
    """
    The factorial function takes a single integer and finds its factorial, the
    product of all integers less than or equal to the given integer.
    """
    fact = 1
    validate_factorial = True
    # This variable initializes the loop by assigning a truth value to it.
    while validate_factorial == True:
        try:
            num = float(input('\nEnter integer: '))
            decimal = num - int(num)
            # This assigns a variable to the decimal part
            if num >= 1 and decimal == 0:
                # This makes sure only whole numbers are used for factorials.
                num = int(num)
                for i in range(1, num + 1):
                    fact *= i
                    # This multiplies all the numbers from 1 to the number
                    # input by the user, giving a factorial.
                print(str(num) + '! =', fact)
                validate_factorial = False
                # This ends the factorial loop, bringing the user back to the
                # main menu
            elif num == 0:
                fact = 1
                # 0! := 1, by definition.
                print('0! = 1')
                validate_factorial = False
                # This ends the factorial loop.
            else:
                print("Invalid number.")
                # This is in case the user inputs a decimal.
        except:
            print("Invalid input.")
            # This prevents the function from running if there are any errors
            # like my program attempting to turn letters into an integer.


def standard_calculator():
    """
    This function is a submenu that gives options for standard math operations:
    -Addition     -Subtraction     -Multiplication
    -Division     -Division w/ remainder     -Exponentiation
    """
    validate_standard = True
    # This initializes the loop.
    while validate_standard == True:
        print("\n1. Add")
        print('2. Subtract')
        print('3. Multiply')
        print('4. Divide')
        print('5. Divide w/ remainder')
        print('6. Exponentiate')
        print('7. Main menu \n')
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input("Enter number of the desired operation: ")
            # The above variables take the first input, then perform the given
            # operation using the second input.
            if operation == '1':
                print(addition(num1, num2))
            elif operation == '2':
                print(subtraction(num1, num2))
            elif operation == '3':
                print(multiplication(num1, num2))
            elif operation == '4':
                print(division(num1, num2))
            elif operation == '5':
                division_with_remainder(num1, num2)
            elif operation == '6':
                print(exponential(num1, num2))
            elif operation == '7':
                validate_standard = False
                # This exits out of the menu and returns the user to the main
                # menu.
            else:
                print('Invalid menu choice.')
                # If they give an input for the operation not on the list,
                # this will inform the user and restart the loop.
        except:
            print('Invalid input. Please input a number.')
            # This catches any inputs that would crash the program.


def modular_arithmetic_calculator():
    """
    This function is a submenu that gives options for math operations that are
    valid in modular arithmetic:
    -Addition     -Subtraction     -Multiplication     -Exponentiation
    """
    validate_modular = True
    # This initializes the loop.
    mod = int(input('\nEnter modulus: '))
    # This sets the modulus for all arithmetic operations until the user
    # returns to the main menu.
    while validate_modular == True:
        print("\n1. Add")
        print('2. Subtract')
        print('3. Multiply')
        print('4. Exponentiate')
        print('5. Main menu\n')
        try:
            num1 = int(input("Enter first integer: "))
            num2 = int(input("Enter second integer: "))
            operation = input("Enter number of the desired operation: ")
            # The above variables take the first input, then perform the given
            # operation using the second input.
            if operation == '1':
                print(addition(num1, num2) % mod)
            elif operation == '2':
                print(subtraction(num1, num2) % mod)
            elif operation == '3':
                print(multiplication(num1, num2) % mod)
            elif operation == '4':
                print(exponential(num1, num2) % mod)
            # '% mod' in the above else if statements leave behind the
            # remainder after dividing by the modulus set at the beginning.
            elif operation == '5':
                validate_modular = False
                # This allows the user to exit the loop and return to the
                # main menu.
            else:
                print('Invalid menu choice.')
                # This informs the user of any invalid menu choices before the
                # loop restarts.
        except:
            print('Invalid input. Must input integer.')
            # This prevents any errors from occuring, such as trying to convert
            # a letter into an integer.


def inequalities():
    """
    This function is a function that compares two numbers together and displays
    whether the first number is less than, greater than, or equal to the second
    number.
    """
    validate_inequalities = True
    # This initializes the loop.
    while validate_inequalities == True:
        try:
            num1 = float(input('\nEnter first number: '))
            num2 = float(input('Enter second number: '))
            # Takes two numbers to check for equality.
            print('\n')
            if num1 == num2:
                print(num1, '=', num2)
                # This lets the user know if the numbers are equal.
            elif num1 > num2:
                print(num1, '>', num2)
                # This lets the user know if the first number is greater than
                # the second
            elif num1 < num2:
                print(num1, '<', num2)
                # This lets the user know if the first number is less than
                # the second.
            validate_inequalities = False
            # This ends the loop after the user successfully compares two
            # numbers.
        except:
            print('Invalid input. Please enter a number.')
            # This informs the user that they've made an improper input that
            # would crash the program.


def string_operations():
    """
    This function is a submenu that gives multiple string operations that are
    irrelevant to the functioning of the calculator:
    -Concatenate     -Repeat strings     -Check for capital letters
    -Check for all uppercase or all lowercase     -something that uses 'end='
    """
    validate_string = True
    # This initializes the loop.
    while validate_string == True:
        print('\n1. Concatenate strings')
        print('2. Repeat string')
        print('3. Check for capital letters')
        print('4. Check for all caps or all lowercase letters')
        print('5. Random crap that uses "end="')
        print('6. Main menu\n')
        try:
            operation = input("Enter number of the operation to be performed: "
                              )
            word1 = input('Enter first word: ')
            if operation == "1":
                word2 = input("Enter second word: ")
                print(word1 + word2)
                # This combines the two strings above and outputs a combined
                # string.
            elif operation == "2":
                num_repetitions = int(input("Enter the number of times you "
                                            "would like the word repeated: "))
                print(word1 * num_repetitions)
                # This repeats the first string as many times as is asked by
                # the user.
            elif operation == '3':
                capital = False
                for letter in word1:
                    if not (letter >= 'a') and letter >= 'A':
                        # This loop checks the individual letters to see
                        # whether they are capitalized or not.
                        capital = True
                if capital == True:
                    print('This string contains at least one capital letter.')
                else:
                    print('This string does not contain capital letters.')
            elif operation == '4':
                if word1 == word1.isupper() or word1.islower():
                    # This checks whether the letters are all uppercase or
                    # lowercase by comparing the word to what it would look
                    # like if it was all uppercase or lowercase.
                    print('This word is either all uppercase or all lowercase.'
                          '\nI cannot tell you which, because because I would '
                          'lose the "or" statement in my code. \nYou can '
                          'probably tell by looking at it, so who cares?')
                else:
                    print('This word is not all uppercase or lowercase.')
            elif operation == "5":
                print(word1, "fart", end="!")
                # This really is just here to include the 'end=' argument. It
                # puts the word 'fart' at the end of the given word, then
                # throws an exclamation mark at the end.
            elif operation == '6':
                validate_string = False
                # This ends the loop and returns the user to the main menu.
            else:
                print("Invalid operation.")
                # This tells the user they didn't use a proper input before
                # the loop restarts.
        except:
            print('Error with input. Please try again.')
            # This prevents the code from crashing and allows the loop to
            # continue.


if __name__ == "__main__":
    main()
