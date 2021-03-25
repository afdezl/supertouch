from setuptools import setup

with open("README.md", 'r') as f:
    readme = f.read()

setup(
    name='supertouch',
    py_modules=['supertouch'],
    version="0.1.1",
    author_email="adrian@luengo.co",
    license="MIT",
    long_description=readme,
    long_description_content_type="text/markdown",
    python_requires=">3.6",
    description="Easily create files and folders.",
    entry_points={
        'console_scripts': ['st=supertouch.cli:main']
    }
)
