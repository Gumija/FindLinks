# python all
import subprocess


def start():
    runCSharp()
    runPython()
    runRust()

def runCSharp():
    subprocess.run([r"dotnet", r".\C#\bin\Release\netcoreapp2.2\C#.dll"])

def runRust():
    subprocess.run([r".\Rust\target\release\Regex.exe"])

def runPython():
    subprocess.run(["python", r".\Python\xml.py"], shell=True)
    subprocess.run(["python", r".\Python\regex.py"], shell=True)

start()