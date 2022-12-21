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
    input_file = sys.argv[1]
    cases = read_excel(input_file)
    cases["anonymizes_user"] = cases.apply(anonymize_id, axis=1)
    write_to_excel(cases, get_base_filename(input_file))


main()    
