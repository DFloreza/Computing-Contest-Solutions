burgerChoice = eval(input())
sideChoice = eval(input())
drinkChoice = eval(input())
dessertChoice = eval(input())

if burgerChoice == 1:
    bcalories = 461
if burgerChoice == 2:
    bcalories = 431
if burgerChoice == 3:
    bcalories = 420
if burgerChoice == 4:
    bcalories = 0
    
if sideChoice == 1:
    scalories = 100
if sideChoice == 2:
    scalories = 57
if sideChoice == 3:
    scalories = 70
if sideChoice == 4:
    scalories = 0
    
if drinkChoice == 1:
    dkcalories = 130
if drinkChoice == 2:
    dkcalories = 160
if drinkChoice == 3:
    dkcalories = 118
if drinkChoice == 4:
    dkcalories = 0

if dessertChoice == 1:
    dcalories = 167
if dessertChoice == 2:
    dcalories = 266
if dessertChoice == 3:
    dcalories = 75
if dessertChoice == 4:
    dcalories = 0
    
totalCalories = bcalories + scalories + dkcalories + dcalories
print("Your total Calorie count is", str(totalCalories) + ".")
