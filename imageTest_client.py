
import grpc
import cv2
import imageTest_pb2
import imageTest_pb2_grpc
import skvideo.io
import numpy as np
#import requests
import PIL
URL="video.AVI"
def run():
   channel = grpc.insecure_channel('localhost:50051')
   stub = imageTest_pb2_grpc.ImageTestStub(channel)
   response = stub.Analyse( generateRequests() )

def generateRequests():
    URL=raw_input("enter video path: ")
    m=0

    for i in range(6):
       
        yield imageTest_pb2.MsgRequest(img= URL.encode())
        break 

if __name__ == '__main__':
  run()
