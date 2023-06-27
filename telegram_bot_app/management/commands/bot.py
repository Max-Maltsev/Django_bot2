import telebot
from telebot import types
from telegram_bot_app.models import Prod, Users, Call, History
config = {
    "name": "maxim_django_shop_bot",
    "token": "6171871423:AAGaeLBgQj-hL7Xyqm63uQ9hCoiav4pMuNo"
}
keybord = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_register = types.KeyboardButton('register📄')
button_entry = types.KeyboardButton('authorisation🔑')
keybord_admin = types.ReplyKeyboardMarkup(resize_keyboard=True)
shoplist = types.KeyboardButton('shoplist🛍')
add_many = types.KeyboardButton('add_many💶')
balance = types.KeyboardButton('balance💳')
cart = types.KeyboardButton('shop_cart🛒')
delete_cart = types.KeyboardButton('delete_cart❌')
delete_his = types.KeyboardButton('delete_history❌')
history = types.KeyboardButton('history📓')
bonus_balance = types.KeyboardButton('bonus_balance')
users_data = types.KeyboardButton('contact')
keybord_admin.add(shoplist, add_many, balance, cart, delete_cart, history, bonus_balance, users_data, delete_his)
keybord.add(button_register, button_entry)
keybord1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
shoplist = types.KeyboardButton('shoplist🛍')
add_many = types.KeyboardButton('add_many💶')
balance = types.KeyboardButton('balance💳')
cart = types.KeyboardButton('shop_cart🛒')
delete_cart = types.KeyboardButton('delete_cart❌')
delete_his = types.KeyboardButton('delete_history❌')
history = types.KeyboardButton('history📓')
bonus_balance = types.KeyboardButton('bonus_balance')
users_data = types.KeyboardButton('contact')
prod = types.KeyboardButton('add_prod')
keybord1.add(shoplist, add_many, balance, cart, delete_cart, history, bonus_balance, users_data, delete_his, prod)
keybord34 = types.ReplyKeyboardMarkup(resize_keyboard=True)
cart = types.KeyboardButton('cart')
bonus = types.KeyboardButton('bonus')
keybord34.add(bonus, cart)
keybord50 = types.ReplyKeyboardMarkup(resize_keyboard=True)
cart = types.KeyboardButton('old')
bonus = types.KeyboardButton('new')
keybord50.add(bonus, cart)
max = telebot.TeleBot(config["token"])
@max.message_handler(commands=["start"])
def start(massage):
    max.send_message(massage.chat.id, "welcome to my bot!", reply_markup=keybord)

