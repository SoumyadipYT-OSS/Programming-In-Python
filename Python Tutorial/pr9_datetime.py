# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 22:42:39 2023

@author: Soumyadip
"""
# =============================================================================
#   CONDITIONAL STATEMENTS IN PYTHON
# =============================================================================
from datetime import datetime
present = datetime.now()
current_time = present.strftime('%I:%M %p')
print(current_time)

import time
localTime = time.localtime()
currentTime = time.strftime('%I:%M %p, %a, %b %d, 20%y',localTime)
print(currentTime)

from datetime import datetime
import pytz
tz_Am = pytz.timezone('America/New_York')
datetime_Am = datetime.now(tz_Am)
print("New York time: ", datetime_Am)