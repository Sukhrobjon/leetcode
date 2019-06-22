class SignalRegister:
    registered_callbacks = {}
    def register(self, signal_id, callback):
        # check if signal_id is registered before
        if signal_id not in self.registered_callbacks:
            # if not then initialize a set with a single callback
            self.registered_callbacks[signal_id] = set([callback])
        else: # if already in registered 
            # simply add new callback to its set of values
            self.registered_callbacks[signal_id].add(callback)


    def unregister(self, signal_id, callback):
        if signal_id in self.registered_callbacks:
            self.registered_callbacks[signal_id].remove(callback)
        

    def signal(self, signal_id):
        if signal_id in self.registered_callbacks:
            for callback in self.registered_callbacks[signal_id]:
                callback()


def a():
    print("it is a")


def b():
    print("it is b")

sr = SignalRegister()
sr.register(2, a)
sr.register(2, b)
sr.register(2, b)
sr.register(2, b)
# sr.unregister(2, a)
# print(sr.registered_callbacks)
sr.signal(2)