# Lógica do fluxo de conversa

from models.lead_model import Lead
from services.langchain_service import get_chat_chain
from views.console_view import get_input, print_output
from utils.validators import is_valid_email

def run_chat():
    lead = Lead()
    chat = get_chat_chain()

    print_output("Olá! Sou o assistente virtual da imobiliária. Vamos começar o atendimento.")

    # Etapas
    lead.tipo_imovel = ask(chat, "Qual o tipo de imóvel você procura? (casa, apartamento, terreno...)")
    lead.operacao = ask(chat, "Você deseja comprar, alugar ou vender o imóvel?")
    lead.caracteristicas = ask(chat, "Descreva as principais características desejadas (quartos, bairro, vaga...)")
    lead.faixa_preco = ask(chat, "Qual a faixa de preço aproximada?")
    
    while True:
        email = ask(chat, "Por favor, informe seu e-mail para contato:")
        if is_valid_email(email):
            lead.email = email
            break
        else:
            print_output("E-mail inválido. Tente novamente.")

    print_output("Obrigado! Suas informações foram registradas:")
    print_output(str(lead))

def ask(chain, question):
    print_output(question)
    user_input = get_input()
    response = chain.run(user_input)
    return user_input  # aqui armazenamos a entrada, não a resposta do LLM
