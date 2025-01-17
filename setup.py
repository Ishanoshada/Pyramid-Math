from setuptools import setup, find_packages

setup(
    name='pyramid_math',
    version='0.0.3',
    packages=find_packages(),
    install_requires=['numpy'],
    author='Ishan Oshada',
    author_email='ishan.kodithuwakku.official@email.com',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    description='A package for performing mathematical calculations on pyramids.',
    url='https://github.com/ishanoshada/pyramid-math',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)