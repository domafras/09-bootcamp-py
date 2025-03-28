import pandas as pd # type: ignore
import os
import glob

# Funçaõ Extract, que lê e consolida dados do arquivo JSON
def extrair_dados_e_consolidar(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_concat = pd.concat(df_list, ignore_index=True)
    return df_concat

# Função Transfortm, que transforma os dados em um DataFrame
def calcular_kpi_total_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

# Função Load, que carrega os dados em CSV ou Parquet
def carregar_dados(df: pd.DataFrame, formato_saida: list):
    """
    parametro que vai ser ou "csv" ou "parquet" ou "os dois"
    """
    for formato in formato_saida:
        if formato == 'csv':
            df.to_csv('data/df.csv', index=False)
        if formato == 'parquet':
            df.to_parquet('data/df.parquet', index=False)

# Função Pipeline que calcula KPI de vendas consolidado
def pipeline_calcular_kpi_vendas(pasta: str, formato_saida: list) -> None:
    df_test = extrair_dados_e_consolidar(pasta)
    df_calculado = calcular_kpi_total_vendas(df_test)
    carregar_dados(df_calculado, formato_saida)
    