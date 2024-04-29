from classe import DadosRepositorios
from repmanip import ManipulaRepositorios


amazon_rep = DadosRepositorios('amzn')
ling_mais_usadas_amzn = amazon_rep.cria_df_linguagens()

netflix_rep = DadosRepositorios('netflix')
ling_mais_usadas_netflix = netflix_rep.cria_df_linguagens()

spotify_rep = DadosRepositorios('spotify')
ling_mais_usadas_spotify = spotify_rep.cria_df_linguagens()

ling_mais_usadas_amzn.to_csv('processedata/linguagens_amzn.csv')
ling_mais_usadas_netflix.to_csv('processedata/linguagens_netflix.csv')
ling_mais_usadas_spotify.to_csv('processedata/linguagens_spotify.csv')

novo_repo = ManipulaRepositorios('igorrmarques')

nome_repo = 'linguagens-repositorios-empresas'
novo_repo.cria_repo(nome_repo)

novo_repo.add_arquivo(nome_repo, 'linguagens_amzn.csv', 'processedata/linguagens_amzn.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_netflix.csv', 'processedata/linguagens_netflix.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_spotify.csv', 'processedata/linguagens_spotify.csv')
