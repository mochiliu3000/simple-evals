from setuptools import setup, find_packages

setup(
    name="simple_evals",
    version="0.1.0",
    packages=find_packages(include=["simple_evals*"]),
    install_requires=[
        "openai",
        "anthropic",
        "numpy",
        "pandas",
        "scipy",
        "tqdm",
        "jinja2",
        "requests",
        "blobfile",
        "human_eval",
    ],
)