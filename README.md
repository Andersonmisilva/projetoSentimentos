## Descrição do Projeto
Este projeto utiliza a API da OpenAI para realizar uma análise de sentimentos em um conjunto de frases. O objetivo é obter insights sobre as emoções expressas nas sentenças fornecidas. O modelo GPT-3 da OpenAI é utilizado para gerar respostas com base nas entradas, indicando o sentimento associado a cada frase.

## Estrutura do Projeto
O projeto está organizado em uma estrutura intuitiva:

# inputs: Contém o arquivo sentencas.txt com as sentenças a serem analisadas.
outputs: Armazena os resultados da análise.
src: Contém o script principal, script.py, responsável por orquestrar o processo.
Configuração
Antes de executar o projeto, certifique-se de:

## Instalar as dependências do projeto: pip install -r requirements.txt.
Configurar a chave da API da OpenAI no arquivo script.py.

## Execução

Para realizar a análise de sentimentos, execute o script script.py com o comando:
bash
Copy code
python ./src/script.py
Este comando exibirá as sentenças do arquivo, enviará para a API da OpenAI e mostrará a resposta da análise de sentimentos.

## Contribuição
#Contribuições são bem-vindas! Sinta-se à vontade para:

Abrir problemas relatando bugs ou sugestões.
Enviar solicitações de pull para melhorias.
