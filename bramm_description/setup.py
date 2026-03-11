from setuptools import setup
import os
from glob import glob

package_name = 'bramm_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),

        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
        (os.path.join('share', package_name, 'meshes'), glob('meshes/*')),
        (os.path.join('share', package_name, 'config'), glob('config/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='author',
    maintainer_email='todo@todo.com',
    description='Robot description package',
    license='TODO',
    entry_points={
        'console_scripts': [
            'patrol_node = bramm_description.patrol_node:main',
            'vision_node_1 = bramm_description.vision_node_1:main',
            'cmd_vel_controller = bramm_description.cmd_vel_controller:main',
            'motor_controller = bramm_description.motor_controller:main',
            'visual_servo_node = bramm_description.visual_servo_node:main',
        ],
    },
)