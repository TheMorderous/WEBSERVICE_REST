# WEBSERVICE_REST_libreria

Estas son las tablas de la base de datos.


-- Crear la tabla libro
CREATE TABLE libro (
  id_libro INT NOT NULL AUTO_INCREMENT,
  titulo VARCHAR(255) NOT NULL,
  autor VARCHAR(255) NOT NULL,
  editorial VARCHAR(255) NOT NULL,
  precio INT NOT NULL,
  PRIMARY KEY (id_libro)
);

-- Crear la tabla sucursal
CREATE TABLE sucursal (
  id_sucursal INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(255) NOT NULL,
  direccion VARCHAR(255) NOT NULL,
  PRIMARY KEY (id_sucursal)
);

-- Crear la tabla pedidos
CREATE TABLE pedidos (
  id_pedido INT NOT NULL AUTO_INCREMENT,
  id_libro INT NOT NULL,
  id_sucursal INT NOT NULL,
  fecha_pedido DATE NOT NULL,
  fecha_entrega DATE NOT NULL,
  PRIMARY KEY (id_pedido),
  FOREIGN KEY (id_libro) REFERENCES libro(id_libro),
  FOREIGN KEY (id_sucursal) REFERENCES sucursal(id_sucursal)
);

-- Crear la tabla pagos
CREATE TABLE pagos (
  id_pago INT NOT NULL AUTO_INCREMENT,
  id_pedido INT NOT NULL,
  fecha_pago DATE NOT NULL,
  monto INT NOT NULL,
  PRIMARY KEY (id_pago),
  FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido)
);

-- Crear la tabla libro_sucursal
CREATE TABLE libro_sucursal (
  id_libro INT NOT NULL,
  id_sucursal INT NOT NULL,
  cantidad INT NOT NULL,
  PRIMARY KEY (id_libro, id_sucursal),
  FOREIGN KEY (id_libro) REFERENCES libro(id_libro),
  FOREIGN KEY (id_sucursal) REFERENCES sucursal(id_sucursal)
);
Un ejemplo de JSON que debe recibir la funcion generar_pedido() es:

{
    "libros": [
        {"id_libro": 1, "cantidad": 3},
        {"id_libro": 2, "cantidad": 3}
    ],
    "id_sucursal": 1
}