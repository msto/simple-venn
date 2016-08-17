"""
Simple venn diagrams.
"""

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

setup(
    name='simple-venn',
    version='0.1.0',
    description='Simple venn diagrams',
    long_description=readme,
    author='Matthew Stone',
    author_email='matthew(dot)stone12(at)gmail.com',
    url='https://github.com/msto/simple-venn',
    license='MIT',
    packages=find_packages(exclude=['demo']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Visualization',
    ],
    keywords='venn diagram matplotlib',
    install_requires=['matplotlib'],
)
