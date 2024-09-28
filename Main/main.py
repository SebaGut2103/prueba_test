def menu():
    while True:    
        print(">>> BILLIFY.ACME <<<<")
        print("<-Elija estos opciones.->")
        print("<-1.Consulta de productos.->")
        print("<-2.Consulta de clientes.->")
        print("<-3.Consulta de inventario.->")
        print("\n>> Opción?\n",end="")
        try:
            option=int(input())
            if option<1 or option>4:
                print("ERROR. Opción no válida.")
                input("Presione cualquier letra para volver al menu...")
                continue
            return option
        except ValueError:
            print("ERROR. Opción no válida.")
            input("Presione cualquier letra para volver al menu...")