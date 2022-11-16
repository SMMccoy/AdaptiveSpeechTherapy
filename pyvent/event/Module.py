import time
import threading
import uuid
import pyvent.event
import pyvent.data
from pyvent.lua.Module import *


class BindableEvent:
    class Connection:
        def __init__(self, event, func, connection_id):
            self.connection_id = connection_id
            self.event = event
            self.func = func
            self.connected = True

        def disconnect(self):
            self.event.__disconnect(self.connection_id)
            self.connection_id = None
            self.func = None
            self.event = None
            self.connected = False

        def fire(self, bundle):
            self.func(bundle)

    class OnceConnection:
        def __init__(self, event, func, connection_id):
            self.connection_id = connection_id
            self.event = event
            self.func = func
            self.connected = True

        def disconnect(self):
            self.event.disconnect(self.connection_id)
            self.connection_id = None
            self.func = None
            self.event = None
            self.connected = False

        def fire(self, bundle):
            self.func(bundle)
            self.disconnect()

    def __init__(self):
        self.connections = {}

    def connect(self, func):
        uuidid = str(uuid.uuid4())
        connection = BindableEvent.Connection(self, func, uuidid)
        self.connections[uuidid] = connection
        return connection

    def connect_once(self, func):
        uuidid = str(uuid.uuid4())
        connection = BindableEvent.OnceConnection(self, func, uuidid)
        self.connections[uuidid] = connection
        return connection

    def disconnect(self, key):
        self.connections[key] = None

    def fire(self, bundle):
        threads = []
        for i, connectionId in enumerate(self.connections):
            connection = self.connections[connectionId]
            threads.append(threading.Thread(target=connection.fire, args=(bundle,)))
            threads[i].start()

        for thread in threads:
            thread.join()

    def wait_for_fire(self):
        return_value = None
        fired = False

        def set_return(bundle):
            nonlocal return_value
            return_value = bundle
            nonlocal fired
            fired = True

        self.connect_once(set_return)

        while not fired:
            wait(1/120)

        return return_value



class InvokeableFunction:
    def __init__(self, func):
        self.func = func

    def invoke(self, bundle):
        if self.func is not None:
            return self.func(bundle)
        else:
            print("No function is binded")
