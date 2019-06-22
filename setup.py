# -*- coding: utf-8 -*-
"""

"""

import os
import subprocess
from setuptools import setup, find_packages


# Change version number here, not in neurotic/version.py, which is generated
# by this script. Try to follow recommended versioning guidelines at semver.org.
MAJOR       = 0     # increment for backwards-incompatible changes
MINOR       = 2     # increment for backwards-compatible feature additions
MICRO       = 0     # increment for backwards-compatible bug fixes
IS_RELEASED = False # determines whether version will be marked as development
VERSION     = f'{MAJOR}.{MINOR}.{MICRO}'

# Try to fetch the git revision number from the .git directory if it exists.
if os.path.exists('.git'):
    try:
        out = subprocess.Popen(['git', 'rev-parse', 'HEAD'],
                               stdout=subprocess.PIPE).communicate()[0]
        GIT_REVISION = out.strip().decode('ascii')
    except OSError:
        GIT_REVISION = 'unknown'
# If the .git directory is absent (perhaps because this is a source distro),
# try to fetch the rev number from neurotic/version.py where it may have been
# stored during packaging.
elif os.path.exists('neurotic/version.py'):
    try:
        v = {}
        with open('neurotic/version.py', 'r') as f:
            exec(f.read(), v)
        GIT_REVISION = v['git_revision']
    except ImportError:
        raise ImportError('Unable to import git_revision. Try removing ' \
                          'neurotic/version.py and the build directory ' \
                          'before building.')
else:
    GIT_REVISION = 'unknown'

# If this is not a release version, mark it as a development build/distro and
# tag it with the git revision number.
if not IS_RELEASED:
    VERSION += '.dev0+' + GIT_REVISION[:7]

# Write the version string to a file that will be included with the
# build/distro. This makes the string accessible to the package via
# neurotic.__version__. The git revision is also written in case a source
# distro is being built, so that it can be fetched later during installation.
with open('neurotic/version.py', 'w') as f:
    try:
        f.write('"""THIS FILE WAS GENERATED BY SETUP.PY DURING BUILDING/PACKAGING"""\n')
        f.write(f'version = \'{VERSION}\'\n')
        f.write(f'git_revision = \'{GIT_REVISION}\'\n')
    finally:
        f.close()

# Read in the README to serve as the long_description, which will be presented
# on pypi.org as the project description.
with open('README.rst', 'r') as f:
    README = f.read()

install_requires = [
    # unreleased versions are needed so install from requirements.txt instead
    # TODO permanent fix?
    # 'av',
    # 'elephant>=0.6.2',
    # 'ephyviewer',  # TODO require latest
    # 'ipywidgets',
    # 'neo',         # TODO require >0.7.1 for AxographRawIO
    # 'numpy',
    # 'pandas',
    # 'pylttb',
    # 'pyqt5',
    # 'pyyaml',
    # 'quantities',
    # 'tqdm',
]

setup(
    name = 'neurotic',
    version = VERSION,
    description = 'Curate, visualize, and annotate your behavioral ephys data using Python',
    packages = find_packages(),
    package_data = {'neurotic': ['example/metadata.yml']},
    install_requires = install_requires,
    entry_points = {'console_scripts': ['neurotic=neurotic.scripts:launch_standalone']},
    long_description = README,
    author = 'Jeffrey Gill',
    author_email = 'jeffrey.p.gill@gmail.com',
    license = 'MIT',
    url = 'https://github.com/jpgill86/neurotic',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
    ],
)
