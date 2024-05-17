cmake_minimum_required(VERSION 3.25)
project(AutoFrac)

set(CMAKE_CXX_STANDARD 17)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

set(CMAKE_PREFIX_PATH "$ENV{QT_PATH}")

find_package(Qt6 REQUIRED COMPONENTS Core Gui Widgets OpenGLWidgets Charts)
find_package(OpenCV REQUIRED COMPONENTS core highgui imgcodecs imgproc features2d calib3d)

file(GLOB_RECURSE FILES "src/*.cpp")
file(GLOB_RECURSE WINDOWS "include/gui/*window.h" "include/gui/glview.h")

# add *window.h files for the ui
add_executable(AutoFrac ${FILES} ${WINDOWS})

target_include_directories(AutoFrac PUBLIC include vendor/NazaraUtils/include ${OpenCV_INCLUDE_DIRS} vendor/gudhi.3.9.0/include)

target_link_libraries(AutoFrac PRIVATE Qt6::Core Qt6::Gui Qt6::Widgets Qt6::OpenGLWidgets Qt6::Charts ${OpenCV_LIBS} gmp gmpxx)

target_compile_options(AutoFrac PRIVATE -Wall -Wextra -Werror)
