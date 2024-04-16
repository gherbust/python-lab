class dish:
    name = ""
    description = ""
    price = 0
    status = ""  # active, requested, in_progres, delivered, candeled

    def __init__(self,name, description,price,status):
        self.name = name
        self.description = description
        self.price = price
        self.status = status # active, requested, in_progres, delivered, candeled