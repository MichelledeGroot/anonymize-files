import pandas as pd

def write_to_excel(cases, filename):
    cases.to_excel("output/"+filename+"_anonymized.xlsx")