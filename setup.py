import setuptools


def load_requirements(filename="requirements.txt"):
    with open(filename, "r") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="micrograduate",
    version="0.1.0",
    author="Christos Karaneen",
    author_email="ckarageorgkaneen@gmail.com",
    description="A self-contained course to learn the basics of neural networks.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ckarageorgkaneen/micrograduate",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.6",
    install_requires=load_requirements(),
)
