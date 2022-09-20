import time
import os
import red_ttp.common
import subprocess
import sys

DELAY = 3
testFileName = ''

def runTest(testFileName):
    print(testFileName)
    errors = []
    for ttp_file in red_ttp.get_ttp_list():
        if str(os.path.basename(ttp_file)) == testFileName:
            #print('found')
            #print(os.path.basename(ttp_file))
            #print(testFileName)
            print("---- %s ----" % os.path.basename(ttp_file))
            p = subprocess.Popen([sys.executable, ttp_file], shell=True)
            p.wait()
            code = p.returncode

            if p.returncode:
                errors.append((ttp_file, code))

            time.sleep(DELAY)
            print("")
            main()
    return len(errors)

def main():
    banner = """
    ██████╗ ██╗      █████╗  ██████╗██╗  ██╗    ██╗███╗   ██╗███╗   ██╗
    ██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝    ██║████╗  ██║████╗  ██║
    ██████╔╝██║     ███████║██║     █████╔╝     ██║██╔██╗ ██║██╔██╗ ██║
    ██╔══██╗██║     ██╔══██║██║     ██╔═██╗     ██║██║╚██╗██║██║╚██╗██║
    ██████╔╝███████╗██║  ██║╚██████╗██║  ██╗    ██║██║ ╚████║██║ ╚████║
    ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝
                                                                   """
    print(banner)

    while True:
        print('''
    Tactics
        
    1. Initial Access
    2. Execution
    3. Persistence
    4. Privilege
    5. Defense Evasion
    6. Credential Access
    7. Discovery
    8. Lateral Movement
    9. Collection
    10. Command & Control
        ''')

        choice1 = int(input(">> "))

        if choice1 == 1:
            print("No techniques are available")
            break

        if choice1 == 2:
            print("""
    Execution
    Choose a technique
            
    1. [T1053] At Command
    2. [T1053] Scheduled Task Privilege Escalation
    3. [T1064] Emulate Suspect MS Office Child Processes
    4. [T1047] Suspicious execution via WMI""")

            choice2 = int(input(">> "))

            if choice2 == 1:
                print("Running....At Command")
                testFileName = "at_command.py"
                runTest(testFileName)
                break

            if choice2 == 2:
                print("Running....Scheduled Task Privilege Escalation")
                testFileName = "schtask_escalation.py"
                runTest(testFileName)
                break

            if choice2 == 3:
                print("Running....Emulate Suspect MS Office Child Processes")
                testFileName = "suspicious_office_children.py"
                runTest(testFileName)
                break

            if choice2 == 4:
                print("Running....Suspicious execution via WMI")
                testFileName = "wmi_tool_execution.py"
                runTest(testFileName)
                break

        if choice1 == 3:
            print("""
    Persistence
    Choose a technique

    1. [T1053] At Command
    2. [T1136] Create User with net.exe
    3. [T1137] Office Application Startup
    4. [T1064] Persistent Scripts
    5. [T1015][T1103] Registry Persistence Creation
    6. [T1053] Scheduled Task Privilege Escalation
    7. [T1546] COM Hijack via Script Object
    8. [T1044] SYSTEM Escalation from User Directory""")

            choice2 = int(input(">> "))

            if choice2 == 1:
                print("Running....At Command")
                testFileName = "at_command.py"
                runTest(testFileName)
                break

            if choice2 == 2:
                print("Running....Create User with net.exe")
                testFileName = "net_user_add.py"
                runTest(testFileName)
                break

            if choice2 == 3:
                print("Running....Office Application Startup")
                testFileName = "office_application_startup.py"
                runTest(testFileName)
                break

            if choice2 == 4:
                print("Running....Persistent Scripts")
                testFileName = "persistent_scripts.py"
                runTest(testFileName)
                break

            if choice2 == 5:
                print("Running....Registry Persistence Creation")
                testFileName = "registry_persistence_create.py"
                runTest(testFileName)
                break

            if choice2 == 6:
                print("Running....Scheduled Task Privilege Escalation")
                testFileName = "schtask_escalation.py"
                runTest(testFileName)
                break

            if choice2 == 7:
                print("Running....COM Hijack via Script Object")
                testFileName = "scrobj_com_hijack.py"
                runTest(testFileName)
                break

            if choice2 == 8:
                print("Running....SYSTEM Escalation from User Directory")
                testFileName = "user_dir_escalation.py"
                runTest(testFileName)
                break

        if choice1 == 4:
            print("""
    Privilege Escalation
    Choose a technique

    1. [T1053] At Command
    2. [T1053] Scheduled Task Privilege Escalation
    3. [T1546] COM Hijack via Script Object
    4. [T1088] Bypass UAC via Event Viewer
    5. [T1088] Bypass UAC via Sdclt""")

            choice2 = int(input(">> "))

            if choice2 == 1:
                print("Running....At Command")
                testFileName = "at_command.py"
                runTest(testFileName)
                break

            if choice2 == 2:
                print("Running....Scheduled Task Privilege Escalation")
                testFileName = "schtask_escalation.py"
                runTest(testFileName)
                break

            if choice2 == 3:
                print("Running....COM Hijack via Script Object")
                testFileName = "scrobj_com_hijack.py"
                runTest(testFileName)
                break

            if choice2 == 4:
                print("Running....Bypass UAC via Event Viewer")
                testFileName = "uac_eventviewer.py"
                runTest(testFileName)
                break

            if choice2 == 5:
                print("Running....Bypass UAC via Sdclt")
                testFileName = "uac_sdclt.py"
                runTest(testFileName)
                break

        if choice1 == 5:
            print("""
    Defense Evasion
    Choose a technique

    1. [T1140] Certutil Encode/Decode
    2. [T1070] Catalog Deletion with wbadmin.exe
    3. [T1070] USN Journal Deletion with fsutil.exe
    4. [T1070] Volume Shadow Copy Deletion with vssadmin and wmic
    5. [T1089] Disable Windows Firewall
    6. [T1218] Network Traffic from InstallUtil
    7. [T1127] MsBuild with Network Activity
    8. [T1218] Microsoft HTA tool (mshta.exe) with Network Callback
    9. [T1218] MsiExec with HTTP Installer
    10. [T1127] msxsl.exe Network
    11. [T1140] Powershell with Suspicious Arguments
    12. [T1036] Executable with Unusual Extensions
    13. [T1036] Windows Core Process Masquerade
    14. [T1564] Run Process from the Recycle Bin
    15. [T1112] Export Registry Hives
    16. [T1218] RegSvr32 Backdoor with .sct Files
    17. [] SIP Provider Modification
    18. [T1116] Trust Provider Modification
    19. [T1088] Bypass UAC via Event Viewer
    20. [T1088] Bypass UAC via Sdclt
    21. [T1127] Unexpected Network Activity from Microsoft Tools
    22. [T1093] Invalid Process Trees in Windows
    23. [T1158] Processes in Unusual Paths
    24. [T1044] SYSTEM Escalation from User Directory
    25. [T1070] Clearing Windows Event Logs
    26. [T1158] Process Execution in System Restore""")

            choice2 = int(input(">> "))

            if choice2 == 1:
                print("Running....Certutil Encode/Decode")
                testFileName = "certutil_file_obfuscation.py"
                runTest(testFileName)
                break

            if choice2 == 2:
                print("Running....Catalog Deletion with wbadmin.exe")
                testFileName = "delete_catalogs.py"
                runTest(testFileName)
                break

            if choice2 == 3:
                print("Running....USN Journal Deletion with fsutil.exe")
                testFileName = "delete_usnjrnl.py"
                runTest(testFileName)
                break

            if choice2 == 4:
                print("Running....Volume Shadow Copy Deletion with vssadmin and wmic")
                testFileName = "delete_volume_shadow.py"
                runTest(testFileName)
                break

            if choice2 == 5:
                print("Running....Disable Windows Firewall")
                testFileName = "disable_windows_fw.py"
                runTest(testFileName)
                break

            if choice2 == 6:
                print("Running....Network Traffic from InstallUtil")
                testFileName = "installutil_network.py"
                runTest(testFileName)
                break

            if choice2 == 7:
                print("Running....MsBuild with Network Activity")
                testFileName = "msbuild_network.py"
                runTest(testFileName)
                break

            if choice2 == 8:
                print("Running....Microsoft HTA tool (mshta.exe) with Network Callback")
                testFileName = "mshta_network.py"
                runTest(testFileName)
                break

            if choice2 == 9:
                print("Running....MsiExec with HTTP Installer")
                testFileName = "msiexec_http_installer.py"
                runTest(testFileName)
                break

            if choice2 == 10:
                print("Running....MsBuild with Network Activity")
                testFileName = "msxsl_network.py"
                runTest(testFileName)
                break

            if choice2 == 11:
                print("Running....Powershell with Suspicious Arguments")
                testFileName = "powershell_args.py"
                runTest(testFileName)
                break

            if choice2 == 12:
                print("Running....Executable with Unusual Extensions")
                testFileName = "process_extension_anomalies.py"
                runTest(testFileName)
                break

            if choice2 == 13:
                print("Running....Windows Core Process Masquerade")
                testFileName = "process_name_masquerade.py"
                runTest(testFileName)
                break

            if choice2 == 14:
                print("Running....Run Process from the Recycle Bin")
                testFileName = "recycle_bin_process.py"
                runTest(testFileName)
                break

            if choice2 == 15:
                print("Running....Export Registry Hives")
                testFileName = "registry_hive_export.py"
                runTest(testFileName)
                break

            if choice2 == 16:
                print("Running....RegSvr32 Backdoor with .sct Files")
                testFileName = "regsvr32_scrobj.py"
                runTest(testFileName)
                break

            if choice2 == 17:
                print("Running....SIP Provider Modification")
                testFileName = "sip_provider.py"
                runTest(testFileName)
                break

            if choice2 == 18:
                print("Running....Trust Provider Modification")
                testFileName = "trust_provider.py"
                runTest(testFileName)
                break

            if choice2 == 19:
                print("Running....Bypass UAC via Event Viewer")
                testFileName = "uac_eventviewer.py"
                runTest(testFileName)
                break

            if choice2 == 20:
                print("Running....Bypass UAC via Sdclt")
                testFileName = "uac_sdclt.py"
                runTest(testFileName)
                break

            if choice2 == 21:
                print("Running....Unexpected Network Activity from Microsoft Tools")
                testFileName = "unusual_ms_tool_network.py"
                runTest(testFileName)
                break

            if choice2 == 22:
                print("Running....Invalid Process Trees in Windows")
                testFileName = "unusual_parent.py"
                runTest(testFileName)
                break

            if choice2 == 23:
                print("Running....Processes in Unusual Paths")
                testFileName = "unusual_process_path.py"
                runTest(testFileName)
                break

            if choice2 == 24:
                print("Running....SYSTEM Escalation from User Directory")
                testFileName = "user_dir_escalation.py"
                runTest(testFileName)
                break

            if choice2 == 25:
                print("Running....Clearing Windows Event Logs")
                testFileName = "wevutil_log_clear.py"
                runTest(testFileName)
                break

            if choice2 == 26:
                print("Running....Process Execution in System Restore")
                testFileName = "system_restore_process.py"
                runTest(testFileName)
                break

        if choice1 == 6:
            print("""
    Credential Access
    Choose a technique

    1. [T1081] Recursive Password Search""")

            choice2 = int(input(">> "))

            if choice2 == 1:
                print("Running....Recursive Password Search")
                testFileName = "findstr_pw_search.py"
                runTest(testFileName)
                break

        if choice1 == 7:
            print("""
    Discovery
    Choose a technique

    1. [T1069][T1077][T1082][T1087][T1124][T1135] Common Enumeration Commands""")

            choice2 = int(input(">> "))

            if choice2 == 1:
                print("Running....Common Enumeration Commands")
                testFileName = "enum_commands.py"
                runTest(testFileName)
                break

        if choice1 == 8:
            print("""
    Lateral Movement
    Choose a technique

    1. [T1021][T1047][T1077][T1124][T1126] Lateral Movement Commands""")

            choice2 = int(input(">> "))

            if choice2 == 1:
                print("Running....Lateral Movement Commands")
                testFileName = "lateral_commands.py"
                runTest(testFileName)
                break

        if choice1 == 9:
            print("""
    Collection
    Choose a technique

    1.  [T1115] Clipboard Data""")

            choice2 = int(input(">> "))

            if choice2 == 1:
                print("Running....Clipboard Data")
                testFileName = "get_clipboard.py"
                runTest(testFileName)
                break

        if choice1 == 10:
            print("""
    Command & Control
    Choose a technique

    1. [T1105] Downloading Files With Certutil
    2. [T1105] RunDll32 with .inf Callback
    3. [T1085] Rundll32 Loading by Ordinal""")

            choice2 = int(input(">> "))

            if choice2 == 1:
                print("Running....Downloading Files With Certutil")
                testFileName = "certutil_webrequest.py"
                runTest(testFileName)
                break

            if choice2 == 2:
                print("Running....RunDll32 with .inf Callback")
                testFileName = "rundll32_inf_callback.py"
                runTest(testFileName)
                break

            if choice2 == 3:
                print("Running....Rundll32 Loading by Ordinal")
                testFileName = "rundll32_ordinal.py"
                runTest(testFileName)
                break


if __name__ == "__main__":
    exit(main())
