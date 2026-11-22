import json

def load_tasks():
    try:
        with open("storage.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(tasks):
    with open("storage.json", "w") as file:
        json.dump(tasks, file, indent=4)