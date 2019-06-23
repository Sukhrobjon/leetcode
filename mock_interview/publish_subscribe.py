"""
    Question: Write a class contains three function will register the callback with its id, 
    unregister specific callback from a signal id, and runs all the callback associated with
    specific signal id. 
    Hint: Think about how to store(using data structure) the signal id and callback
"""

class SignalRegister:
    # to keep the persistence of the callbacks we declare
    # global dictionary for signal id and set of callbacks
    # { signal_id: {callback1}}
    registered_callbacks = {}
    def register(self, signal_id, callback):
        """
            Takes two arguments signal id and callback. Registers the signal id
            with its associated callback
        """
        # check if signal_id is registered before
        if signal_id not in self.registered_callbacks:
            # add initialize the set with new callback
            callback = set([callback])
            # if not then initialize a set with a single callback
            self.registered_callbacks[signal_id] = callback
        else: # if signal id already registered 
            # simply add new callback to its set of values
            self.registered_callbacks[signal_id].add(callback)


    def unregister(self, signal_id, callback):
        """
            Takes two arguments signal id and callback. And unregisters the specific 
            callback from its signal id
        """
        # if the callback was registered the remove it 
        if signal_id in self.registered_callbacks:
            self.registered_callbacks[signal_id].remove(callback)
        

    def signal(self, signal_id):
        """
            Takes signal id and runs all the callbacks are associated with
        """
        # if signal id is registered runs all its callbacks
        if signal_id in self.registered_callbacks:
            for callback in self.registered_callbacks[signal_id]:
                callback()


def a():
    print("It is a!")


def b():
    print("It is b!")

def c():
    print("It is c!")
sr = SignalRegister()
sr.register(2, a)
sr.register(2, b)
sr.register(3, c)
sr.signal(2) 
"""
    Output: 
    It is b!
    It is a!
"""
sr.signal(3)
"""
    Output: 
    It is b!
    It is a!
    It is c!
"""
sr.unregister(2, a)
print("Now signal id 2 has: ")
sr.signal(2)
