head = None


def create_node(task_id, title, description, completed=False):
    return {
        "id": task_id,
        "title": title,
        "description": description,
        "completed": completed,
        "next": None
    }


def add_node(task_id, title, description, completed=False):
    global head

    new_node = create_node(task_id, title, description, completed)

    if head is None:
        head = new_node
        return True

    current = head

    while current["next"] is not None:
        if current["id"] == task_id:
            return False
        current = current["next"]

    if current["id"] == task_id:
        return False

    current["next"] = new_node
    return True


def show_nodes():
    current = head

    if current is None:
        print("No tasks found!")
        return

    while current is not None:
        print(f'''
ID: {current["id"]}
Title: {current["title"]}
Description: {current["description"]}
Completed: {current["completed"]}
''')
        current = current["next"]


def search_node(task_id):
    current = head

    while current is not None:
        if current["id"] == task_id:
            return current

        current = current["next"]

    return None


def delete_node(task_id):
    global head

    if head is None:
        return False

    if head["id"] == task_id:
        head = head["next"]
        return True

    current = head

    while current["next"] is not None:
        if current["next"]["id"] == task_id:
            current["next"] = current["next"]["next"]
            return True

        current = current["next"]

    return False


def update_node(task_id, title, description):
    node = search_node(task_id)

    if node is None:
        return False

    node["title"] = title
    node["description"] = description
    return True


def complete_node(task_id):
    node = search_node(task_id)

    if node is None:
        return False

    node["completed"] = True
    return True


def show_completed():
    current = head

    while current is not None:
        if current["completed"]:
            print(current["id"], current["title"])

        current = current["next"]


def show_pending():
    current = head

    while current is not None:
        if not current["completed"]:
            print(current["id"], current["title"])

        current = current["next"]


def get_all_tasks():
    tasks = []
    current = head

    while current is not None:
        tasks.append({
            "id": current["id"],
            "title": current["title"],
            "description": current["description"],
            "completed": current["completed"]
        })

        current = current["next"]

    return tasks


def load_nodes(tasks):
    global head
    head = None

    for task in tasks:
        add_node(
            task["id"],
            task["title"],
            task["description"],
            task["completed"]
        )