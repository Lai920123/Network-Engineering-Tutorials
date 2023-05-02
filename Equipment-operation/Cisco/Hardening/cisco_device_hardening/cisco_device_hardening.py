from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
import textfsm
import re

def check_cisco_security_config(task):
    cmd = "show running-config"
    result = task.run(task=netmiko_send_command, command_string=cmd)
    print(result)


def main():
    nr = InitNornir(config_file="config.yaml")
    results = nr.run(task=check_cisco_security_config)

if __name__ == "__main__":
    check_cisco_security_config()