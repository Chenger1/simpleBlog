from setuptools import setup

setup(
    name='blogApp',
    packages=['blog_app'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'pytest'
    ]
)