from objetos.ticket import ticket
from objetos.comanda import comanda
from objetos.order import order
from objetos.dish import dish
import objetos.menu as Menu

def create_menu(menu):
    d1= dish("Enfrijoladas", "tortillas con frijoles, queso y crema",80, "active")
    menu.add_dish(d1)
    d2 = dish("Mole poblano", "tortillas con frijoles, queso y crema",150, "active")
    menu.add_dish(d2)

    d3 = dish("Carnitas", "tortillas con frijoles, queso y crema",120, "active")
    menu.add_dish(d3)
    d4 = dish("Barbacoa", "tortillas con frijoles, queso y crema",200, "active")
    menu.add_dish(d4)
    d5 = dish("milanesa de pollo", "tortillas con frijoles, queso y crema",115, "active")
    menu.add_dish(d5)

def print_comanda(orden_comanda: comanda):
    print("numero de Clientes:",orden_comanda.clients)
    print("Numero de mesa: ", orden_comanda.table_number)
    for dish in orden_comanda.dishes:
        print(dish.name)
        print(dish.description)


menu = Menu.menu()
create_menu(menu)

orden = order(15,2)

orden.add_dish(menu.dishes[0])
orden.add_dish(menu.dishes[4])

print(orden.table_number)

orden_comanda = comanda(orden)

print_comanda(orden_comanda)
orden_comanda.status= "done"

orden_ticket =  ticket(orden_comanda,15)
orden_ticket.charge(0,10)

print(orden_ticket.total)






