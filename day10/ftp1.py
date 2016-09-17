#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"

import ftplib
import os
import socket
HOST = 'ftp.mozilla.org'
DIRN = 'pbu/mozilla.org/webtools'
FILE = 'bugzilla-LATEST.tar.gz'

def main():
    try:
        f = ftplib.FTP(HOST)
    except (socket.error,socket.gaierror) as e:
        print('ERROR:cannot reach "%s"' %HOST)
        return
    print('***Connected to host "%s"***' %HOST)

    try:
        f.login()
    except ftplib.error_perm:
        print('ERROR:cannot login anonymously')
        f.quit()
        return
    print("***Logged in as anonymous")

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print('ERROR:cannot CD  to "%s"' %DIRN)
        f.quit()
        return
    try:
        f.retrbinary('RETR %s' %FILE,open(FILE,'wb').write())
    except ftplib.error_perm:
        print('ERROR:cannot read file "%s"' %FILE)
        os.unlink(FILE)
    else:
        print('Downloaded "%s" to CWD' %FILE)
    f.quit()

if __name__ == '__main__':
    main()