Working test for Python 3.9
rpi@rpi:~ $ sudo apt-get install build-essential checkinstall
rpi@rpi:~ $ sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev
rpi@rpi:~ $ sudo apt-get install  libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev
rpi@rpi:~ $ cd /opt
rpi@rpi:/opt $ cd Python-3.9.2
rpi@rpi:~ $ sudo ./configure --enable-optimizations
rpi@rpi:~ $ sudo make altinstall
rpi@rpi:~ $ cd ..
rpi@rpi:~ $ cd /usr/local/bin/
rpi@rpi:~ $ sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1
rpi@rpi:~ $ sudo  update-alternatives --install /usr/bin/python3 python3 /usr/local/bin/python3.9 2
rpi@rpi:~ $ update-alternatives --config python3
------------------------
requarements.txt
Adafruit-Blinka                          8.62.0
adafruit-circuitpython-busdevice         5.2.13
adafruit-circuitpython-connectionmanager 3.1.5
adafruit-circuitpython-motor             3.4.17
adafruit-circuitpython-pca9685           3.4.19
adafruit-circuitpython-register          1.10.4
adafruit-circuitpython-requests          4.1.13
adafruit-circuitpython-servokit          1.3.21
adafruit-circuitpython-typing            1.12.1
Adafruit-PlatformDetect                  3.81.0
Adafruit-PureIO                          1.1.11
binho-host-adapter                       0.1.6
numpy                                    2.0.2
pip                                      25.2
pyftdi                                   0.56.0
pyserial                                 3.5
pyusb                                    1.3.1
RPi.GPIO                                 0.7.1
setuptools                               49.2.1
smbus                                    1.1.post2
sysv-ipc                                 1.1.0
toml                                     0.10.2
typing_extensions                        4.14.1
