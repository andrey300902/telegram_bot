from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from search import search
from distance import lonlat_distance
import afisha

def cinema(bot, update, user_data):
    loc = update.message.location
    coord = [str(loc['longitude']), str(loc['latitude'])]
    cinemas = search(','.join(coord))
    user_data['cinemas'] = cinemas
    for i in cinemas:
        if 'cinemastar' in i[2] or 'karo' in i[2] or 'mirage' in i[2] or 'kinomax' in i[2] or 'cinemapark' in i[2]:
            dist = round(lonlat_distance(coord, i[1]))
            update.message.reply_text(i[0]+':  '+str(dist)+' метров')
        else:
            cinemas = []
    if cinemas:
        update.message.reply_text("Пришлите номер понравившегося кинотеатра\n"
                                  "Или введите /search_film + название фильма, который хотите найти")
        return 2
    else:
        return ConversationHandler.END

def swith_cinema(bot, update, user_data):
    teatr = user_data['cinemas'][int(update.message.text)-1]
    films = []
    if 'cinemastar' in teatr[2]:
        films = afisha.cinemastar(teatr[2])
    if 'karo' in teatr[2]:
        films = afisha.karofilm(teatr[2])
    if 'mirage' in teatr[2]:
        films = afisha.mirage(teatr[2])
    if 'kinomax' in teatr[2]:
        films = afisha.kinomax(teatr[2])
    if 'cinemapark' in teatr[2]:
        films = afisha.cinemapark(teatr[2])
    for i in films:
        update.message.reply_text(i)
    return ConversationHandler.END

def search_film(bot, update, user_data, args):
    cinemas = user_data['cinemas']
    film = ' '.join(args)
    kino = []
    print(film)
    for cinem in cinemas:
        print(cinem)
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
    print(kino)
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
                 2: [MessageHandler(Filters.text, swith_cinema, pass_user_data=True), CommandHandler('search_film', search_film, pass_user_data=True, pass_args=True)]
        },
        fallbacks=[CommandHandler('stop', stop)]

    )
    dp.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()