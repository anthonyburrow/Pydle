import setuptools
from setuptools import setup


setup(name='Pydle', version='0.1',
      description='Idle game.',
      url='https://github.com/anthonyburrow/Pydle',
      author='Anthony Burrow',
      packages=setuptools.find_packages(),
      include_package_data=True,
      install_requires=['numpy', 'keyboard'],
      )
