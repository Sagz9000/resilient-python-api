__author__ = 'Resilient Systems'

import logging
from resilient_circuits import app

app.log(logging.DEBUG)
app.run()