import pytest
from utilities.driver_factory import DriverFactory
from utilities.config_reader import config


@pytest.fixture(scope='session')
def driver():
    drv = DriverFactory.create_driver()
    yield drv
    drv.quit()


@pytest.fixture
def base_url():
    return config.get('base_url')
