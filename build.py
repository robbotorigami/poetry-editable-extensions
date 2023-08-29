from pathlib import Path
from pybind11.setup_helpers import Pybind11Extension, build_ext


def build(setup_kwargs):
    moduleb_ext = Pybind11Extension('example.moduleb',
                                    sources=[str(Path('src/example/moduleb_src/bindings.cpp'))])

    setup_kwargs.update({
        'cmdclass': {'build_ext': build_ext},
        'ext_modules': [moduleb_ext],
    })
