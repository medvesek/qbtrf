
import winreg

def addRegistryEntry(keyConfig):
  with winreg.CreateKey(winreg.HKEY_CURRENT_USER, keyConfig["key"]) as key:
    winreg.SetValueEx(key, keyConfig["valueName"], 0, winreg.REG_SZ, keyConfig["value"])

def addRegistryEntries(keyConfigs):
  for keyConfig in keyConfigs:
    addRegistryEntry(keyConfig)