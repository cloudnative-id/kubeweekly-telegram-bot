# kubeweekly-telegram-bot

This project is build for sending [kubeweekly.io](https://kubeweekly.io/) (The weekly newsletters for all things Kubernetes) into Telegram.

#### Requirement
---
- Python 3
  
#### How to Run
---
__Install Dependencies__

```
pip3 install -r requirement.txt
```
__Run The APP__

```
python3 main.py
```

#### How to Build
---
__Build Docker__
```
docker build -t <DOCKERIMAGE> .
```

__Run Docker Locally__

```
docker run -e CHATID=123456789 -e TELEGRAM_TOKEN=nomunomuchua -e GITHUB_TOKEN=nomunomuchua <DOCKERIMAGE>
```
