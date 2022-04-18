# SyncFtp

A synchronizer between a localfolder and a remote folder

## Example of use

If you want to always get files from ftp:

* Create file syncme.pyw and start the application with the code bellow changing the informations with your real info.

```python
from sync_ftp import SyncFtp

SYNC = SyncFtp("ftphost", "login", "password")
while True:
    SYNC.send_to_ftp("/locafolder/to/sync/", "remotefolder/to/sync")
    time.sleep(60 * 10) # 60 segundos * 10 = 10 minutos
```

Or a little bit smarter

```python
import time
import config
from sync_ftp import SyncFtp

syncronizing = input("Would you like to start your synchronization? (y/n): ")
if syncronizing == "y":
    SYNC = SyncFtp("ftphost", "login", "password")
    getorput = input("Should I get files from FTP or put files on FTP (g/p): ")
    if getorput == "g" or getorput=="get":
        SYNC.get_from_ftp("D:\\syncfolder", "/syncfolder/")
    if getorput == "p" or getorput=="put":
        continuous = input("Should I continue to syncing your files? (y/n): ")
        if continuous == "y":
            while True:
                SYNC.send_to_ftp("/locafolder/to/sync/", "remotefolder/to/sync")
                time.sleep(60 * 10)

```
