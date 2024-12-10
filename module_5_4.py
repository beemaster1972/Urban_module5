from house import House


h1 = House('ЖК Эльбрус', 10)
print(1, House.get_house_history())
h2 = House('ЖК Акация', 20)
print(2, House.get_house_history())
h3 = House('ЖК Матрёшки', 20)
print(3, House.get_house_history())

# Удаление объектов
del h2
del h3


print(4, House.get_house_history())