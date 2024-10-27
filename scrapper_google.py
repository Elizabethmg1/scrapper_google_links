import requests
from bs4 import BeautifulSoup
import argparse

def scrape_google(palabras, paginas):
    busqueda = '+'.join(palabras)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
    
    param_paginas = (paginas - 1) * 10
    saltos = 0
    
    while saltos < param_paginas + 1:
        r = requests.get(
            f'https://www.google.com/search?q={busqueda}&start={saltos}',
            headers=headers
        )
        response = r.text
        soup = BeautifulSoup(response, "html.parser")
        
        div = soup.find("div", {'id': 'search'})
        if div:
            all_a = div.find_all("a", attrs={"data-ved": True})
            for a in all_a:
                link = a['href']
                if link.startswith('https'):
                    print(link)
        else:
            print("No se encontraron resultados.")
        saltos += 10

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script para buscar enlaces en Google.")
    parser.add_argument("palabras", nargs='+', help="Palabras para la búsqueda en Google (separadas por espacio).")
    parser.add_argument("paginas", type=int, help="Número de páginas a consultar.")
    
    args = parser.parse_args()
    
    scrape_google(args.palabras, args.paginas)
