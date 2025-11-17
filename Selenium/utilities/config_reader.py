import yaml
from pathlib import Path


CONFIG_PATH = Path(__file__).parents[1] / 'config' / 'config.yaml'


class Config:
    def __init__(self, path=CONFIG_PATH):
        with open(path) as f:
            self.cfg = yaml.safe_load(f)

    def get(self, key, default=None):
        return self.cfg.get(key, default)


config = Config()
