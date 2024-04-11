from objetos.order import order


class ticket(order):
    sub_total = 0
    discount = 0
    taxes = 0
    tip = 0
    total = 0
    status = ""

    def __init__(self,order: order, taxes):
        self.dishes = order.dishes
        self.table_number = order.table_number
        self.taxes = taxes
    
    
    def charge(self, discount,tip):
        sub_total = 0
        for dish in range(self.add_dish):
            


        self.sub_total = sub_total
        self.total = self.sub_total - discount + tip + self.taxes

        self.discount = discount
        self.tip = tip



