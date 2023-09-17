tasks = []

with open("tasks.txt", "r") as f:
  for line in f:
    tasks.append(line.strip())

def create_a_task():
    task_name = input("What is the title of your task? ")
    tasks.append(task_name)
    print("Your tasks are now:", tasks)

def delete_a_task():
    while True:
        print(tasks)
        task_deletion = input("What task would you like to delete? (Case sensitive) ")
        try:
            tasks.remove(task_deletion)
            break
        except ValueError:
            print("This task does not exist. Please try again.")

while True:
    action = input("What would you like to do? [1. view tasks, 2. add tasks, 3. delete tasks, 4. exit] ")
    if action == "1":
        print(tasks)

    elif action == "2":
        create_a_task()

        while True:
            q = input("Would you like to add another task? ")
            if q.lower() == "yes":
                create_a_task()
            else:
                break

    elif action == "3":
        delete_a_task()

        while True:
            q2 = input("Would you like to delete another task? ")
            if q2.lower() == "yes":
                delete_a_task()
            else:
                break

    elif action == "4":
        break

with open("tasks.txt", "w") as f:
    for t in tasks:
        f.write(str(t) + "\n")
