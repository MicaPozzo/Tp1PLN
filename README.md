# Trabajo Práctico NLP
Trabajo Práctico 1 de la materia NLP de la TUIA
## Integrantes
- Abril Nazarena Rodriguez.
- Enzo Ferrari.
- Micaela Pozzo.
## Descripción
Este trabajo tiene como objetivo incorporar los conocimientos y técnicas aprendidas en el curso. Incluye temas tales como Web Scraping y limpieza de texto, clasificación de texto, técnicas de vectorización incluyendo redes neuronales y modelos de similitud.
###  Archivos
- INFORME - NLP.pdf : Documentación del trabajo.
- TP_NLP.ipynb : Desarrollo del trabajo.
- TP-NLP-Extraer.py : Web Scraping por selenium, muestra cómo se recolectaron los datos de Economía. Ejecutar en entorno local (selenium no funciona en colab).
- economia.csv : csv de las noticias de Economía conseguidos del archivo anterior.
- resumen_noticiasBot-1.py : archivo para iniciar el bot de Telegram.
- df.csv : csv donde se encuentran todas las noticias. Se necesita para el bot de Telegram.

### Instrucciones de uso
#### Ejercicios 1-4
El trabajo se encuentra plasmado en una notebook de Jupyter. Puede ser accedida tanto por Jupyter como Colab. Sin embargo, algunas partes del trabajo debieron hacerse en un entorno local por lo que antes de ejecutar el colab se debe cargar en el entorno el archivo economia.csv, que cuenta con las noticias de la categoría Economía. Esto se debe a que la página de donde conseguimos los datos tiene vistas dinámicas generadas por scripts de Javascript. Estos datos fueron 
#### Ejercicio 5
Para iniciar el bot de Telegram que resume noticias, se debe descargar el archivo 'resumen_noticiasBot.py' y 'df.csv' y colocarlos en el mismo directorio. Luego, se deberá instalar las bibliotecas Transformers, pyTelegramBotApi, torch, torchvision y torchaudio en el entorno donde se ejecutará el código y, a continuación, ejecutar el archivo. Si se desea ejecutarlo en la consola, simplemente se debe utilizar el comando 'python3 resumen_noticicasBot.py'. Cuando se vea la leyenda 'Iniciando bot...' en la pantalla, el bot estará listo para su uso.

