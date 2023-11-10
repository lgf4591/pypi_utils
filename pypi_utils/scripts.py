import os
import subprocess


def dev():
    cmd = "python main.py"
    subprocess.run(cmd, shell=True, check=True)


def pylint():
    # cmd = "pylint $(git ls-files '*.py')"
    # cmd = "pylint **/**/*.py --disable=missing-docstring"
    # cmd = "pylint --rcfile=pylint.conf ./pypi_template/**/*.py ./tests/**/*.py main.py"
    # cmd = "pylint ./pypi_template/**/*.py ./tests/**/*.py main.py"
    cmd = "pylint **/**/*.py"
    subprocess.run(cmd, shell=True, check=True)


def fix():
    # cmd = "autopep8 --in-place --aggressive --aggressive **/**/*.py"
    # cmd = "yapf -ir main.py ./pypi_utils ./tests"
    package_folder = os.path.basename(
        os.path.dirname(os.path.abspath(__file__)))
    cmd = f"yapf -ir main.py ./tests ./{package_folder}"
    subprocess.run(cmd, shell=True, check=True)


if __name__ == "__main__":
    print("scripts module",
          os.path.basename(os.path.dirname(os.path.abspath(__file__))))
