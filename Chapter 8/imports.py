import imports_module
imports_module.test()

from imports_module import test
test()

from imports_module import test as t
t()

import imports_module as im
im.test()

from imports_module import *
test()