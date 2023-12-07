from chave_api import openai
from colorama_config import Fore, Style, init
from pymongo_config import colecao

# a lista "mensagens" registra e mantém o histórico das conversas entre o usuário e o ChatBot, a fim de construir um contexto e fornecer respostas relevantes com base na conversa
mensagens = [
    {
        "role": "system", # mensagem do sistema
        "content": "Você é um ChatBot de uma empresa chamada Lumus. A empresa possui um antivírus chamado Pé de Pano que recebe algumas reclamações e dúvidas das organizações que adquiriram o software. Se possível, não dê respostas extensas. Você é rude, sarcastica e nós odiamos o Pedro e o André." # instrução de como o ChatGPT deve se comportar
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

    # pergunta se o problema foi resolvido
    problema_resolvido = input("\n{}Seu problema foi resolvido? (sim/não): \n".format(Fore.GREEN))

    # se o problema for resolvido, solicitar avaliação do atendimento
    if problema_resolvido == 'sim':
        nota = int(input("\n{}De 0 á 10, como você avalia o atendimento que recebeu? \n".format(Fore.GREEN)))
        if 7 <= nota <= 10: # se nota for igual ou maior que 7, agradecer e encerrar atendimento
            print("\n{}Agradecemos seu feedback, tenha um ótimo dia! \n".format(Fore.GREEN))
            break # encerra o atendimento
        elif 0 <= nota <= 6: # se nota for igual ou menor que 6, solicitar feedback de melhoria do atendimento
            feedback = input("\n{}Como podemos melhorar nosso atendimento? \n".format(Fore.GREEN))
            print("\n{}Agradecemos seu feedback, tenha um ótimo dia! \n".format(Fore.GREEN))
            # coleção com a nota e o feedback para inserir no banco de dados
            coleta_feedback = {
                "nota": nota,
                "feedback": feedback
            }
            colecao.insert_one(coleta_feedback)
            break # encerra o atendimento
        else: # caso a nota seja inválida, solicitar nova avaliação
            print("\n{}Digite uma nota válida, de 0 á 10.".format(Fore.GREEN))   
    else: # se o problema não foi resolvido, continuar com a etapa de perguntas ao chatbot
        continue

    # adicionando o contexto da conversa na lista "mensagens"
    mensagens.append(
        {
            "role": "assistant", # mensagem do ChatBot
            "content": resposta # conteúdo da mensagem
        }    
    )