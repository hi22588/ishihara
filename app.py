import os
from datetime import datetime

from flask import Flask, abort, request

# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get("CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.environ.get("CHANNEL_SECRET"))


@app.route("/", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        return "Hello Heroku"
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK"
    
def test(keyword):
        flex_message = FlexSendMessage(
            alt_text='hello',
            contents={
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "hello, world"
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "button",
                        "action": {
                        "type": "postback",
                        "label": "action",
                        "data": "測試hello{}".format(keyword),
                        "displayText": "測試{}".format(keyword)
                        }
                    }
                    ]
                }
            }
        )    
        return flex_message

@handler.add(MessageEvent, message=TextMessage)   
import re 
   if re.search(r'測試$', event.message.text.lower()) != None:
        #我好肥 測試  
        keyword = event.message.text[:-2] #我好肥
        print(keyword)
        abc = test(keyword) #call模板 並代入切片後的字串
        line_bot_api.reply_message(event.reply_token, abc)
        return 0
    
def handle_postback(event):
    ts = event.postback.data
    print(ts)
    keyword = ts[7:]
    print(keyword)
    if ts[7:] == '{}'.format(keyword):

        text_message = TextSendMessage(text='訊息{}'.format(keyword))

        line_bot_api.reply_message(event.reply_token, text_message)    
