class order:
    table_number = 0
    clients = 0
    dishes = []

    def __init__(self,table_number, clients):
        self.clients = clients
        self.table_number = table_number
    
    def add_dish(self,dish):
        self.dishes.append(dish)