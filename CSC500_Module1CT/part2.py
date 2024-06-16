# Part 2 CSC500 Module 1 Critical Thinking Assignment
# Code by Aaron Faurot
def main():
    # Gather user input
    num1 = int(input("Enter a whole number: \n"))
    num2 = int(input("Enter another whole number: \n"))
    # Print product
    print(num1, '*', num2, 'equals', num1 * num2)
    # Print quotient after a conditional check for division by 0
    if num2 == 0:
        print(num1, '/', num2, 'is an undefined result (division by 0)')
    else:
        print(num1, '/', num2, 'equals', num1 / num2)


if __name__ == '__main__': main()
