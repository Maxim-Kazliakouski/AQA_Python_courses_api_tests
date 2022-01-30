import requests
import conftest
from tests_api_data.api_data import Api_data as test_data


class Tests_for_deleting_user:
    class Tests_positive:
        def test_delete_user(self):
            response = requests.delete(test_data.REQUEST_FOR_DELETING)
            # json_response = response.json()
            # conftest.pars_for_creation_user(json_response)
            assert response.status_code == test_data.STATUS_CODE_204, "The user hasn't been deleted"
