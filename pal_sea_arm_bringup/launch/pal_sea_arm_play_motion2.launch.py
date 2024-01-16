import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch_pal.include_utils import include_launch_py_description
from launch_pal.arg_utils import read_launch_argument
from pal_sea_arm_description.pal_sea_arm_utils import get_pal_sea_arm_hw_suffix


def declare_args(context, *args, **kwargs):

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

    return [end_effector,
            ft_sensor]


def launch_setup(context, *args, **kwargs):

    end_effector = read_launch_argument('end_effector', context)
    ft_sensor = read_launch_argument('ft_sensor', context)

    approach_planner_file = 'approach_planner' + get_pal_sea_arm_hw_suffix(end_effector=end_effector,
                                                                           ft_sensor=ft_sensor) + '.yaml'
    approach_planner_file_path = os.path.join(
        get_package_share_directory("pal_sea_arm_bringup"),
        "config", "approach_planner", approach_planner_file
    )

    motions_file = 'pal_sea_arm_motions' + get_pal_sea_arm_hw_suffix(end_effector=end_effector,
                                                                     ft_sensor=ft_sensor) + '.yaml'
    motions_file_path = os.path.join(
        get_package_share_directory(
            "pal_sea_arm_bringup"), "config", "motions", motions_file
    )

    play_motion2 = include_launch_py_description(
        "play_motion2",
        ["launch", "play_motion2.launch.py"],
        launch_arguments={
            "motions_file": motions_file_path,
            "approach_planner_config": approach_planner_file_path
        }.items(),
    )

    return [play_motion2]


def generate_launch_description():

    ld = LaunchDescription()

    ld.add_action(OpaqueFunction(function=declare_args))
    ld.add_action(OpaqueFunction(function=launch_setup))

    return ld
