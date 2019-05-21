try:
    from configparser import ConfigParser, SafeConfigParser
except ImportError:
    from ConfigParser import ConfigParser, SafeConfigParser
import os
import time
import sys

conf = ConfigParser()

os.chdir(sys.path[0])
if os.path.exists('data_empty.ini'):
    conf.read('data_empty.ini')
else:
    raise FileNotFoundError('Config file, config.ini, was not found.')

for each_section in conf.sections():
    for (each_key, each_val) in conf.items(each_section):
        try:
            int(each_val)
        except ValueError:
            pass
        else:
            conf.set(each_section, each_key, '')
            with open('data_empty.ini', 'w') as configfile:
                conf.write(configfile)
                time.sleep(0.2)
                print(f"Cleansing [{each_section}]: {each_key}")