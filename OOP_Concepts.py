class Classroom:
    def __init__(self):
        self._people = []

    def add_person(self, person):
        self._people.append(person)

    def remove_person(self, person):
        self._people.remove(person)

    def greet(self):
        for p in self._people:
            print(p.say_hello())

class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, " + self.name)

room = Classroom()
room.add_person(Person("Robespierre"))
room.add_person(Person("Maximillian"))
room.add_person(Person("Premkumar"))

room.greet()
