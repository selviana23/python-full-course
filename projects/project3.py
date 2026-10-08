tasks = ["Study Python", "Do Maths", "Revise Physics"]
def add():
    task = input("Enter a task: ")
    tasks.append(task)
def view():
    for task in tasks:
        print(tasks)
def delete():
    print(tasks)
    number = int(input("Which tasks you want to remove?"))
    number = number - 1
    tasks.pop(number)
def done():
    print(tasks)

    number = int(input("Which task is done? "))
    number = number - 1

    tasks[number] = tasks[number] + " - DONE"

add()
view()
done()
view()