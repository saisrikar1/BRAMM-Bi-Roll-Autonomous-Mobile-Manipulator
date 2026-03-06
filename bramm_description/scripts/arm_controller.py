#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray,String

class ArmControllerClass(Node):
  def __init__(self):
    super().__init__("arm_controller_node")
    self.sub = self.create_subscription(String,'keyboard_input_topic',self.keyboard_input_callback,10)
    self.pub =self.create_publisher(Int32MultiArray,'arm_controller_topic',10)


  def keyboard_input_callback(self, input_msg):
    msg = Int32MultiArray()
    input_data = input_msg.data
    if input_data:
      if input_data == 'W':
        msg = [90,45]
      elif input_data == 'S':
        msg = [90,135]
      elif input_data == 'A':
        msg = [45,90]
      elif input_data == 'D':
        msg = [135,90]
    self.pub.publish(msg)

def main():
  rclpy.init()
  node = ArmControllerClass()
  rclpy.spin(node)
  rclpy.shutdown()

if __name__ == '__main__':
  main()