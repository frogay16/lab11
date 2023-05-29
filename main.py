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


# 12 задание
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors, location, operating_hours):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
        # 12.2
        # Создания атрибутов для описания локации и времени работы
        self.location = location
        self.operating_hours = operating_hours

    # 12.2
    # Методы добавления и удаления сортов мороженого
    def add_flavor(self, flavor):
        self.flavors.append(flavor)
        print(f"Added {flavor} to the menu")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"Removed {flavor} from the menu")
        else:
            print(f"{flavor} is not on the menu")

    # 12.2
    # Метод проверки наличия сорта мороженого
    def check_flavor(self, flavor):
        return flavor in self.flavors

    def display_flavors(self):
        print(f"Flavors available in {self.restaurant_name} are:")
        print(*self.flavors, sep="\n")

    # 12.3
    # Получить все сорта мороженого
    def get_flavors(self):
        return "\n".join(self.flavors)


# 12.2
# Создание подклассов для разных видов мороженого
class SoftIceCream(IceCreamStand):
    def serve_soft_ice_cream(self):
        print("Serving soft ice cream")


class StickIceCream(IceCreamStand):
    def serve_stick_ice_cream(self):
        print("Serving stick ice cream")


# 12.3
# Функция для отображения сортов мороженого
def show_flavors():
    text.delete(1.0, tk.END)
    text.insert(tk.END, newIceCreamStand.get_flavors())


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

# 12.1
# Создание экземпляра класса IceCreamStand
newIceCreamStand = IceCreamStand(
    "Ice Cream Stand 1",
    "Ice Cream",
    ["Vanilla", "Chocolate", "Strawberry"],
    "Russia",
    "8:00-22:00",
)

# Вызов метода
newIceCreamStand.display_flavors()

# 12.2.4
# Создание экземпляра класса SoftIceCream и StickIceCream
newSoftIceCream = SoftIceCream(
    "Soft Ice Cream 1",
    "Soft Ice Cream",
    ["Chocolate", "Strawberry"],
    "Russia",
    "8:00-22:00",
)
newStickIceCream = StickIceCream(
    "Stick Ice Cream 1",
    "Stick Ice Cream",
    ["Vanilla", "Strawberry"],
    "Russia",
    "8:00-22:00",
)

# Вызов методов
newSoftIceCream.serve_soft_ice_cream()
newStickIceCream.serve_stick_ice_cream()

# 12.3
# Создание окна приложения
root = tk.Tk()
root.geometry("150x150")
root.title("Ice Cream Stand")

# Добавление виджетов
button = tk.Button(root, text="Show flavors", command=show_flavors)
button.pack(pady=10)

text = tk.Text(root, height=5, width=15)
text.pack()

root.mainloop()
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


# 12 задание
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors, location, operating_hours):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
        # 12.2
        # Создания атрибутов для описания локации и времени работы
        self.location = location
        self.operating_hours = operating_hours

    # 12.2
    # Методы добавления и удаления сортов мороженого
    def add_flavor(self, flavor):
        self.flavors.append(flavor)
        print(f"Added {flavor} to the menu")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"Removed {flavor} from the menu")
        else:
            print(f"{flavor} is not on the menu")

    # 12.2
    # Метод проверки наличия сорта мороженого
    def check_flavor(self, flavor):
        return flavor in self.flavors

    def display_flavors(self):
        print(f"Flavors available in {self.restaurant_name} are:")
        print(*self.flavors, sep="\n")

    # 12.3
    # Получить все сорта мороженого
    def get_flavors(self):
        return "\n".join(self.flavors)


# 12.2
# Создание подклассов для разных видов мороженого
class SoftIceCream(IceCreamStand):
    def serve_soft_ice_cream(self):
        print("Serving soft ice cream")


class StickIceCream(IceCreamStand):
    def serve_stick_ice_cream(self):
        print("Serving stick ice cream")


# 12.3
# Функция для отображения сортов мороженого
def show_flavors():
    text.delete(1.0, tk.END)
    text.insert(tk.END, newIceCreamStand.get_flavors())


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

# 12.1
# Создание экземпляра класса IceCreamStand
newIceCreamStand = IceCreamStand(
    "Ice Cream Stand 1",
    "Ice Cream",
    ["Vanilla", "Chocolate", "Strawberry"],
    "Russia",
    "8:00-22:00",
)

# Вызов метода
newIceCreamStand.display_flavors()

# 12.2.4
# Создание экземпляра класса SoftIceCream и StickIceCream
newSoftIceCream = SoftIceCream(
    "Soft Ice Cream 1",
    "Soft Ice Cream",
    ["Chocolate", "Strawberry"],
    "Russia",
    "8:00-22:00",
)
newStickIceCream = StickIceCream(
    "Stick Ice Cream 1",
    "Stick Ice Cream",
    ["Vanilla", "Strawberry"],
    "Russia",
    "8:00-22:00",
)

# Вызов методов
newSoftIceCream.serve_soft_ice_cream()
newStickIceCream.serve_stick_ice_cream()

# 12.3
# Создание окна приложения
root = tk.Tk()
root.geometry("150x150")
root.title("Ice Cream Stand")

# Добавление виджетов
button = tk.Button(root, text="Show flavors", command=show_flavors)
button.pack(pady=10)

text = tk.Text(root, height=5, width=15)
text.pack()

root.mainloop()
