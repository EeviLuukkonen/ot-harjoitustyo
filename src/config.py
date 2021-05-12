import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

SCORES_FILENAME = os.getenv("SCORES") or "scores.sqlite"
SCORES_FILEPATH = os.path.join(dirname, '..', 'data', SCORES_FILENAME)
