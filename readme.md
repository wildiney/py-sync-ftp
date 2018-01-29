#SyncFtp
## A syncronizer between a localfolder and a remote folder

Example of use
* Create file syncme.pyw and start the application with the code bellow changing the informations with your real info.

```python
from sync_ftp import SyncFtp

SYNC = SyncFtp("ftphost", "login", "password")
SYNC.get_from_ftp("/locafolder/to/sync/", "remotefolder/to/sync")
```

