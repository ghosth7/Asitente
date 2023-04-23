import webbrowser
import pywhatkit
import subprocess
import sys
import os

try:
    import googlesearch
except ImportError:
    print("googlesearch no está instalado. Instalando...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "googlesearch-python"])
try:
    import pywhatkit
except ImportError:
    print("pywhatkit no está instalado. Instalando...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pywhatkit"])

def abrir_pagina_web(url):
    webbrowser.get().open(url)

def buscar_en_google(pregunta):
    # Realizamos la búsqueda en Google y obtenemos los resultados
    resultados = googlesearch.search(pregunta, num_results=5, lang='es')

    # Devolvemos el primer resultado de la búsqueda
    for resultado in resultados:
        return resultado

    # Si no encontramos ningún resultado en Google, devolvemos None
    return None

#se puden abrir directamnete facebook, google,twitter y youtube tomando en base el primer ejemplo(abrir google)
print("Bienvenido al asistente virtual")
print("Ejemplo de preguntas que puedes hacer:")
print("- Abrir Google")
print("- Buscar en Google ¿Cómo hacer un pastel?")
print("- Buscar en YouTube 'Despacito'")
print("- Reproducir en YouTube 'Phonk'")
print("- Salir")

while True:
    pregunta = input("¿Qué quieres hacer? ").lower() # Convertimos la pregunta a minúsculas para simplificar la comparación

    if "abrir" in pregunta:
        # Si la pregunta incluye la palabra "abrir", abrimos la página web correspondiente
        if "google" in pregunta:
            abrir_pagina_web("https://www.google.com")
        elif "youtube" in pregunta:
            abrir_pagina_web("https://www.youtube.com")
        elif "facebook" in pregunta:
            abrir_pagina_web("https://www.facebook.com")
        elif "twitter" in pregunta:
            abrir_pagina_web("https://www.twitter.com")
        else:
            print("Lo siento, no sé cómo abrir esa página web.")
    elif "buscar" in pregunta:
        # Si la pregunta incluye la palabra "buscar", buscamos en Google o en YouTube
        if "en google" in pregunta:
            busqueda = pregunta.replace("buscar", "").replace("en google", "").strip()
            url = buscar_en_google(busqueda)
            if url is not None:
                print(f"Encontré esto en Google: {url}")
                opcion = input("¿Quieres abrir la página web? (s/n) ").lower() # Convertimos la respuesta a minúsculas
                if opcion == "s":
                    abrir_pagina_web(url)
            else:
                print("Lo siento, no encontré nada en Google.")
        elif "en youtube" in pregunta:
            busqueda = pregunta.replace("buscar", "").replace("en youtube", "").strip()
            urls = pywhatkit.search(busqueda)
            if len(urls) > 0:
                print(f"Encontré esto en YouTube: {urls[0]}")
                opcion = input("¿Quieres reproducir la canción? (s/n) ").lower() # Convertimos la respuesta a minúsculas
                if opcion == "s":
                    pywhatkit.playonyt(urls[0])
            else:
                print("Lo siento, no encontré nada en YouTube.")
    elif "reproducir" in pregunta:
        if "en youtube" in pregunta:
            cancion = pregunta.replace("reproducir", "").replace("en youtube", "").strip()
            pywhatkit.playonyt(cancion)
        else:
            print("Lo siento, solo puedo reproducir canciones en YouTube.")

