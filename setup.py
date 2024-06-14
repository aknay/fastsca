from setuptools import setup, find_packages

setup(
    name='fastsca',
    version='0.0.1',
    description='fastsca',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/aknay/fastsca',
    author='Nay Aung Kyaw',
    author_email='aknay@outlook.com',
    license='GPLv3',
    packages=find_packages(),
    install_requires=[
        "numpy",
        "h5py",
        "matplotlib",
    ],
    extras_require={
        'dev': [
            'pytest',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
