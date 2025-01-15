import json

FILENAME = "tasks.json"

def save_tasks(tasks):
    """Salva as tarefas no arquivo JSON."""
    with open(FILENAME, 'w', encoding='utf-8') as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)

def load_tasks():
    """Carrega as tarefas do arquivo JSON."""
    try:
        with open(FILENAME, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

#:V