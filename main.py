import telegram
from flask import Flask, request
from jinja2 import Environment, FileSystemLoader

# set current directory
ENV = Environment(loader=FileSystemLoader('.'))

# get template
baseline = ENV.get_template("./template_message.j2")

# flask
app = Flask(__name__) 

# telegram bot
bot = telegram.Bot('TOKEN')

def telegram_kubeweekly(data):
    config = baseline.render(data=data)
    bot.send_message(chat_id=-"CHATID", text=config, parse_mode=telegram.ParseMode.MARKDOWN)

@app.route('/content/kubeweekly', methods=['POST'])
def kubeweekly():
    data = request.get_json()
    telegram_kubeweekly(data)
    return 'Success'

if __name__ == '__main__':
    app.run()