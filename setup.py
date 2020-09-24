import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="telegos",
    version="0.0.1",
    author="4ippers",
    author_email="example@example.com",
    description="telegos models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="github.com/4ippers/teletos",
    package_dir={'models': 'telegos/models',
                 'task': 'telegos/task',
                 },
    packages=['models', 'task.core', 'task.module'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)