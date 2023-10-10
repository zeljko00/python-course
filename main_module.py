print("__name__ printed from main-module:",__name__)
from test_module import f as ff
import test_package.first_module

ff()
test_package.first_module.f()