@max.message_handler(content_types=['text'])
def get_text(message):
    # if message.text.lower() == "add_prod":
    #     if message.chat.id == 5495467597:
    #         img = max.send_message(message.chat.id, f'Enter img prod:')
    #         max.register_next_step_handler(img, prod)
    #     else:
    #         max.send_message(message.chat.id, f'YOU NAVEN`T RIGHTS!!!!!!!:')
    if message.text.lower() == "delete_history❌":
        History.objects.filter(chat_id=message.chat.id).delete()
        max.send_message(message.chat.id, f'Your all history is delete: ')
    if message.text.lower() == "new":
        data = max.send_message(message.chat.id, f'Enter your address: ')
        max.register_next_step_handler(data, new123)
    if message.text.lower() == "old":
        user_address = Users.objects.get(chat_id=message.chat.id)
        max.send_message(message.chat.id, f'Your number_phone: {user_address.nambers},\n mail: {user_address.mail} and call delivered to this address: {user_address.adress}', reply_markup=keybord1)
    if message.text.lower() == "cart":

        money = Users.objects.get(chat_id=message.chat.id).many
        totle_money = Call.objects.filter(chat_id=message.chat.id)
        for i in totle_money:
            History.objects.create(
                chat_id=message.chat.id,
                prise=i.prise,
                name=i.name
                )
        price = 0
        for i in totle_money:
            price += i.prise
        if money == price or money > price:
            max.send_message(message.chat.id, f'Your order products a buying, what address a use: ', reply_markup=keybord50)
            balance = Users.objects.get(chat_id=message.chat.id)
            new = balance.bonus + price / 100 * 3
            balance.bonus = new
            balance.save()
            Call.objects.filter(chat_id=message.chat.id).delete()
            monys = Users.objects.get(chat_id=message.chat.id)
            sum_mony = int(monys.many) - int(price)
            monys.many = sum_mony
            monys.save()
        else:
            max.send_message(message.chat.id, f'Your order bigger than your balance! ', reply_markup=keybord1)
    if message.text.lower() == "bonus":
        money = Users.objects.get(chat_id=message.chat.id).bonus
        totle_money = Call.objects.filter(chat_id=message.chat.id)
        for i in totle_money:
            History.objects.create(
                chat_id=message.chat.id,
                prise=i.prise,
                name=i.name
            )
        price = 0
        for i in totle_money:
            price += i.prise
        if money == price or money > price:
            max.send_message(message.chat.id, f'Your order products a buying! ', reply_markup=keybord1)
            data = max.send_message(message.chat.id, f'Enter your address: ')
            max.register_next_step_handler(data, new123)
            Call.objects.filter(chat_id=message.chat.id).delete()
            monys = Users.objects.get(chat_id=message.chat.id)
            sum_mony = monys.bonus - price
            monys.bonus = sum_mony
            monys.save()
        else:
            max.send_message(message.chat.id, f'Your order bigger than your bonus balance! ', reply_markup=keybord1)
    if message.text.lower() == "authorisation🔑":
        login = max.send_message(message.chat.id, "enter your password: ")
        max.register_next_step_handler(login, entry)
    if message.text.lower() == "contact":
        keybord_inline21 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text=f'password', callback_data=f'password')
        button1 = types.InlineKeyboardButton(text=f'mail', callback_data=f'mail')
        button2 = types.InlineKeyboardButton(text=f'number', callback_data=f'num')
        keybord_inline21.add(button, button1, button2)
        max.send_message(message.chat.id, "Settings", reply_markup=keybord_inline21)
    if message.text.lower() == "register📄":
        login = max.send_message(message.chat.id, "enter your password/mail/namber_phone/address:")
        max.register_next_step_handler(login, register)
    if message.text.lower() == "привіт" or message.text.lower() == "hello" or message.text.lower() == "hi" or message.text.lower() == "🖖":
        max.send_message(message.chat.id, "привіт")
    if message.text.lower() == "history📓":
        user_history = History.objects.filter(chat_id=message.chat.id)
        mes = ""
        price = 0
        for i in user_history:
            price += i.prise
            if not f'{i.name} ' in mes:
                count_prod = History.objects.filter(chat_id=message.chat.id).filter(name=i.name).count()
                mes += f'Name: {i.name} Prise: {i.prise} Count: {count_prod}\n'
        max.send_message(message.chat.id, f'{mes}\nTotal price: {price}$')
    if message.text.lower() == "shoplist🛍":
        products = Prod.objects.all()
        keybord_inline = types.InlineKeyboardMarkup()
        for i in products:
            button = types.InlineKeyboardButton(text=f'{i.good}\n {i.prise}$', callback_data=f'{i.good}')
            keybord_inline.add(button)
        max.send_message(message.chat.id, 'Choise', reply_markup=keybord_inline)
    if message.text.lower() == "bonus_balance":
        bonus = Users.objects.get(chat_id=message.chat.id)
        max.send_message(message.chat.id, f'Your bonus balance: {bonus.bonus}')
    if message.text.lower() == "add_many💶":
        many = max.send_message(message.chat.id, "enter your sum add to many: ")
        max.register_next_step_handler(many, add_to_many)
    if message.text.lower() == "balance💳":
        users = Users.objects.get(chat_id=message.chat.id)
        max.send_message(message.chat.id, f'Your balance {users.many} ')
    if message.text.lower() == "shop_cart🛒":
        call = Call.objects.filter(chat_id=message.chat.id)
        mes = ""
        price = 0
        for i in call:
            price += i.prise
            # if i.name in mes:
            #     mes = mes.replace(mes[mes.index(" ")+1: mes.index(" ")+2], f'{int(mes[mes.index(" ")+1: mes.index(" ")+2])+1}')
            # else:
            if not f'{i.name} ' in mes:
                count_prod = Call.objects.filter(chat_id=message.chat.id).filter(name=i.name).count()
                mes = mes + f'{i.name} {count_prod} {i.prise*count_prod}\n'
        keybord2_inline = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text=f'Buy all', callback_data=f'buy_all')
        keybord2_inline.add(button)
        max.send_message(message.chat.id, f'{mes}\nTotal price: {price}$', reply_markup=keybord2_inline)
    if message.text.lower() == "delete_cart❌":
        Call.objects.filter(chat_id=message.chat.id).delete()
        max.send_message(message.chat.id, "Your prod a delete!!!")
