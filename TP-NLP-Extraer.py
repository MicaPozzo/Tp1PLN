from bs4 import BeautifulSoup
import requests
from datetime import datetime
from selenium import webdriver
import pandas as pd
import time

# BeautifulSoup está hecho para archivos HTML estáticos, no puede manejar contenido dinámico
# Para esto, es necesario implementar otras librerías, que permitan manejar contenido JavaScript
# Para extraer datos generados por contenido generado dinámicamente, usamos la librería selenium
# En pocas palabras, el html que retorna BeautifulSoup no es el mismo que vemos al inspeccionar elemento en la página

# Iterar sobre cada link que cargamos desde colab
links = [('Economía sale a buscar al menos $505.000 millones para cerrar el fondeo del mes electoral',
  'https://www.ambito.com/economia/sale-buscar-al-menos-505000-millones-cerrar-el-fondeo-del-mes-electoral-n5856965'),
 ('Petróleo: cae el precio ante esfuerzos diplomáticos para enfriar el conflicto bélico',
  'https://www.ambito.com/economia/petroleo-cae-el-precio-esfuerzos-diplomaticos-enfriar-el-conflicto-belico-n5856978'),
 ('Los salarios subieron en agosto 7,6% y quedaron lejos de la inflación',
  'https://www.ambito.com/economia/los-salarios-subieron-agosto-76-y-quedaron-lejos-la-inflacion-n5856855'),
 ('Precios de la carne al alza: cortes caros vs. cortes baratos, ¿cuáles son?',
  'https://www.ambito.com/economia/precios-la-carne-al-alza-cortes-caros-vs-cortes-baratos-cuales-son-n5856669'),
 ('Desde noviembre aumentan un 50% los peajes: cómo quedarán las tarifas',
  'https://www.ambito.com/economia/desde-noviembre-aumentan-un-50-los-peajes-como-quedaran-las-tarifas-n5856658'),
 ('Amplían la bonificación de tasa en créditos para economía del conocimiento',
  'https://www.ambito.com/economia/amplian-la-bonificacion-tasa-creditos-del-conocimiento-n5856482'),
 ('Créditos con tasa del 50% para MiPyMEs: qué sector se beneficia con esta medida del Gobierno',
  'https://www.ambito.com/economia/creditos-tasa-del-50-mipymes-que-sector-beneficia-esta-medida-del-gobierno-n5856386'),
 ('La economía de EEUU se aceleró al 4,9% en el tercer trimestre, mayor al nivel esperado',
  'https://www.ambito.com/economia/la-eeuu-crecio-al-49-el-tercer-trimestre-mayor-al-esperado-n5856404'),
 ('Mercado Pago ahora paga más por dejar la plata: cuánto da por $100.000',
  'https://www.ambito.com/economia/mercado-pago-ahora-paga-mas-dejar-la-plata-cuanto-da-100000-n5856351'),
 ('¿Sube el precio del pan?: actualizan valor de la bolsa de harina',
  'https://www.ambito.com/economia/sube-el-precio-del-pan-actualizan-valor-la-bolsa-harina-n5856344')]

# Cargamos a un dataframe
columns = ['title','category','url','text']
data = pd.DataFrame(columns=columns)

# Iteramos sobre cada link
for title, url in links:
    # delay para no saturar la página
    time.sleep(2)
    # Inicializar una instancia WebDriver
    driver = webdriver.Chrome()
    driver.get(url)
    # Extraer el contenido dinámico de la página (primera vista)
    page_source = driver.page_source
    driver.quit()

    # Parsear el contenido con BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # El texto se encuentra debajo de clases que comienzan con article-body
    text_tag = soup.select('[class^="article-body article-body--"]')

    # El texto está cortado, debemos juntarlo
    splitted_text = []
    for tag in text_tag:
        text = tag.get_text()
        splitted_text.append(text)

    text = ' '.join(splitted_text)

    new_row = {'title':title,
               'category':'Economía',
               'text':text,
               'url':url}
    data = data._append(new_row, ignore_index=True)


# Exportamos a un archivo csv (sería más lógico un json ¿no?)
data.to_csv('economia.csv')