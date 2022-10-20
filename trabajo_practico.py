""" 
Deyner Fabian Serrano / Luigi Navarro 
MacoWins es una reconocida cadena de ropa formal, con tiendas en muchas ciudades de Argentina.
Recientemente, le han pedido a 2Diseños, nuestra consultora de software, que desarrolle un nuevo
sistema para la gestión de sus ventas y stock.
MacoWins guarda la información de sus productos en una lista con la siguiente forma:
"""
from math import prod
import time
from collections import Counter
productos = []
ventas = []



# Productos definidos
buzo_talle_s = {"codigo":100,"nombre":"buzo talle s","categoria":"buzo","precio": 3000,"stock":0}
buzo_talle_m = {"codigo":125,"nombre":"buzo talle m","categoria":"buzo","precio": 4000,"stock":0}
buzo_talle_l = {"codigo":1500,"nombre":"buzo talle l","categoria":"buzo","precio": 5000,"stock":0}
jean_talle_38 = {"codigo":200,"nombre":"jean talle 38","categoria":"jean","precio":8000,"stock":0}
jean_talle_40 = {"codigo":250,"nombre":"jean talle 40","categoria":"jean","precio":9000,"stock":0}
jean_talle_42 = {"codigo":300,"nombre":"jean talle 42","categoria":"jean","precio":10000,"stock":0}

productos = []
ventas = []

""" 1.Registra un producto ya definido
registrar_producto: recibe un diccionario con codigo, nombre, categoria, precio y agrega un
producto nuevo a la lista de productos. El stock del producto agregado debe estar inicialmente
en cero. """ 
def registrar_producto(nuevo_producto):
    list.append(productos,nuevo_producto)

""" 2.Recarga el stock del producto ingresado por codigo
recargar_stock: toma un código de producto y una cantidad de unidad de stock a agregar,
e incrementa el stock correspondiente a ese producto. Si el código de producto indicado no
existe, debe lanzar una excepción."""
def recargar_stock(codigo_producto,cantidad_a_agregar):
    codigo_valido = False
    for producto in productos:
        if codigo_producto == producto["codigo"]:
            codigo_valido = True
            producto["stock"] += cantidad_a_agregar
    if not codigo_valido:
        raise ValueError ("El codigo no corresponde a un producto registrado") # pero lo toma        

""" 3. Consulta si hay stock del producto ingresado por codigo
hay_stock: recibe un código de producto y dice si hay stock (es decir, si el stock
correspondiente es mayor a cero). Si el código indicado no existe en la lista de productos,
debe devolver False. """
def hay_stock(codigo_producto):
    codigo_valido = False
    for producto in productos:
        if codigo_producto == producto["codigo"]:
            return producto["stock"] > 0
    if not codigo_valido:
        raise ValueError ("El codigo no corresponde a un producto registrado")


""" 4.Calcula el precio final y aplica recargo si no es extranjero
calcular_precio_final: toma un producto (un diccionario) y un booleano es_extranjero y
calcula su valor final, según la siguiente regla: a. si quien calcula el precio es extranjero
y el valor es mayor de $70, es el mismo valor sin cambios. b. en caso contrario, es el valor
original más un 21% """
def calcular_precio_final(producto,es_extranjero):
    valor_final = 0
    if es_extranjero and producto["precio"] > 70:
        valor_final = producto["precio"]
        return valor_final
    else:
        valor_final = producto["precio"]+(21*producto["precio"])/100
        return valor_final                      

""" 5.Cuantas categorias unicas de productos registrados hay """
def contar_categorias():
    total_categorias = 0
    lista_categorias = []
    for producto in productos:
        if not producto["categoria"] in lista_categorias:
            total_categorias += 1
            list.append(lista_categorias,producto["categoria"])
    return total_categorias    

""" 6.Realiza una compra y disminuye el stock del los productos vendidos
 realizar_compra: recibe un código de producto y una cantidad de items a comprar. En base a
 ello, decrementa el stock del producto correspondiente y crea una nueva venta con la
 información correspondiente. Si no hay suficiente stock, lanzar una excepción"""
def realizar_compra(codigo_producto,cantidad_a_comprar):
    codigo_valido = False
    stock = False
    for producto in productos:
        if codigo_producto == producto["codigo"]:
            codigo_valido = True
            if producto["stock"] > 0 and producto["stock"] >= cantidad_a_comprar:
                stock = True
                producto["stock"] -= cantidad_a_comprar
                monto_total = producto["precio"]*cantidad_a_comprar
                list.append(ventas,{"local":"macowins","producto":producto["nombre"],"cantidad_vendida":cantidad_a_comprar,"monto":monto_total,"fecha":time.strftime("%x"), "anio":time.strftime("%Y")})
            if not stock:
                raise ValueError ("No hay suficiente stock para realizar la venta")
        
    if not codigo_valido:
            raise ValueError ("El codigo no corresponde a un producto registrado")

""" 7.Discontinua "elimina" los productos que no tengan stock """
def descontinuar_productos():
    for producto in productos:
        if producto["stock"] <= 0:
            list.remove(productos,producto)

""" 8.valor_ventas_del_dia: retorna el valor total de las ventas del día de hoy."""
   
def valor_ventas_del_dia():
    importe_del_dia = 0
    for venta in ventas:
        if venta["fecha"] == time.strftime("%x"):
            importe_del_dia += venta["monto"]
    return importe_del_dia  

""" 9. ventas_del_anio: retorna un listado con todas las ventas para el año actual."""
def ventas_del_anio():
    importe_del_año = 0
    for venta in ventas:
        if venta["anio"] == time.strftime("%Y") == venta["anio"]:
            importe_del_año += venta["monto"]
    return importe_del_año        
    
""" 10.  productos_mas_vendidos: toma una cantidad n de productos y 
retorna los nombres de los n productos más vendidos """ 

def productos_mas_vendidos(cantidad_de_productos):
    productos_vendidos =[] 
    mas_vendidos = []
    for venta in ventas:
        list.append(productos_vendidos,venta["producto"])
        
        mas_vendidos = Counter(productos_vendidos)
        print(" ", mas_vendidos.most_comon(cantidad_de_productos)) 
        

    
""" 11. actualizar_precios_por_categoria: toma una categoría y un porcentaje,
y actualiza según ese porcentaje el precio de todos los productos que 
tengan esa categoría. La búsqueda de categoría en este procedimiento no
debe ser exacta: por ejemplo tanto si se pasa como 
argumento "REMERA", " REMERA" o "Remera", deben actualizarse los productos de la categoría "remera".
"""            

def actualizar_precios_por_categoria(categoria, porcentaje):
    for producto in productos:
        if producto["categoria"] == categoria.lower():
            producto["precio"] += producto["precio"] * porcentaje / 100
            
            
# Reiniciar productos de la tienda
def reiniciar_productos_de_la_tienda():
    productos.clear()
    
# Reiniciar ventas de la tienda 
def reiniciar_ventas_de_la_tienda():
    ventas.clear()            
            
# memoria para dos productos cargados

def lista_de_stock_con_dos_productos():
    reiniciar_productos_de_la_tienda()
    reiniciar_ventas_de_la_tienda()
    registrar_producto(jean_talle_38)
    jean_talle_38[" stock"] = 0
    registrar_producto(buzo_talle_s)
    buzo_talle_s["stock"] = 0
    recargar_stock(200, 50)
    recargar_stock(100, 50)
    

        
    
    


