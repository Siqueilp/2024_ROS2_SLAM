import os
from setuptools import setup
from glob import glob

package_name = 'warehouse_robot_controller_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='focalfossa',
    maintainer_email='focalfossa@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
          'robot1_controller = warehouse_robot_controller_pkg.robot1_controller:main',
          'robot1_estimator = warehouse_robot_controller_pkg.robot1_estimator:main',
          'robot2_controller = warehouse_robot_controller_pkg.robot2_controller:main',
          'robot2_estimator = warehouse_robot_controller_pkg.robot2_estimator:main'
        ],
    },
)
