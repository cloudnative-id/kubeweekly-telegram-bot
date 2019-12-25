import os
import yaml
import telegram
from github import Github
from jinja2 import Environment, FileSystemLoader

def telegram_kubeweekly(data):
    # render markdown message.
    message = baseline.render(data=data)

    # send message.
    bot.send_message(chat_id=-chat_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)

# Set current directory.
ENV = Environment(loader=FileSystemLoader('.'))

# Jinja template of the bot.
TEMPLATE_PATH = './templates/template_message.j2'

# Load Jinja template.
baseline = ENV.get_template(TEMPLATE_PATH)

# get environment data.
chat_id = int(os.getenv('CHATID'))
telegram_token = os.getenv('TELEGRAM_TOKEN')
github_token = os.getenv('GITHUB_TOKEN')

# telegram bot.
bot = telegram.Bot(telegram_token)

# github.
g = Github(github_token)

# read repo
repo = g.get_repo("cloudnative-id/kubeweekly-scrapper")

# get file contentList.yaml
contents_raw = repo.get_contents("contentList.yaml")
content_list = yaml.load(contents_raw.decoded_content)

# temporary variable
x = 0

# check every content with stattus not delivered
for data in content_list['contentList']:
    if data['status'] == 'not delivered':

        # get file spesific kubeweekly
        kubeweekly_raw = repo.get_contents(data['content'])
        kubeweekly_data = yaml.load(kubeweekly_raw.decoded_content)
        
        # run telegram bot
        telegram_kubeweekly(kubeweekly_data)

        # change status to delivered
        content_list['contentList'][x]['status'] = 'delivered'

    x += 1

# update contentList.yaml
repo.update_file(contents_raw.path, "Updated by Bot", yaml.dump(content_list), contents_raw.sha)

        


