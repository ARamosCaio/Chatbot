# Chatbot for Whatsapp

## Description

A chatbot for whatsapp that returns duck photos and famous quotes.

## Tools Used

- [Python](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- [Twilio](https://www.twilio.com/en-us)
- [ngrok](https://ngrok.com/docs/getting-started/)

## How To Run It

Before running the chatbot, it's necessary to create a twilio account.

First create a virtual environment:

```shell
python -m venv .venv
```

Then activate it
For windows:

```shell
.venv\Scripts\activate.bat
```

For linux:

```shell
.venv\Scripts\activate.bat
```

After that, install the required packages:

```shell
pip install -r requirements.txt
```

Run the server:

```shell
make start
```

After that go to the twilio website and log-in.

Go to Messagin -> Try it out -> Send a WhatsApp message.

Add the number or scan the QR code and on sandbox settings paste the link avaible on the ngrok terminal after fowarding and add/bot at the end.

Save it and that's it, enjoy your duck pics and the quotes!

## What I´ve Learned

- How to create chatbots using flask
- How to use ngork to create a safe connection
- How to use twilio to send messages to WhatsApp
- I learned more about APIs using flask, and how to use public APIs