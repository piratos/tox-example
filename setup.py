import setuptools


install_requires = [
    "Jinja2",
]

setuptools.setup(
    name="stringz",
    version="1.0",
    description="Best string library ever. Seriously.",

    packages=setuptools.find_packages(),
    include_package_data=True,

    install_requires=install_requires,
)
