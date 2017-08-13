from person import Person

class Manager(Person):
    def __init__(self, name, age, pay=0):
        Person.__init__(self, name, age, pay, "Manager")

    def giveRaise(self, percent, bonus=0.1):
        Person.giveRaise(self, percent + bonus)

if __name__ == "__main__":
    tom = Manager("Tom Roberts", 35, 60000)
    print(tom)
    tom.giveRaise(0.1)
    print(tom)
    print(tom.lastName())