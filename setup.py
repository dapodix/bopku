import os
from setuptools import setup, find_packages

__version__ = ""
packages = find_packages(exclude=["tests*"])

fn = os.path.join("bopku", "version.py")
with open(fn) as fh:
    code = compile(fh.read(), fn, "exec")
    exec(code)

setup(
    name="bopku",
    version=__version__,
    author="hexatester",
    license="GPLv3",
    url="https://github.com/dapodix/bopku",
    keywords="boppaud bop bopku kemdikbud",
    description="Alat bantu administrasi BOP (Bantuan Operasional) Paud.",
    packages=packages,
    install_requires=["python", "SQLAlchemy", "alembic", "dacite"],
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Education",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    entry_points={"console_scripts": ["bopku=bopku.main:main"]},
)
