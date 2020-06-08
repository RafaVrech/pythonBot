import requests 

BOT_TOKEN = "1211221294:AAEXDgSi3JuGafKsNaGMDdKZVbmw49T-0hE"
BOT_CHAT_ID = "-1001415988305"

def sendMessage(msg):
    sendText = "https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage?chat_id=" + BOT_CHAT_ID + "&parse_mode=Markdown&text=" + msg
    response = requests.get(sendText)
    print(response.json())
    return response.json()