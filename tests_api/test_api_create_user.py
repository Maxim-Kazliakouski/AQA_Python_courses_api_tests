import pytest as pytest
import requests
import conftest
from tests_api_data.api_data import Api_data as test_data


# user creation
class Tests_for_user_creation:
    class Tests_positive:
        @pytest.mark.parametrize('params', test_data.DATA_FOR_USER_CREATION)
        def test_create_user(self, params):
            data = params
            response = requests.post(test_data.REQUEST_FOR_CREATION, json=data)
            json_response = response.json()
            conftest.pars_for_creation_user(json_response)
            assert response.status_code == test_data.STATUS_CODE_201, "User hasn't been created"

    class Tests_negative:
        def test_create_without_user_name(self):
            data = test_data.DATA_FOR_REG_ONLY_WORK
            response = requests.post(test_data.REQUEST_FOR_CREATION, json=data)
            json_response = response.json()
            conftest.pars_for_creation_user(json_response)
            assert response.status_code == test_data.STATUS_CODE_201, "User hasn't been created"

        def test_create_without_user_job(self):
            data = test_data.DATA_FOR_REG_ONLY_NAME
            response = requests.post(test_data.REQUEST_FOR_CREATION, json=data)
            json_response = response.json()
            conftest.pars_for_creation_user(json_response)
            assert response.status_code == test_data.STATUS_CODE_201, "User hasn't been created"

        def test_create_without_user_data(self):
            data = test_data.DATA_FOR_REG_WITHOUT_DATA
            response = requests.post(test_data.REQUEST_FOR_CREATION, json=data)
            json_response = response.json()
            conftest.pars_for_creation_user(json_response)
            assert response.status_code == test_data.STATUS_CODE_201, "User hasn't been created"
