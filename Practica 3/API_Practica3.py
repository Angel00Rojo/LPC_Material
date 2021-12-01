import requests
import os
import io
from bs4 import BeautifulSoup as b
from PIL import Image
#import win32api
import xlsxwriter


directorio = "imagenes"
try:
    os.mkdir(directorio)
except OSError:
    print("La creación del directorio %s ya ha sido creada con anterioridad" % directorio)
else:
    print("Se ha creado el directorio: %s " % directorio)

fotos= r"C:\Users\Reyes\Desktop\pia"


datos= xlsxwriter.Workbook("Datos obtenidos.xlsx")
negrita = datos.add_format({'bold': True})
libro1 = datos.add_worksheet("Contacto")
libro1.write("A1" , "Telefono" , negrita)
libro1.write("A3" , "Correo Electronico" , negrita)
libro1.write("A5" , "Direccion" , negrita)
libro2 = datos.add_worksheet("Noticias")
libro2.write("A1" , "Titulares" , negrita)
libro2.write("B1" , "Enlaces" , negrita)
libro3 = datos.add_worksheet("Temperatura")
libro3.write("A1" , "Fecha" , negrita)
libro3.write("B1" , "Ciudad" , negrita)
libro3.write("C1" , "Temperatura" , negrita)


w = open('test.txt', 'r')
url=w.readline()
#url ="https://vamoscruzazul.bolavip.com/"
print(url)
headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
"Accept-Encoding":"gzip, deflate",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"DNT":"1"
}

html = requests.get(url,headers=headers)
content = html.content
soup = b(content,"lxml")
#print(soup)

#Informacion de contacto
telefono = soup.find("div",{"class":"bottomBar__content__phone"})
print(telefono)
#print(telefono)
libro1.write("A2" , telefono.text)
mail = soup.find("div",{"class":"bottomBar__content__mail"})
#print(mail.text)
libro1.write("A4" , mail.text)
direccion = soup.find("div",{"class":"bottomBar__content__headquarters"})
#print(direccion.text)
libro1.write("A6",direccion.text)
			
i=1
for post in soup.findAll("figure",{"class":"news-media"}):
	title = post.find('img')['alt']
	#print(title)
	url_img =post.find('img')["src"]
	f = open ('linksImagenes.txt','w')
	f.write("https://vamoscruzazul.bolavip.com"+url_img)
	f.close()
	w2 = open('linksImagenes.txt', 'rb')
	url_img2=w2.readline()
	print(url_img2)
	r = requests.get(url_img2)
	file = io.BytesIO(r.content)
	img = Image.open(file)
	img.save(fotos+"\\"+str(title)+".jpg")
	print(i)
	i+=1
j=1
for post in soup.findAll("h2",{"class":"news-title"}):
	url_news = post.find('a')['href']
	news_title = post.find('a')['title']
	print(url_news)
	f = open ('linksNoticias.txt','w')
	f.write("https://vamoscruzazul.bolavip.com"+url_news)
	f.close()
	w3 = open('linksNoticias.txt', 'r')
	url_news2=w3.readline()
	libro2.write(j,0,news_title)
	libro2.write(j,1,url_news2)
	j+=1

for k in range(3):
	api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
	city = input(f'En que ciudad sera el {k} partido?')
	dia = input(f'En quedia sera el {k} partido?')
	mes =input(f'En que mes sera el {k} partido?')
	fecha = mes+ "-" +dia
	url = api_address + city
	json_data = requests.get(url).json()
	format_add = json_data['main']['temp']
	libro3.write(k+1,0,fecha)
	libro3.write(k+1,1,city)
	libro3.write(k+1,2,(format_add-273.15))
	k+=1

datos.close()
#win32api.MessageBox(False,"Procesos finalizado","terminado", 0x0001000)
