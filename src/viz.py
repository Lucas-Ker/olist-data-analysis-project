# src/viz.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
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
    
    sns.histplot(series, bins=bins, linewidth=0.4, alpha=0.7, stat='percent', label=xlabel)
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
        print(f"Histogram saved at: {full_path}")

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
        print(f"Plot saved at: {full_path}")

    plt.show()


def plot_bar(x: pd.Series, y: pd.Series, title: str = "", xlabel: str = "", ylabel: str = "", save_path: str = None, hue: str = None):
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
    sns.barplot(x=x, y=y, palette=colors, hue=hue)
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
        print(f"Plot saved at: {full_path}")

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
        print(f"Heatmap saved at: {full_path}")

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
        print(f"Regression plot saved at: {full_path}")

    plt.show()


def plot_count(data: pd.DataFrame, column: str, title: str = "", xlabel: str = "", save_path: str = None):
    """
    Plots and optionally saves a count plot for a DataFrame.
    Pass a specific column to the `data` parameter in the function call.

    Args:
        data (pd.DataFrame): The DataFrame containing the data to be plotted.
        title (str, optional): Title of the plot.
        xlabel (str, optional): X-axis label.
        ylabel (str, optional): Y-axis label.
        save_path (str, optional): Name of the file to save the figure (e.g., 'my_plot.png').
                                   The figure will be saved in outputs/figures/.
    """
    plt.style.use('seaborn-v0_8-paper')
    plt.figure(figsize=(12, 6))
    colors = sns.color_palette("husl", len(data[column].unique()))
    sns.countplot(data=data, x=column, palette=colors, stat='percent')
    plt.title(title, fontsize=12)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel('Percentage', fontsize=12)
    plt.tight_layout()
    plt.grid(True, linestyle='--', alpha=0.6)

    if save_path:
        # Garante que o diretório de outputs exista
        OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
        full_path = OUTPUTS_DIR / save_path
        plt.savefig(full_path, dpi=600)
        print(f"Count plot saved at: {full_path}")

    plt.show()



def plot_line(data: pd.Series, title: str = "", xlabel: str = "", ylabel: str = "", save_path: str = None):
    """
    Plots a line chart for a Series (index on the X-axis, values on the Y-axis).

    Args:
        data (pd.Series): The data series to plot.
        title (str, optional): Title of the plot.
        xlabel (str, optional): X-axis label.
        ylabel (str, optional): Y-axis label.
        save_path (str, optional): Name of the file to save the figure.
    """
    plt.style.use('seaborn-v0_8-paper')
    plt.figure(figsize=(12, 6))

    # Normalize colors to the [0,1] range
    n = len(data)
    colors = plt.cm.rainbow(np.linspace(0, 1, n))

    # Plot each segment with a different color
    for i in range(n - 1):
        plt.plot(
            data.index[i:i+2].to_timestamp(), # .to_timestamp() para converter Período para Datetime
            data.values[i:i+2],
            linestyle='-',
            marker='o',
            color=colors[i]
        )
    plt.title(title, fontsize=12)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.tight_layout()
    plt.grid(True, linestyle='--', alpha=0.6)

    if save_path:
        OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
        full_path = OUTPUTS_DIR / save_path
        plt.savefig(full_path, dpi=600)
        print(f"Line plot saved at: {full_path}")

    plt.show()


# def lm_plot2(data: pd.DataFrame, x: str, y: str, hue: str = None, title: str = "", xlabel: str = "", ylabel: str = "", data_1: str = "", data_2: str = "", color_data_1: str = "", color_data_2: str = "", save_path: str = None):
#     """
#     Plots and optionally saves a linear model plot for a DataFrame.

#     Args:
#         data (pd.DataFrame): The DataFrame containing the data to be plotted.
#         x (str): The column name for the x-axis.
#         y (str): The column name for the y-axis.
#         hue (str, optional): The column name for color encoding.
#         title (str, optional): Title of the plot.
#         xlabel (str, optional): X-axis label.
#         ylabel (str, optional): Y-axis label.
#         save_path (str, optional): Name of the file to save the figure (e.g., 'my_plot.png').
#                                    The figure will be saved in outputs/figures/.
#     """
#     plt.style.use('seaborn-v0_8-paper')
#     plt.figure(figsize=(12, 6))
#     g = sns.lmplot(data=data, x=x, y=y, hue=hue, palette={data_1: color_data_1, data_2: color_data_2}, legend=False)
#     g.ax.get_lines()[1].set_color('yellow')  
#     handles_originais, labels_originais = g.ax.get_legend_handles_labels()
#     black_line = mlines.Line2D([], [], color='black', label='Regression ' + data_1)
#     yellow_line = mlines.Line2D([], [], color='yellow', label='Regression ' + data_2)

