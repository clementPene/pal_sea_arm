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

from typing import Dict
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, GroupAction
from controller_manager.launch_utils import generate_load_controller_launch_description
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration, PythonExpression


def generate_launch_description():

    # Create the launch description and populate
    ld = LaunchDescription()

    launch_args = declare_launch_arguments()

    for arg in launch_args.values():
        ld.add_action(arg)

    declare_actions(ld, launch_args)

    return ld


def declare_launch_arguments() -> Dict:

    arg_dict = {}

    sim_time_arg = DeclareLaunchArgument(
        'use_sim_time', default_value='false',
        description='Use sim time. ')

    arg_dict[sim_time_arg.name] = sim_time_arg

    end_effector = DeclareLaunchArgument(
        'end_effector',
        default_value='pal-pro-gripper',
        description='End effector model of the arm.',
        choices=['pal-pro-gripper', 'no-ee'])

    arg_dict[end_effector.name] = end_effector

    namespace = DeclareLaunchArgument(
        'namespace',
        default_value='',
        description='Define namespace of the robot. ')

    arg_dict[namespace.name] = namespace

    return arg_dict


def declare_actions(launch_description: LaunchDescription, launch_args: Dict):

    pkg_share_folder = get_package_share_directory(
        'pal_sea_arm_controller_configuration')

    joint_state_broadcaster = GroupAction(
        [generate_load_controller_launch_description(
            controller_name='joint_state_broadcaster',
            controller_type='joint_state_broadcaster/JointStateBroadcaster',
            controller_params_file=os.path.join(
                pkg_share_folder,
                'config', 'joint_state_broadcaster.yaml'))
         ],
        forwarding=False)

    launch_description.add_action(joint_state_broadcaster)

    arm_controller = GroupAction(
        [generate_load_controller_launch_description(
            controller_name='arm_controller',
            controller_type='joint_trajectory_controller/JointTrajectoryController',
            controller_params_file=os.path.join(
                get_package_share_directory(
                    'pal_sea_arm_controller_configuration'),
                'config', 'arm_controller.yaml'))
         ],
        forwarding=False)

    launch_description.add_action(arm_controller)

    end_effector_controller = GroupAction(
        [generate_load_controller_launch_description(
            controller_name='gripper_controller',
            controller_type='joint_trajectory_controller/JointTrajectoryController',
            controller_params_file=os.path.join(
                get_package_share_directory(
                    'pal_pro_gripper_controller_configuration'),
                'config', 'gripper_controller.yaml'))
         ],
        forwarding=False,
        condition=IfCondition(
            PythonExpression(
                ["'", LaunchConfiguration(
                    'end_effector'), "' != 'no-ee'"]
            )
        ))
    launch_description.add_action(end_effector_controller)

    return
