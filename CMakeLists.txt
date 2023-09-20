cmake_minimum_required(VERSION 3.25)
project(AutoFrac)

set(CMAKE_CXX_STANDARD 17)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

set(CMAKE_PREFIX_PATH "$ENV{QT_PATH}")

find_package(Qt6 REQUIRED COMPONENTS Core Gui Widgets OpenGLWidgets Charts)
find_package(OpenCV REQUIRED COMPONENTS core highgui imgcodecs imgproc features2d calib3d)

qt_standard_project_setup()

file(GLOB_RECURSE FILES "src/*.cpp")

# add mainwindow.h file because Qt is weird
add_executable(AutoFrac ${FILES} include/gui/mainwindow.h include/gui/glview.h)

target_include_directories(AutoFrac PUBLIC include)
target_include_directories(AutoFrac PUBLIC vendor/NazaraUtils/include)
target_include_directories(AutoFrac PUBLIC ${OpenCV_INCLUDE_DIRS})

target_link_libraries(AutoFrac PRIVATE Qt6::Core)
target_link_libraries(AutoFrac PRIVATE Qt6::Gui)
target_link_libraries(AutoFrac PRIVATE Qt6::Widgets)
target_link_libraries(AutoFrac PRIVATE Qt6::OpenGLWidgets)
target_link_libraries(AutoFrac PRIVATE Qt6::Charts)

target_link_libraries(AutoFrac PRIVATE ${OpenCV_LIBS})

target_compile_options(AutoFrac PRIVATE -Wall -Wextra -Wpedantic -Werror)
