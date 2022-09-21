from setuptools import setup

setup(
  install_requires=[
    'tensorflow==2.1.0'
  ],
)

import tensorflow as tf
tf.strings.substr(input='abc', len=1, pos=[1,2])
