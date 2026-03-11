import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Float64MultiArray


class VisualServo(Node):

    def __init__(self):

        super().__init__('visual_servo_controller')

        self.sub = self.create_subscription(
            Float32MultiArray,
            '/target_detection',
            self.target_callback,
            10
        )

        self.pub = self.create_publisher(
            Float64MultiArray,
            '/arm_controller/commands',
            10
        )

        self.joint8 = 0.0
        self.joint9 = 0.0

        self.kx = 0.0005
        self.ky = 0.0005

    def clamp(self,val,low,high):
        return max(low,min(high,val))

    def target_callback(self,msg):

        x = msg.data[0]
        y = msg.data[1]
        area = msg.data[2]

        if x < 0:
            return

        cx = 320
        cy = 240

        error_x = x - cx
        error_y = y - cy

        self.joint8 += -error_x * self.kx
        self.joint9 += -error_y * self.ky

        # limit angles
        self.joint8 = self.clamp(self.joint8,-1.5,1.5)
        self.joint9 = self.clamp(self.joint9,-1.5,1.5)

        cmd = Float64MultiArray()
        cmd.data = [self.joint8,self.joint9]

        self.pub.publish(cmd)


def main():

    rclpy.init()

    node = VisualServo()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()