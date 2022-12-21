import pandas as pd
import os, logging


def write_to_csv(cases, filename):
    isExist = os.path.exists("output")
    if not isExist:
        os.makedirs("output")
    output_name = os.path.abspath("output/"+filename+"_anonymized.csv")
    cases.to_csv(output_name, index=False)
    logging.info("Wrote to file: "+ output_name)