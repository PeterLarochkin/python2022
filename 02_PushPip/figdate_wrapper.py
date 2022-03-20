from venv import create
from tempfile import mkdtemp
from subprocess import run, DEVNULL
from shutil import rmtree
import argparse


if __name__ == "__main__":
    temp_dir = mkdtemp()
    parser = argparse.ArgumentParser()
    parser.add_argument("-format", default="%Y %d %b, %A", type=str)
    parser.add_argument("-font", default="graceful", type=str)
    args = parser.parse_args()
    create(temp_dir, clear=True, with_pip=True)
    run([temp_dir+"/bin/pip3", "install", "pyfiglet"], stdout=DEVNULL)
    run([temp_dir+"/bin/python3", "-m", "figdate", "-format", args.format, "-font", args.font])
    rmtree(temp_dir)