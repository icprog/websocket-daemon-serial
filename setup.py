# setup.py
from distutils.core import setup
import py2exe

class Target:
    def __init__(self, **kw):
        self.__dict__.update(kw)
        # for the versioninfo resources
        self.version = "0.1.0"
        self.company_name = "LexinSmart"
        self.copyright = "LexinSmart 2016"
        self.name = "lexinSerialBridge"


my_data_files = [('avrdudes', ['avrdudes/Windows/avrdude.conf']),
                ('avrdudes', ['avrdudes/Windows/avrdude.exe']),
                ('avrdudes', ['avrdudes/Windows/libusb0.dll']),
                ('drivers/FTDI', ['drivers/Windows/FTDI/arduino.cat']),
                ('drivers/FTDI', ['drivers/Windows/FTDI/arduino.inf']),
                ('drivers/FTDI', ['drivers/Windows/FTDI/dpinst-x86.exe']),
                ('drivers/FTDI', ['drivers/Windows/FTDI/dpinst-amd64.exe']),
                ('',['vcredist_x86.exe'])]

myservice = Target(
    description = 'lexinSerialBridge',
    modules = ['winservice'],
    cmdline_style='pywin32'
)

#    console=["mywinserver.py"],
setup(
    options = {"py2exe": {"compressed": 1, "bundle_files": 1} },
    data_files = my_data_files,
    zipfile = None,
    service=[myservice]
)
