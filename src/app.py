#Se importan todas las cositas necesarias
from flask import Flask, jsonify, request
from config import config
from flask_mysqldb import MySQL
from datetime import datetime, timedelta

app=Flask(__name__)

conexion = MySQL(app)
#Funcion para listra todos los libros disponibles en las distintas sucursales
@app.route('/listar', methods =['GET'])
def listar_libros():
    try:
        cursor=conexion.connection.cursor()
        sql="""
            SELECT libro.titulo AS 'Nombre del libro', libro.id_libro AS 'ID del libro', sucursal.nombre AS 'Nombre de la sucursal', libro_sucursal.cantidad AS 'Cantidad de libros en la sucursal'
            FROM libro
            JOIN libro_sucursal ON libro.id_libro = libro_sucursal.id_libro
            JOIN sucursal ON libro_sucursal.id_sucursal = sucursal.id_sucursal;
            """
        cursor.execute(sql)
        datos=cursor.fetchall()
        libros=[]
        for fila in datos:
            libro={'cantidad':fila[0],'titulo_libro': fila[1], 'nombre_sucursal': fila[2], 'id_libro': fila[3]}
            libros.append(libro)
        return jsonify({'Consulta':libros ,'mensaje':"Libros listados correctamente chuchetumare"})
    except Exception as ex:
        return "Algo hiciste mal, wea" 
    
#Funcion para buscar libros especificos por el nombre en todas las sucursales que esten disponibles (asumimos que no se sabran los ID de memoria)
@app.route('/buscar/<titulo>', methods =['GET'])
def buscar(titulo):
    print(f"El valor del parámetro 'titulo' es: {titulo}")
    try:
        cursor=conexion.connection.cursor()
        sql="""
            SELECT libro.titulo AS 'Nombre del libro', libro.id_libro AS 'ID del libro', sucursal.nombre AS 'Nombre de la sucursal', libro_sucursal.cantidad AS 'Cantidad de libros en la sucursal'
            FROM libro
            JOIN libro_sucursal ON libro.id_libro = libro_sucursal.id_libro
            JOIN sucursal ON libro_sucursal.id_sucursal = sucursal.id_sucursal
            WHERE libro.titulo LIKE '%{0}%';
            """.format(titulo)
        print("Consulta SQL:", sql)
        cursor.execute(sql)
        datos=cursor.fetchall()
        print(datos)
        libros=[]
        for fila in datos:
            libro={'id_libro':fila[0],'titulo_libro': fila[1], 'nombre_sucursal': fila[2], 'cantidad': fila[3]}
            libros.append(libro)
        if len(datos) > 0:
            return jsonify({'Consulta':libros ,'mensaje':"Libros listados correctamente chuchetumare"})
        else:
            return "Algo hiciste mal, wea, no se encontro ningun libro"
    except Exception as ex:
        return "Algo hiciste mal, wea"



##Funcion para generar un pedido
#Funcion para generar un nuevo pedido
# Funcion para generar un nuevo pedido
@app.route('/pedido', methods=['POST'])
def generar_pedido():
    try:
        # Se obtienen los datos del pedido a través del cuerpo de la solicitud
        datos_pedido = request.get_json()
        
        # Se obtienen los datos necesarios del pedido
        libros = datos_pedido['libros']
        cantidad = []
        for libro in libros:
            cantidad.append(libro['cantidad'])
        id_sucursal = datos_pedido['id_sucursal']
        fecha_pedido = datetime.now().strftime('%Y-%m-%d')
        fecha_entrega = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
        
        # Se crea el registro del pedido en la tabla pedidos
        cursor = conexion.connection.cursor()
        sql = """
            INSERT INTO pedidos (id_libro, id_sucursal, fecha_pedido, fecha_entrega)
            VALUES (%s, %s, %s, %s);
            """
        
        # Se recorren los libros y se actualiza la tabla libro_sucursal
        for i in range(len(libros)):
            id_libro = libros[i]['id_libro']
            cant = cantidad[i]
            # Se actualiza la cantidad de libros en la sucursal correspondiente
            sql_update = "UPDATE libro_sucursal SET cantidad = cantidad - %s WHERE id_libro = %s AND id_sucursal = %s"
            cursor.execute(sql_update, (cant, id_libro, id_sucursal))
            # Se agrega el detalle del libro al pedido
            cursor.execute(sql, (id_libro, id_sucursal, fecha_pedido, fecha_entrega))
        
        conexion.connection.commit()
        return "Pedido generado correctamente"
    
    except Exception as ex:
        print(str(ex))
        conexion.connection.rollback()
        return "Algo hiciste mal, wea"

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run() 


