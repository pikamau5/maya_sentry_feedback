import sys
import excepthook_override

ex = excepthook_override.Except()
ex.run_excepthook(os.path.basename(__file__))

divide_by_zero = 1/0