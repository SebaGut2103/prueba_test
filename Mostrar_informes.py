
def productoInfo():
            fd = open("InformeProduct.txt","r")
            cad =fd.read()
            fd.seek(0)
            cad=fd.read(5)
            print(cad)
            fd.close()
productoInfo
