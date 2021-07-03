# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "kobuki_project: 1 messages, 0 services")

set(MSG_I_FLAGS "-Ikobuki_project:/home/jay/catkin_ws/src/kobuki_project/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(kobuki_project_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/jay/catkin_ws/src/kobuki_project/msg/Status.msg" NAME_WE)
add_custom_target(_kobuki_project_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "kobuki_project" "/home/jay/catkin_ws/src/kobuki_project/msg/Status.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(kobuki_project
  "/home/jay/catkin_ws/src/kobuki_project/msg/Status.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/kobuki_project
)

### Generating Services

### Generating Module File
_generate_module_cpp(kobuki_project
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/kobuki_project
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(kobuki_project_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(kobuki_project_generate_messages kobuki_project_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/jay/catkin_ws/src/kobuki_project/msg/Status.msg" NAME_WE)
add_dependencies(kobuki_project_generate_messages_cpp _kobuki_project_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(kobuki_project_gencpp)
add_dependencies(kobuki_project_gencpp kobuki_project_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS kobuki_project_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(kobuki_project
  "/home/jay/catkin_ws/src/kobuki_project/msg/Status.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/kobuki_project
)

### Generating Services

### Generating Module File
_generate_module_eus(kobuki_project
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/kobuki_project
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(kobuki_project_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(kobuki_project_generate_messages kobuki_project_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/jay/catkin_ws/src/kobuki_project/msg/Status.msg" NAME_WE)
add_dependencies(kobuki_project_generate_messages_eus _kobuki_project_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(kobuki_project_geneus)
add_dependencies(kobuki_project_geneus kobuki_project_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS kobuki_project_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(kobuki_project
  "/home/jay/catkin_ws/src/kobuki_project/msg/Status.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/kobuki_project
)

### Generating Services

### Generating Module File
_generate_module_lisp(kobuki_project
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/kobuki_project
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(kobuki_project_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(kobuki_project_generate_messages kobuki_project_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/jay/catkin_ws/src/kobuki_project/msg/Status.msg" NAME_WE)
add_dependencies(kobuki_project_generate_messages_lisp _kobuki_project_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(kobuki_project_genlisp)
add_dependencies(kobuki_project_genlisp kobuki_project_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS kobuki_project_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(kobuki_project
  "/home/jay/catkin_ws/src/kobuki_project/msg/Status.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/kobuki_project
)

### Generating Services

### Generating Module File
_generate_module_nodejs(kobuki_project
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/kobuki_project
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(kobuki_project_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(kobuki_project_generate_messages kobuki_project_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/jay/catkin_ws/src/kobuki_project/msg/Status.msg" NAME_WE)
add_dependencies(kobuki_project_generate_messages_nodejs _kobuki_project_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(kobuki_project_gennodejs)
add_dependencies(kobuki_project_gennodejs kobuki_project_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS kobuki_project_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(kobuki_project
  "/home/jay/catkin_ws/src/kobuki_project/msg/Status.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/kobuki_project
)

### Generating Services

### Generating Module File
_generate_module_py(kobuki_project
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/kobuki_project
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(kobuki_project_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(kobuki_project_generate_messages kobuki_project_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/jay/catkin_ws/src/kobuki_project/msg/Status.msg" NAME_WE)
add_dependencies(kobuki_project_generate_messages_py _kobuki_project_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(kobuki_project_genpy)
add_dependencies(kobuki_project_genpy kobuki_project_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS kobuki_project_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/kobuki_project)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/kobuki_project
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(kobuki_project_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/kobuki_project)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/kobuki_project
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(kobuki_project_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/kobuki_project)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/kobuki_project
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(kobuki_project_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/kobuki_project)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/kobuki_project
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(kobuki_project_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/kobuki_project)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/kobuki_project\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/kobuki_project
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(kobuki_project_generate_messages_py std_msgs_generate_messages_py)
endif()
