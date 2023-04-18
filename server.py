from concurrent import futures
import logging
import grpc
import jwt
import datetime
import multiprocessing

import proto.auth_pb2 as auth_pb2
import proto.auth_pb2_grpc as auth_pb2_grpc

from token_exception import *
from core.settings import SECRET_KEY, ALGORITHM
from db.auth_repo import find_user_by_id
from db.session import get_db


def dateformat(date: datetime):
    return date.strftime("%Y-%m-%d %H:%M:%S")

class Auth(auth_pb2_grpc.AuthServicer):
    def TokenCheck(self, request, context):
        db = next(get_db())
        try:
            if request.token is None or request.token == "":
                return auth_pb2.AuthRes(status_code=empty_token_exception()["status_code"],
                                        response_code=empty_token_exception()["response_code"])
            payload = jwt.decode(request.token, SECRET_KEY, algorithms=ALGORITHM)
            user_id = payload.get("user_id")
            if (user_id is None) or (payload.get("pwd_updated_date") is None):
                return auth_pb2.AuthRes(status_code=token_exception()["status_code"],
                                        response_code=token_exception()["response_code"])
        except jwt.exceptions.ExpiredSignatureError:
            raise expired_exception

        except jwt.exceptions.InvalidTokenError:
            return auth_pb2.AuthRes(status_code=token_exception()["status_code"],
                                    response_code=token_exception()["response_code"])
        user = find_user_by_id(db, user_id)

        if not user:
            return auth_pb2.AuthRes(status_code=expired_exception()["status_code"], response_code=expired_exception()["response_code"])

        if payload.get("pwd_updated_date") < dateformat(user.pwd_updated_date):
            return auth_pb2.AuthRes(status_code=password_token_exception()["status_code"],
                                    response_code=password_token_exception()["response_code"])

        db.close()
        return auth_pb2.AuthRes(user_id=payload["user_id"], user_account=payload["user_account"],
                                created_date=payload["created_date"], pwd_updated_date=payload["pwd_updated_date"],
                                status_code=200, response_code="CODE2000")


# def _run_server():
#     server = grpc.server(futures.ThreadPoolExecutor(max_workers=3))
#
#     auth_pb2_grpc.add_AuthServicer_to_server(Auth(), server)
#
#     server.add_insecure_port('[::]:50051')
#     server.start()
#     server.wait_for_termination()
#     logging.info(f"process id is {os.getpid()}")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))

    auth_pb2_grpc.add_AuthServicer_to_server(Auth(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


def main():
    workers = []
    for _ in range(5):
        worker = multiprocessing.Process(target=serve)
        worker.start()
        workers.append(worker)
    for worker in workers:
        worker.join()


if __name__ == "__main__":
    logging.basicConfig()
    main()
