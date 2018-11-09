from concurrent import futures
import time
import grpc
import Response_streaming_pb2
import Response_streaming_pb2_grpc
number=6;
def run():
    
    channel = grpc.insecure_channel('{host}:{port}'.format(host="localhost",port=50051))
    stub=Response_streaming_pb2_grpc.rsStub(channel=channel)
    req=Response_streaming_pb2.number()
    req.number=6
    for s in stub.numbers(req):
        print(s.square)
        import time
        time.sleep(10)
    

run()
