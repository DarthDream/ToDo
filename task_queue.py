from collections import deque

task_queue = deque()


def enqueue(task_id):
    task_queue.append(task_id)


def dequeue():
    if not task_queue:
        return None

    return task_queue.popleft()


def peek():
    if not task_queue:
        return None

    return task_queue[0]


def remove_task(task_id):
    try:
        task_queue.remove(task_id)
        return True
    except ValueError:
        return False


def show_queue():
    if not task_queue:
        print("Queue is empty!")
        return

    for task_id in task_queue:
        print("Task ID:", task_id)


def queue_size():
    return len(task_queue)


def sync_queue(tasks):
    task_queue.clear()

    for task in tasks:
        if not task["completed"]:
            enqueue(task["id"])