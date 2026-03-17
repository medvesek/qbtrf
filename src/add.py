from src.lib.config import readConfig
from src.lib.qbittorrent import QBittorrent

def addTorrent(torrentFilePath):
  config = readConfig()
  client = QBittorrent(
    baseUrl=config["url"],
    username=config["username"],
    password=config["password"]
  )
  client.login()
  client.addTorrent(torrentFilePath)
