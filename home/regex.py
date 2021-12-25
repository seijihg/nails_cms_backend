"""A home for regular expressions, so we don't reinvent the wheel"""

import re

PHONE_NUMBER_REGEX_SIGNUP = re.compile(r'^[(+]*(?:[\s().-]*\d){9,15}$')
