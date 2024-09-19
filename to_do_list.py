import tkinter as tk
from tkinter import messagebox, simpledialog


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("500x500")  # Set a fixed size for the window

        # Create listbox to display tasks
        self.task_listbox = tk.Listbox(root, font=("Arial", 14), height=10, width=40)
        self.task_listbox.pack(pady=20)

        # Create entry box to add tasks
        self.task_entry = tk.Entry(root, font=("Arial", 14), width=30)
        self.task_entry.pack(pady=10)

        # Create buttons inside a frame for better layout
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        add_button = tk.Button(
            button_frame, text="Add Task", font=("Arial", 14), command=self.add_task
        )
        add_button.grid(row=0, column=0, padx=10)

        remove_button = tk.Button(
            button_frame,
            text="Remove Task",
            font=("Arial", 14),
            command=self.remove_task,
        )
        remove_button.grid(row=0, column=1, padx=10)

        update_button = tk.Button(
            button_frame,
            text="Update Task",
            font=("Arial", 14),
            command=self.update_task,
        )
        update_button.grid(row=0, column=2, padx=10)

        clear_button = tk.Button(
            root, text="Clear All Tasks", font=("Arial", 14), command=self.clear_tasks
        )
        clear_button.pack(pady=10)

    def add_task(self):
        """Add a task to the listbox."""
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)  # Clear the entry box after adding
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def remove_task(self):
        """Remove the selected task from the listbox."""
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to remove.")

    def update_task(self):
        """Update the selected task with a new task."""
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            current_task = self.task_listbox.get(selected_task_index)
            new_task = simpledialog.askstring(
                "Update Task", "Enter new task:", initialvalue=current_task
            )
            if new_task:
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, new_task)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def clear_tasks(self):
        """Clear all tasks from the listbox."""
        if messagebox.askyesno(
            "Clear All", "Are you sure you want to clear all tasks?"
        ):
            self.task_listbox.delete(0, tk.END)


# Create the main window and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
