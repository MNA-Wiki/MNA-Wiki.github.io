import datetime

# Lista de noticias. En un caso real, podrías obtener esto desde una API o un archivo de datos
noticias = [
    {
        "fecha": "2024-06-21",
        "titulo": "IA y Ética: Nuevas Regulaciones en Europa",
        "descripcion": "Europa Establece Nuevas Regulaciones para el Uso Ético de la IA. La Unión Europea ha aprobado un nuevo marco regulatorio que establece directrices estrictas para el uso ético de la inteligencia artificial. Estas regulaciones buscan garantizar la transparencia, equidad y responsabilidad en el desarrollo y despliegue de tecnologías de IA, protegiendo así los derechos de los ciudadanos y fomentando la innovación responsable."
    },
    {
        "fecha": "2024-06-20",
        "titulo": "IA en la Agricultura: Detección de Plagas",
        "descripcion": "Un equipo de la Universidad de Stanford ha presentado un sistema de IA que utiliza imágenes satelitales y datos meteorológicos para detectar la presencia de plagas en cultivos agrícolas. Esta tecnología permite a los agricultores actuar de manera proactiva, mejorando la salud de los cultivos y aumentando la producción."
    },
    {
        "fecha": "2024-06-19",
        "titulo": "Avances en la IA Médica para Diagnóstico Temprano",
        "descripcion": "Investigadores del MIT han desarrollado un algoritmo de IA capaz de detectar enfermedades cardíacas en etapas tempranas con una precisión del 95%. Este avance promete mejorar significativamente los diagnósticos y tratamientos preventivos, reduciendo la mortalidad asociada a enfermedades cardíacas."
    }
]

# Leer el contenido actual de noticias.md
with open('noticias.md', 'r', encoding='utf-8') as file:
    contenido_actual = file.read()

# Generar el contenido actualizado
nuevo_contenido = "# Noticias Relevantes sobre la Maestría y el Campo de la IA\n\n## Últimas Noticias\n\n"

for noticia in noticias:
    nuevo_contenido += f"### {noticia['fecha']} - {noticia['titulo']}\n**{noticia['titulo']}**\n{noticia['descripcion']}\n\n"

nuevo_contenido += "## Archivo de Noticias\n"

for noticia in noticias:
    nuevo_contenido += f"- {noticia['fecha']} - [{noticia['titulo']}](#)\n"

# Escribir el contenido actualizado en noticias.md
with open('noticias.md', 'w', encoding='utf-8') as file:
    file.write(nuevo_contenido)
