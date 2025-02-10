def maiores_que_media(conteudo:dict)->list:
    acima_da_media = []
    media = sum(conteudo.values())/len(conteudo)
    for chave,valor in conteudo.items():
        if valor > media:
            acima_da_media.append((chave,valor))
    return sorted(acima_da_media, key=lambda valor: valor[1])
    
        
