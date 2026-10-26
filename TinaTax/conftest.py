import pytest
import requests
from clients.page_api import Page
from utils.csv_reader import load_form as _load_form
from clients.form_api import Form

BASE_URL="https://www.tinataxresolution.com/"


@pytest.fixture(scope="session")
def api_session():
    session = requests.Session()
    yield session
    session.close()
@pytest.fixture
def load_form():
    return _load_form()  # now returns a list of all rows

@pytest.fixture
def web_api(api_session):
    return Page(api_session)
@pytest.fixture
def form_api(api_session):
    return Form(api_session)


