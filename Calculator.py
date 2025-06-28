import datetime

#defining a function to get the type of operation from the user
def choose_opr (x , y):
    opr = input("Enter the type of operation you want to do\n"
                "Enter + for addition\n"
                "Enter - for subtraction\n"
                "Enter * for multiplication\n"
                "Enter / for division:\n"
                "Enter ** for Exponentiation:\n"
                "And enter % for Modulo: ")

    #these are valid operation which user allowed to input
    valid_operations = ['+', '-', '*', '/', '**', '%']
    if opr in valid_operations:  #check if the user input is valid or not
        return opr
    else:
        return "invalid input"

#define a new function to calculate what user wanted to
def calculate (x , y , opr):
    if opr == '+':
        return x + y
    elif opr == '-':
        return x - y
    elif opr == '*':
        return x * y
    elif opr == '/':
        return x / y
    elif opr == '**':
        return x ** y
    elif opr == '%':
        return x % y

#defining a new function to write each calculation in a file
def calculation_file(x , y , opr , result):
    my_time = datetime.datetime.now()  #time and date of each calculation
    my_date = my_time.strftime("%d/%m/%Y;%H:%M:%S")  #showing time and date in a particular order
    with open("calculator.csv", "a") as file:  #opening file in append mode
        #add each calculation with time and date in the file
        file.write(f"{x} {opr} {y} = {result};time: {my_date}\n")

#defining a function to show the last 5 calculations as a history
def history():
    try:
        #we need to read this from the file we made in the last function
        with open("calculator.csv") as file:  #opening the file
            lines = file.readlines() #reading the file line by line
            print("last 5 calculations:\n")
            #printing the last five calculations using a for loop
            for line in lines[-5:]:
                line = line.strip()
                print(line)
    except:  #if the user didn't have any calculations
        print("you didn't have any calculations.")

#going through the main function
def main():
    while True:
        num1 = input("input the first number\n"
              "(Enter to exit): ")
        if (num1 == ""):  #if the user input enter program should be exited
            print("thanks for using Calculator!\n"
                  "bye!")
            break
        try:
            num1 = int(num1)
            num2 = int(input("input the second number: "))
            history()
            opr = choose_opr(num1, num2)
            if opr != "invalid input":
                result = calculate(num1, num2, opr)
                print("resulte:", result)
                calculation_file(num1, num2, opr, result)
            else:
                print("invalid operation\n"
                      "please try again")
        except ValueError:
            print("invalid number input\n"
                  "please try again")
        except TypeError:
            print("You entered an invalid type of number.\n"
                  "please try again")
        except Exception as e:
            print("something went wrong:", e)

main()