from collections import deque


queue = deque()


def enqueue(task):
    queue.append(task)


def dequeue():
    if len(queue) == 0:
        print("Queue is bos")
        return None

    return queue.popleft()


def peek():
    if len(queue) == 0:
        return None

    return queue[0]


def show_queue():
    if len(queue) == 0:
        print("Queue is bos")
        return

    for task in queue:
        print(task)


def queue_size():
    return len(queue)


def is_empty():
    return len(queue) == 0