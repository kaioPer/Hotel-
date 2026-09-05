from agno.models.openai import OpenAIChat
from agno.agent import Agent
from dotenv import load_dotenv
from flask import Flask,jsonify,request
from flask_cors import CORS
from supabase import create_client
import os

#Lendo chave API
load_dotenv()


#Criar conexão Banco de dados
supabase = create_client(os.getenv("SUPABASE_URL"),os.getenv("SUPABASE_KEY"))

app = Flask(__name__)
CORS(app)


#Criar o agente
agente = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
   description="Você é um agente de hotel Travesseiro nervoso, slogan:Aqui ate a insonia dorme, que auxilia hospedes a encontrarem o quarto ideal.Quartos Stardard:R$400, Quarto Deluxe:R$600, Quarto Luxo:R$1000. Serviços:Cafe da Manha, academia, restaurante, piscina, estacionamento, servoço de quarto", 
   markdown=False
   
)


@app.route("/",methods=['GET'])
def testar_agente():
    return app.send_static_file("index.html")

@app.route("/perguntar", methods=["POST"])    
def enviar_pergunta():
    dados=request.get_json()
    pergunta = dados['pergunta']
    resposta = agente.run(pergunta)
    return jsonify({"mensagem": resposta.content})


@app.route("/reservas",methods=['POST'])
def criar_reserva():
    dados = request.get_json()
    supabase.table("reservas").insert(dados).execute()
    return jsonify({"mensagem":"Reserva realizada com sucesso!"})


@app.route("/reservas",methods=['GET'])
def reservas_realizadas():
    resultado = supabase.table("reservas").select("*").execute()
    return jsonify (resultado.data)


if __name__ == '__main__':
    app.run(port=8000,host="0.0.0.0", debug=True)