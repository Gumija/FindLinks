
import subprocess
from pip._internal import main as pip

pip(['install', 'selectolax'])
pip(['install', 'lxml'])

subprocess.run("cargo build --release", cwd="Rust", shell=True)
subprocess.run("dotnet build -c Release", cwd="C#", shell=True)