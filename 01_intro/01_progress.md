



Creating new VM in Oracle [VirtualBox v.5.2.22](https://www.virtualbox.org/wiki/VirtualBox) from the command line on Windows Host:

```
> cd C:\Program Files\Oracle\VirtualBox
> VBoxManage createvm --name Debian --ostype Debian_64 --register`
> VBoxManage modifyvm Debian --memory 2048 --vram 32 --cpus 2`
> VBoxManage createmedium --filename "C:\Users\<user_name>\VirtualBox VMs\Debian\Debian.vdi" --sizebyte 26843545600 --variant Standard` 
> VBoxManage storagectl Debian --name "SATA" --add sata --bootable on`
> VBoxManage storageattach Debian --storagectl "SATA" --port 0 --device 0 --type hdd --medium "C:\Users\<user_name>\VirtualBox VMs\Debian\Debian.vdi"`
> VBoxManage storagectl Debian --name "IDE" --add ide`
> VBoxManage storageattach Debian --storagectl "IDE" --port 0  --device 0 --type dvddrive --medium "C:\Users\<user_name>\Downloads\debian-9.6.0-amd64-netinst.iso"`
```


```
C:\Program Files\Oracle\VirtualBox>VBoxManage showvminfo Debian --details
Name:            Debian
Groups:          /
Guest OS:        Debian (64-bit)
Memory size:     2048MB
VRAM size:       32MB
Number of CPUs:  2
Storage Controller Name (0):            SATA
Storage Controller Name (1):            IDE
Storage Controller Type (1):            PIIX4
Storage Controller Bootable (1):        on
SATA (0, 0): C:\Users\<user_name>\VirtualBox VMs\Debian\Debian.vdi (UUID: a1a7b109-1170-4faf-b867-bb2d461dd726)
IDE (0, 0): C:\Users\<user_name>\Downloads\debian-9.6.0-amd64-netinst.iso (UUID: 0a5023d3-3bd7-4cc7-817e-a0f0fe18a888)
NIC 1:           MAC: 0800272E66E0, Attachment: NAT, Cable connected: on, Trace: off (file: none), Type: 82540EM, Reported speed: 0 Mbps, Boot priority: 0, Promisc Policy: deny, Bandwidth group: none
NIC 1 Settings:  MTU: 0, Socket (send: 64, receive: 64), TCP Window (send:64, receive: 64)
```

###On Guest VM

```
~$ cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux 9 (stretch)"
NAME="Debian GNU/Linux"
VERSION_ID="9"
VERSION="9 (stretch)"
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
```

Installing Python 3.6 on Debian:

```
$ sudo apt-get install build-essential ca-certificates curl gcc libbz2-dev libffi-dev libncurses5-dev libncursesw5-dev libreadline-dev libssl-dev libsqlite3-dev llvm make python3-dev tk-dev wget xz-utils zlib1g-dev liblzma-dev
$ wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tgz
$ tar xvf Python-3.6.3.tgz
$ cd Python-3.6.3
$ ./configure --enable-optimizations --enable-loadable-sqlite-extensions
$ make -j8
$ sudo make altinstall

$ whereis python
python: 
/usr/bin/python3.5-config
/usr/bin/python3.5m
/usr/bin/python
/usr/bin/python3.5
/usr/bin/python2.7
/usr/bin/python3.5m-config
/usr/lib/python3.5
/usr/lib/python2.7 
/etc/python 
/etc/python3.5 
/etc/python2.7
/usr/local/bin/python3.6m
/usr/local/bin/python3.6
/usr/local/bin/python3.6m-config
/usr/local/lib/python3.5
/usr/local/lib/python2.7
/usr/local/lib/python3.6
/usr/include/python3.5m
/usr/include/python3.5
/usr/include/python2.7
/usr/share/python
/usr/share/man/man1/python.1.gz

$ sudo update-alternatives --install /usr/bin/python python /usr/local/bin/python3.6 50
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 40
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.5 30

$ sudo update-alternatives --config python
```

Adding virtual environments

```
$ sudo pip3.6 install virtualenvwrapper
$ mkdir ~/venv
$ echo "export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3.6/
export WORKON_HOME=~/venv/
. /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
$ exec bash
$ mkvirtualenv --python=/usr/local/lib/python3.6 pyneng
```
