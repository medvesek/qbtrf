# qbtrf

## qBittorrent remote forwader

This utlility will forward opened torrents to a remote qbittorrent instalation.

For example if you have qbittorent running on your NAS and want to add torrents from your local machine, instead of manually adding them through the web ui, you can simply set qbtrf.exe as the default application for your torrents and it will automatically send any opened torrent file directly to your remote qbittorrent. Also works for magnet links.

Windows only.

### How to use

1. Download .exe or compile it yourself
2. Put it anywhere you want and run it - this will trigger setup. You will be prompted to enter:
   - **URL**: the url of the qbittorent web ui
   - **Username**: username for the web ui
   - **Password**: password for the web ui
3. As part of the setup qbtrf will also register itself as the default app to open magnet links
4. All that is left to do is to set qbtrf.exe as the default app for torrents. You can do this either by right clicking a .torrent file and open with or by using windows settings -> default apps.
