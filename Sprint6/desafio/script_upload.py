import boto3
import os

continuar = True

while continuar:
    # Menu do script
    print('[ENVIADOR DE ARQUIVOS PARA BUCKETS 2000]')
    print('[1] Enviar arquivo')
    print('[2] Criar bucket')
    print('[0] Sair')
    acao = int(input('Insira o número de acordo com a ação desejada: '))

    # Área de envio de arquivos
    if acao == 1:
        print('\n[Registrando Credênciais AWS...]')
        aws_acess_key_id = input('Insira a AWS Acess Key ID: ')
        aws_secret_acess_key = input('Insira a AWS Secret Acess key: ')
        aws_session_token = input('Insira o AWS Session Token: ')
        print('\n[Enviando Arquivo...]')
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
        except Exception as erro:
            print(f"[Erro no envio] {erro}")
        print('\n')

    #Área de criação de buckets
    elif acao == 2:
        print('\n[Registrando Credênciais AWS...]')
        aws_acess_key_id = input('Insira a AWS Acess Key ID: ')
        aws_secret_acess_key = input('Insira a AWS Secret Acess key: ')
        aws_session_token = input('Insira o AWS Session Token: ')
        print('\n[Criando Bucket...]')
        nome_novo_balde = input('Insira o nome do novo bucket: ').strip()
        regiao = input('Insira a região do bucket (ex: us-east-1): ').strip()
        print('\n')

        
        os.environ['AWS_ACCESS_KEY_ID'] = aws_acess_key_id
        os.environ['AWS_SECRET_ACCESS_KEY'] = aws_secret_acess_key
        os.environ['AWS_SESSION_TOKEN'] = aws_session_token

        s3 = boto3.client('s3', region_name=regiao)

        try:
            if regiao == 'us-east-1':
                s3.create_bucket(Bucket=nome_novo_balde)
            else:
                s3.create_bucket(Bucket=nome_novo_balde,CreateBucketConfiguration={'LocationConstraint': regiao})
            print(f'[Bucket criado com sucesso!] Nome do bucket: "{nome_novo_balde}", Região do bucket: "{regiao}".')
            print('\n')
        except Exception as erro:
            print(f"[Erro na criação do bucket] {erro}")
            print('\n')

    elif acao == 0:
        continuar = False


