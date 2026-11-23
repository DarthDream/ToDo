from collections import deque

queue = deque()


def enqueue(task):
    queue.append(task)


def dequeue():
    if not queue:
        print("Queue is empty!")
        return None

    return queue.popleft()


def peek():
    if not queue:
        print("Queue is empty!")
        return None

    return queue[0]


def get_all_tasks():
    return list(queue)


def display():
    if not queue:
        print("Queue is empty!")
        return

    for task in queue:
        print(task)


def size():
    return len(queue)


def is_empty():
    return len(queue) == 0