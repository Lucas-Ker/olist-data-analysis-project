# scripts/download_data.py

import os
import subprocess

def download_and_unzip_kaggle_dataset():
    """
    Baixa e descompacta o dataset Olist do Kaggle.
    
    Certifique-se de que a API do Kaggle está configurada com o token
    no diretório ~/.kaggle/kaggle.json.
    """
    dataset = 'olistbr/brazilian-ecommerce'
    destination_folder = 'data/raw'
    
    # Cria a pasta de destino se ela não existir
    os.makedirs(destination_folder, exist_ok=True)
    
    print(f"Baixando o dataset '{dataset}' para a pasta '{destination_folder}'...")
    
    # Constrói o comando do Kaggle API
    command = [
        'kaggle', 'datasets', 'download',
        '-d', dataset,
        '-p', destination_folder,
        '--unzip'
    ]
    
    try:
        # Executa o comando
        subprocess.run(command, check=True, capture_output=True, text=True)
        print("Download e descompressão concluídos com sucesso!")
        
    except FileNotFoundError:
        print("Erro: O comando 'kaggle' não foi encontrado.")
        print("Certifique-se de que a biblioteca do Kaggle está instalada ('pip install kaggle') e que o executável está no seu PATH.")
        
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando do Kaggle: {e}")
        print("Verifique se suas credenciais da API do Kaggle estão corretas em ~/.kaggle/kaggle.json.")
        print(f"Stderr: {e.stderr}")

if __name__ == '__main__':
    download_and_unzip_kaggle_dataset()