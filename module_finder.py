import importlib

module_location = importlib.import_module('cv2')
print(module_location.__file__)


# import os
# print(os.__file__)


# import sys
# print(sys.modules['os'].__file__)


# import os
# print(os.name)


# import importlib.util
# import os
# spacy = 'os'
# spec = importlib.util.find_spec(spacy)
# module_file = spec.origin
# print(
#     f"The file path of the {spacy} module is: {os.path.abspath(module_file)}")
