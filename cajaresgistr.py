
import unittest

#---------------------------------------------------------------
#                    PRUEBAS UNITARIAS
#---------------------------------------------------------------

"""class miTest(unittest.TestCase):    

    def test_cocaCola(self):
        self.codigo=2324
        self.assertEqual(self.codigo,2324)

    def test_arroz(self):
        self.codigo=2325
        self.assertEqual(self.codigo,2325)   
    
    def test_harina(self):
        self.codigo=2326
        self.assertEqual(self.codigo,2326)    
    
    def test_cerrarCompra(self):
        self.codigo=0
        self.assertEqual(self.codigo,0)
        self.assertFalse(self.codigo>0)

    def test_sumaCoca(self):
        self.total=0
        self.codigo=2324
        self.total+=60
        self.assertEqual(self.total,60)
    
    def test_sumaArroz(self):
        self.total=0
        self.codigo=2325
        self.total+=55
        self.assertEqual(self.total,55)
    
    def test_sumaHarina(self):
        self.total=0
        self.codigo=2326
        self.total+=65
        self.assertEqual(self.total,65)
        
    def test_aplicarDescuento(self):
        self.total=0
        self.descuento=10
        self.assertEqual(self.total*self.descuento,0)
         

    def test_gestionarPago(self):
        self.reciboCliente=0
        self.faltante=0
        self.subtotal=0
        
        while self.reciboCliente<self.subtotal:
             self.reciboCliente+=self.faltante

        if self.reciboCliente>self.subtotal:
           self.subtotal=self.reciboCliente-self.subtotal 
           self.assertTrue(self.reciboCliente<self.subtotal)
    

if __name__=="__main__":
    unittest.main()"""

#COMENTAR LAS PRUEBAS UNITARIAS  PARA EJUCUTAR EL PROGRAMA. 

#---------------------------------------------------------
#           PROGRAMA  -CAJA RESGISTRADORA- 
#---------------------------------------------------------

class CajaRegistradora():#----Declaracion de la clase
    
    def __init__(self):
        self.total=0

    def ingresarProducto(self):
        """ Función que permite el ingreso y lectura de 
            productos por medio de un código de ID.
            El cajero puede cancelar en cualquier 
            momento precionando "0" """

        self.total=0
       
        while 1:
            self.codigo=int(input("\nIngrese el código del producto:"))
    
            if self.codigo==2324:
                print("\nCoca-Cola 600ml")
                print("Precio unitario: $60 ")
                print("Precio con descuento: $54")
                self.total+=60
                print("Subtotal: $",self.total)
                print()
                print("Precione 0 para finalizar.")
                print("Precione 1 para aplicar descuento.") 
                print()
            elif self.codigo==2325:
                print("\nArroz 500gr.")
                print("Precio unitario: $55 ")
                print("Precio con descuento: $49,50")
                self.total+=55
                print("Subtotal: $",self.total)
                print() 
                print("Precione 0 para finalizar.")
                print("Precione 1 para aplicar descuento.")
                print()   
            elif self.codigo==2326:
                print("\nHarina 1kg.")
                print("Precio unitario: $65 ")
                print("Precio con descuento: $58,50")
                self.total+=65
                print("Subtotal: $",self.total)
                print()
                print("Precione 0 para finalizar.")
                print("Precione 1 para aplicar descuento.")
                print()
            elif self.codigo==1:
                print("Calculando descuento...")
                self.descuento=(self.total*10)/100
                self.total=self.total-self.descuento
                print("Descuento aplicado!\n")
                print("El total es: $",self.total)
              

            elif self.codigo==0:
                print("\nCalulando compra...\n")
                break
            else:
                print("\nCodigo incorrecto!")    
   

    def cobrar(self):
        """ Función que realiza el cobro de los productos
            comprados,verifando que el pago sea
            correcto."""

        self.reciboCliente=0
        self.faltante=0
        self.subtotal=0

        print("\nEl total de la su compra es: $",self.total)
        self.reciboCliente=int(input("Ingrese dinero recibido: $"))
       
        while self.reciboCliente<self.total:

            self.subtotal=self.total-self.reciboCliente
            print("\nFaltan: $",self.subtotal)
            self.faltante=int(input("Ingrese dinero faltante: $"))
            self.reciboCliente=self.reciboCliente+self.faltante
           

        if self.reciboCliente>self.total:
            print("\nCalculando vuelto...")
                    
        elif self.reciboCliente==self.total:    
            print("Pago exacto!")    
       

    def devolver(self):
        """ Comprueba el dinero recibido por el cliente 
            y devuelve el cambio en caso de ser necesario."""
        vuelto=0
        if self.reciboCliente>self.total:
            self.vuelto=self.reciboCliente-self.total
            print("Vuelto: $",self.vuelto)
        else:
            print("Compra finalizada.")    

class ListaPrecios(CajaRegistradora):
  
    def sinDescuento(self):
        self.coca_2324=60
        self.arroz_2325=55
        self.harina_2326=65

    def aplicarDescuento(self):
        self.total=(self.total*10)/100
        print("Descuento aplicado!\n")
        print("El total es: $",self.total)
        
        
#------------------Ejecucion del Programa---------------------
miCompra=CajaRegistradora()
miCompra.ingresarProducto()
miCompra.cobrar()
miCompra.devolver()
