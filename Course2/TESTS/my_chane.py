types = {int: 'INT', float: 'FLOAT', str: 'STR'}

class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, obj, event):
        if self.__successor is not None:
            return self.__successor.handle(obj, event)


class EventGet:
    def __init__(self, type):
        self.type = type


class EventSet:
    def __init__(self, value):
        self.value = value


class IntHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, EventGet):
            if types[event.type] == 'INT':
                return obj.integer_field
            else:
                return super().handle(obj, event)
        elif isinstance(event, EventSet):
            if isinstance(event.value, int):
                obj.integer_field = event.value
            else:
                super().handle(obj, event)
        else:
            super().handle(obj, event)



class FloatHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, EventGet):
            if types[event.type] == 'FLOAT':
                return obj.float_field
            else:
                return super().handle(obj, event)
        elif isinstance(event, EventSet):
            if isinstance(event.value, float):
                obj.float_field = event.value
            else:
                super().handle(obj, event)
        else:
            super().handle(obj, event)


class StrHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, EventGet):
            if types[event.type] == 'STR':
                return obj.string_field
            else:
                return super().handle(obj, event)
        elif isinstance(event, EventSet):
            if isinstance(event.value, str):
                obj.string_field = event.value
            else:
                super().handle(obj, event)
        else:
            super().handle(obj, event)



obj = SomeObject()
obj.integer_field = 42
obj.float_field = 3.14
obj.string_field = "some text"
chain = IntHandler(FloatHandler(StrHandler(NullHandler())))
print(chain.handle(obj, EventGet(int)))
print(chain.handle(obj, EventGet(float)))
print(chain.handle(obj, EventGet(str)))
chain.handle(obj, EventSet(100))
print(chain.handle(obj, EventGet(int)))
chain.handle(obj, EventSet(0.5))
print(chain.handle(obj, EventGet(float)))
chain.handle(obj, EventSet('new text'))
print(chain.handle(obj, EventGet(str)))
