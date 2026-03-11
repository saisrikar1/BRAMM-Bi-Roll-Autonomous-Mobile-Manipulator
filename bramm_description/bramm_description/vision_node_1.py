import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from std_msgs.msg import Float32MultiArray

import cv2
import numpy as np


class VisionClass(Node):

    def __init__(self):
        super().__init__('vision_node_1')

        self.bridge = CvBridge()

        self.subscription = self.create_subscription(
            Image,
            'camera2/image_raw',
            self.image_callback,
            10
        )

        self.pub = self.create_publisher(
            Float32MultiArray,
            '/target_detection',
            10
        )

    def image_callback(self, msg):

        frame = self.bridge.imgmsg_to_cv2(msg, 'bgr8')

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_red = np.array([0,120,70])
        upper_red = np.array([10,255,255])

        mask = cv2.inRange(hsv, lower_red, upper_red)

        kernel = np.ones((5,5), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if contours:

            largest = max(contours, key=cv2.contourArea)
            area = cv2.contourArea(largest)

            if area > 500:

                x, y, w, h = cv2.boundingRect(largest)

                cx = x + w // 2
                cy = y + h // 2

                cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
                cv2.circle(frame, (cx,cy), 5, (255,0,0), -1)

                self.get_logger().info(
                    f"cube detected: {cx}, {cy} area: {area}"
                )

                msg_out = Float32MultiArray()
                msg_out.data = [float(cx), float(cy), float(area)]

                self.pub.publish(msg_out)

        cv2.imshow("vision", frame)
        cv2.waitKey(1)


def main():

    rclpy.init()
    node = VisionClass()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()