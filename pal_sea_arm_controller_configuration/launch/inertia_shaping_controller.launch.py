# Copyright (c) 2024 PAL Robotics S.L. All rights reserved.
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
from controller_manager.launch_utils import (
    generate_load_controller_launch_description,
    generate_controllers_spawner_launch_description_from_dict
)
from launch.actions import GroupAction, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch import LaunchDescription, LaunchContext

from launch_pal.arg_utils import LaunchArgumentsBase, read_launch_argument
from launch_pal.param_utils import parse_parametric_yaml
from launch.actions import DeclareLaunchArgument, SetLaunchConfiguration
from dataclasses import dataclass
from launch_pal.robot_arguments import CommonArgs


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):
    side: DeclareLaunchArgument = CommonArgs.side


def declare_actions(launch_description: LaunchDescription, launch_args: LaunchArguments):

    # Launches (inactive) 7 IS controllers
    launch_description.add_action(OpaqueFunction(
        function=setup_inertia_shaping_controllers))

    return


def setup_inertia_shaping_controllers(context: LaunchContext):

    side = read_launch_argument('side', context)

    arm_prefix = "arm"
    if side:
        arm_prefix = f"arm_{side}"

    params_path = os.path.join(
        get_package_share_directory("pal_sea_arm_controller_configuration"),
        'config', 'inertia_shaping_controller'
    )

    inertia_shaping_controllers_dict = {}
    for i in range(1, 8):

        controller_name = f"{arm_prefix}_{i}_joint_inertia_shaping_controller"

        # This is the ref for config, not the actual joint name
        # e.g. both arm_right_1 and arm_left_1 would use the same config
        config_ref = f'arm_{i}_joint'
        param_file = os.path.join(
            params_path, f"{config_ref}_params.yaml"
        )

        remappings = {"ARM_SIDE_PREFIX": arm_prefix,
                      "JOINT_POSITION": i,
                      "PARAMS_PATH": params_path}

        parsed_yaml = parse_parametric_yaml(source_files=[param_file], param_rewrites=remappings)

        inertia_shaping_controllers_dict.update(
            {controller_name: parsed_yaml}
        )

    inertia_shaping_controllers = generate_controllers_spawner_launch_description_from_dict(
        inertia_shaping_controllers_dict,
        extra_spawner_args=['--inactive'],
    )

    return inertia_shaping_controllers


def generate_launch_description():

    # Create the launch description
    ld = LaunchDescription()

    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld
