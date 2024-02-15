import socket
import src.proto.algo_commander_pb2 as algo_commander_pb2

def send_robot_position(robot_id, pos_x, pos_y, blue_team, host, port):
    # Create a RobotPosition message
    robot_position = algo_commander_pb2.RobotPosition()
    robot_position.id = robot_id
    robot_position.pos_x = pos_x
    robot_position.pos_y = pos_y
    robot_position.blue_team = blue_team

    # Serialize the message to bytes
    serialized_data = robot_position.SerializeToString()

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Send the serialized data
        sock.sendto(serialized_data, (host, port))
        print("Packet sent successfully: ", len(serialized_data))
    finally:
        sock.close()


def send_udp_message(message, host='localhost', port=12345):
    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        # Send the message
        sock.sendto(message.encode(), (host, port))
        print(f"Sent message: {message} to {host}:{port}")


def main():
    #message = "Hello, UDP!"
    #send_udp_message(message)
    # Define host and port to send packets
    host = '127.0.0.1'  # Change this to your desired destination IP address
    port = 12345        # Change this to your desired destination port number

    # Send a sample RobotPosition message
    robot_id = 1
    pos_x = 10.5
    pos_y = 20.7
    send_robot_position(robot_id, pos_x, pos_y, True, host, port)

if __name__ == "__main__":
    main()