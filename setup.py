import io
import os

from setuptools import setup


setup(
    name='soft-asserts',
    version='1.0.0',
    description='Soft assertions for Python/Pytest',
    long_description=io.open(os.path.join(os.path.dirname('__file__'), 'README.md'), encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='pashkatrick',
    url='https://github.com/balalaiQA/soft-asserts',
    packages=['soft_asserts']
)
