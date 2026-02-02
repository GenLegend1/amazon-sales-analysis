import pandas as pd

def prepare_prophet_data(df):
    """Prepare dataframe for Prophet forecasting."""
    ts = df.groupby('order_date')['total_revenue'].sum().reset_index()
    ts = ts.sort_values('order_date')
    ts = ts.rename(columns={'order_date': 'ds', 'total_revenue': 'y'})
    return ts
