# src/viz.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Define o caminho para salvar as figuras, usando a mesma lógica do data_utils
PROJECT_ROOT = Path(__file__).parent.parent
OUTPUTS_DIR = PROJECT_ROOT / "outputs" / "figures"

def plot_hist(series: pd.Series, title: str = "", xlabel: str = "", bins: int = 1000, save_path: str = None):
    """
    Plota e opcionalmente salva um histograma para uma série de dados.

    Args:
        series (pd.Series): A série de dados a ser plotada.
        title (str, optional): Título do gráfico.
        xlabel (str, optional): Rótulo do eixo X.
        bins (int, optional): Número de bins do histograma.
        save_path (str, optional): Nome do arquivo para salvar a figura (ex: 'meu_grafico.png').
                                   A figura será salva em outputs/figures/.
    """
    plt.style.use('seaborn-v0_8-paper')
    plt.figure(figsize=(12, 6))
    
    sns.histplot(series, bins=bins, linewidth=0.35, alpha=0.7, stat='percent', label=xlabel)
    plt.title(title, fontsize=12)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel("Percent", fontsize=12)
    plt.tight_layout()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()

    if save_path:
        # Garante que o diretório de outputs exista
        OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
        full_path = OUTPUTS_DIR / save_path
        plt.savefig(full_path, dpi=600)
        print(f"Gráfico salvo em: {full_path}")
        
    plt.show()


def plot_scatter(x: pd.Series, y: pd.Series, title: str = "", xlabel: str = "", ylabel: str = "", save_path: str = None):
    """
    Plota e opcionalmente salva um gráfico de dispersão para duas séries de dados.

    Args:
        x (pd.Series): A série de dados para o eixo X.
        y (pd.Series): A série de dados para o eixo Y.
        title (str, optional): Título do gráfico.
        xlabel (str, optional): Rótulo do eixo X.
        ylabel (str, optional): Rótulo do eixo Y.
        save_path (str, optional): Nome do arquivo para salvar a figura (ex: 'meu_grafico.png').
                                   A figura será salva em outputs/figures/.
    """
    plt.style.use('seaborn-v0_8-paper')
    plt.figure(figsize=(12, 6))
    plt.scatter(x, y, c='red', s=100, edgecolors="k")
    plt.title(title, fontsize=12)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.tight_layout()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()

    if save_path:
        # Garante que o diretório de outputs exista
        OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
        full_path = OUTPUTS_DIR / save_path
        plt.savefig(full_path, dpi=600)
        print(f"Gráfico salvo em: {full_path}")

    plt.show()


def plot_bar(x: pd.Series, y: pd.Series, title: str = "", xlabel: str = "", ylabel: str = "", save_path: str = None):
    """
    Plota e opcionalmente salva um gráfico de barras para duas séries de dados.

    Args:
        x (pd.Series): A série de dados para o eixo X.
        y (pd.Series): A série de dados para o eixo Y.
        title (str, optional): Título do gráfico.
        xlabel (str, optional): Rótulo do eixo X.
        ylabel (str, optional): Rótulo do eixo Y.
        save_path (str, optional): Nome do arquivo para salvar a figura (ex: 'meu_grafico.png').
                                   A figura será salva em outputs/figures/.
    """
    plt.style.use('seaborn-v0_8-paper')
    plt.figure(figsize=(12, 6))
    colors = sns.color_palette("husl", len(x))
    sns.barplot(x=x, y=y, palette=colors)
    plt.title(title, fontsize=12)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.tight_layout()
    plt.grid(True, linestyle='--', alpha=0.6)

    if save_path:
        # Garante que o diretório de outputs exista
        OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
        full_path = OUTPUTS_DIR / save_path
        plt.savefig(full_path, dpi=600)
        print(f"Gráfico salvo em: {full_path}")

    plt.show()



def plot_heatmap(data: pd.DataFrame, title: str = "", xlabel: str = "", ylabel: str = "", save_path: str = None):
    """
    Plota e opcionalmente salva um gráfico de mapa de calor para um DataFrame.

    Args:
        data (pd.DataFrame): O DataFrame contendo os dados a serem plotados.
        title (str, optional): Título do gráfico.
        xlabel (str, optional): Rótulo do eixo X.
        ylabel (str, optional): Rótulo do eixo Y.
        save_path (str, optional): Nome do arquivo para salvar a figura (ex: 'meu_grafico.png').
                                   A figura será salva em outputs/figures/.
    """
    plt.style.use('seaborn-v0_8-paper')
    plt.figure(figsize=(12, 6))
    sns.heatmap(data, annot=True, cmap='coolwarm')
    plt.title(title, fontsize=12)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.tight_layout()
    plt.grid(True, linestyle='--', alpha=0.6)

    if save_path:
        # Garante que o diretório de outputs exista
        OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
        full_path = OUTPUTS_DIR / save_path
        plt.savefig(full_path, dpi=600)
        print(f"Gráfico salvo em: {full_path}")

    plt.show()

def plot_regression(x: pd.Series, y: pd.Series, title: str = "", xlabel: str = "", ylabel: str = "", save_path: str = None):
    """
    Plota e opcionalmente salva um gráfico de regressão para duas séries de dados.

    Args:
        x (pd.Series): A série de dados para o eixo X.
        y (pd.Series): A série de dados para o eixo Y.
        title (str, optional): Título do gráfico.
        xlabel (str, optional): Rótulo do eixo X.
        ylabel (str, optional): Rótulo do eixo Y.
        save_path (str, optional): Nome do arquivo para salvar a figura (ex: 'meu_grafico.png').
                                   A figura será salva em outputs/figures/.
    """
    plt.style.use('seaborn-v0_8-paper')
    plt.figure(figsize=(12, 6))
    sns.regplot(x=x, y=y, ci=None, scatter_kws={'s': 10}, line_kws={'color': 'red'})
    plt.title(title, fontsize=12)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.tight_layout()
    plt.grid(True, linestyle='--', alpha=0.6)

    if save_path:
        # Garante que o diretório de outputs exista
        OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
        full_path = OUTPUTS_DIR / save_path
        plt.savefig(full_path, dpi=600)
        print(f"Gráfico salvo em: {full_path}")

    plt.show()




