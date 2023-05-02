import os

HF_TOKEN = os.environ.get('HF_TOKEN', None)
HF_TOKEN = None if HF_TOKEN == "<insert your HF token here>" else HF_TOKEN
