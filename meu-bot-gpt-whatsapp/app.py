from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
from flask import Flask, request
import openai
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# INFORMAÇÕES DA SUA CONTA
openai.api_key = api_key

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    msg = request.form.get('Body')
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é uma IA especialista em relacionamentos e investigações amorosas."},
            {"role": "user", "content": msg}
        ]
    )
    reply = response['choices'][0]['message']['content']

    r = MessagingResponse()
    r.message(reply)
    return str(r)

if __name__ == "__main__":
    app.run()
