import pandas as pd

pd.options.display.max_columns = None
pd.options.display.max_rows = None

try:
    my_cols = [str(i) for i in range(45)]
    df = pd.read_csv('test12.txt', sep="\t+|\s+", names=my_cols, 
                                    header=None, 
                                    engine="python")

    #Dropped NAN columns and sorted
    df = df.dropna(axis=1).sort_values(by=['4'])

    #Dropped duplicate values
    duplicate_cols = df.drop_duplicates()

    #reversed the order
    reverse_order = duplicate_cols[duplicate_cols.columns[::-1]]

    #Data to csv file
    reverse_order.to_csv('reverse_out.csv')
except Exception as e:
    print(f"Something went wrong: {e}")