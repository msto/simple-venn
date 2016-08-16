"""
Simple venn diagrams.
"""

from setuptools import setup, find_packages

setup(
    name='simple-venn',
    version='0.1',
    description='Simple venn diagrams',
    long_description='',
    url='https://github.com/msto/simple-venn',
    license='MIT',
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
