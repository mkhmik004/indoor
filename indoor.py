#MKHABELE MMM
#27/06/2023
def main():
    #promt user input on new line
    stringInput=input("Enter non numeric string to convert to lower case:\n")
    #if input is numeric, promt user until alphabet charector is inputed on new line
    while stringInput.isnumeric()==True:
        print("Input in not word charector")
        stringInput=input("Enter non numeric string to convert to lower case:\n")
    else:
        print(stringInput.lower())
main()
