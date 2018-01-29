""" CLASS TO SYNC LOCAL FOLDER AND FTP FOLDER """
import os
import platform
import ftputil


class SyncFtp:
    """ MAIN CLASS """

    def __init__(self, host, login, password):
        self.host = host
        self.login = login
        self.password = password
        self.localfolder = "./"
        self.remotefolder = "./"
        self.label = 15
        self.path = 50

    def get_from_ftp(self, localfolder, remotefolder):
        """
        get_from_ftp
            :param self:
            :param localfolder:
            :param remotefolder:
        """
        print("[ FTP -> LOCAL".ljust(self.label, " ") + " ]")
        self.localfolder = localfolder
        self.remotefolder = remotefolder
        os.chdir(self.localfolder)
        with ftputil.FTPHost(self.host, self.login, self.password) as ftp_host:
            ftp_host.synchronize_times()
            ftp_host.chdir(self.remotefolder)
            print("[ PLATFORM ".ljust(self.label, " ") + " ]  " + platform.system())
            for root, dirs, files in ftp_host.walk("./"):
                for d in dirs:
                    try:
                        if platform.system() == "Windows":
                            newdir = os.path.join(root, d).replace("\\", "/")
                        else:
                            newdir = os.path.join(root, d)
                        if os.path.isdir(newdir) is True:
                            print("[ Directory".ljust(self.label, " ") + " ]  " +
                                  newdir.ljust(self.path, " ") + " already exists")
                        else:
                            os.mkdir(os.path.join(root, d))
                            print("[ Directory".ljust(self.label, " ") + " ]  " +
                                  newdir.ljust(self.path, " ") + " was created")
                    except Exception as exc:
                        print(exc)
                        print("Error Creating directory " + newdir)

                for name in files:
                    if platform.system() == "Windows":
                        newfile = os.path.join(root, name).replace("\\", "/")
                    else:
                        newfile = os.path.join(root, name)

                    try:
                        downloaded = ftp_host.download_if_newer(
                            newfile, newfile)
                        if downloaded is True:
                            print("[ File".ljust(self.label, " ") + " ]  " +
                                  newfile.ljust(self.path, " ") + " was updated")
                        else:
                            print("[ File".ljust(self.label, " ") + " ]  " +
                                  newfile.ljust(self.path, " ") + " is up-to-date")
                    except Exception as exc:
                        print(exc)
                        print("Error downloading file " + newfile)

    def send_to_ftp(self, localfolder, remotefolder):
        """
        send_to_ftp
            :param self:
            :param localfolder:
            :param remotefolder:
        """
        print("[ LOCAL -> FTP".ljust(self.label, " ") + " ]")
        self.localfolder = localfolder
        self.remotefolder = remotefolder
        os.chdir(self.localfolder)
        with ftputil.FTPHost(self.host, self.login, self.password) as ftp_host:
            ftp_host.synchronize_times()
            ftp_host.chdir(self.remotefolder)
            print("[ PLATFORM ".ljust(self.label, " ") + " ]  " + platform.system())
            for root, dirs, files in os.walk("./"):
                for d in dirs:
                    if platform.system() == "Windows":
                        newdir = os.path.join(root, d).replace("\\", "/")
                    else:
                        newdir = os.path.join(root, d)
                    try:
                        if ftp_host.path.isdir(newdir):
                            print("[ Directory".ljust(self.label, " ") + " ]  " +
                                  newdir.ljust(self.path, " ") + " already exists")
                        else:
                            ftp_host.mkdir(newdir)
                            print("[ Directory".ljust(self.label, " ") + " ]  " +
                                  newdir.ljust(self.path, " ") + " was created")
                    except ftputil.error.FTPError as exc:
                        print(exc)
                        print("Error Creating directory " + newdir)

                for file in files:
                    if platform.system() == "Windows":
                        newfile = os.path.join(root, file).replace("\\", "/")
                    else:
                        newfile = os.path.join(root, file)
                    try:
                        uploaded = ftp_host.upload_if_newer(newfile, newfile)
                        if uploaded is True:
                            print("[ File".ljust(self.label, " ") + " ]  " +
                                  newfile.ljust(self.path, " ") + " was updated")
                        else:
                            print("[ File".ljust(self.label, " ") + " ]  " +
                                  newfile.ljust(self.path, " ") + " is up-to-date")
                    except ftputil.error.FTPError as exc:
                        print(exc)
                        print("Error at sending file " + newfile)
