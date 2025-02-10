import json

# Filmes drama/romance populares pandemia (2020-2022) com IDs e ano de produção
filmes_2020_2022 = [
    {'ID': 'tt9683478', 'Título Original': 'The Half of It', 'Ano de Producao': 2019},
    {'ID': 'tt1893273', 'Título Original': 'The Last Letter from Your Lover', 'Ano de Producao': 2019},
    {'ID': 'tt7798646', 'Título Original': 'The Photograph', 'Ano de Producao': 2018},
    {'ID': 'tt3581652', 'Título Original': 'West Side Story', 'Ano de Producao': 2019},
    {'ID': 'tt9100054', 'Título Original': 'The Lost Daughter', 'Ano de Producao': 2019},
    {'ID': 'tt9620292', 'Título Original': 'Promising Young Woman', 'Ano de Producao': 2019},
    {'ID': 'tt10293406', 'Título Original': 'The Power of the Dog', 'Ano de Producao': 2019},
    {'ID': 'tt11847410', 'Título Original': 'The Fallout', 'Ano de Producao': 2019},
    {'ID': 'tt10366460', 'Título Original': 'CODA', 'Ano de Producao': 2020},
    {'ID': 'tt3108894', 'Título Original': 'The Tender Bar', 'Ano de Producao': 2020},
    {'ID': 'tt7983894', 'Título Original': 'Ammonite', 'Ano de Producao': 2018},
    {'ID': 'tt10362466', 'Título Original': 'After We Collided', 'Ano de Producao': 2019},
    {'ID': 'tt12676326', 'Título Original': 'Malcolm & Marie', 'Ano de Producao': 2020},
    {'ID': 'tt8847712', 'Título Original': 'The French Dispatch', 'Ano de Producao': 2018},
    {'ID': 'tt3661210', 'Título Original': 'The Dig', 'Ano de Producao': 2016},
    {'ID': 'tt9827834', 'Título Original': "Sylvie's Love", 'Ano de Producao': 2014},
    {'ID': 'tt11161474', 'Título Original': 'Pieces of a Woman', 'Ano de Producao': 2019},
    {'ID': 'tt9354842', 'Título Original': 'To All the Boys: P.S. I Still Love You', 'Ano de Producao': 2018},
    {'ID': 'tt3907584', 'Título Original': 'All the Bright Places', 'Ano de Producao': 2015},
    {'ID': 'tt9866072', 'Título Original': 'Holidate', 'Ano de Producao': 2018}
]

# Filmes drama/romance populares pré-pandemia (2017-2019) com IDs e ano de produção
filmes_2017_2019 = [
    {'ID': 'tt5726616', 'Título Original': 'Call Me by Your Name', 'Ano de Producao': 2008},
    {'ID': 'tt5580390', 'Título Original': 'The Shape of Water', 'Ano de Producao': 2015},
    {'ID': 'tt1517451', 'Título Original': 'A Star Is Born', 'Ano de Producao': 2015},
    {'ID': 'tt5164432', 'Título Original': 'Love, Simon', 'Ano de Producao': 2016},
    {'ID': 'tt5776858', 'Título Original': 'Phantom Thread', 'Ano de Producao': 2016},
    {'ID': 'tt3281548', 'Título Original': 'Little Women', 'Ano de Producao': 2016},
    {'ID': 'tt3104988', 'Título Original': 'Crazy Rich Asians', 'Ano de Producao': 2015},
    {'ID': 'tt7125860', 'Título Original': 'If Beale Street Could Talk', 'Ano de Producao': 2017},
    {'ID': 'tt7653254', 'Título Original': 'Marriage Story', 'Ano de Producao': 2017},
    {'ID': 'tt5462602', 'Título Original': 'The Big Sick', 'Ano de Producao': 2015},
    {'ID': 'tt1289403', 'Título Original': 'The Guernsey Literary and Potato Peel Pie Society', 'Ano de Producao': 2015},
    {'ID': 'tt2226597', 'Título Original': 'The Mountain Between Us', 'Ano de Producao': 2012},
    {'ID': 'tt6472976', 'Título Original': 'Five Feet Apart', 'Ano de Producao': 2017},
    {'ID': 'tt5977276', 'Título Original': 'The Aftermath', 'Ano de Producao': 2016},
    {'ID': 'tt4799066', 'Título Original': 'Midnight Sun', 'Ano de Producao': 2015},
    {'ID': 'tt3799232', 'Título Original': 'The Kissing Booth', 'Ano de Producao': 2014},
    {'ID': 'tt1667321', 'Título Original': 'On Chesil Beach', 'Ano de Producao': 2014},
    {'ID': 'tt7942742', 'Título Original': 'Her Smell', 'Ano de Producao': 2017},
    {'ID': 'tt0385887', 'Título Original': 'Motherless Brooklyn', 'Ano de Producao': 2017},
    {'ID': 'tt3846674', 'Título Original': 'Blue Jay', 'Ano de Producao': 2015}
]

# Função para salvar os dados em um arquivo JSON
def salvar_json(dados, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

# Salvando os dados em arquivos JSON
salvar_json(filmes_2020_2022, 'ano_prod_pan_drama_romance.json')
salvar_json(filmes_2017_2019, 'ano_prod_pre_pan_drama_romance.json')

