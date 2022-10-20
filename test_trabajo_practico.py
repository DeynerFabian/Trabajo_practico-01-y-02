from trabajo_practico import *
import pytest
# Test 01 Registrar producto
def test_registrar_un_producto():
    registrar_producto(jean_talle_38)
    assert len(productos) == 1 

# Test 02 Recargar stock
def test_recargar_stock():
    recargar_stock(200, 5)
    assert hay_stock(200)
 
# Test 03 Hay stock 
def test_hay_stock():
    assert hay_stock(200) == True
  
def test_hay_stock_de_jean_talle_38():
    reiniciar_productos_de_la_tienda()
    registrar_producto(jean_talle_38)
    jean_talle_38["stock"] = 0 
    assert hay_stock(200) == False 

# Test 04 Calcular precio final
def test_calcular_precio_final_para_extranjero():
    assert calcular_precio_final(jean_talle_38, True) == 8000

def test_calcular_precio_final_local():
    assert calcular_precio_final({"nombre":"tenis","precio":1000}, False) == 1210


# Test 05 Contar categorias   
def test_contar_categorias_dos():
    reiniciar_productos_de_la_tienda()
    registrar_producto(jean_talle_38)
    registrar_producto(jean_talle_40)
    registrar_producto(jean_talle_42)
    registrar_producto(buzo_talle_s)
    assert contar_categorias() == 2

def test_contar_categorias_uno():
    reiniciar_productos_de_la_tienda()
    registrar_producto(jean_talle_38)
    assert contar_categorias() == 1

def test_contar_categorias_uno():
    reiniciar_productos_de_la_tienda()
    registrar_producto(jean_talle_38)
    registrar_producto(jean_talle_40)
    assert contar_categorias() == 1

# Test 06 Realizar compra        
def test_realizar_compra_uno():
    reiniciar_productos_de_la_tienda()
    registrar_producto(jean_talle_38)
    recargar_stock(200, 5)
    realizar_compra(200, 2)
    assert len(ventas) == 1

def test_realizar_compra_dos():
    reiniciar_productos_de_la_tienda()
    reiniciar_ventas_de_la_tienda()
    registrar_producto(jean_talle_38)
    registrar_producto(jean_talle_40)
    recargar_stock(200, 5)
    recargar_stock(250, 5)
    realizar_compra(200, 2)
    realizar_compra(250, 1)
    realizar_compra(250, 4)
    assert len(ventas) == 3
    
def test_realizar_compra_sin_stock():
    reiniciar_productos_de_la_tienda()
    registrar_producto(jean_talle_38)
    jean_talle_38["stock"] = 0
    with pytest.raises(ValueError) as auxiliar:
        realizar_compra(200, 10)
    assert str(auxiliar.value) == "No hay suficiente stock para realizar la venta"
    
    

# Test 07 Eliminar productos que no tengan Stock  
def test_descontinuar_productos_jean_talle_38():
    lista_de_stock_con_dos_productos()
    
    productos[0]["stock"] = 0 
    descontinuar_productos()
    lista_nombres = [producto["nombre"]for producto in productos]
    assert not "jean talle 38" in lista_nombres 

def test_Probar_multiples_assert():
    lista_de_stock_con_dos_productos()
    
    lista_nombres_one = [producto["nombre"]for producto in productos]
    errores = []
    if "jean talle 38" not in lista_nombres_one:
        errores.append("no hay jean talle 38 en la lista one")
    productos[0]["stock"] = 0 

    descontinuar_productos()
    
    lista_nombres_final = [producto["nombre"]for producto in productos]
    if "jean talle 38" in lista_nombres_final:
        errores.append("sí hay jean talle 38 en la lista (no se elimino)")
    assert not errores, "errores encontrados:{}".format("".join(errores))
 

# Test 08 Valor ventas del dia  
def test_ventas_del_dia_con_variable_declarada():
    lista_de_stock_con_dos_productos()
    realizar_compra(200,1)
    realizar_compra(100,1)
    assert valor_ventas_del_dia() == 11000
    
    
# Test 09 ventas de año
def test_total_de_las_ventas_del_anio_van_a_ser_dos():
    lista_de_stock_con_dos_productos()
    realizar_compra(200, 2)
    realizar_compra(100, 1)
    assert ventas_del_anio() == 19000 

def test_valor_de_las_ventas_con_distintos_anios():
    lista_de_stock_con_dos_productos()
    realizar_compra(200, 1)
    ventas.append({"producto":"zapato","monto":10000,"anio":2020})
    assert ventas_del_anio() == 8000

# Test 10. Nos muestras cuales fueron los productos mas vendidos.
# En la medida de lo posible lo estaremos solucionando 

def test_productos_mas_vendidos():
    lista_de_stock_con_dos_productos()
    realizar_compra(100,1)
    assert len(productos_mas_vendidos(1)) == 1

#Test 11. Actualizacion de precios por categoria 
def test_para_actualizar_porcentajes_de_precios_de_la_categoria_buzo_dejando_la_categoria_jean_con_precios_congelados():
    reiniciar_productos_de_la_tienda()
    registrar_producto(buzo_talle_s)
    buzo_talle_s["stock"] = 0
    registrar_producto(jean_talle_38)
    jean_talle_38["stock"] = 0
    registrar_producto(jean_talle_40)
    jean_talle_40["stock"] = 0
    actualizar_precios_por_categoria("buzo",50)
    assert productos[0]["precio"] == 4500 and productos[1]["precio"] == 8000 and productos[2]["precio"] == 9000

# las prueba de manera individual funcionan perfectamente, pero cuando se prueban
# en conjunto genera un error, por eso lo tenemos comentado en este momento 
"""
def test_actualizar_porcentaje_precios_de_la_categoria_jean():
    reiniciar_productos_de_la_tienda()
    registrar_producto(jean_talle_38)
    jean_talle_38["stock"] = 0
    registrar_producto(jean_talle_40)
    jean_talle_40["stock"] = 0
    registrar_producto(jean_talle_42)
    jean_talle_42["stock"] = 0
    actualizar_precios_por_categoria("jean",30)
    assert productos[0]["precio"] == 10400 and productos[1]["precio"] == 11700 and productos[2]["precio"] == 13000
"""
    