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

Rellenar tablas BBDD

INSERT INTO libro (titulo, autor, editorial)
VALUES
('ChainsawMan #1', 'Tatsuki Fujimoto', 'IVREA'),
('ChainsawMan #2', 'Tatsuki Fujimoto', 'IVREA'),
('ChainsawMan #3', 'Tatsuki Fujimoto', 'IVREA'),
('ChainsawMan #4', 'Tatsuki Fujimoto', 'IVREA'),
('ChainsawMan #5', 'Tatsuki Fujimoto', 'IVREA'),
('ChainsawMan #6', 'Tatsuki Fujimoto', 'IVREA'),
('ChainsawMan #7', 'Tatsuki Fujimoto', 'IVREA'),
('ChainsawMan #8', 'Tatsuki Fujimoto', 'IVREA'),
('ChainsawMan #9', 'Tatsuki Fujimoto', 'IVREA'),
('ChainsawMan #10', 'Tatsuki Fujimoto', 'IVREA'),
('ChainsawMan #11', 'Tatsuki Fujimoto', 'IVREA'),
('ChainsawMan #12', 'Tatsuki Fujimoto', 'IVREA'),
('Jujutsu Kaisen #1', 'Gege Akutami', 'Norma Editorial'),
('Jujutsu Kaisen #2', 'Gege Akutami', 'Norma Editorial'),
('Jujutsu Kaisen #3', 'Gege Akutami', 'Norma Editorial'),
('Jujutsu Kaisen #4', 'Gege Akutami', 'Norma Editorial'),
('Jujutsu Kaisen #5', 'Gege Akutami', 'Norma Editorial'),
('Jujutsu Kaisen #6', 'Gege Akutami', 'Norma Editorial'),
('Jujutsu Kaisen #7', 'Gege Akutami', 'Norma Editorial'),
('Jujutsu Kaisen #8', 'Gege Akutami', 'Norma Editorial'),
('Jujutsu Kaisen #9', 'Gege Akutami', 'Norma Editorial'),
('Jujutsu Kaisen #10', 'Gege Akutami', 'Norma Editorial'),
('Jujutsu Kaisen #11', 'Gege Akutami', 'Norma Editorial'),
('Jujutsu Kaisen #12', 'Gege Akutami', 'Norma Editorial'),
('Jujutsu Kaisen #13', 'Gege Akutami', 'Norma Editorial'),
('Jujutsu Kaisen #14', 'Gege Akutami', 'Norma Editorial'),
('Jujutsu Kaisen #15', 'Gege Akutami', 'Norma Editorial'),
('Jujutsu Kaisen #16', 'Gege Akutami', 'Norma Editorial'),
('Jujutsu Kaisen #17', 'Gege Akutami', 'Norma Editorial'),
('Jujutsu Kaisen #18', 'Gege Akutami', 'Norma Editorial'),
('Jujutsu Kaisen #19', 'Gege Akutami', 'Norma Editorial'),
('Jujutsu Kaisen #20', 'Gege Akutami', 'Norma Editorial');

INSERT INTO sucursal (nombre, direccion, pais) 
VALUES 
  ('Librería Nacional', 'Av. Providencia 2700, Providencia', 'Chile'),
  ('Librería Antártica', 'Costanera Center, Av. Andrés Bello 2425, Providencia', 'Chile'),
  ('Librería Qué Leo', 'Av. Chile España 393, Providencia', 'Chile'),
  ('Librería Catalonia', 'Nueva Providencia 2353, Providencia', 'Chile'),
  ('Librería Golden Book', 'Mall Alto Las Condes, Av. Kennedy 9001, Las Condes', 'Chile');


Un ejemplo de JSON que debe recibir la funcion generar_pedido() es:

{
    "libros": [
        {"id_libro": 1, "cantidad": 3},
        {"id_libro": 2, "cantidad": 3}
    ],
    "id_sucursal": 1
}