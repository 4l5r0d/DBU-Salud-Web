let listElements = document.querySelectorAll('.list__button--click');
/*El de arriba menciona a todos los que tengan subelementos botones*/
listElements.forEach(listElement => {
    listElement.addEventListener('click', ()=>{

        listElement.classList.toggle('arrow');

        let height = 0;
        let menu = listElement.nextElementSibling;/*esto llama al hermano adyasente, de (listbutton--click) el hermano es (ul) o sea los subtemas*/
        console.log(menu.scrollHeight)/*(scrollHeight) te dira el alto minimo de un elemento para que exista y no se desborde, o sea da un número de cada subelemento te dira el tamaño */
        if(menu.clientHeight == "0"){ /*Entonces se crea una condicional, para lograr que se despliegue el menú*/
            height=menu.scrollHeight;
        }
        menu.style.height = height+"px";
    })
});

document.addEventListener('DOMContentLoaded', function () {
    var menuItems = document.querySelectorAll('.nav__link');
    var contenidoDiv = document.getElementById('contenido');

    menuItems.forEach(function (item) {
        item.addEventListener('click', function () {
            var menuItemId = this.getAttribute('data-menu-item-id');

            // Lista de identificadores de opciones que deben mostrar el contenido
            var opcionesMostrarContenido = [
                'medicina', 'odontologia', 'psico', 'laboratorio', 'inicio', 
                'campanas', 'objetivos', 'funciones', 'unidad', 'contacto'
            ];

            // Verificar si la opción seleccionada debe mostrar el contenido
            if (opcionesMostrarContenido.includes(menuItemId)) {
                cargarContenido('/obtener_contenido/' + menuItemId);
            } else {
                // Si no debe mostrar contenido, vaciar el div de contenido
                contenidoDiv.innerHTML = '';
            }
        });
    });

    function cargarContenido(url) {
        fetch(url)
            .then(response => response.text())
            .then(data => {
                contenidoDiv.innerHTML = data;
            })
            .catch(error => console.error('Error al cargar contenido:', error));
    }
});