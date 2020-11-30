import os
import sys

def check_reboot():
    return os.path.exists("run/reboot-required")

def main():
    if check_reboot():
        print('pending reboot')
        sys.exit(1)
    print('Ok')
    sys.exit(1)

main()
main()
