import sys
import subprocess


def create_executable(script_path, icon_path=None) -> None:
    """
    Cria um executável a partir de um script Python usando PyInstaller.

    Args:
        script_path (str): O nome do script Python que será transformado em executável.
        icon_path (str, opcional): O caminho para um ícone (.ico) para o executável. Default é None.
    """

    # Verifica se o PyInstaller está instalado
    try:
        import PyInstaller.__main__
    except ImportError:
        print("PyInstaller não está instalado. Instalando automaticamente...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

    # Comando base do PyInstaller
    command = [sys.executable, "-m", "PyInstaller", "--onefile", script_path]

    # Adiciona o ícone se fornecido
    if icon_path:
        command.extend(["--icon", icon_path])

    # Executa o comando
    try:
        subprocess.run(command, check=True)
        print(f"Executável criado com sucesso! Você pode encontrá-lo na pasta 'dist'.")
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao tentar criar o executável: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    # Exemplo de uso:
    script = "meu_script.py"  # Nome do script que você deseja transformar em executável
    icon = "meu_icone.ico"  # Opcional: caminho para um arquivo .ico para o ícone

    # Chama a função para criar o executável
    create_executable(script)
