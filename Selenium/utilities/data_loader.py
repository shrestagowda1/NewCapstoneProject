import json
import csv
import yaml
from pathlib import Path


ROOT = Path(__file__).parents[1]


def load_json(path):
    with open(path) as f:
        return json.load(f)


def load_csv(path):
    with open(path) as f:
        reader = csv.DictReader(f)
        return list(reader)


def load_yaml(path):
    with open(path) as f:
        return yaml.safe_load(f)
