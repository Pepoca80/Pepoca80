import requests
import os

def get_quote():
    # Usando uma API pública de citações (ZenQuotes)
    response = requests.get("https://zenquotes.io/api/random")
    json_data = response.json()
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return quote

def update_readme(quote):
    readme_path = "README.md"
    
    # 1. Ler o conteúdo atual do arquivo
    with open(readme_path, "r", encoding="utf-8") as file:
        content = file.read()
    
    # 2. Definir os marcadores
    start_marker = ""
    end_marker = ""
    
    # 3. Verificar se os marcadores existem
    if start_marker not in content or end_marker not in content:
        print("Erro: Marcadores não encontrados no README.md")
        return

    # 4. Substituir o conteúdo entre os marcadores
    # Tudo antes do marcador inicial + marcador inicial + NOVA FRASE + marcador final + tudo depois
    before = content.split(start_marker)[0]
    after = content.split(end_marker)[1]
    
    new_content = f"{before}{start_marker}\n*{quote}*\n{end_marker}{after}"
    
    # 5. Salvar o arquivo
    with open(readme_path, "w", encoding="utf-8") as file:
        file.write(new_content)
    print("README atualizado com sucesso!")

if __name__ == "__main__":
    quote = get_quote()
    update_readme(quote)
