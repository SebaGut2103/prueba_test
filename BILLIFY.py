from Main.main import menu
from Mostrar_informes import productoInfo
while True:
    op = menu()
    match op:
        case 1:
            productoInfo()
        case 2:
            open("InformeCliente.txt", "r")
        case 3:
            open("INFO_INV_Dato.txt")    
        case 4:
            print("\n\tGracias por usar el software.\n")
            break