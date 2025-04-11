tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks added yet.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            status = "✔️ Completed" if task['completed'] else "❌ Not Completed"
            print(f"{i}. {task['name']} [{status}]")

def add_task():
    names = input("Enter task name(s) (use comma to separate multiple): ").strip()
    if names:
        name_list = [name.strip() for name in names.split(",") if name.strip()]
        for name in name_list:
            tasks.append({'name': name, 'completed': False})
        print(f"{len(name_list)} task(s) added.")
    else:
        print("Task name cannot be empty.")


def edit_task():
    show_tasks()
    try:
        num = int(input("Enter task number to edit: "))
        if 1 <= num <= len(tasks):
            new_name = input("Enter new task name: ").strip()
            if new_name:
                tasks[num - 1]['name'] = new_name
                print("Task updated.")
            else:
                print("New name cannot be empty.")
        else:
            print("Invalid task number. Please choose a valid task.")
    except ValueError:
        print("Please enter a valid number.")

def mark_complete():
    show_tasks()
    try:
        num = int(input("Enter task number to mark as completed: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]['completed'] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number. Please choose a valid task.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    show_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Task '{removed['name']}' deleted.")
        else:
            print("Invalid task number. Please choose a valid task.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Edit Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            edit_task()
        elif choice == '4':
            mark_complete()
        elif choice == '5':
            delete_task()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Please enter a valid option (1-6).")

if __name__ == "__main__":
    main()
