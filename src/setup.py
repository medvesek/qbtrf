from src.lib.config import writeConfig
from src.lib.util import getCliToExecuteCurrentProgram
from src.lib.registry import addRegistryEntries
import getpass

def setup():
  print("Let's set up")
  url = input("URL: ")
  username = input("Username: ")
  password = getpass.getpass("Password: ")
  
  writeConfig({
    "url": url,
    "username": username,
    "password": password
  })

  makeAvailableToOpenTorrentFiles()
  makeDefaultForMagnetLinks()

def makeAvailableToOpenTorrentFiles():
  addRegistryEntries(registryEntriesForOpenWith())

def makeDefaultForMagnetLinks():
  addRegistryEntries(registryEntriesForMagnetLinks())

def registryEntriesForOpenWith():
  progId = "qbtrf.torrent"
  return [
    {
      "key": rf'Software\Classes\{progId}\shell\open\command',
      "valueName": "",
      "value": getExecCommand(),
    },
    {
      "key": r'Software\Classes\.torrent\OpenWithProgids',
      "valueName": progId,
      "value": "",
    }
  ]

def registryEntriesForMagnetLinks():
  return [
    {
      "key": r"Software\Classes\magnet'",
      "valueName": "URL Protocol",
      "value": "",
    },
    {
      "key": r'Software\Classes\magnet\shell\open\command',
      "valueName": "",
      "value": getExecCommand()
    }
  ]

def getExecCommand():
  return f'{getCliToExecuteCurrentProgram()} "%1"'


