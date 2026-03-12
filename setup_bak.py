<<<<<<< HEAD:setup_bak.py
=======
"""Installation script for the 'unitree_rl_mjlab' python package."""

>>>>>>> 4a734a83c8fd00727e2fb4764c6febc126145d40:setup.py
from setuptools import setup, find_packages

# Minimum dependencies required prior to installation
INSTALL_REQUIRES = [
    "mjlab>=1.1.0",
]

setup(
    name="unitree_rl_mjlab",
<<<<<<< HEAD:setup_bak.py
=======
    packages=["src"],
>>>>>>> 4a734a83c8fd00727e2fb4764c6febc126145d40:setup.py
    version="0.0.1",
    packages=find_packages(),  # ← ここが重要
    install_requires=INSTALL_REQUIRES,
)
