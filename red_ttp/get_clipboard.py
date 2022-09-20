# Name: Clipboard Data
# RTA: get_clipboard.py
# ATT&CK: T1115
# Description: Adversaries may collect data stored in the clipboard from users copying information within or between applications

import os
import common
import base64


def encode(command):
    return base64.b64encode(command.encode('utf-16le')).decode()


def main():
    common.log("Getting Clipboard Data")


    powershell_commands = [
        'powershell.exe Get-Clipboard'
    ]

    for command in powershell_commands:
        common.execute(command)



if __name__ == "__main__":
    exit(main())