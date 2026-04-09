
import requests

musica = requests.get('https://itunes.apple.com/search?term=ogrilo&media=music&limit=5')

dicionario = (musica.json())

musicas = (dicionario['results'])

decisao = input('Qual artista você quer ouvir?: ')
# if decisao:




i = 1

for musica in musicas:
    print(f'Musica {i}:  {musica['trackName']}')
    i += 1
