#Building EigenSolver---------------------------------------------------------------------
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/SuPyMode/Binary)
pybind11_add_module(CppSolver MODULE SuPyMode/Cpp/EigenSolver.cpp )
target_link_libraries(CppSolver PRIVATE ${PYTHON_LIBRARIES})
set_target_properties(CppSolver PROPERTIES POSITION_INDEPENDENT_CODE TRUE)
set_target_properties(CppSolver PROPERTIES CXX_STANDARD 17)
set_target_properties(CppSolver PROPERTIES OUTPUT_NAME "CppSolver")
target_compile_options (CppSolver PRIVATE -O3)


#Building SuperModes---------------------------------------------------------------------
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/SuPyMode/Binary)
pybind11_add_module(SuperMode MODULE SuPyMode/Cpp/SuperMode.cpp )
target_link_libraries(SuperMode PRIVATE ${PYTHON_LIBRARIES})
set_target_properties(SuperMode PROPERTIES POSITION_INDEPENDENT_CODE TRUE)
set_target_properties(SuperMode PROPERTIES CXX_STANDARD 17)
set_target_properties(SuperMode PROPERTIES OUTPUT_NAME "SuperMode")
target_compile_options (SuperMode PRIVATE -O3)



