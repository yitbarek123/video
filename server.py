from concurrent import futures
import time
import grpc
import Response_streaming_pb2
import Response_streaming_pb2_grpc
_ONE_DAY_IN_SECONDS=24*60*60

class rs(Response_streaming_pb2_grpc.rsServicer):
      def numbers(self, request, context):
          for x in range(request.number):
            print("request came")
            sq=Response_streaming_pb2.square()
            sq.square=x+1
            yield sq


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Response_streaming_pb2_grpc.add_rsServicer_to_server(rs(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
