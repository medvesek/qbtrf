import requests
import urllib

class QBittorrent:
  def __init__(self, baseUrl, username, password):
    self.baseUrl = baseUrl
    self.username = username
    self.password = password
    self.session = requests.Session()

  def addTorrent(self, torrentFilePath):
    url = self.url("/api/v2/torrents/add")
    if self.isMagnetLink(torrentFilePath):
      return self.session.post(url, data={
        "urls": torrentFilePath
      })
    
    with open(torrentFilePath, "rb") as file:
      files = {
        "torrents": file
      }
      return self.session.post(url, files=files)

  def login(self):
    self.session.post(self.url("/api/v2/auth/login"), {
      "username": self.username,
      "password": self.password,
    })

  def isMagnetLink(self, string):
    return string.startswith("magnet:")

  def url(self, path):
    return urllib.parse.urljoin(self.baseUrl, path)
