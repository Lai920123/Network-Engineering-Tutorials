from nornir import InitNornir

nr = InitNornir(config_file="config.yaml")

print(nr.inventory.hosts)
print(nr.inventory.groups)
