
import subprocess

# subprocess.run(["cd", "Rust", "&&", "cargo", "run"])
subprocess.run("cargo build --release", cwd="Rust", shell=True)