import re
import sys


for line in sys.stdin:
    line = line.rstrip()
    # process line
    tmpl = r"^(1(01*0)*1|0)+$"  # ^(1(01*0)*1|0)+$ признак делимости на 3
    if re.match(tmpl, line):
        print(line)