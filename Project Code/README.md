# CS7IS4 Temproality (Group 7)

## Setup
Preferably create a virtual environment: `python3 -m venv .env`

Activate the virtual environment: `source .env/bin/activate`

Install all required libraries: `pip install -r requirements.txt`

### Development
Do make sure to update the `requirements.txt` file if you use any new library.

### NLTK Errors
There can be some issues with NLTK. There might be some internal that could be missing. To resolve these, try the steps mentioned for below error.

`NLTK download SSL: Certificate verify failed`: Do the following to resolve:
Search 'Install Certificates.command' in finder and open it.
Then do following steps in `python3` interpreter:

```console
>> import nltk
>> nltk.download()
```

(Source: https://stackoverflow.com/questions/38916452/nltk-download-ssl-certificate-verify-failed/59530679#59530679 )

## Run

- For extracting sentence level and article level tense sequences: `TenseSeqGenerator.ipynb` (Jupyter Notebook)
- For similarity analysis: `TenseSimilarityAnalysis.ipynb` (Jupyter Notebook)