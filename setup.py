import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="micrograduate",
    version="0.1.0",
    author="Christos Karaneen",
    author_email="ckaraneen@gmail.com",
    description="Learn about neural networks, from backprop to GPT.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ckarageorgkaneen/micrograduate",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
