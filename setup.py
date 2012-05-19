try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='riak_statsd',
    version='0.0.1',
    description='Transport proxy for instrumenting Riak clients',
    author='Andrea Luzzardi',
    author_email='andrea@luzzardi.com',
    url='https://github.com/aluzzardi/riak-statsd-python',
    packages=['riak_statsd'],
    install_requires=[
            'statsd>=0.5.1',
            'riak>=1.3.0'
    ],
    license='MIT'
)
