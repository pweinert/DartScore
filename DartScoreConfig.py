__author__ = 'teddycool'
#Config vaues for DartScore. This is the only place for these.

config = {'cam': {'res':(1024,768), 'id':1},  #CAM settings id=0 for webcam, 1 for netcam probably...
          'color':{'sector':(0,255,0),'hit': (255,0,0), 'aim':  (0,255,0), 'calibrate':(0,0,255)}, #colors of sectors and markers
          'mounting': {'aimrectx': 80,'aimrecty': 40},  #values for mounting the cam and center bulls-eye
         "Streamer": {"StreamerImage": "/tmp/stream/pic.jpg", "StreamerLib": "/tmp/stream"},
                   }