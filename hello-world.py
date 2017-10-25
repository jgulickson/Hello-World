# !/usr/bin/env python

try:
    import random
except ImportError:
    raise ImportError("Random package failed to load")


#
# Unnecessarily lengthy/complex print of 'Hello World'
#
class HelloWorld:
    def __init__(self):
        self.index = range(4)
        self._hello_possibilities = None
        self.hello = None
        self._space_possibilities = None
        self.space = None
        self._world_possibilities = None
        self.world = None

    def message_hello(self, index):
        self._hello_possibilities = ["Hello", "hello", "HELLO", "hElLo"]
        self.hello = self._hello_possibilities[index]

    def message_space(self, index):
        self._space_possibilities = [" ", ".", "-", "_"]
        self.space = self._space_possibilities[index]

    def message_world(self, index):
        self._world_possibilities = ["World", "world", "WORLD", "wOrLd"]
        self.world = self._world_possibilities[index]


def print_message():
    """
    Prints "Hello World" four times;
    Content is random each time with one value
    selected from each of the three lists.
    """
    x = HelloWorld()

    for i in x.index:
        x.message_hello(random.randint(min(x.index), max(x.index)))
        x.message_space(random.randint(min(x.index), max(x.index)))
        x.message_world(random.randint(min(x.index), max(x.index)))
        print("#" + str(i + 1) + " " + x.hello + x.space + x.world)


if __name__ == "__main__":
    print(print_message.__doc__)
    print_message()
