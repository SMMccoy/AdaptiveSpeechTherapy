import threading
import time


def spawn(call):
    thread = threading.Thread(target=call)
    thread.start()
    return thread


def wait(seconds):
    time.sleep(seconds)
