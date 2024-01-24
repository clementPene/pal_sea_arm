# Copyright (c) 2023 PAL Robotics S.L. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from pathlib import Path

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch_param_builder import load_xacro
from launch_ros.actions import Node
from launch_pal.arg_utils import read_launch_argument


def declare_args(context, *args, **kwargs):

    sim_time_arg = DeclareLaunchArgument(
        'use_sim_time', default_value='False',
        description='Use simulation time')

    end_effector = DeclareLaunchArgument(
        'end_effector',
        default_value='pal-pro-gripper',
        description='End effector model of the pal-sea-arm.',
        choices=['pal-pro-gripper', 'no-ee'])

    ft_sensor = DeclareLaunchArgument(
        'ft_sensor',
        default_value='rokubi',
        description='Force torque model of the pal-sea-arm.',
        choices=['rokubi', 'no-ft-sensor'])

    return [sim_time_arg,
            end_effector,
            ft_sensor]


def launch_setup(context, *args, **kwargs):

    robot_description = {'robot_description': load_xacro(
        Path(os.path.join(
            get_package_share_directory('pal_sea_arm_description'),
            'robots', 'pal_sea_arm.urdf.xacro')),
        {
            'use_sim': read_launch_argument('use_sim_time', context),
            'end_effector': read_launch_argument('end_effector', context),
            'ft_sensor': read_launch_argument('ft_sensor', context),
        }
    )}

    rsp = Node(package='robot_state_publisher',
               executable='robot_state_publisher',
               output='both',
               parameters=[{'use_sim_time': LaunchConfiguration('use_sim_time')},
                           robot_description])

    return [rsp]


def generate_launch_description():

    ld = LaunchDescription()

    ld.add_action(OpaqueFunction(function=declare_args))

    # Execute robot_state_publisher node
    ld.add_action(OpaqueFunction(function=launch_setup))

    return ld
