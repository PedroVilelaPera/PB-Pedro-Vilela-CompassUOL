import boto3
import os

continuar = True

while(continuar):
    print('[ENVIADOR DE ARQUIVOS PARA BUCKETS 2000]')
    print('[1] Enviar arquivo')
    print('[0] Sair')
    acao = int(input('Insira o número de acordo com a ação desejada: '))

    if acao == 1:
        print('\n')
        print('[Registrando Credênciais AWS...]')
        aws_acess_key_id = input('Insira a AWS Acess Key ID: ')
        aws_secret_acess_key = input('Insira a AWS Secret Acess key: ')
        aws_session_token = input('Insira o AWS Session Token: ')
        print('\n')
        print('[Enviando Arquivo...]')
        nome_balde = input('Insira o nome do seu bucket: ')
        nome_arquivo = input('Insira o nome do arquivo que gostaria de enviar: ')
        nome_objeto = input('Insira o nome dele dentro do bucket: ')
        print('\n')

        os.environ['AWS_ACCESS_KEY_ID'] = aws_acess_key_id
        os.environ['AWS_SECRET_ACCESS_KEY'] = aws_secret_acess_key
        os.environ['AWS_SESSION_TOKEN'] = aws_session_token

        s3 = boto3.client('s3')

        try:
            s3.upload_file(nome_arquivo, nome_balde, nome_objeto)
            print(f'[Envio bem-sucedido!] Arquivo disponível como "{nome_objeto}" no bucket "{nome_balde}".')
            print('\n')
        except Exception as erro:
            print(f"[Erro no envio] {erro}")
            print('\n')
        
    elif acao == 0:
        continuar = False
