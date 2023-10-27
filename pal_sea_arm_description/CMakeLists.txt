cmake_minimum_required(VERSION 2.8.3)
project(pal_sea_arm_description)

find_package(catkin REQUIRED)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES canopies_description
#  CATKIN_DEPENDS other_catkin_pkg
#  DEPENDS system_lib
)
foreach(dir config gazebo meshes robots urdf)
    install(DIRECTORY ${dir}/
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)

#############
## Testing ##
#############

if(CATKIN_ENABLE_TESTING)
  find_package(rostest REQUIRED)
  foreach(arm_model pal-sea-arm-standalone tiago-pro tiago-sea tiago-sea-dual)
      foreach(end_effector false pal-pro-gripper custom)
          foreach(ft_sensor false rokubi)
                      add_rostest(test/test_pal_sea_arm.test ARGS arm_model:=${arm_model}
                          end_effector:=${end_effector} ft_sensor:=${ft_sensor})
          endforeach(ft_sensor)
      endforeach(end_effector)
  endforeach(arm_model)
endif()