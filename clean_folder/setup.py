from setuptools import setup, find_namespace_packages

setup(
    name="Упорядкування файлів",
    version="1.0",
    description="Пакет для упорядкування файлів у папці",
    author="Oksana Ustymenko",
    packages=find_namespace_packages(),
    include_package_data=True,
    install_requires=['pathlib', 'os', 'sys', 'shutil'],
    entry_points={'console_scripts': ['clean_folder=clean_folder.clean:main']}
)