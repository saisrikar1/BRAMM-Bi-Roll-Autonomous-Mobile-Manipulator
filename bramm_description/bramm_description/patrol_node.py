import rclpy
from rclpy.node import Node
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped

class PatrolClass(Node):
  def __init__(self):
    super().__init__('patrol_node')
    self.navigator = BasicNavigator()

    waypoints = [
      (4.0, -1.0),
      (1.8, 1.1),
      (2.7, -2.7),
      (0.5, -1.0)
    ]

    for x,y in waypoints:
      goal = PoseStamped()
      goal.header.frame_id = 'map'
      goal.pose.position.x = x
      goal.pose.position.y = y
      goal.pose.orientation.w = 1.0

      self.navigator.goToPose(goal)
      self.navigator.waitUntilNav2Active()
      while not self.navigator.isTaskComplete():
        rclpy.spin_once(self, timeout_sec=0.1)


def main():
  rclpy.init()
  node = PatrolClass()
  rclpy.spin(node)
  rclpy.shutdown()