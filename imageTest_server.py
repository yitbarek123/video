from concurrent import futures
import time
import numpy as np
#import av
import cv2
import grpc
import base64
import StringIO
import imageTest_pb2
import imageTest_pb2_grpc
import skvideo.io
import PIL
from scipy.misc import toimage
_ONE_DAY_IN_SECONDS = 24*60*60
class Greeter(imageTest_pb2_grpc.ImageTestServicer):
 
 def Analyse(self, request_iterator, context):
  c=0
  for req in request_iterator:
  
         l=str(req.img.decode())    
 
  videogen = skvideo.io.vreader(l)
   
  for frame in videogen:
       
        cv2.imshow('Image', frame)
        cv2.waitKey(1)
  return imageTest_pb2.MsgReply(reply = 1 )
   
def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  imageTest_pb2_grpc.add_ImageTestServicer_to_server(Greeter(),     server)
  server.add_insecure_port('[::]:50051')
  server.start()
  try:
    while True:
     time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
   server.stop(0)

if __name__ == '__main__':
  serve()
