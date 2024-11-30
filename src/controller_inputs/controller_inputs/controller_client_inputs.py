import rclpy
import socket
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
import pickle
import sys


class ControllerClientSocket(Node):
    def __init__(self):
        super().__init__("controller_inputs")
        self.input_publisher = self.create_publisher(
            Float32MultiArray, "input_topic", 10
        )
        HOST = "192.168.1.125"
        PORT = 8080
        ADDRESS = (HOST, PORT)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(ADDRESS)

        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.publish_inputs)

    def publish_inputs(self):
        while True:
            try:
                message = self.s.recv(1024)
            except socket.error:
                print("Connection closed on server side")
                sys.exit(0)

            try:
                self.inputs = pickle.loads(message)
            except pickle.UnpicklingError:
                print(f"Cannot Unpickle {self.inputs}")
                # raise

            print(self.inputs)
            msg = Float32MultiArray()
            msg.data = self.inputs
            self.input_publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    controller_inputs = ControllerClientSocket()
    rclpy.spin(controller_inputs)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
