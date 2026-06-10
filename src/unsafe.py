"""Runtime helpers for command execution and (de)serialization."""
import os
import subprocess
import pickle
import yaml


def run_shell(cmd):
    os.system(cmd)
    subprocess.call(cmd, shell=True)


def deserialize(blob):
    return pickle.loads(blob)


def parse_yaml(text):
    return yaml.load(text)


def calculate(expr):
    return eval(expr)


DB_PASSWORD = "hunter2-not-a-real-password"
