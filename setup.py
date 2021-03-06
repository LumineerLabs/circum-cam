from setuptools import setup, find_packages
from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='circum-cam',
    version_format='{tag}',
    author="Lane Haury",
    author_email="lane@lumineerlabs.com",
    description="Webcam + ML sensor plugin for circum.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/LumineerLabs/circum-cam",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        'circum',
        'click',
        'setuptools',
        'setuptools-git-version'
    ],
    entry_points={
        'circum.sensors': [
            'cam=circum_cam.cam:webcam_command'
        ]
    },
    extras_require={
        'lint': [
            'flake8',
            'flake8-import-order',
            'flake8-builtins',
            'flake8-comprehensions',
            'flake8-bandit',
            'flake8-bugbear',
        ]
    }
)
