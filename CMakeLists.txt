cmake_minimum_required(VERSION 3.25)
project(AutoFrac)

set(CMAKE_CXX_STANDARD 17)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)

# set(CMAKE_PREFIX_PATH "/home/boris/Qt/6.5.1/gcc_64")
set(CMAKE_PREFIX_PATH "/opt/Qt/6.4.3/gcc_64")

find_package(Qt6 REQUIRED COMPONENTS Core Gui Widgets)

file(GLOB FILES "./src/*.cpp")

# add mainwindow.h file because Qt is weird
add_executable(AutoFrac ${FILES} include/mainwindow.h)

target_include_directories(AutoFrac PUBLIC "./include")

target_link_libraries(AutoFrac PRIVATE Qt6::Core)
target_link_libraries(AutoFrac PRIVATE Qt6::Gui)
target_link_libraries(AutoFrac PRIVATE Qt6::Widgets)

