^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package tiago_sea_arm_description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.0.4 (2023-09-13)
------------------
* Merge branch 'fix-urdf' into 'master'
  Fix urdf
  See merge request robots/tiago_sea_arm_robot!8
* Update arm limits
* Change meshes orientation according to the robot
* Add material urdf
* Contributors: David ter Kuile, davidterkuile

0.0.2 (2023-08-31)
------------------
* Merge branch 'add_new_meshes' into 'master'
  Add new meshes of the arm
  See merge request robots/tiago_sea_arm_robot!5
* move joint limits to special xacro file and remove tiago_dual arg
* Update stl origins of arm
* Fix arm_7_link
* Update collision meshes
* Update joint angles for tiago-single
* Update inertia matrices
* Update center of mass for the links
* New set of updated meshes with orientation same as the previous
* Update faulty arm_1_link mesh that contained part of arm_base mesh
* Add new meshes of the arm
* Merge branch 'collision-arm-tool-link' into 'master'
  added collision and description values of the tool link
  See merge request robots/tiago_sea_arm_robot!6
* added collision and description values of the tool link
* Contributors: David ter Kuile, Sai Kishor Kothakota, davidterkuile, ileniaperrella, thomaspeyrucain

0.0.1 (2023-07-10)
------------------
* Merge branch 'dtk/description' into 'master'
  Update TIAGo sea arm to work as a standalone robot
  See merge request robots/tiago_sea_arm_robot!4
* add missing param to xacro cmd
* remove deprecated xacro --inorder arugment
* Change ati to rokubi
* Update stl + frames + collision of the ft_sensor
* Update arm joint limits
* Update default settings in show.launch
* update arm_link_1 limit for tiago_dual
* Add ft_sensor to TIAGo sea
* Update joint limits for tiago dual
* Update inertias
* Update joint limits based on visuals
* update arm joint limits based on visual limit
* Move gazebo.urdf.xacro to main xacro file
* Add joint transmissions and damping to urdf
* Update robot urdf
* remove old meshes, only uses the right arm, add calibration constants
* Urdf only using meshes of right arm
* update models + urdf
* fixed tool_link position
* Merge branch 'mass_modification_for_joints' into 'master'
  added more mass to arm links
  See merge request robots/tiago_sea_arm_robot!2
* added more mass
* rotate arm_7_link axis to point outwards
* Merge branch 'change_joint_4_orientation' into 'master'
  elbow aligned with joint 2
  See merge request robots/tiago_sea_arm_robot!1
* Add blacklisted collisions
* elbow aligned with joint 2
* Separate joint limits in extra file, set convention for joints
* Separate origin of first joint to robot xacro
* Rotate joints 3 and 5 to fix arm
* Add robot and tf in config file
* First commit
* Contributors: David ter Kuile, Luca Marchionni, Narcis Miguel, davidterkuile, luca, narcismiguel, thomaspeyrucain
