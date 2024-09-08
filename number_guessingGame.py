import random                                #Notwendig um das random Modul unten nutzen zu können

print("Welcome to my Number-Guessing Game")
print("This is the first program in which I used the while-loop and the random-module")
print("Published by derCollegeblock")
print("")
print("")
print("")
solution = random.randint(1 , 15)       #lässt das programm eine zufällige Ganzzahl generieren und speichert diese in der variable "solution"
input_number = int(input("Please enter an integer between 1 and 15: "))

while input_number != solution:         #führt den inhalt von der while schleife so lange aus, bis die bedingung nicht mehr erfüllt ist
    if input_number <= solution:
        print("Integer is to small!")
    elif input_number >= solution:
        print("Integer is too big")
    # Die else-Bedingung hier ist nicht notwendig, da die while-schleife aufhört, sobald der Benutzer die richtige Zahl angegeben hat und das sonst zu verwirrung führt.
    input_number = int(input("Try again :) : "))

print(f"That's Correct! The Solution is: {solution}. Congrats!")  # Das ist ein f-String, der verwendet wird, um Elemente zwischen einen String zu schreiben
print("Thank you for using my program :D")

input("Press enter to end the programm...")




