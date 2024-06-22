import requests
import xml.etree.ElementTree as ET

# URL del feed RSS de Google News para un tema específico
rss_url = 'https://news.google.com/rss/search?q=Inteligencia+Artificial&hl=es-419&gl=MX&ceid=MX:es-419'

# Hacer una solicitud GET al feed RSS
response = requests.get(rss_url)

# Parsear el contenido del feed RSS
root = ET.fromstring(response.content)

# Extraer noticias del feed RSS
noticias = []
for item in root.findall('.//item'):
    titulo = item.find('title').text
    descripcion = item.find('description').text
    link = item.find('link').text
    pub_date = item.find('pubDate').text
    noticias.append({
        'fecha': pub_date,
        'titulo': titulo,
        'descripcion': descripcion,
        'link': link
    })

# Leer el contenido actual de noticias.md
with open('noticias.md', 'r', encoding='utf-8') as file:
    contenido_actual = file.read()

# Generar el contenido actualizado
nuevo_contenido = "# Noticias Relevantes sobre la Maestría y el Campo de la IA\n\n## Últimas Noticias\n\n"

for noticia in noticias:
    nuevo_contenido += f"### {noticia['fecha']} - {noticia['titulo']}\n"
    nuevo_contenido += f"**{noticia['titulo']}**\n"
    nuevo_contenido += f"{noticia['descripcion']}\n"
    nuevo_contenido += f"[Leer más]({noticia['link']})\n\n"

nuevo_contenido += "## Archivo de Noticias\n"
for noticia in noticias:
    nuevo_contenido += f"- {noticia['fecha']} - [{noticia['titulo']}]({noticia['link']})\n"

# Escribir el contenido actualizado en noticias.md
with open('noticias.md', 'w', encoding='utf-8') as file:
    file.write(nuevo_contenido)