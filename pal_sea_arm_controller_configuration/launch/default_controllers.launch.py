# Copyright (c) 2022 PAL Robotics S.L. All rights reserved.
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

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch_pal.arg_utils import read_launch_argument
from launch_pal.include_utils import include_launch_py_description


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


def launch_end_effector_controller(context, *args, **kwargs):

    if (read_launch_argument('end_effector', context) == 'no-ee'):
        return []

    end_effector_launcher = read_launch_argument(
        'end_effector_controller_launch', context)
    end_effector_controller_launch = include_launch_py_description(
        'pal_sea_arm_controller_configuration',
        ['launch', end_effector_launcher])

    return [end_effector_controller_launch]


def generate_launch_description():

    end_effector_controller = DeclareLaunchArgument(
        'end_effector_controller_launch',
        default_value=[LaunchConfiguration(
            'end_effector'), '_controller.launch.py'],
        description='end effector controller launch file')

    joint_state_broadcaster_launch = include_launch_py_description(
        'pal_sea_arm_controller_configuration',
        ['launch', 'joint_state_broadcaster.launch.py'])

    arm_controller_launch = include_launch_py_description(
        'pal_sea_arm_controller_configuration',
        ['launch', 'arm_controller.launch.py'])

    ld = LaunchDescription()

    ld.add_action(OpaqueFunction(function=declare_args))
    ld.add_action(joint_state_broadcaster_launch)
    ld.add_action(end_effector_controller)
    ld.add_action(arm_controller_launch)
    ld.add_action(OpaqueFunction(function=launch_end_effector_controller))

    return ld
