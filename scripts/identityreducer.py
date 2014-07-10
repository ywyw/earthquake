#!/usr/bin/env python

import sys

# implements a passthrough reducer for MR
for line in sys.stdin:
    sys.stdout.write(line)
