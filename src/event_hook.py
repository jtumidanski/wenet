class EventHook(object):
    def __init__(self):
        super().__init__()
        self._handlers = []

    def __iadd__(self, other):
        self._handlers.append(other)
        return self

    def __isub__(self, other):
        self._handlers.remove(other)
        return self

    def fire(self, *args, **keyargs):
        for handler in self._handlers:
            handler(*args, **keyargs)