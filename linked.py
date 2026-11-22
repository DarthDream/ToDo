head = None


def create_node(task_id, title, description):
    return {
        "id": task_id,
        "title": title,
        "description": description,
        "completed": False,
        "next": None
    }


def add_node(task_id, title, description):
    global head

    new_node = create_node(task_id, title, description)

    if head is None:
        head = new_node
        return

    current = head

    while current["next"] is not None:
        current = current["next"]

    current["next"] = new_node


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