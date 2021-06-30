import telegram
from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters, InlineQueryHandler
from wiki import search_wiki
from record_event import record_event
from record_note import record_note
from allnotes import print_notes
from allevents import print_events
from notify import inter
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

bot = telegram.Bot(token="1827937849:AAFbBdFVdOviyxCZwChEacTjZj9MMiESkFA")


def start(update, context):
    id = update.message.from_user["id"]
    update.message.reply_text(
        "Чтобы узнать больше введите /help")


def help(update, context):
    update.message.reply_text(
        "Все возможные команды:\n"
        "/help - список команд\n"
        "/wiki {слово для поиска}, поиск в Wikipedia\n"
        "/event {заголовок  описание  ДД.ММ.ГГГГ  чч:мм:сс}(создать событие с напоминанием)\n"
        "/notewrite  {заголовок  описание}(создать заметку)\n"
        "/allnotes - вывод всех записок\n"
        "/allevents - вывод всех событий\n"
        "(двойной пробел для записи следующего пункта)")


def event(update, context):
    record_event(update.message.text)
    # word = ' '.join(context.args)
    update.message.reply_text("Событие создано")


#     context.job_queue.run_repeating(callback_minute, interval=60 * 60 * 24, first=inter(word),
#                                     context=update.message.chat_id)
#

def note(update, context):
    record_note(update.message.text)
    update.message.reply_text("Заметка создана")


#
# def callback_minute(context):
#     chat_id = context.job.context
#     context.bot.send_message(chat_id=chat_id,
#                              text="глэк")


def allnotes(update, context):
    update.message.reply_text(print_notes())


def allevents(update, context):
    update.message.reply_text(print_events())


def wiki(update, context):
    print(context.args)
    word = ' '.join(context.args)
    if word:
        update.message.reply_text("Идет поиск...")
        response, url = search_wiki(word)
        update.message.reply_text(response + url)
    else:
        update.message.reply_text("Необходимо ввести данные для поиска")


def main():
    updater = Updater("1827937849:AAFbBdFVdOviyxCZwChEacTjZj9MMiESkFA", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("event", event))
    dp.add_handler(CommandHandler("note", note))
    dp.add_handler(CommandHandler("allprint", allnotes))
    dp.add_handler(CommandHandler("allevents", allevents))
    dp.add_handler(CommandHandler("wiki", wiki))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
