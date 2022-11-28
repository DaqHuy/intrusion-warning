import telegram

def send_telegram(photo_path="D:\MiAI_Intrusion_Warning\alert.png"):
    try:
        my_token = "5826652814:AAFnpHm_tsy8wvYh6PbBbTqy5vgO3chFk8s"
        bot = telegram.Bot(token=my_token)
        bot.sendPhoto(chat_id="1578574748", photo=open(photo_path, "rb"), caption="Có xâm nhập, nguy hiêm!")
    except Exception as ex:
        print("Can not send message telegram ", ex)

    print("Send sucess")