#     g.ax.legend(
#         handles=handles_originais + [black_line, yellow_line],
#         loc='upper left'
#     )
#     g.set(title=title)
#     plt.grid(True, linestyle='--', alpha=0.6)

#     if save_path:
#         OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
#         full_path = OUTPUTS_DIR / save_path
#         plt.savefig(full_path, dpi=600)
#         print(f"LM plot saved at: {full_path}")

#     plt.show()

 

def lm_plot(df: pd.DataFrame, x: str, y: str, hue: str = None, title: str = "", save_path: str = None):
    """
    Plots and optionally saves a linear model plot for a DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame containing the data to be plotted.
        x (str): The column name for the x-axis.
        y (str): The column name for the y-axis.
        hue (str, optional): The column name for color encoding.
        title (str, optional): Title of the plot.
        xlabel (str, optional): X-axis label.
        ylabel (str, optional): Y-axis label.
        save_path (str, optional): Name of the file to save the figure (e.g., 'my_plot.png').
                                   The figure will be saved in outputs/figures/.
    """
    plt.style.use('seaborn-v0_8-paper')
    plt.figure(figsize=(12, 6))
    g = sns.lmplot(data=df, x=x, y=y, hue=hue, ci=None, scatter_kws={'s': 10}, line_kws={'linewidth': 2}, legend=True)
    g.set(title=title)
    plt.xlabel(x, fontsize=12)
    plt.ylabel(y, fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    # plt.legend()
    if save_path:
        OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
        full_path = OUTPUTS_DIR / save_path
        plt.savefig(full_path, dpi=600)
        print(f"LM plot saved at: {full_path}")

    plt.show()




def plot_box(df: pd.DataFrame, x: str, y: str, title: str = "", xlabel: str = "", ylabel: str = "", save_path: str = None, hue: str = None):
    """
    Plots and optionally saves a box plot for a DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame containing the data to be plotted.
        x (str): The column name for the x-axis.
        y (str): The column name for the y-axis.
        title (str, optional): Title of the plot.
        xlabel (str, optional): X-axis label.
        ylabel (str, optional): Y-axis label.
        save_path (str, optional): Name of the file to save the figure (e.g., 'my_plot.png').
                                   The figure will be saved in outputs/figures/.
    """
    plt.style.use('seaborn-v0_8-paper')
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x=x, y=y, hue=hue)
    plt.title(title, fontsize=12)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)

    if save_path:
        OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
        full_path = OUTPUTS_DIR / save_path
        plt.savefig(full_path, dpi=600)
        print(f"Box plot saved at: {full_path}")

    plt.show()


# Em src/viz.py

# Em src/viz.py

def plot_stacked_bar(data: pd.DataFrame, title: str = "", xlabel: str = "", ylabel: str = "", save_path: str = None):
    """
    Plots and optionally saves a 100% stacked bar chart from a pre-formatted DataFrame.
    """
    plt.style.use('seaborn-v0_8-paper')
    
    data_to_plot = data.copy()
 
    data_to_plot.index = data_to_plot.index.get_level_values(0).astype(int)
    ax = data_to_plot.plot(
        kind='bar',
        stacked=True,
        figsize=(12, 6),
        colormap='coolwarm_r',
        edgecolor='black'
    )

    # Adicionar anotações
    for p in ax.patches:
        width, height = p.get_width(), p.get_height()
        x, y = p.get_xy() 
        if height > 1:
            ax.text(x + width / 2, 
                    y + height / 2, 
                    f'{height:.1f}%',
                    horizontalalignment='center', 
                    verticalalignment='center',
                    fontsize=8,
                    fontweight='bold',
                    color='white')

    # Formatação do Gráfico
    plt.title(title, fontsize=12)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.xticks(rotation=0)
    ax.legend(title=data.columns.name, bbox_to_anchor=(1.02, 1), loc='upper left')
    plt.tight_layout()

    if save_path:
        OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
        full_path = OUTPUTS_DIR / save_path
        plt.savefig(full_path, dpi=600)
        print(f"Stacked bar plot saved at: {full_path}")

    plt.show()


