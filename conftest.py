import atexit
import os
import time
import pytest


def pars_for_creation_user(json_response):
    print()
    for i, j in json_response.items():
        print(f'{i}: {j}')


# @pytest.fixture(scope='session')
# def clearing_results_folder():
#     print('\nClearing results folder...')
#     time.sleep(5)
#     os.system("rm -rf results/*")
#     yield
#     print('Ending tests...')


# def start_allure_report():
#     print('\nGenerating allure report...')
#     os.system('allure serve results/')
#     time.sleep(5)
