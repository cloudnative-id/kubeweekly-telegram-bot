import telegram
import os
from flask import Flask, request
from jinja2 import Environment, FileSystemLoader

# Set current directory.
ENV = Environment(loader=FileSystemLoader('.'))
# Jinja template of the bot.
TEMPLATE_PATH = './templates/template_message.j2'

# Load Jinja template.
baseline = ENV.get_template()

# flask
app = Flask(__name__) 

# telegram bot
telegram_token = os.getenv('TOKEN')
chat_id = os.getenv('CHATID')
bot = telegram.Bot(telegram_token)

def telegram_kubeweekly(data):
    config = baseline.render(data=data)
    bot.send_message(chat_id=-chat_id, text=config, parse_mode=telegram.ParseMode.MARKDOWN)

@app.route('/content/kubeweekly', methods=['POST'])
def kubeweekly():
    data = request.get_json()
    telegram_kubeweekly(data)
    return 'Success'

if __name__ == '__main__':
    app.run()
