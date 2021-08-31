__version__ = "0.1.0"

# DADOS DE CONFIGURAÇÃO
__DefaultWidth__ = 1100
__DefaultHeight__ = 800

__darkMode__ = ""

__update_automatically__ = ""
__releases__ =  ""
__untested_releases__ = ""

__title__ = "Untitled"

class Global:
  __conf = {
    "darkMode": "",
    "update_automatically": "",
    "releases": "",
    "untestedReleases": "",
    "my_capivara": ""
  }
  __setters = ["darkMode", "update_automatically", "releases", "untestedReleases", "my_capivara"]

  @staticmethod
  def config(name):
    return Global.__conf[name]

  @staticmethod
  def set(name, value):
    if name in Global.__setters:
      Global.__conf[name] = value
    else:
      raise NameError("Name not accepted in set() method")



