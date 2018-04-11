from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from search import search
from distance import lonlat_distance
import afisha


def cinema(bot, update, user_data):
    loc = update.message.location


def search_film(bot, update, user_data, args):
    cinemas = user_data['cinemas']
    film = ' '.join(args)
    kino = []
    for cinem in cinemas:
        if 'cinemastar' in cinem[2]:
            films = afisha.cinemastar(cinem[2])
            if film in films:
                kino.append(cinem[0])
        if 'karo' in cinem[2]:
            films = afisha.karofilm(cinem[2])
            if film in films:
                kino.append(cinem[0])
        if 'mirage' in cinem[2]:
            films = afisha.mirage(cinem[2])
            if film in films:
                kino.append(cinem[0])
        if 'kinomax' in cinem[2]:
            films = afisha.kinomax(cinem[2])
            if film in films:
                kino.append(cinem[0])
        if 'cinemapark' in cinem[2]:
            films = afisha.cinemapark(cinem[2])
            if film in films:
                kino.append(cinem[0])
    if kino:
        for i in kino:
            update.message.reply_text(i)
    else:
        update.message.reply_text("К сожалению, ничего не найдено.")


def start(bot, update):
    update.message.reply_text("Я бот-искатель кинотеатров\n"
                              "Отправьте свою геопозицию")
    return 1


def stop(bot, update):
    update.message.reply_text("Надеюсь Вы нашли то, что хотели")
    return ConversationHandler.END


def main():
    updater = Updater('508776994:AAFjLrAkpmpgAfFTcfwJymGGd5zm_1BcdgI')
    dp = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            1: [MessageHandler(Filters.location, cinema, pass_user_data=True)],
            2: [MessageHandler(Filters.text, swith_cinema, pass_user_data=True),
                CommandHandler('search_film', search_film, pass_user_data=True, pass_args=True)]
        },
        fallbacks=[CommandHandler('stop', stop)]

    )
    dp.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
