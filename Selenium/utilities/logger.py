import logging
from pathlib import Path


LOG_PATH = Path(__file__).parents[1] / 'logs'
LOG_PATH.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_PATH / 'test.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

logger = logging.getLogger()
