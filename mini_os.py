import os
import subprocess
import platform

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def execute_command(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        print(output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando: {e.output.decode('utf-8')}")

def text_editor(file_name):
    print(f"Iniciando o editor de texto. Digite 'salvar' para salvar e sair.")
    content = []

    while True:
        line = input()
        if line.lower() == 'salvar':
            with open(file_name, 'w') as file:
                file.write('\n'.join(content))
            print(f"Arquivo '{file_name}' salvo.")
            break
        else:
            content.append(line)

def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f"Arquivo '{file_name}' excluído com sucesso.")
    except FileNotFoundError:
        print(f"Erro: Arquivo '{file_name}' não encontrado.")
    except PermissionError:
        print(f"Erro: Permissão negada para excluir '{file_name}'.")

def show_help():
    print("Comandos disponíveis:")
    print("  help            - Exibe esta ajuda.")
    print("  cls ou clear    - Limpa a tela.")
    print("  exit ou quit    - Sai do MiniOS.")
    print("  cd <diretório>  - Muda o diretório atual.")
    print("  editor <arquivo> - Inicia o editor de texto.")
    print("  del <arquivo>   - Exclui o arquivo especificado.")

def mini_os_shell():
    print("Bem-vindo ao MiniOS! Digite 'help' para ver os comandos disponíveis.")
    
    while True:
        current_dir = os.getcwd()
        command = input(f"{current_dir}> ")

        if command.lower() in ['exit', 'quit']:
            break
        
        elif command.startswith('cd '):
            path = command[3:].strip()
            try:
                os.chdir(path)
            except FileNotFoundError:
                print(f"Erro: Diretório '{path}' não encontrado.")
        
        elif command.lower() in ['cls', 'clear']:
            clear_screen()
        
        elif command.startswith('editor '):
            file_name = command.split(' ', 1)[1] if len(command.split(' ', 1)) > 1 else 'novo_arquivo.txt'
            text_editor(file_name)

        elif command.startswith('del '):
            file_name = command.split(' ', 1)[1]
            delete_file(file_name)

        elif command.lower() == 'help':
            show_help()
        
        else:
            print(f"Commando não encontrado: {command}")

if __name__ == "__main__":
    mini_os_shell()
