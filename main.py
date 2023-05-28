import tkinter as tk


# 11 задание
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        # 11.3
        # Создание начального рейтинга
        self.rating = rating

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now!")

    def set_rating(self, new_rating):
        self.rating = new_rating
        print(f"The new rating for {self.restaurant_name} is {self.rating}")

# 11.1
# Создание экземпляра класса Restaurant
newRestaurant = Restaurant("New Restaurant", "Russian")

# Вывод атрибутов
print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)

# Вызов методов
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()

# 11.2
# Создание трех разных экземпляров
restaurant1 = Restaurant("Restaurant 1", "American")
restaurant2 = Restaurant("Restaurant 2", "Chinese")
restaurant3 = Restaurant("Restaurant 3", "Indian")

# Вызов метода для каждого экземпляра
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# 11.3
# Установка нового рейтинга
newRestaurant.set_rating(4)
