import pandas as pd

# Read the xlsx file
def Import(path):
    df = pd.read_excel(path, index_col=None, header=0)
    return df['URL']

def Export(path, data):
    df = pd.DataFrame(data)
    df.to_excel(path, index=False, header=True)
    