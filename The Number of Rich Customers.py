import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    df = store[store['amount'] > 500]
    # rich_count = len(set(df['customer_id']))
    #rich_count = df['customer_id'].nunique()
    rich_count = len(df['customer_id'].drop_duplicates())

    return pd.DataFrame([rich_count], columns= ['rich_count'])
    