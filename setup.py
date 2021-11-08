from setuptools import setup, find_packages

setup(
    name='cis301',
    version='0.1.0',
    license='MIT',
    description='CIS301 Class Projects',
    author='Ali Sazegar',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=['pytest-runner', 'pytest','Flask', 'requests', 'flask-bootstrap'],
    entry_points={
        'console_scripts': [
            'project4= cis301.project4.__main__:main',
        ]
    },
)
