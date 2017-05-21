from setuptools import setup, find_packages

setup(
    name='Sigillum',
    version=0.1,
    packages=find_packages(),
    include_package_data=True,
    py_modules=['Sigillum'],
    install_requires=[
        'Click',
    ],
    entry_points='''
    [console_scripts]
    Sigillum = sigillum:cli
    ''', )
