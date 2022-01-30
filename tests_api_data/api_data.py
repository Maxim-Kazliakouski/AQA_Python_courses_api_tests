class Api_data:
    # user creation
    REQUEST_FOR_CREATION = 'https://reqres.in/api/users'
    STATUS_CODE_201 = 201
    DATA_FOR_USER_CREATION = [{"name": "Max",
                               "job": "Tester"},
                              {"name": "Alex",
                               "job": "Dev"}]
    DATA_FOR_REG_ONLY_WORK = {"job": "Tester"}
    DATA_FOR_REG_ONLY_NAME = {"name": "Max"}
    DATA_FOR_REG_WITHOUT_DATA = {}
    # user registration
    DATA_FOR_USER_REG = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    REQUEST_FOR_REG = 'https://reqres.in/api/register'
    STATUS_CODE_200 = 200
    STATUS_CODE_400 = 400
    DATA_FOR_USER_REG_ONLY_PASSWORD = {"password": "pistol"}
    DATA_FOR_USER_REG_ONLY_EMAIL = {"email": "eve.holt@reqres.in"}

    # user login
    REQUEST_FOR_LOGIN = 'https://reqres.in/api/login'
    DATA_FOR_USER_LOGIN = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    DATA_FOR_USER_LOG_WITHOUT_EMAIL = {"password": "pistol"}
    DATA_FOR_USER_LOG_WITHOUT_PASSWORD = {"email": "eve.holt@reqres.in"}

    # deleting user
    REQUEST_FOR_DELETING = 'https://reqres.in/api/users'
    STATUS_CODE_204 = 204

