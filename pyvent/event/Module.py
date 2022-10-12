import time
import threading
import uuid
import pyvent.event
import pyvent.data

class BindableEvent:
    class Connection:
        def __init__(self, event, id):
            self.id = id
            self.event = event
            self.connected = True;

        def disconnect(self):
            self.event.__disconnect(self.id)
            self.id = None
            self.event = None
            self.connected = False

    def __init__(self):
        self.connections = {}

    def connect(self, func):
        uuidid = str(uuid.uuid4())
        self.connections[uuidid] = func
        connection = BindableEvent.Connection(self, uuidid)
        return connection

    def __disconnect(self, key):
        self.connections[key] = None

    def fire(self, bundle):
        threads = []
        for i, connectionId in enumerate(self.connections):
            connection = self.connections[connectionId]
            threads.append(threading.Thread(target=connection, args=(bundle,)))
            threads[i].start()

        for thread in threads:
            thread.join()


class InvokeableFunction:
    def __init__(self, func):
        self.func = func

    def invoke(self, bundle):
        if self.func is not None:
            return self.func(bundle)
        else:
            print("No function is binded")
