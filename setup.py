from setuptools import setup

with open("README.md", 'r') as f:
    readme = f.read()

setup(
    name='supertouch',
    packages=['supertouch'],
    version="0.1.2",
    author_email="adrian@luengo.co",
    url="https://github.com/afdezl/supertouch",
    license="MIT",
    long_description=readme,
    long_description_content_type="text/markdown",
    python_requires=">3.6",
    description="Easily create files and folders.",
    entry_points={
        'console_scripts': ['st=supertouch.cli:main']
    }
)
