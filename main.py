print("This application will allow you to save tasks and put their priorty and completion.")

tasks = []

while True:
    taskname = ""
    datedue = ""
    priority = ""
    completion = ""

    while taskname == "": 
        taskname = input("Type in a task: ")

    while datedue == "":
        datedue = input("What is the date it is due (Format: MM/DD/YY): ")

    while priority not in ["Low", "Medium", "High"]:
        priority = input("What is the priority of the task (Low, Medium, High): ")

    while completion not in ["True", "False"]:
        completion = input("Has it been completed or not (True or False): ")

    task = {
        "name": taskname,
        "datedue": datedue,
        "priority": priority,
        "completion": completion
    }

    tasks.append(task)

    continue_or_not = input("Continue? Y/N: ")
    if continue_or_not.lower() == "y":
        continue
    elif continue_or_not.lower() == "n":
        break
    else:
        continue_or_not = input("Invalid Input. Try again. Y/N: ")

print(tasks)

print("This is the end of this instance of the TO-DO List. ")
