/play_motion:
  ros__parameters:
    disable_motion_planning: false
    approach_planner:
      planning_groups: # Sorted by order of preference
        - arm
@[if end_effector in ["pal-pro-gripper"]]@
      exclude_from_planning_joints:
        - gripper_finger_joint
@[end if]@
      joint_tolerance: 0.01
      skip_planning_approach_vel: 0.5
      skip_planning_approach_min_dur: 0.5