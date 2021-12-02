import requests
from bs4 import BeautifulSoup
import os

link = input("Ingrese URL: ")


def Imagenes(url, carpeta):
    try:
        os.mkdir(os.path.join(os.getcwd(), carpeta))
        print("Carpeta creada")
    except:
        pass
        print("La Carpeta ya existe")
    os.chdir(os.path.join(os.getcwd(), carpeta))

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    # imagen = soup.find_all("span",{"class":"img"},limit=20)
    imagen = soup.find_all("img")[3:45]
    cont = 1
    for image in imagen:
        NameImagen = "img" + str(cont) + ".jpg"
        link = image["src"]
        cont += 1
        with open(NameImagen, "wb") as f:
            im = requests.get(link)
            f.write(im.content)
            print("Guardando Imagen: ", NameImagen)


Imagenes(url=link, carpeta="Imagenes")
