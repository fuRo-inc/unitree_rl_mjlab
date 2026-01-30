from setuptools import setup, find_packages

# Minimum dependencies required prior to installation
INSTALL_REQUIRES = [
    "prettytable",
    "tqdm",
    "tyro>=1.0.1",
    "torch>=2.7.0",
    "torchrunx>=0.3.4",
    "warp-lang>=1.11.0.dev20251211",
    "mujoco-warp",
    "mujoco>=3.4.0",
    "trimesh>=4.8.3",
    "viser>=1.0.16",
    "moviepy",
    "tensordict",
    "rsl-rl-lib==3.1.0",
    "tensorboard>=2.20.0",
    "onnxscript>=0.5.4",
    "wandb>=0.22.3",
]

setup(
    name="unitree_rl_mjlab",
    version="0.0.1",
    packages=find_packages(),  # ← ここが重要
    install_requires=INSTALL_REQUIRES,
)
