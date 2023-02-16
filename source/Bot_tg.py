import logging
from telegram import Update
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, InlineQueryHandler

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)


async def start(update, context):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!"
    )


async def echo(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


async def caps(update, context):
    text_caps = ''.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


async def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = []
    results.append(InlineQueryResultArticle(id=query.upper(), title='Caps',
                                            input_message_content=InputTextMessageContent(query.upper())))
    await context.bot.answer_inline_query(update.inline_query.id, results)


async def unknown(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command")

if __name__ == '__main__':
    TOKEN = '5992639409:AAHoNN7SrAY7t6sVanHvBuW3tYmjHtGyxGQ'

    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    caps_handler = CommandHandler('caps', caps)
    inline_caps_handler = InlineQueryHandler(inline_caps)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(caps_handler)
    application.add_handler(inline_caps_handler)
    application.add_handler(unknown_handler)

    application.run_polling()
