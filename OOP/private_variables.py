class Person:
    accounts = 0

    def __init__(self, name, dob):
        self._name = name
        self.age = self.calcualte_age(dob)

    def __print_name(self):
        # Single _: Protected- Shouldn't be directly accessed from outside
        # Double _: Private- Can't be seen and accessed from outside

        # private or protected function and cannot be accessed directly from
        # outside of the Person class, but can be accessed through
        # private name mangling
        print(self._name)

    def calcualte_age(self, dob):
        import datetime
        now = datetime.datetime.now()
        days = (now - datetime.datetime.strptime(dob, "%Y-%m-%d")).days

        if self.__isleap(now.year):
            return days//366
        else:
            return days//365

    def concat(self):
        return f'My name is {self._name}'

    def __isleap(self, year):
        isleap = False
        if year % 4 == 0:
            if year % 100 != 0 or (year % 100 == 0 and year % 400 == 0):
                isleap = True

        return isleap


p = Person("Tina", "1998-12-4")
# p.__print_name()  # raises AttributeError
p._Person__print_name  # private name mangling
print(p.concat())

# print(f"Person.__doc__: {Person.__doc__}")
# print(f"p.__doc__: {p.__doc__}")

# print(f"\nPerson.__name__: {Person.__name__}")

# print(f"\nPerson.__module__: {Person.__module__}")
# print(f"p.__module__: {p.__module__}")

# print(f"\nPerson.__bases__: {Person.__bases__}")

# print(f"\nPerson.__dict__: {list(Person.__dict__)}")
# print(f"p.__dict__: {list(p.__dict__)}")

# print()
