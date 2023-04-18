def expired_exception():
    return {"status_code": 401, "response_code": "CODE4001"}


def token_exception():
    return {"status_code": 401, "response_code": "CODE4002"}


def empty_token_exception():
    return {"status_code": 401, "response_code": "CODE4003"}


def password_token_exception():
    return {"status_code": 400, "response_code": "CODE4004"}

