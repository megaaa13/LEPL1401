class EmployeeDidntWorked(BaseException):
    def __str__(self):
        return "Fo travailler"
class EmployeeWorkedNegatively(BaseException):
    def __str__(self):
        return "Fo travailler un peu quand même"
class EmployeeWorkedTooMuch(BaseException):
    def __str__(self):
        return "Fo travailler moins"
class PayIsNegative(BaseException):
    def __str__(self):
        return "Donne moi de l'argent"
class PayIsTooBig(BaseException):
    def __str__(self):
        return "Riche."
def pay_employee(employee, hours):
    if hours == 0:
        raise EmployeeDidntWorked
    if hours < 0:
        raise EmployeeWorkedNegatively
    if hours > 24*31:
        raise EmployeeWorkedTooMuch
    if employee.pay < 0:
        raise PayIsNegative
    if employee.pay > 100:
        raise PayIsTooBig
    employee.receive_salary(hours * employee.pay)

class Command:
    commands = 0
    price = 0

    def __init__(self, id_buyer, id_item, quantity_item, price_item):
        self.id_buyer = id_buyer
        self.id_item = id_item
        self.quantity_item = quantity_item
        self.price_item = price_item
        Command.commands += 1
        Command.price += price_item * quantity_item

    def get_price(self):
        return self.price_item * self.quantity_item

    def __str__(self):
        return f"{self.id_buyer}, {self.id_item} : {self.price_item} * {self.quantity_item} = " \
               f"({self.price_item * self.quantity_item})"

    @classmethod
    def get_number_total_command(cls):
        return cls.commands

    @classmethod
    def get_total_price(cls):
        return cls.price
