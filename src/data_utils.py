# src/data_utils.py
import pandas as pd
from pathlib import Path

# __file__ é o caminho para o arquivo atual (data_utils.py)
# .parent nos leva para o diretório pai (a pasta 'src')
# .parent novamente nos leva para o pai de 'src', que é a RAIZ DO PROJETO.
PROJECT_ROOT = Path(__file__).parent.parent

# Agora definimos os caminhos de dados a partir da raiz do projeto.
DATA_DIR = PROJECT_ROOT / "data"

def load_raw(filename: str) -> pd.DataFrame:
    """Carrega um arquivo CSV da pasta data/raw."""
    raw_path = DATA_DIR / "raw" / filename
    print(f"Loading data from: {raw_path}")
    return pd.read_csv(raw_path)

def save_processed(df: pd.DataFrame, name: str):
    """Salva um DataFrame como .parquet na pasta data/processed."""
    processed_dir = DATA_DIR / "processed"
    processed_dir.mkdir(parents=True, exist_ok=True)
    save_path = processed_dir / f"{name}.parquet"
    df.to_parquet(save_path, index=False)
    print(f"Data saved to: {save_path}")

def load_processed(name: str) -> pd.DataFrame:
    """Carrega um arquivo .parquet da pasta data/processed."""
    load_path = DATA_DIR / "processed" / f"{name}.parquet"
    print(f"Loading processed data from: {load_path}")
    return pd.read_parquet(load_path)