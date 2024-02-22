import openai
import os

# Configurar a chave da API da OpenAI
openai.api_key = 'SUA_CHAVE_DE_API'

def ler_arquivo_senctences(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        return arquivo.readlines()

def main():
    # Caminho do arquivo com as sentenças
    caminho_arquivo = os.path.join('inputs', 'sentencas.txt')

    # Ler as sentenças do arquivo
    sentencas = ler_arquivo_senctences(caminho_arquivo)

    # Exibir as sentenças
    print("Sentenças no Arquivo:")
    for sentenca in sentencas:
        print(sentenca.strip())

    # Enviar as sentenças para a GPT-3 para análise
    resposta_gpt3 = openai.Completion.create(
        engine="text-davinci-003",
        prompt=''.join(sentencas),
        max_tokens=150
    )

    # Exibir a resposta da GPT-3
    print("\nResposta da GPT-3:")
    print(resposta_gpt3.choices[0].text.strip())

if __name__ == "__main__":
    main()
