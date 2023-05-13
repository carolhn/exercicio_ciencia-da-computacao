class Address:
    def __init__(self, street, number, district):
        self.street = street
        self.number = number
        self.district = district


class User:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


class Company:
    def __init__(self, name, address):
        self.name = name
        self.address = address
