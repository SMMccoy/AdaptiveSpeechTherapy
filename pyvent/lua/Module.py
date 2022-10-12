import threading


def spawn(call):
    thread = threading.Thread(target=call)
    thread.start()
    return thread
