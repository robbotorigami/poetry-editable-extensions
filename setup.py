# -*- coding: utf-8 -*-
from setuptools import setup
from pathlib import Path
from pybind11.setup_helpers import Pybind11Extension, build_ext

package_dir = \
{'': 'src'}

packages = \
['example']

package_data = \
{'': ['*'], 'example': ['moduleb_src/*']}

install_requires = \
['pybind11==2.10.4']

moduleb_ext = Pybind11Extension('example.moduleb',
                                sources=[str(Path('src/example/moduleb_src/bindings.cpp'))])

setup_kwargs = {
    'name': 'poetry-editable-extensions',
    'version': '0.1.0',
    'description': '',
    'long_description': 'None',
    'author': 'Robert Belter',
    'author_email': 'robertjohnbelter@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
    'cmdclass': {'build_ext': build_ext},
    'ext_modules': [moduleb_ext],
}

setup(**setup_kwargs)
