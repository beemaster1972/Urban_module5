class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    @staticmethod
    def get_other(other):
        return other.number_of_floors if isinstance(other,House) else other

    def __eq__(self, other):
        num_of_floor = self.get_other(other)
        return self.number_of_floors == num_of_floor

    def __lt__(self, other):
        num_of_floor = self.get_other(other)
        return self.number_of_floors < num_of_floor

    def __le__(self, other):
        num_of_floor = self.get_other(other)
        return self.number_of_floors <= num_of_floor

    def __gt__(self, other):
        num_of_floor = self.get_other(other)
        return self.number_of_floors > num_of_floor

    def __ge__(self, other):
        num_of_floor = self.get_other(other)
        return self.number_of_floors >= num_of_floor

    def __ne__(self, other):
        num_of_floor = self.get_other(other)
        return self.number_of_floors != num_of_floor
    @staticmethod
    def check(value):
        return value if isinstance(value,int) else 0

    def __add__(self, value):
        num_of_floor = self.check(self.get_other(value))
        self.number_of_floors += num_of_floor
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __sub__(self, value):
        num_of_floor = self.check(self.get_other(value))
        self.number_of_floors -= num_of_floor
        return self

    def __rsub__(self, value):
        num_of_floor = self.check(self.get_other(value))
        self.number_of_floors = num_of_floor - self.number_of_floors
        return self

    def __isub__(self, value):
        return self.__sub__(value)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название {self.name}, кол-во этажей: {self.number_of_floors}'

    def go_to(self,new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
            return False
        print(*[_ for _ in range(1,new_floor+1)])


if __name__ == "__main__":
    h1 = House('ЖК Горский', 18)
    h2 = House('Домик в деревне', 2)
    h1.go_to(5)
    h2.go_to(10)