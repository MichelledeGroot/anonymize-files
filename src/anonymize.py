import hashlib
import sys, os

from readers import *
from writers import *


def anonymize_id(case):
    case_id = case.get("aggregate_identifier")
    user_id = case.get("user")
    
    # create a hash of the input value and the original ID
    hash_value = hashlib.sha256((case_id + user_id).encode()).hexdigest()
    
    # return the first 10 characters of the hash as the anonymized ID
    return hash_value[:10]


def get_base_filename(file):
    file_name = os.path.basename(file)
    name, _ = os.path.splitext(file_name)
    return name


def main():
    logging.basicConfig(level=logging.DEBUG)
    input_file = sys.argv[1]
    cases = read_csv(input_file)
    
    mandatory_columns = {'aggregate_identifier', 'user'}
    if check_mandatory_columns(cases, mandatory_columns):
        logging.info("Creating anonymized ids...")     
        cases["user"] = cases.apply(anonymize_id, axis=1)
        write_to_csv(cases, get_base_filename(input_file))
    else:
        logging.error("Missing column, please check if the following columns are present in your dataset: %s" , mandatory_columns)


main()    
