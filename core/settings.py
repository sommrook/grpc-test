import os

# JWT KEY
SECRET_KEY = "sksmdmdmsdlekzmfthadlq"
ALGORITHM = "HS256"

# DB
MYSQL_USER = os.environ.get("MYSQL_USER", "rEgT6+Cxrdz4g6U+0uIaJw==")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "XCOFnUHPrMaUBYKY1t15ag==")
MYSQL_HOST = os.environ.get("MYSQL_HOST", "localhost")
MYSQL_PORT = int(os.environ.get("MYSQL_PORT", 3306))
MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE", "concurrent_access")

# cyper -> 32 / 16
KEY = os.environ.get("KEY", "sksmsdlekhadlqdfegslkzmffhdldldq")
IV = os.environ.get("IV", "dlekthadlqslekzm")
IS_CYPER = int(os.environ.get("IS_CYPER", 1))


# test token
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1" \
        "c2VyX2FjY291bnQiOiJjaGxvZSIsImNyZWF0ZWRfZGF0ZSI6IjIwMjMtMD" \
        "QtMTQgMDA6MDA6MDAiLCJwd2RfdXBkYXRlZF9kYXRlIjoiMjAyMy0wNC0xN" \
        "CAwMDowMDowMCIsImV4cCI6MTY4MjM4MTg4NX0.uYhT2vibspbkBDY0kWPP4W6fO5s_GrzEO9kz60tzaQg"

# grpc test server
grpc_server_url = "localhost:50051"
