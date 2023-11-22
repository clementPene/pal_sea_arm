play_motion2:
  ros__parameters:
@[if end_effector in ["pal-pro-gripper"]]@
    controllers: [arm_controller, gripper_controller]
@[end if]@
@[if end_effector in ["no-ee"]]@
    controllers: [arm_controller]
@[end if]@
    motions:
      home:
        joints: [arm_1_joint,
        arm_2_joint, arm_3_joint, arm_4_joint, arm_5_joint,
        arm_6_joint, arm_7_joint]
        times_from_start: [0.5, 4.0, 7.0]        
        positions: [1.8557, -1.5919, 0.35538, 1.9818, 0.0, -1.5976, 1.57,
                    0.36, -1.6008, 0.3489, 1.9818, 0.0, -1.5829, 1.57,
                    0.36, -1.83, 0.47, 2.39, 0.0, -1.5463, 1.72]
        meta:
          name: Home
          usage: demo
          description: 'Go home'
