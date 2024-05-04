from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

menu = [
    [
        KeyboardButton(text="🔻Купить"),
    ],
    [
        KeyboardButton( text="💰Пополнить баланс"),
        KeyboardButton(text="☎️Поддержка"),
        KeyboardButton(text="📜Правила"),
    ],
    [
        KeyboardButton(text="👤О нас"),
    ]
]

keyboard1 = ReplyKeyboardMarkup(keyboard=menu, resize_keyboard=True)


def keyboard2():
    markup = InlineKeyboardMarkup()
    row1 = [InlineKeyboardButton( "🏰 Москва", callback_data='msk' ),
            InlineKeyboardButton( "🏢 Санкт-Петербург", callback_data='spb' )]
    markup.row( *row1 )

    row2 = [InlineKeyboardButton( "⛪️ Екатеринбург", callback_data='ekb' ),
            InlineKeyboardButton( "🏛 Удомля", callback_data='udom' ),
            InlineKeyboardButton("🏛🏥 Сочи", callback_data='sochi' )]
    markup.row( *row2 )
    return markup

def keyboard3():
    markup1 = InlineKeyboardMarkup()
    row1 = [InlineKeyboardButton( "Шишки HQ", callback_data='shishki' ),
            InlineKeyboardButton( "Alpha PvP", callback_data='sol' )]
    markup1.row( *row1 )

    row2 = [InlineKeyboardButton( "Мефедрон", callback_data='mef' ),
            InlineKeyboardButton( "Гашиш Ice-O-Lator", callback_data='gashish' ),
            InlineKeyboardButton("Шишки (100% индика)", callback_data='shishki' )]
    markup1.row( *row2 )
    return markup1

def keyboard4():
    markup3 = InlineKeyboardMarkup()
    row1 = [InlineKeyboardButton( "Мефедрон Мука", callback_data='mef' ),
            InlineKeyboardButton( "Шишки 20% ТГК", callback_data='shishki' )]
    markup3.row( *row1 )

    row2 =  [InlineKeyboardButton( "Мефедрон Кристалл", callback_data='mef' ),
            InlineKeyboardButton("Экстази", callback_data='ext' )]
    markup3.row( *row2 )
    return markup3

def keyboard5():
    markup4 = InlineKeyboardMarkup()
    row1 = [InlineKeyboardButton( "Alpha PVP", callback_data='sol' )]
    markup4.row( *row1 )

    row2 = [InlineKeyboardButton( "План", callback_data='gashish' ),
            InlineKeyboardButton("Экстази HQ", callback_data='ext' )]
    markup4.row( *row2 )
    return markup4

def keyboard6():
    markup5 = InlineKeyboardMarkup()
    row1 = [InlineKeyboardButton( "Шишко-План", callback_data='gashish' ),
            InlineKeyboardButton( "Мефедрон Кристалл", callback_data='mef' )]
    markup5.row( *row1 )

    row2 = [InlineKeyboardButton( "Кокаин", callback_data='cox' ),
            InlineKeyboardButton( "Мефедрон HQ Мука", callback_data='mef' ),
            InlineKeyboardButton("Гашиш HQ | groove", callback_data='gashish' )]
    markup5.row( *row2 )
    return markup5

def keyboard7():
    markup6 = InlineKeyboardMarkup()
    row1 = [InlineKeyboardButton( "Кокаин HQ", callback_data='cox' ),
            InlineKeyboardButton( "Мефедрон Кристалл", callback_data='mef' )]
    markup6.row( *row1 )

    row2 = [InlineKeyboardButton( "Кокаин", callback_data='cox' ),
            InlineKeyboardButton( "Шишки", callback_data='shishki' ),
            InlineKeyboardButton("Гашиш HQ | groove", callback_data='gashish' )]
    markup6.row( *row2 )
    return markup6

def buy():
    markup2 = InlineKeyboardMarkup()
    row1 = [InlineKeyboardButton( "1 г", callback_data='buy1'),
            InlineKeyboardButton( "2 г", callback_data='buy1')]
    markup2.row( *row1 )

    row2 = [InlineKeyboardButton( "3 г", callback_data='buy1'),
            InlineKeyboardButton( "4 г", callback_data='buy1'),
            InlineKeyboardButton("5 г", callback_data='buy1')]
    markup2.row( *row2 )
    return markup2

def buy1():
    markup3 = InlineKeyboardMarkup()
    markup3.row(InlineKeyboardButton("🧨КУПИТЬ🧨", callback_data='error'))
    return markup3






'''
def mskkb():
    markup = InlineKeyboardMarkup()
    row1 = [InlineKeyboardButton( "🏰 Арбат", callback_data='arbat' ),
            InlineKeyboardButton( "🏢 Мещанский", callback_data='mesh'),
            InlineKeyboardButton( "🏢 Хамовники", callback_data='ham')]
    return markup
'''


