# src/features.py
import pandas as pd

def add_order_value(df: pd.DataFrame):
    """
    Calcula o valor total de cada pedido e o adiciona como uma nova coluna 'order_value'.

    Args:
        df (pd.DataFrame): DataFrame contendo os dados dos pedidos. 
                           Deve incluir 'order_id' e 'price'.

    Returns:
        pd.DataFrame: DataFrame com a nova coluna 'order_value'.
    """
    # Garante que a coluna 'price' exista antes de tentar a transformação
    if 'price' in df.columns:
        df['order_value'] = df.groupby('order_id')['price'].transform('sum')
    else:
        print("Aviso: Coluna 'price' não encontrada. A feature 'order_value' não foi criada.")
    return df

def compute_shipping_time(df: pd.DataFrame):
    """
    Calcula o tempo de envio em dias entre a compra e a entrega.

    Args:
        df (pd.DataFrame): DataFrame contendo os dados dos pedidos.
                           As colunas de data já devem estar no formato datetime.

    Returns:
        pd.DataFrame: DataFrame com a nova coluna 'shipping_time_days'.
    """
    # Converte colunas para datetime se ainda não forem, tratando erros
    purchase_col = 'order_purchase_timestamp'
    delivered_col = 'order_delivered_customer_date'
    
    
    df['shipping_time_days'] = (df[delivered_col] - df[purchase_col]).dt.days
    df['shipping_time_days'] = df['shipping_time_days'].astype('Int64')
    return df


def compute_shipping_delay(df: pd.DataFrame):
    """
    Calculates the shipping delay in days between the promised and delivered dates.

    Args:
        df (pd.DataFrame): DataFrame containing the order data.
                           The date columns must already be in datetime format.

    Returns:
        pd.DataFrame: DataFrame with the new 'shipping_delay_days' column.
    """
    # Convert columns to datetime if they are not already, handling errors
    promised_col = 'order_estimated_delivery_date'
    delivered_col = 'order_delivered_customer_date'

   

    df['shipping_delay_days'] = (df[delivered_col] - df[promised_col]).dt.days

    # If there wasnt a delay, we need to set the negative number in 'shipping_delay_days' to 0:
    df['shipping_delay_days'] = df['shipping_delay_days'].clip(lower=0)
    df['shipping_delay_days'] = df['shipping_delay_days'].astype('Int64') 
    return df

 
def compute_delivery_total_time(df: pd.DataFrame):

    # Calculates the number of days between the order purchase day and delivery day

    # Args:
    #     df (pd.DataFrame): DataFrame containing the order data.
    #                        The date columns must already be in datetime format.

    # Returns:
    #     pd.DataFrame: DataFrame with the new 'delivery_total_time' column.

    purchase_col = 'order_purchase_timestamp'
    delivered_col = 'order_delivered_customer_date'

    df['total_delivery_time'] = (df[delivered_col] - df[purchase_col]).dt.days

    df['total_delivery_time'] = df['total_delivery_time'].astype('Int64')

    return df



# def compute_delay_vs_shippinglimit(df: pd.DataFrame):

#     # Calculates the shipping delay in days between the shipping limit date and delivered dates.

#     # Args:
#     #     df (pd.DataFrame): DataFrame containing the order data.
#     #                        The date columns must already be in datetime format.

#     # Returns:
#     #     pd.DataFrame: DataFrame with the new 'shipping_delay_days' column.

#     limit_col = 'shipping_limit_date'
#     delivered_col = 'order_delivered_customer_date'

#     df['delaydays_vs_shippinglimit'] = (df[delivered_col] - df[limit_col]).dt.days

#     # If there wasnt a delay, we need to set the negative number in 'delaydays_vs_shippinglimit' to 0:
#     df['delaydays_vs_shippinglimit'] = df['delaydays_vs_shippinglimit'].clip(lower=0)
#     df['delaydays_vs_shippinglimit'] = df['delaydays_vs_shippinglimit'].astype('Int64')

#     return df