__version__ = "0.1.0"

# DADOS DE CONFIGURAÇÃO
__DefaultWidth__ = 1100
__DefaultHeight__ = 800

__darkMode__ = ""

__update_automatically__ = ""
__releases__ =  ""
__untested_releases__ = ""

__title__ = "Untitled"
__capivara_file__ = "Untitled.capivara"

class Global:
  __conf = {
    "version" : "",
    "title": "",
    "capivara_file_open": "",
    "last_file_open" : "",
    "darkMode": "",
    "update_automatically": "",
    "releases": "",
    "untestedReleases": "",
    "my_capivara": "",
    "flag_edit": ""
  }
  __setters = ["version", "title", "last_file_open", "capivara_file_open", "darkMode", "update_automatically", "releases", "untestedReleases", "my_capivara", "flag_edit"]

  @staticmethod
  def config(name):
    return Global.__conf[name]

  @staticmethod
  def set(name, value):
    if name in Global.__setters:
      Global.__conf[name] = value
    else:
      raise NameError("Name not accepted in set() method")



