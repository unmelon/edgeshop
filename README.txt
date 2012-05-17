**************************************
**************************************
**************************************

        EDGE SHOP
        
**************************************
**************************************
**************************************


**************************************
**************************************
**************************************
INSTALACION

Instalar los paquetes requeridos por el programa:
- MySQLdb
- Scrapy 0.14.4 o superior

- ejecutar las sentencias sql del fichero: create_tables

**************************************
**************************************
**************************************
Ejecucion

ejecutar en consola : 
>python edge.py
*se necesita conexion a internet



**************************************
**************************************
**************************************
NOTAS:
el programa ejecuta :
    os.system("scrapy crawl edgeshopspider")
justo al empezar, para contar con los datos actualizados.

La interfaz grafica esta desprovista de botones
(las imagenes son los botones)

para volver desde una categoria a la vista general
cerrar la ventana de elementos (de manera normal)

**************************************
**************************************
**************************************

funcionamiento:

la aplicacion captura el catalogo de productos de la empresa
edge : www.edge.com
descarga los nombres , las imagenes y los enlaces web a los productos
y los guarda en una base de datos,
el programa obtiene dichos datos de la BD 
y los muestra en manera de botones con imagenes
de una forma totalmente dinamiga
(se generan los botones jutos y necesarios para cada elemento)
la interfaz es totalmente limpia, la ventana y los iconos, nada mas.

