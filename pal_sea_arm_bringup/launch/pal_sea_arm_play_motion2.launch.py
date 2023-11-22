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

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction

from launch_pal.arg_utils import read_launch_argument
from launch_pal.include_utils import include_launch_py_description
from pal_sea_arm_description.pal_sea_arm_utils import get_pal_sea_arm_hw_suffix


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

    end_effector = read_launch_argument('end_effector', context)
    ft_sensor = read_launch_argument('ft_sensor', context)

    motions_file = 'pal_sea_arm_motions' + get_pal_sea_arm_hw_suffix(end_effector=end_effector,
                                                                     ft_sensor=ft_sensor) + '.yaml'

    play_motion2_config = os.path.join(
        get_package_share_directory('pal_sea_arm_bringup'), 'config', 'motions', motions_file)

    play_motion2 = include_launch_py_description(
        'play_motion2', ['launch', 'play_motion2.launch.py'],
        launch_arguments={'play_motion2_config': play_motion2_config}.items())

    return [play_motion2]


def generate_launch_description():

    ld = LaunchDescription()
    ld.add_action(OpaqueFunction(function=declare_args))
    ld.add_action(OpaqueFunction(function=launch_setup))

    return ld
