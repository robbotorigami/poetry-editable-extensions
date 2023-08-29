#include <pybind11/pybind11.h>

namespace py = pybind11;

void hello_world(){
    py::print("Hello world!");
}

PYBIND11_MODULE(moduleb, m){
    m.def("hello_world", &hello_world);
}
