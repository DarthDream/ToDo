head = None


def create_node(data):
    return {
        "data": data,
        "next": None
    }


def append(data):
    global head

    new_node = create_node(data)

    if head is None:
        head = new_node
        return

    current = head

    while current["next"] is not None:
        current = current["next"]

    current["next"] = new_node


def get_all_tasks():
    tasks = []
    current = head

    while current is not None:
        tasks.append(current["data"])
        current = current["next"]

    return tasks

def find_task(task_id):
    current = head

    while current is not None:
        if current["data"]["id"] == task_id:
            return current["data"]

        current = current["next"]

    return None


def display():
    current = head

    if current is None:
        print("No tasks found!")
        return

    while current is not None:
        print(current["data"])
        current = current["next"]
