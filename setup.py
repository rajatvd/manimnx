from setuptools import *

LONG_DESC = """
An interface between `manim` and `networkx` to make animating graphs easier.
"""

setup(name='manimnx',
      version='0.1',
      description='Interface between `manim` and `networkx`',
      long_description=LONG_DESC,
      author='Rajat Vadiraj Dwaraknath',
      url='https://github.com/rajatvd/manim-nx',
      install_requires=['manimlib', 'networkx'],
      author_email='rajatvd@gmail.com',
      license='MIT',
      packages=find_packages(),
      zip_safe=False)
