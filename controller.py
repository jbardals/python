def application(environ, start_response):
    # Genero la salida HTML a mostrar al usuario
    output = "<p>Bienvenido a mi <b>PythonApp</b>!!!</p>"
    #output = bytes(output, encoding='utf-8')
    # Inicio una respuesta al navegador
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    # Retorno el contenido HTML
    return [bytes(output, 'utf-8')]