import os.path
import datetime
import socket
import subprocess

host = "www.flemingcollege.ca"

ping = subprocess.Popen(
    ["ping", "-c", "4", host],
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE
)

out, error = ping.communicate()
print(host)


save_path = 'c:/temp/'
file_name = ("lab4")
save_as = os.path.join(save_path, file_name+".txt")
dt = datetime.datetime.now()
hostname =socket.gethostname()
ip = socket.gethostbyname(hostname)






fh = open(save_as, "w")
timestamp = (dt.strftime("%Y-%m-%d %H:%M:%S\n"))
ipaddress = (ip)
fh.write('"hacked" -finally\n')
fh.write(timestamp)
fh.write(ipaddress)



fh.close()
