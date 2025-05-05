import os
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def upload_file_to_s3(file_name, bucket_name, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_name)
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_name, bucket_name, object_name)
        print(f"Arquivo '{file_name}' enviado para o bucket '{bucket_name}' como '{object_name}'.")
    except FileNotFoundError:
        print(f"Erro: o arquivo '{file_name}' não foi encontrado.")
    except NoCredentialsError:
        print("Erro: credenciais da AWS não encontradas.")
    except PartialCredentialsError:
        print("Erro: credenciais da AWS incompletas.")
    except Exception as e:
        print(f"Erro: {e}")

def create_text_files(directory, num_files=3):
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_paths = []
    for i in range(1, num_files + 1):
        file_path = os.path.join(directory, f"arquivo{i}.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"<html><body><h1>Arquivo {i}</h1><p>Conteúdo do arquivo {i}.</p></body></html>")
        file_paths.append(file_path)
    return file_paths

if __name__ == "__main__":
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    arquivos = create_text_files(desktop_path, num_files=3)
    bucket = "walter10111980"
    for arquivo in arquivos:
        upload_file_to_s3(arquivo, bucket)
