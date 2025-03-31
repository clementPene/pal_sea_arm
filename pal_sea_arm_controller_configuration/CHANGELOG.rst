^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package pal_sea_arm_controller_configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.0.3 (2024-03-22)
------------------
* Merge branch 'dtk/fix/restructure' into 'humble-devel'
  Dtk/fix/restructure
  See merge request robots/pal_sea_arm!23
* Update copyright year
* Remove unused imports for flake test
* Refactor arm_controller
* Remove unused default_safety_parameters
* Create force-torque sensor related launch file
* Restructure launch files
* Contributors: David ter Kuile, Noel Jimenez, davidterkuile

Forthcoming
-----------
* Remove choices for ft-sensor side for triago compatibility
* Contributors: David ter Kuile

1.15.0 (2025-03-27)
-------------------
* Support in pal_sea_arm_bringup
* Support in pal_sea_arm_controller_configuration
* SEA transmission optional loading
* added joint torque state broadcaster
* Contributors: Daniel Costanzi, oscarmartinez

1.14.5 (2025-02-28)
-------------------

1.14.4 (2025-02-19)
-------------------
* Merge branch 'tpe/fix_ft_sensor' into 'humble-devel'
  Fix ATI sensor in gazebo simulation
  See merge request robots/pal_sea_arm!62
* Fix ATI sensor in gazebo simulation
* Contributors: thomas.peyrucain, thomaspeyrucain

1.14.3 (2025-02-05)
-------------------
* Use ft_sensor suffix for force-torque sensor name
* Contributors: Noel Jimenez

1.14.2 (2025-01-23)
-------------------

1.14.1 (2025-01-21)
-------------------

1.14.0 (2025-01-16)
-------------------

1.13.0 (2024-11-07)
-------------------
* Set update_rate for joint_state_broadcaster
* Contributors: Noel Jimenez

1.12.0 (2024-10-29)
-------------------

1.11.6 (2024-10-21)
-------------------

1.11.5 (2024-10-09)
-------------------

1.11.4 (2024-10-08)
-------------------

1.11.3 (2024-10-02)
-------------------

1.11.2 (2024-09-30)
-------------------
* Merge branch 'vmo/ati_controller' into 'humble-devel'
  Adding ati controller
  See merge request robots/pal_sea_arm!43
* Adding ati controller
* Contributors: thomaspeyrucain, vivianamorlando

1.11.1 (2024-09-27)
-------------------

1.11.0 (2024-09-19)
-------------------

1.10.1 (2024-09-09)
-------------------

1.10.0 (2024-08-06)
-------------------
* Use controller_type from the controllers config
* Contributors: Noel Jimenez

1.0.9 (2024-07-11)
------------------

1.0.8 (2024-07-09)
------------------
* Add warning for pal_module_cmake not found
* add modules for description and controller*
* Contributors: Aina, Noel Jimenez

1.0.7 (2024-06-26)
------------------
* Merge branch 'dtk/move-robot-args' into 'humble-devel'
  Change import for launch args
  See merge request robots/pal_sea_arm!30
* Create standalone robot args for sea arms
* Contributors: David ter Kuile, davidterkuile

1.0.6 (2024-05-22)
------------------
* Merge branch 'feat/auto-generated_srdf_files' into 'humble-devel'
  add no-end-effector condition in controllers
  See merge request robots/pal_sea_arm!26
* linters
* add no-end-effector condition in controllers
* Contributors: Aina Irisarri, davidterkuile

1.0.5 (2024-05-09)
------------------

1.0.4 (2024-04-26)
------------------
* 1.0.3
* Update Changelog
* Update copyright year
* Remove unused imports for flake test
* Refactor arm_controller
* Remove unused default_safety_parameters
* Create force-torque sensor related launch file
* Restructure launch files
* Contributors: David ter Kuile, Noel Jimenez

1.0.2 (2024-03-07)
------------------

1.0.1 (2024-01-29)
------------------

1.0.0 (2024-01-29)
------------------
* Merge branch 'ros2-migration' into 'humble-devel'
  Ros2 migration
  See merge request robots/pal_sea_arm!17
* remove unused type param from controller config files
* update to 3.8 the cmake_minimum_required Version
* clean default controller + playmotion2 added
* update launch files
* update motions files
* default controllers added
* controller_configuration configs file
* add more dependencies to pal_sea_arm_controller_configuration
* migration of pal_sea_arm_description folder
* migration of CMakeLists.txt and package.xml to ros2
* Contributors: Adria Roig, ileniaperrella

0.1.3 (2023-10-27)
------------------

0.1.2 (2023-10-24)
------------------

0.1.1 (2023-10-23)
------------------

0.1.0 (2023-10-20)
------------------
* Merge branch 'new_name' into 'master'
  Change tiago_pro_arm ro pal_sea_arm and combine both urdf
  See merge request robots/pal_sea_arm!9
* Changes after removing pal_sea_arm_controller_configuration_gazebo
* Address comments + fix colors
* Change tiago_pro_arm ro pal_sea_arm and combine both urdf
* Contributors: Jordan Palacios, thomaspeyrucain
