import logging, os
import pandas as pd

def read_csv(filename):
    file = os.path.abspath(filename)
    logging.info("Reading file: "+ file)
    cases = pd.read_csv(file)
    return cases


def check_mandatory_columns(cases, mandatory_columns):
    return mandatory_columns.issubset(cases.columns)
