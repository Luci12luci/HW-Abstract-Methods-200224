class Shoes:
    def __init__(self, shoes_id, gender_type, color, price, brand, size):
        self.id = shoes_id
        self.type = gender_type
        self.color = color
        self.price = price
        self.brand = brand
        self.size = size


class ShoesModel:
    def __init__(self):
        self.shoes = []

    def add_shoes_id(self):
        self.shoes.append(shoes)

    def remove_shoes_id(self):
        self.shoes.remove(shoes)

    def get_all_shoes_id(self):
        return [shoes for shoes in self.shoes if id == id]

    def get_shoes_size(self, shoes_size):
        return [shoes for shoes in self.shoes if shoes_size == size]

    def get_shoes_price(self, shoes_price):
        return [shoes for shoes in self.shoes if shoes_price == price]


def display_shoes():
    print("\nShoes:")


class ShoesView:
    pass
    # for Shoes in Shoes: print(f"id: {shoe.shoe_id}, Brand: {shoe.brand}, Size: {shoe.size}, Color: {shoe.color},
    # Availability: {shoe.availability})


from ShoesModel import Shoes


def add_shoes(name):
    shoes = Shoes(name)
    self.model.add_shoes(shoes)


class ShoesController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def complete_shoes(self, name):
        for shoes in self.model_get_shoes():
            if shoes.name == name:
                shoes.complete()

    def display_shoes(self):
        self.model.get_shoes()
        self.view.display_shoes(shoes)

    from shoescontroller import ShoesController
    from shoesmodel import ShoesModel
    from shoesview import ShoesView

    model = ShoesModel()
    view = ShoesView()
    controller = ShoesController(model, view)

    controller.add_shoes("")
    controller.add_shoes("")
    controller.add_shoes("")

    controller.complete_shoes("")

    controller.diplay_shoes()
