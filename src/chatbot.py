from chave_api import openai
from colorama_config import Fore, Style, init

# a lista "mensagens" registra e mantém o histórico das conversas entre o usuário e o ChatBot, a fim de construir um contexto e fornecer respostas relevantes com base na conversa
mensagens = [
    {
        "role": "system", # mensagem do sistema
        "content": "Você é um ChatBot de uma empresa chamada Lumus. A empresa possui um antivírus chamado Pé de Pano que recebe algumas reclamações e dúvidas das organizações que adquiriram o software. Se possível, não dê respostas extensas." # instrução de como o ChatGPT deve se comportar
     }
]

# a conversa é um loop infinito
while True:
    try:
        while True:
            # capturando a mensagem do usuário
            msg = input("\n{}Você:\n".format(Fore.CYAN))

            # se o usuário não digitou nada
            if not msg:
                print("Erro! Você precisa digitar algo...")
            else:
                break # se digitou, pare de pedir para que ele digite novamente
    except KeyboardInterrupt:
        # tratamento para interrupção de teclado
        print("\nChat encerrado.")
        break # encerra o chat
    except Exception:
        # tratamento para uma interrupção inesperada
        print("Ocorreu um erro inesperado!")
        break # encerra o chat

    # adicionando o contexto da conversa na lista "mensagens"
    mensagens.append(
        {
            "role": "user", # mensagem do usuário
            "content": msg # conteúdo da mensagem
        },
    )
    # solicitando a API a gerar uma resposta do modelo GPT-3.5-turbo com base nas conversas fornecidas na lista "mensagens"
    gpt = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = mensagens, temperature=0.5 # 0.5 gera respostas mais coerentes
    )

    # capturando a resposta do ChatGPT
    resposta = gpt.choices[0].message.content

    # printando a resposta
    print("\n{}Assistente Marianna:\n{}".format(Fore.MAGENTA, resposta))
    
    # adicionando o contexto da conversa na lista "mensagens"
    mensagens.append(
        {
            "role": "assistant", # mensagem do ChatBot
            "content": resposta # conteúdo da mensagem
        }
    )