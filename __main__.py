import os
import pathlib
import sys
import time

from src.SR import SR_queue

t1 = time.time()
if getattr(sys, 'frozen', False):
    # frozen
    projectPATH = pathlib.Path(os.path.abspath(os.path.dirname(sys.executable)))
else:
    # unfrozen
    projectPATH = pathlib.Path(os.path.abspath(os.path.dirname(os.path.realpath(__file__))))

print("projectPATH: ", projectPATH)
print("time: ", time.time() - t1)

# from src.utils.getConfig import saveConfig, configDict, SRCONFIG
#
# p_yaml = str(projectPATH / "config.yaml")
# p_model = str(projectPATH / "models")
#
# s = SRCONFIG()
# s.getConfig(p_yaml, p_model)
# print(s.model)
#
# from src.SRFactory import REALCUGAN
#
# r = REALCUGAN()
