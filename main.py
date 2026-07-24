print("This application will allow you to save tasks and put their priorty and completion.")

while True:
    continue_or_not = input("Continue? Y/N: ")
    if continue_or_not.lower() == "y":
        continue
    elif continue_or_not.lower() == "n":
        break
    else:
        continue_or_not = input("Invalid Input. Try again. Y/N: ")

print("This is the end of this instance of the TO-DO List. ")

tasks = {

}