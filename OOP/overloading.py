class Person:
    accounts = 0

    def __init__(self, name):
        self._name = name

    def concat(self):
        return f'My name is {self._name}'

    def concat(self, last_name):
        return f'My name is {self._name} {last_name}'


# print(Person("Tina").concat())
# TypeError: concat() missing 1 required positional argument: 'last_name'

print(Person("Tina").concat("Murimi"))
# My name is Tina Murimi