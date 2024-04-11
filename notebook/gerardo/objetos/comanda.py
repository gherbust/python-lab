from objetos.order import order

class comanda(order):
    status = ""
    def __init__(self, order:order):
        self.table_number = order.table_number
        self.dishes= order.dishes
        self.clients=order.clients