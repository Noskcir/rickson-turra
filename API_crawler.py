import json
import urllib.request
from bs4 import BeautifulSoup
lista_quantidade = []


def quantidade_de_palavras(lista_urls, palavra):
    for cad in lista_urls:
        u = urllib.request.urlopen(cad)
        html = u.read()
        soup = BeautifulSoup(html, "html.parser")
        paragrafo = soup.find_all("p")
        quantidade = 0
        for each in paragrafo:
            convert = str(each)
            if x in convert:
                quantidade+= 1
        lista_quantidade.append(quantidade)
    the_dict = {"Primeiro Site": lista_quantidade[0],
    "Segundo Site": lista_quantidade[1],
    "Terceiro Site": lista_quantidade[2]}
    the_json = json.dumps(the_dict)
    return the_json        


urls = input("Digite as URLs: ") 
lista_urls = urls.split(', ')       
x = input("Digite a palavra a ser procurada na página: ")
quantidade_de_palavras(lista_urls, x)   
