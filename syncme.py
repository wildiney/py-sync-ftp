""" SYNCING """
from sync_ftp import SyncFtp

SYNC = SyncFtp("", "", "")
SYNC.get_from_ftp("/Users/wildiney/Projetos/SyncFtp/syncfolder/", "syncfolder")
