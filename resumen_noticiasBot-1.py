import telebot
import pandas as pd
from transformers import AutoTokenizer, BartForConditionalGeneration

df = pd.read_csv("df.csv")
TELEGRAM_TOKEN = '6794408121:AAHn-Ylpskgutxn2JBb_G8SAJWxdi3RtVw0'

modelo3 = 'ELiRF/NASES' # Abstracción
tokenizer = AutoTokenizer.from_pretrained(modelo3)
model = BartForConditionalGeneration.from_pretrained(modelo3)

def resumir(texto, min_length=50, max_length=100):
  '''Recibe un texto y genera un resumen'''
  inputs = tokenizer.encode("summarize: " + texto, return_tensors="pt", max_length=512, truncation=True)
  summary_ids = model.generate(inputs, max_length=max_length, min_length=min_length, length_penalty=2.0, num_beams=4, early_stopping=True)
  resumen = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
  return resumen

# Inicializamos el bot con el token
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Mensaje cuando el usuario envía el comando /start
@bot.message_handler(commands=['start'])
def cmd_start(message):
    "Da la bienvenida al usuario y muestra las categorías disponibles"
    bot.send_message(message.chat.id, 
                     "¡Bienvenido! Puedo mostrarte resúmenes de noticias de las categorías: Economía, Deportes, IA y Salud. \n\n" +
                     "- Para leer un resumen de noticias sobre 'Economía' escriba el comando /economia.\n\n" +
                     "- Para leer un resumen de noticias sobre 'Deportes' escriba el comando /deportes.\n\n" + 
                     "- Para leer un resumen de noticias sobre 'Inteligencia Artificial' escriba el comando /ia.\n\n" +
                     "- Para leer un resumen de noticias sobre 'Salud' escriba el comando /salud.\n")


@bot.message_handler(commands=['economia'])
def show_economia_news(message):
    '''Devuelve un resumen de las cinco primeras noticias
    de la categoría Economía'''
    df_categoria = df[df['Categoria'] == 'Economía']
    response = "\nNoticias sobre 'Economía':\n\n"
    for i, (titulo, texto, url) in enumerate(zip(df_categoria['Titulo'][:5], df_categoria['Texto'][:5], df_categoria['URL'][:5])):
        response += f"{i+1} - {titulo}\n\n"
        resumen = resumir(texto)
        response += f"Resumen: {resumen}\n\nNoticia completa: {url}\n\n"
    bot.send_message(message.chat.id, response)

@bot.message_handler(commands=['deportes'])
def show_deportes_news(message):
    '''Devuelve un resumen de las cinco primeras noticias
    de la categoría Deportes'''
    df_categoria = df[df['Categoria'] == 'Deportes']
    response = "\nNoticias sobre 'Deportes':\n\n"
    for i, (titulo, texto, url) in enumerate(zip(df_categoria['Titulo'][:5], df_categoria['Texto'][:5], df_categoria['URL'][:5])):
        response += f"{i+1} - {titulo}\n\n"
        resumen = resumir(texto)
        response += f"Resumen: {resumen}\n\nNoticia completa: {url}\n\n"
    bot.send_message(message.chat.id, response)

@bot.message_handler(commands=['ia'])
def show_ia_news(message):
    '''Devuelve un resumen de las cinco primeras noticias
    de la categoría Inteligencia Artificial'''
    df_categoria = df[df['Categoria'] == 'Inteligencia Artificial']
    response = "\nNoticias sobre 'Inteligencia Artificial':\n\n"
    for i, (titulo, texto, url) in enumerate(zip(df_categoria['Titulo'][:5], df_categoria['Texto'][:5], df_categoria['URL'][:5])):
        response += f"{i+1} - {titulo}\n\n"
        resumen = resumir(texto)
        response += f"Resumen: {resumen}\n\nNoticia completa: {url}\n\n"
    bot.send_message(message.chat.id, response)

@bot.message_handler(commands=['salud'])
def show_salud_news(message):
    '''Devuelve un resumen de las cinco primeras noticias
    de la categoría Salud'''
    df_categoria = df[df['Categoria'] == 'Salud']
    response = "\nNoticias sobre 'Salud':\n\n"
    for i, (titulo, texto, url) in enumerate(zip(df_categoria['Titulo'][:5], df_categoria['Texto'][:5], df_categoria['URL'][:5])):
        response += f"{i+1} - {titulo}\n\n"
        resumen = resumir(texto)
        response += f"Resumen: {resumen}\n\nNoticia completa: {url}\n\n"
    bot.send_message(message.chat.id, response)

@bot.message_handler(content_types=["text"])
def bot_mensajes_texto(message):
    "Gestiona mensajes recibidos no válidos"
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, "Comando no disponible.")
    else:
        bot.send_message(message.chat.id, "Ingrese un comando válido. Para ver los comandos válidos ingrese /start")

if __name__ == '__main__':
    print("Iniciando bot...")
    bot.infinity_polling()