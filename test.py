import sys
import excepthook_override

ex = excepthook_override.Except()
ex.run_excepthook(os.path.basename(__file__))