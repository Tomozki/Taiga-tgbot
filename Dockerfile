FROM python:3.10.6-buster

WORKDIR /root/Taiga-tgbot

COPY . .

RUN pip install -U -r requirements.txt

CMD ["python3","-m","TaigaRobot"]
