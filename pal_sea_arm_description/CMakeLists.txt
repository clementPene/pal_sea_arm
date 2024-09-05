cmake_minimum_required(VERSION 3.8)
project(pal_sea_arm_description)

find_package(ament_cmake_auto REQUIRED)

ament_auto_find_build_dependencies()
if(pal_module_cmake_FOUND)
  pal_register_modules(
    module/10_robot_state_publisher.yaml
  )
elseif(DEFINED ENV{PAL_DISTRO})
  message(FATAL_ERROR "The pal_module_cmake package was not found. Modules not registered.")
endif()

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()

  foreach(arm_type tiago-pro tiago-sea tiago-sea-dual)
    foreach(end_effector no-end-effector pal-pro-gripper)
      foreach(ft_sensor no-ft-sensor rokubi)

        if(arm_type STREQUAL "tiago-pro")
          # Supports both wrists
          foreach(spherical-wrist straight-wrist)
            add_launch_test(
              test/test_description.launch.py
              TARGET "pal_sea_arm_description_${arm_type}_${end_effector}_${ft_sensor}"
              ARGS "wrist_model:=${wrist_model}" "arm_type:=${arm_type}" "end_effector:=${end_effector}" "ft_sensor:=${ft_sensor}"
            )
          endforeach()
        else()
          # Hardcoded straight-wrist for other arm types
          add_launch_test(
            test/test_description.launch.py
            TARGET "pal_sea_arm_description_${arm_type}_${end_effector}_${ft_sensor}"
            ARGS "wrist_model:=straight-wrist" "arm_type:=${arm_type}" "end_effector:=${end_effector}" "ft_sensor:=${ft_sensor}"
          )
        endif()

      endforeach()
    endforeach()
  endforeach()

endif()


# Install Python modules
ament_python_install_package(${PROJECT_NAME})

ament_auto_package(INSTALL_TO_SHARE config gazebo launch meshes robots ros2_control urdf) #test
