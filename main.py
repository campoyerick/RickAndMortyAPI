import requests
import json
from tabulate import tabulate
from colorama import Fore, Style, init

init(autoreset=True)

def get_character_data(id):
    url = f"https://rickandmortyapi.com/api/character/{id}"
    response = requests.get(url)

    response.raise_for_status()

    if "error" in response.json():
        raise ValueError(response.json()["error"])
    
    return response.json()

def print_colored(message, color=Fore.WHITE):
    print(color + message + Style.RESET_ALL)

def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def display_character_data(data):
    table_data = [
        ["Nome", data["name"]],
        ["Status", data["status"]],
        ["Espécie", data["species"]],
        ["Tipo", data["type"]],
        ["Gênero", data["gender"]],
        ["Origem", data["origin"]["name"]],
        ["Localização", data["location"]["name"]]
    ]

    table = tabulate(table_data, headers=["Informações", "Valores"], tablefmt="fancy_grid")
    print(table)

def main():
    try:
        id = input("Digite o ID do personagem: ")
        data = get_character_data(id)
        display_character_data(data)

        filename = f"character_{id}.json"
        save_to_json(data, filename)
        print_colored(f"Dados salvos em {filename}", Fore.GREEN)
    

    # caso a API esteja OFF
    except requests.exceptions.HTTPError as e:
        print_colored(f"Erro na requisição: {e}", Fore.RED)

    # caso personagem não existe
    except ValueError as e:
        print_colored(f"Erro: {e}", Fore.RED)

    # Erros alatorios.
    except Exception as e:
        print_colored(f"Erro inesperado: {e}", Fore.YELLOW)

if __name__ == "__main__":
    main()
