tasks = []


def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added to the list")


def complete_task(task_index):
    task = tasks.pop(task_index)
    print(f"Task '{task}' completed")


def list_tasks():
    print("To-Do List:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")


while True:
    print("\nEnter a command (add, complete, list, exit):")
    user_input = input().strip()
    if user_input == "add":
        task = input("Enter a task: ").strip()
        add_task(task)
    elif user_input == "complete":
        task_index = int(input("Enter task number: ").strip()) - 1
        complete_task(task_index)
    elif user_input == "list":
        list_tasks()
    elif user_input == "exit":
        break
    else:
        print("Invalid command")

        import tkinter as tk


def save_text():
    with open("notes.txt", "w") as f:
        f.write(text.get("1.0", "end"))


root = tk.Tk()
root.title("Notepad")

text = tk.Text(root, wrap="word")
text.pack(fill="both", expand=True)

save_button = tk.Button(root, text="Save", command=save_text)
save_button.pack(side="right", padx=5, pady=5)

root.mainloop()
