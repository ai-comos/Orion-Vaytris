cmake_minimum_required(VERSION 3.20)
project(AegisMasterEngine LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Hardware optimization flags: native instruction sets (AES-NI, AVX2), strict warnings
add_compile_options(-O3 -march=native -Wall -Wextra -pthread)

find_package(OpenSSL REQUIRED)
find_library(OQS_LIB NAMES oqs REQUIRED PATHS /usr/local/lib /usr/lib)
find_path(OQS_INCLUDE_DIR NAMES oqs/oqs.h PATHS /usr/local/include /usr/include)

add_executable(aegis_master_engine aegis_master_engine.cpp)
target_include_directories(aegis_master_engine PRIVATE ${OQS_INCLUDE_DIR})
target_link_libraries(aegis_master_engine PRIVATE
    OpenSSL::Crypto
    ${OQS_LIB}
    rt
    pthread
)