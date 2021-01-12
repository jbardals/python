#### Como servir aplicacións Python na Web, correndo en Apache, pero sen utilizar un framework

Nun servidor con Apache2.4 e python3

1.  Comprobamos se está habilitado (e se non é o caso, instalamos e habilitamos) o módulo **libapache2-mod-wsgi-py3**
2.  Crear un directorio para montar toda a aplicación:
    
    mkdir /home/ubuntu/curso-python/trunk/python-web
    
    Dentro deste directorio, crearemos:
    
    1.  Un directorio para a aplicación Python pura (será un directorio privado, non se vai server).
    2.  Un directorio con contidos estáticos (directorio público para servir a aplicación).
    
    mkdir python-web/mypythonapp
    
    mkdir python-web/public_html
    
    En `mypythonapp`, almacenaremos entón todos os módulos e paquetes da nosa aplicación Python, mentres que en `public_html`, estarán os archivos estáticos e será o único directorio ao que se poida acceder desde o navegador Web.
    
3.  En `mypythonapp` crearemos o controlador da aplicación, ver ficheiro *controller.py* 
4. Todas as peticións /URI ás que o usuario acceda polo navegador serán xestionadas polo controlador, que chamará aos módulos correspondentes á URI solicitada.
Se encargará de definir unha función, que actúe con cada petición do usuario. Esta función:
- Deberá chamarse  `application`
- Deberá recibir 2 parámetros:  `environ`, do módulo  `os`, que provee un diccionario das peticións HTTP estándar e outras variables de entorno, e a función  `start_response`, de WSGI, encargada de entregar a resposta HTTP ao usuario.
5. **Configurar o VirtualHost de apache**
Creamos e editamos o ficheiro de configuración do sitio virtual ao que imos dirixir as peticións á webapp python, p.ex:
      *sudo nano /etc/apache2/sites-available/python-web*
   e o configuramos do seguinte xeito:
     DocumentRoot do sitio -> será a carpeta pública, `public_html`
     Coa liña
      *WSGIScriptAlias / /home/ubuntu/python-web/mypythonapp/controller.py* 
      rediriximos as peticións públicas do usuario ao front controller_.
6. Habilitamos o sitio web:  `sudo a2ensite python-web` e recargamos Apache:  `sudo service apache2 reload`
7. Abrindo a url http://python-web se debería ver: _"Bienvenido a mi PythonApp"_.
