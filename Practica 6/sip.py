import nmap
import base64
nm = nmap.PortScanner()
hostnum = "192.168.100.9"
nm.scan(hosts=str(hostnum)+'/24', arguments='-n -sP -PE -PA21,23,80,3389')
hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
a = []
b = []
def iphostss():
	for host in nm.all_hosts():
		print('----------------------------------------------------')
		print('Host : %s (%s)' % (host, nm[host].hostname()))
		a.append('Host : %s (%s)' % (host, nm[host].hostname()))
		print('State : %s' % nm[host].state())
		b.append('State : %s' % nm[host].state())

filename = "sips.txt"
outfile = open(filename, 'w')
iphostss()
print("--------")
m=0



for n in a:
	outfile.write(str(a[m])+"\n")
	outfile.write(str(b[m])+"\n")
	m=m+1

outfile.close()

with open('sips.txt') as f:
    lines = f.readlines()

sample_string = str(lines)
sample_string_bytes = sample_string.encode("ascii")
  
base64_bytes = base64.b64encode(sample_string_bytes)
base64_string = base64_bytes.decode("ascii")
  
#print(f"Encoded string: {base64_string}")

outfile = open(filename, 'w')
outfile.write(base64_string)
outfile.close()
