""" CLASS TO SYNC LOCAL FOLDER AND FTP FOLDER """
import os
import ftputil


class SyncFtp:
    """ MAIN CLASS """

    def __init__(self, host, login, password):
        self.host = host
        self.login = login
        self.password = password
        self.localfolder = "./"
        self.remotefolder = "./"

    def get_from_ftp(self, localfolder, remotefolder):
        """
        get_from_ftp
            :param self:
            :param localfolder:
            :param remotefolder:
        """
        self.localfolder = localfolder
        self.remotefolder = remotefolder
        os.chdir(self.localfolder)
        with ftputil.FTPHost(self.host, self.login, self.password) as ftp_host:
            ftp_host.synchronize_times()
            ftp_host.chdir(self.remotefolder)
            for root, dirs, files in ftp_host.walk("./"):
                for d in dirs:
                    try:
                        os.mkdir(os.path.join(root, d))
                        print("Creating directory " + os.path.join(root, d))
                    except:
                        pass

                for name in files:
                    try:
                        print("RECEBENDO O ARQUIVO: " +
                              os.path.join(root, name))
                        ftp_host.download_if_newer(os.path.join(
                            root, name), os.path.join(root, name))
                    except:
                        pass

    def send_to_ftp(self, localfolder, remotefolder):
        """
        send_to_ftp
            :param self:
            :param localfolder:
            :param remotefolder:
        """
        self.localfolder = localfolder
        self.remotefolder = remotefolder
        os.chdir(self.localfolder)
        with ftputil.FTPHost(self.host, self.login, self.password) as ftp_host:
            ftp_host.synchronize_times()
            ftp_host.chdir(self.remotefolder)
            for root, dirs, files in os.walk("./"):
                for d in dirs:
                    try:
                        ftp_host.mkdir(os.path.join(root, d))
                        print("Creating directory " + os.path.join(root, d))
                    except:
                        pass

                for file in files:
                    try:
                        ftp_host.upload_if_newer(os.path.join(
                            root, file), os.path.join(root, file))
                        print("ARQUIVO ENVIADO: "+os.path.join(root, file))
                    except:
                        print("ERRO AO ENVIAR O ARQUIVO " +
                              os.path.join(root, file))
