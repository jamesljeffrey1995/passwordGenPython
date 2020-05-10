import random, string #importing libaries random and string

def tryAgain():
    while(True): #infinite loop to go through options
        decision = input("Would you like to choose another password? Y/N: ") #user defined decision
        if decision.upper() == 'Y': #converts variable to uppercase and if it is == to Y, then it will main() function
            main()
        elif decision.upper() == 'N': # if it is equal to N, then it will print and then return and close program
            print("Thank you for using the password generator")
            return
        else:   #if the user has entered an invalid option, then it will print and warn them
            print("Enter either Y or N")

def passwordGeneration(amountOfChar):
    result = random.choices(string.printable[:-6], k=amountOfChar) #uses choices out of random and printable out of string, [:6} allows for no white space, k is user defined
    print(''.join(result))#This prints the password, uses join to join the string together as multiple characters are used

def main():
    while (True): # Infinited loop
        try: #Using a try, except so the user can only enter the int data type
            userDefinedAmount = int(input("Enter the amount of characters for password: "))
            break
        except ValueError:
            print("Please enter an integer.")
    passwordGeneration(userDefinedAmount)
    tryAgain()

main()