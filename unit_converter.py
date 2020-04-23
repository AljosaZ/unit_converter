print("Hello dear user, this program will convert units from kilometers into miles.")

answer = "yes"
while answer.lower() == "yes":
    kilometers = input("Please enter the number of kilometers you want to convert into miles: ")

    if "," in kilometers:
        kilometers = float(kilometers.replace(",", "."))
    else:
        kilometers = (float(kilometers))

    miles = round(kilometers * 0.6213712, 3)

    print(f"{kilometers} kilometers are equal to {miles} miles.\n")

    answer = input("If you would like to do another conversion please enter yes: ")

print("Thank you and goodbye.")