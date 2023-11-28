from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, filters, MessageHandler


key_token = "6433242103:AAFjvwVUafZujzDcpT0qCYLDNMsdlQ_2gnU" #Masukkan KEY-TOKEN BOT 
user_bot = "Nelgantenkbot" #Masukkan @user bot


async def  start_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Gunakan /help untuk menampilkan apa yang dapat saya berikan..")
    
async def  help_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Kirim pesan, bot akan membalas pesan..")


async def  text_massage(update: Update, context:ContextTypes.DEFAULT_TYPE):
    text_diterima : str = update.message.text
    print(f"Pesan diterima : {text_diterima}")
    text_lwr_diterima = text_diterima.lower()
    if 'halo' in text_lwr_diterima:
        await update.message.reply_text("Hallo juga")
    elif 'selamat malam' in text_lwr_diterima:
        await update.message.reply_text("Selamat malam..., jangan lupa istirahat 😊")
    elif 'selamat sekolah' in text_lwr_diterima:
        await update.message.reply_text("Selamat sekolah..., jangan terlambat!")
    elif 'siapa kamu ?' in text_lwr_diterima:
        await update.message.reply_text(f"bot adalah : {user_bot}")
    elif 'siapa massimo ?' in text_lwr_diterima:
        await update.message.reply_text("massimo adalah PREMAN penabur")
    elif 'dimana sekolah terbaik 2023 ?' in text_lwr_diterima:
        await update.message.reply_text("kusuma bangsa")
    elif 'gigitan pertama buat kalian' in text_lwr_diterima:
        await update.message.reply_text("MUKBANG coyyy")
    elif 'SD TERBAIK SELAMANYA?' in text_lwr_diterima:
        await update.message.reply_text("PENABUR PALEMBANG")
    else:
        await update.message.reply_text("bot tidak mengerti")

async def photo_message(update: Update, context:ContextTypes.DEFAULT_TYPE):
    return await update.message.reply_text("Gambar kamu bagus")
        
async def  error(update: Update, context:ContextTypes.DEFAULT_TYPE):
    print(f"error... : {context.error}")


if __name__ == '__main__':
    print("Mulai")
    app = Application.builder().token(key_token).build()
    #COMMAND :
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    #MESSAGE:
    app.add_handler(MessageHandler(filters.TEXT, text_massage))
    app.add_handler(MessageHandler(filters.PHOTO, photo_message))
    #error :
    app.add_error_handler(error)
    #polling :
    app.run_polling(poll_interval=1)
