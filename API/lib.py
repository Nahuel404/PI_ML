import io

def leer_html(path):
    with io.open(path, 'r', encoding='utf8') as archivo_html:
        contenido_html = archivo_html.read()
    return contenido_html