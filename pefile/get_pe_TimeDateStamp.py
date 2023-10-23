import datetime
import pefile
# PE file path
filename = 'aaa.Installer.x64.exe'
# read PE file
pe = pefile.PE(filename)
# get TimeDateStamp (int)
ts = int(pe.FILE_HEADER.dump_dict()['TimeDateStamp']['Value'].split()[0], 16)
# to UTC datetime
utc_time = datetime.datetime.utcfromtimestamp(ts)
print(utc_time.strftime("%Y-%m-%d %H:%M:%S +00:00 (UTC)"))
# output example: 2021-09-25 21:56:47 +00:00 (UTC)
