version = input().split(".")
print(version)

new = int("".join(version))
print(new)
new_version = int(new + 1)

print(".".join(str(new_version)))