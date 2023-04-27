from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/bot", methods=['"POST'])
def bot():
    received_msg = request.values.get('Body', '').lower()
    response = MessagingResponse()
    msg_response = response.message()
    responded = False

    if 'citação' in received_msg:
        get_quote = requests.get('https://api.quotable.io/random')
        if get_quote.status_code == 200:
            data = get_quote.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'Não consegui recuperar uma citação neste momento, desculpe.'
        msg_response.body(quote)
        responded = True

    if 'pato' in received_msg or 'pata' in received_msg:
        msg_response("https://tenor.com/pt-BR/view/cat-catdriving-gif-22785638")
        responded = True

    if not responded:
        msg_response.body('Apenas patos')
    return str(response)


if __name__ == "__main__":
    app.run()

#teste