from proto_compiled.messages_robocup_ssl_detection_pb2 import SSL_DetectionRobot, SSL_DetectionBall

# Observer pattern, the only use is in the World class
class Observer:
    def update_world(self, blue : list[SSL_DetectionRobot], yellow : list[SSL_DetectionRobot], ball : SSL_DetectionBall):
        pass