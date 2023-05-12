//Funcion para Listar los datos de la Api
function listarLibros() {
    fetch('http://127.0.0.1:5000/listar')
        .then(response => response.json())
        .then(data => {
            // Obtener la tabla y la cabecera
            let tabla = document.getElementById('tabla');
            let cabecera = tabla.createTHead();
            let filaCabecera = cabecera.insertRow();
            
            // Crear las celdas de la cabecera
            let celdaNombre = filaCabecera.insertCell();
            let celdaId = filaCabecera.insertCell();
            let celdaSucursal = filaCabecera.insertCell();
            let celdaCantidad = filaCabecera.insertCell();
            
            // Asignar los valores a las celdas de la cabecera
            celdaNombre.innerText = 'Nombre del libro';
            celdaId.innerText = 'ID del libro';
            celdaSucursal.innerText = 'Nombre de la sucursal';
            celdaCantidad.innerText = 'Cantidad de libros en la sucursal';
            
            // Agregar las filas con los datos de los libros
            for (let libro of data.Consulta) {
                let fila = tabla.insertRow();
                
                let celdaNombre = fila.insertCell();
                let celdaId = fila.insertCell();
                let celdaSucursal = fila.insertCell();
                let celdaCantidad = fila.insertCell();
                
                celdaNombre.innerText = libro.titulo_libro;
                celdaId.innerText = libro.id_libro;
                celdaSucursal.innerText = libro.nombre_sucursal;
                celdaCantidad.innerText = libro.cantidad;
            }
        })
        .catch(error => console.error(error));
}

// Funcion para Consumir el metodo buscar de la API
const botonBuscar = document.querySelector("#boton-buscar");
      const inputTitulo = document.querySelector("#input-titulo");
      const tablaResultados = document.querySelector("#tabla-resultados");
      
      botonBuscar.addEventListener("click", () => {
        // Obtener el título ingresado por el usuario
        const titulo = inputTitulo.value;
        
        // Realizar la solicitud GET al servidor
        fetch(`http://127.0.0.1:5000/buscar/${titulo}`)
          .then(response => response.json())
          .then(data => {
            // Limpiar la tabla de resultados
            tablaResultados.innerHTML = "";
            
            // Mostrar los resultados en la tabla
            data.Consulta.forEach(libro => {
              const fila = document.createElement("tr");
              const celdaNombre = document.createElement("td");
              const celdaId = document.createElement("td");
              const celdaSucursal = document.createElement("td");
              const celdaCantidad = document.createElement("td");
              
              celdaNombre.textContent = libro.titulo_libro;
              celdaId.textContent = libro.id_libro;
              celdaSucursal.textContent = libro.nombre_sucursal;
              celdaCantidad.textContent = libro.cantidad;
              
              fila.appendChild(celdaNombre);
              fila.appendChild(celdaId);
              fila.appendChild(celdaSucursal);
              fila.appendChild(celdaCantidad);
              
              tablaResultados.appendChild(fila);
            });
          })
          .catch(error => console.log(error));
      });