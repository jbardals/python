#### Utilizando la información sobre la petición para generar la respuesta

El controlador de ejerc 1 no tiene en cuenta la URL con la que hemos accedido al servidor y siempre va a generar la misma respuesta. Utilizando la información sobre la petición que tenemos guardada en el diccionario  `environ`  podemos construir diferentes respuestas según la petición, por ejemplo teniendo en cuenta la URL de acceso.

El diccionario  `environ`  que se recibe con cada pedido HTTP, contiene las variables estándar de la especificación CGI, entre ellas:

-   `REQUEST_METHOD`: método “GET”, “POST”, etc.
-   `SCRIPT_NAME`: la parte inicial de la “ruta”, que corresponde a la aplicación.
-   `PATH_INFO`: la segunda parte de la “ruta”, determina la “ubicación” virtual dentro de la aplicación.
-   `QUERY_STRING`: la porción de la URL que sigue al “?”, si existe.
-   `CONTENT_TYPE`,  `CONTENT_LENGTH`  de la petición HTTP.
-   `SERVER_NAME`,  `SERVER_PORT`, que combinadas con  `SCRIPT_NAME`  y  `PATH_INFO`  dan la URL.
-   `SERVER_PROTOCOL`: la versión del protocolo (“HTTP/1.0” or “HTTP/1.1”).

De esta forma podemos hacer un [controlador](controller.py) que según el tipo de petición haga diferentes operaciones aritméticas con los valores pasados en los parámetros de la petición para obtener el resultado que se muestra en la [imagen](imgs/resultado.png)

**Modifica el controlador para que además de la suma se pueda enviar una petición para que multiplique los valores que se le pasen como parámetros.**

