import requests
import conftest
from tests_api_data.api_data import Api_data as test_data


class Tests_for_registration:
    class Tests_positive:
        def test_login_user(self):
            data = test_data.DATA_FOR_USER_LOGIN
            response = requests.post(test_data.REQUEST_FOR_LOGIN, json=data)
            json_response = response.json()
            conftest.pars_for_creation_user(json_response)
            assert response.status_code == test_data.STATUS_CODE_200, "The user hasn't been logged"

    class Tests_negative:
        def test_login_without_email(self):
            data = test_data.DATA_FOR_USER_LOG_WITHOUT_EMAIL
            response = requests.post(test_data.REQUEST_FOR_LOGIN, json=data)
            json_response = response.json()
            conftest.pars_for_creation_user(json_response)
            assert response.status_code == test_data.STATUS_CODE_400, 'The user has been logged'

        def test_login_without_password(self):
            data = test_data.DATA_FOR_USER_LOG_WITHOUT_PASSWORD
            response = requests.post(test_data.REQUEST_FOR_LOGIN, json=data)
            json_response = response.json()
            conftest.pars_for_creation_user(json_response)
            assert response.status_code == test_data.STATUS_CODE_400, 'The user has been logged'

        def test_login_without_data(self):
            data = {}
            response = requests.post(test_data.REQUEST_FOR_LOGIN, json=data)
            json_response = response.json()
            conftest.pars_for_creation_user(json_response)
            assert response.status_code == test_data.STATUS_CODE_400, 'The user has been logged'
