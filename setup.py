from setuptools import find_packages, setup

setup(
    name="ANN Churn Classification",
    version="0.0.1",
    author="Muhammad Usman Akram",
    author_email="m.usman.akram021@gmail.com",
    intall_requires=[
        "tensorflow",
        "pandas",
        "numpy",
        "scikit-learn",
        "tensorboard",
        "streamlit"
    ],
    packages=find_packages()
)