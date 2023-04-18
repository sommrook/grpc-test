from __future__ import print_function

import logging

import grpc

import proto.auth_pb2 as auth_pb2
import proto.auth_pb2_grpc as auth_pb2_grpc

from core.settings import grpc_server_url, token
from core.status_code import StatusCode

status_code = {"CODE4001": StatusCode.CODE4001.message,
               "CODE4002": StatusCode.CODE4002.message,
               "CODE4003": StatusCode.CODE4003.message,
               "CODE4004": StatusCode.CODE4004.message}
def run():
    with grpc.insecure_channel(grpc_server_url) as channel:
        stub = auth_pb2_grpc.AuthStub(channel)
        response = stub.TokenCheck(auth_pb2.AuthReq(token=token))
        if response.status_code == 200:
            print("token check success")
            payload = {
                "user_id": response.user_id,
                "user_account": response.user_account,
                "created_date": response.created_date,
                "pwd_updated_date": response.pwd_updated_date
            }
            print(payload)
        else:
            print("token check error")
            response_code = response.response_code
            print(status_code[response_code])


if __name__ == "__main__":
    logging.basicConfig()
    run()