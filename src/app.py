#Se importan todas las cositas necesarias
from flask import Flask, jsonify, request
from config import config
from flask_mysqldb import MySQL
from datetime import datetime

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

@app.route('/nuevo_pedido', methods=['POST'])
def nuevo_pedido():
    try:
        datos_pedido = request.get_json()
        libros = datos_pedido.get('libros')
        id_sucursal = datos_pedido.get('id_sucursal')
        fecha_pedido = datetime.strptime(datos_pedido.get('fecha_pedido'), '%Y-%m-%d')
        fecha_entrega = datetime.strptime(datos_pedido.get('fecha_entrega'), '%Y-%m-%d')
        
        cursor = conexion.connection.cursor()
        
        # Verificar que hay suficiente stock en la bodega central
        for libro in libros:
            id_libro = libro.get('id_libro')
            cantidad = libro.get('cantidad')
            
            sql = "SELECT cantidad FROM libro_sucursal WHERE id_libro = %s AND id_sucursal = 1"
            cursor.execute(sql, (id_libro,))
            stock_bodega_central = cursor.fetchone()
            if stock_bodega_central is None:
                return jsonify({'mensaje': f"No se encontró el libro con id {id_libro}."})
            stock_bodega_central = stock_bodega_central[0]
            
            if stock_bodega_central < cantidad:
                return jsonify({'mensaje': f"No hay suficiente stock en la bodega central para el libro con id {id_libro}."})
        
        # Agregar el pedido a la base de datos
        for libro in libros:
            id_libro = libro.get('id_libro')
            cantidad = libro.get('cantidad')
            
            # Actualizar la cantidad de libros en la sucursal correspondiente
            sql = "UPDATE libro_sucursal SET cantidad = cantidad - %s WHERE id_libro = %s AND id_sucursal = 6"
            cursor.execute(sql, (cantidad, id_libro))
            
            # Insertar el pedido en la tabla "pedidos"
            sql = "INSERT INTO pedidos (id_libro, id_sucursal, fecha_pedido, fecha_entrega) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (id_libro, id_sucursal, fecha_pedido, fecha_entrega))
            
        # Guardar los cambios en la base de datos
        conexion.connection.commit()
        
        return jsonify({'mensaje': 'Pedido agregado correctamente.'})
    
    except Exception as ex:
        return jsonify({'mensaje': f"Error al agregar el pedido: {ex}"})


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run() 