@max.callback_query_handler(func=lambda call: True)
def call_me(call):
    if call.data == "buy_all":
        max.send_message(call.message.chat.id, "You use a bonus or balance?", reply_markup=keybord34)
    elif "password" in call.data:
        login = max.send_message(call.message.chat.id, "Enter your new password:")
        max.register_next_step_handler(login, password)
    elif "mail" in call.data:
        login = max.send_message(call.message.chat.id, "Enter your new mail:")
        max.register_next_step_handler(login, mail)
    elif "num" in call.data:
        login = max.send_message(call.message.chat.id, "Enter your new num:")
        max.register_next_step_handler(login, num)
    elif "yes" in call.data:
        prouct = Prod.objects.get(good=call.data.split()[1])
        Call.objects.create(
            chat_id=call.message.chat.id,
            prise=int(prouct.prise),
            name=prouct.good
        )
        max.send_message(call.message.chat.id, "Your product add to cart")
    else:
            prod = Prod.objects.get(good=call.data)
            mess = f'Name: {prod.good}\nPrise: {prod.prise}\nDiscripsion: {prod.disc}'
            keybord4_inline = types.InlineKeyboardMarkup()
            button = types.InlineKeyboardButton(text=f'add to cart', callback_data=f'yes {prod.good}')
            keybord4_inline.add(button)
            max.send_photo(call.message.chat.id, photo=prod.image, caption=mess, reply_markup=keybord4_inline)
def password(message):
    users = Users.objects.get(chat_id=message.chat.id)
    password1 = message.text
    users.password = password1
    users.save()
    max.send_message(message.chat.id, "Ok")
def mail(message):
    users = Users.objects.get(chat_id=message.chat.id)
    mail1 = message.text
    users.mail = mail1
    users.save()
    max.send_message(message.chat.id, "Ok")
def num(message):
    users = Users.objects.get(chat_id=message.chat.id)
    num1 = message.text
    users.nambers = num1
    users.save()
    max.send_message(message.chat.id, "Ok")
def add_to_many(message):
    if message.text.isdigit() == True:
        users = Users.objects.get(chat_id=message.chat.id)
        users.many = int(message.text)
        users.save()
        max.send_message(message.chat.id, "Your money is credited to the account")
    else:
        max.send_message(message.chat.id, "Your text is not int")
def entry(message):
    users = Users.objects.get(chat_id=message.chat.id)
    if users:
        if users.password == message.text:
            max.send_message(message.chat.id, f'hello {message.from_user.first_name}!', reply_markup=keybord1)
    else:
        max.send_message(message.chat.id, f'password error!')
def register(message):
    user = message.text.split("/")
    Users.objects.create(chat_id=message.chat.id, password=user[0], mail=user[1], nambers=user[2], adress=user[3], many=0)
    max.send_message(message.chat.id, f'your acount create!', reply_markup=keybord)
def new123(message):
    users = Users.objects.get(chat_id=message.chat.id)
    data = message.text
    users.adress = data
    users.save()
    max.send_message(message.chat.id, f'Ok, your pizza create!', reply_markup=keybord1)
# def prod(message):
#     img = message.text
#     data = max.send_message(message.chat.id, f'Enter prod: name/disc/prise:')
#     Prod.objects.create(
#         good=str(data).split("/")[0],
#         prise=str(data).split[2],
#         disc=str(data).split[1],
#         image=img
#     )
max.polling(none_stop=True,interval=0)