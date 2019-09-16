# python all
import subprocess


def start():
    runPython()
    runRust()

def runRust():
    subprocess.run([r".\Rust\target\release\Regex.exe"])

def runPython():
    subprocess.run(["python", r".\Python\xml.py"], shell=True)
    subprocess.run(["python", r".\Python\regex.py"], shell=True)

start()