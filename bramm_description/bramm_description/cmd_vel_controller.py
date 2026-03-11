import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CmdVelController(Node):

    def __init__(self):
        super().__init__('cmd_vel_controller')

        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.cmd_callback,
            10
        )

    def cmd_callback(self, msg):
        linear = msg.linear.x
        angular = msg.angular.z

        self.get_logger().info(f'Linear: {linear} Angular: {angular}')

        # TODO: send PWM to motors
        # Example placeholder
        left_motor = linear - angular
        right_motor = linear + angular

        self.get_logger().info(f'Left: {left_motor} Right: {right_motor}')

def main(args=None):
    rclpy.init(args=args)
    node = CmdVelController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()