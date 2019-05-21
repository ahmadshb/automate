import time
import datetime
import sys
from colorama import Fore, init

init()

for remaining in range(360, 0, -1):
    remaining = str(datetime.timedelta(seconds=remaining))[3:]
    sys.stdout.write("\r")
    sys.stdout.write(
        "\r" + Fore.RED +
        f"Inadequate Boost Points. {remaining} until next attempt.")
    sys.stdout.flush()
    time.sleep(1)

sys.stdout.write(
    "\rInadequate Boost Points. Retrying...                        \n")
