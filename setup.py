#!/usr/bin/env python
import os
from distutils.core import setup

setup(name='ssm',
      version='0.9',
      description='Bayesian learning and inference for a variety of state space models',
      author='Scott Linderman',
      author_email='scott.linderman@stanford.edu',
      url='https://github.com/lindermanlab/ssm',
      install_requires=['numpy', 'scipy', 'matplotlib', 'scikit-learn', 'tqdm', 'seaborn', 'jax', 'jaxlib'],
      packages=['ssm', 'ssm.hmm'],
    )
