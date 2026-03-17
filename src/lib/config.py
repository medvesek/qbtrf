import configparser
import os
from src.lib.util import programRootDir

def readConfig():
  config = configparser.ConfigParser()
  config.read(configFilePath())
  return config["DEFAULT"]

def writeConfig(data):
  config = configparser.ConfigParser()
  config["DEFAULT"] = data
  with open(configFilePath(), "w") as configFile:
    config.write(configFile)

def configExists():
  return os.path.exists(configFilePath())

def configFilePath():
  return programRootDir("config.ini")
