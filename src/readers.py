import pandas as pd

def read_excel(filename):
    cases = pd.read_excel(filename)
    return cases.loc[:, ["aggregate_identifier", "sequence_number","user"]]


    #print(selected_df.columns.values)
    #print(selected_df.groupby("aggregate_identifier")[["sequence_number", "user"]].nunique())