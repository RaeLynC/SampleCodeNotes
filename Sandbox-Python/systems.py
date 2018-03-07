from sys import platform
from platform import architecture

if __name__ == '__main__':
    arch, plat = architecture()
    print(platform)
    print(arch)
    print(plat)
