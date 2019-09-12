import sys
import excepthook_override

# load the exceptionhook override to this script
ex = excepthook_override.Except()
ex.run_excepthook(os.path.basename(__file__))

# divide by zero
divide_by_zero = 1/0