# Anonymize IDs

Clone the repository:

```
git clone https://github.com/MichelledeGroot/anonymize-files.git
```

To run the script for anonymizing ids, first install the dependencies using (python 3):

```
pip3 install -r requirements.txt
``` 

Make sure the input file (.csv) has the at least the following columns (including column name): user and aggregate_identifier

Example of running the script:

```
python3 src/anonymize.py "examples/data/example.csv"
```
