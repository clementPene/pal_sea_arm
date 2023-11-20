joy_teleop:
  ros__parameters:
    move:
      type: topic
      interface_type: geometry_msgs/msg/Twist
      topic_name: cmd_vel
      deadman_buttons: [5]
      axis_mappings:
        linear-x:
          axis: 1
          scale: 1.0
          offset: 0.0
        angular-z:
          axis: 2
          scale: 1.0
          offset: 0.0

    joy_priority:
      type: action
      action_name: joy_priority_action
      buttons: [9]

@[if end_effector in ["pal-pro-gripper"]]@
#    close_gripper:
#      type: action
#      action_name: /gripper_controller/increment
#      action_goal:
#        increment_by: [0.1]
#      buttons: [7] # R2
#
#    open_gripper:
#      type: action
#      action_name: /gripper_controller/increment
#      action_goal:
#        increment_by: [-0.1]
#      buttons: [5] # R1
@[end if]@