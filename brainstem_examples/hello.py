import brainstem
import time

#for easy access to error constants
from brainstem.result import Result

# Create USBStem object
print '\nCreating USBStem and connecting to first module found'
stem = brainstem.stem.USBStem()
