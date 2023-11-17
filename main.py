import requests
import json
from colorama import Fore, Style, init

init(autoreset=True)

def get_character_data(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def print_colored(message, color=Fore.WHITE):
    print(color + message + Style.RESET_ALL)

def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def main():
    id = input("Digite o ID do personagem: ")
    data = get_character_data(id)

    if data is not None:
        print_colored("Nome: " + data["name"], Fore.CYAN)
        print_colored("Status: " + data["status"], Fore.GREEN)
        print_colored("Espécie: " + data["species"], Fore.YELLOW)
        print_colored("Tipo: " + data["type"], Fore.YELLOW)
        print_colored("Gênero: " + data["gender"], Fore.MAGENTA)
        print_colored("Origem: " + data["origin"]["name"], Fore.BLUE)
        print_colored("Localização: " + data["location"]["name"], Fore.BLUE)
        filename = f"character_{id}.json"
        save_to_json(data, filename)
        print_colored(f"Dados salvos em {filename}", Fore.WHITE)
    else:
        print_colored("Personagem não encontrado.", Fore.RED)

if __name__ == "__main__":
    main()
