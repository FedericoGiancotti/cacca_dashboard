import pandas as pd

def load_data(file):
    df = pd.read_csv(file, delimiter="\t", header=None)
    df = df[df[0].str.endswith('💩')]
    pattern = r'\[(.*?)\] (.*?): (.*)'
    df[['timestamp', 'name', 'element']] = df[0].str.extract(pattern)
    df = df.drop(columns=[0])
    df['timestamp'] = pd.to_datetime(df['timestamp'], format='%d/%m/%y, %H:%M:%S')
    return df
