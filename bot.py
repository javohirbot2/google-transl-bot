from telegram.ext import Updater,MessageHandler,CommandHandler,Filters
from googletrans import Translator

updater = Updater('5265168259:AAGZgscvx4R7Ohgq5KLwAC_QPieusvV19q4',use_context = True )

def start(updater,context):
 updater.message.reply_html("👋🏻Assalomu alaykum <b>{}!</b>\n \n<b>Ushbu bot orqali matnlarni eng-uzb\n tarzida tarjima qilishingiz\n mumkin bo'ladi. Botga matn\n yuboring</b>".
                           format(user.first_name))
format(user.first_name))
 
def echo(updater,context):
  user = updater.message.from_user
 usr_msg =updater.message.text
 translator = Translator()
 translation = translator.translate(usr_msg,dest='uz') 
 updater.message.reply_text(translation.text)
 
dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(MessageHandler(Filters.text,echo))

updater.start_polling()
updater.idle()
