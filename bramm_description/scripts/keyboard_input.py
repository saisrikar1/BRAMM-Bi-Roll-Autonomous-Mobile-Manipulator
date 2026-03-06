#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class KeyboardInputClass(Node):
  def __init__(self):
    super().__init__('keyboard_input_node')
    self.publisher = self.create_publisher(String,'keyboard_input_topic',10)

  def publish_input(self):
    msg = String()
    while rclpy.ok:
      msg.data = input('enter desired poisition W , A , S or D :')
      self.publisher.publish(msg)


def main():
  rclpy.init()
  node = KeyboardInputClass()
  rclpy.spin(node)
  rclpy.shutdown()

if __name__ == '__main__':
  main()
