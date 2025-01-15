import tkinter as tk
from tkinter import ttk, messagebox
from task_model import save_tasks, load_tasks

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Tarefas")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.tasks = load_tasks()

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TButton", font=("Segoe UI", 12), padding=6)
        self.style.configure("TLabel", font=("Segoe UI", 14))
        self.style.configure("TEntry", font=("Segoe UI", 12), padding=5)

        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill="both", expand=True)

        self.task_var = tk.StringVar()
        task_input_frame = ttk.Frame(main_frame)
        task_input_frame.pack(fill="x", pady=5)

        self.task_entry = ttk.Entry(task_input_frame, textvariable=self.task_var, width=30)
        self.task_entry.pack(side="left", padx=5)
        self.task_entry.focus()

        add_button = ttk.Button(task_input_frame, text="Adicionar Tarefa", command=self.add_task)
        add_button.pack(side="right", padx=5)

        self.task_listbox = tk.Listbox(
            main_frame, font=("Segoe UI", 12), height=15, selectmode=tk.SINGLE
        )
        self.task_listbox.pack(pady=10, fill="both", expand=True)
        self.update_task_listbox()

        action_frame = ttk.Frame(main_frame)
        action_frame.pack(pady=10, fill="x")

        complete_button = ttk.Button(action_frame, text="Concluir", command=self.complete_task)
        complete_button.pack(side="left", padx=10, expand=True)

        delete_button = ttk.Button(action_frame, text="Excluir", command=self.delete_task)
        delete_button.pack(side="right", padx=10, expand=True)

    def add_task(self):
        """Adiciona uma nova tarefa à lista."""
        task = self.task_var.get().strip()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.task_var.set("")
            self.update_task_listbox()
            save_tasks(self.tasks)
        else:
            messagebox.showwarning("Aviso", "A tarefa não pode estar vazia!")

    def complete_task(self):
        """Marca uma tarefa como concluída."""
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.update_task_listbox()
            save_tasks(self.tasks)
        else:
            messagebox.showinfo("Informação", "Selecione uma tarefa para marcar como concluída.")

    def delete_task(self):
        """Exclui uma tarefa selecionada."""
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.update_task_listbox()
            save_tasks(self.tasks)
        else:
            messagebox.showinfo("Informação", "Selecione uma tarefa para excluir.")

    def update_task_listbox(self):
        """Atualiza a lista de tarefas exibida."""
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            display_text = f"[{'✔' if task['completed'] else ' '}] {task['task']}"
            self.task_listbox.insert(tk.END, display_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()


#:V