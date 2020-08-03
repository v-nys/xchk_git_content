# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xchk_git_content', 'xchk_git_content.migrations']

package_data = \
{'': ['*'],
 'xchk_git_content': ['static/images/*', 'templates/xchk_git_content/*']}

install_requires = \
[]

setup_kwargs = {
    'name': 'xchk-git-content',
    'version': '0.1.8',
    'description': 'Course material related to Git for the xchk teaching framework',
    'long_description': None,
    'author': 'Vincent Nys',
    'author_email': 'vincentnys@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'dependency_links': ['http://github.com/v-nys/xchk_regex_strategies/tarball/develop#egg=xchk-regex-strategies'],
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
