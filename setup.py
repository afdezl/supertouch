from setuptools import setup

setup(
    name='supertouch',
    py_modules=['supertouch'],
    version="0.1.0",
    author_email="adrian@luengo.co",
    license_files=("LICENSE.txt",),
    python_requires=">3.6",
    description="Easily create files and folders.",
    entry_points={
        'console_scripts': ['st=supertouch.cli:main']
    }
)
