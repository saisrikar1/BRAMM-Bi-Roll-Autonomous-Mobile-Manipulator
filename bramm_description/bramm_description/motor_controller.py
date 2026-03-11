import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MotorController(Node):

    def __init__(self):
        super().__init__('motor_controller')

        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.cmd_callback,
            10
        )

        # robot parameters
        self.wheel_base = 0.14
        self.max_pwm = 255

    def cmd_callback(self, msg):

        v = msg.linear.x
        w = msg.angular.z

        left = v - (w * self.wheel_base / 2)
        right = v + (w * self.wheel_base / 2)

        self.drive_motors(left, right)

    def drive_motors(self, left, right):

        pwm_left = int(left * 200)
        pwm_right = int(right * 200)

        print("Left PWM:", pwm_left)
        print("Right PWM:", pwm_right)

        # here you send to motor driver


def main(args=None):    # here you send to motor driver


    rclpy.init(args=args)
    node = MotorController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()