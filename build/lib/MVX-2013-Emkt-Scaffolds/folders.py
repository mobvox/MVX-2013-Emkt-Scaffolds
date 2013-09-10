import os
import common


class Folders(object):
  """Folders Scaffolding"""

  def generatePaths(self, projectName, langs):
    paths = [[projectName, 'imgs']]
    for lang in langs:
      if not lang in common.SUPPORTED_LANGS:
        raise KeyError('Unsupported language %s' % lang)
      paths.append([projectName, lang, 'imgs'])
    return paths

  def folderExists(self, folderName):
    return os.path.exists(folderName)

  def createProjectFolders(self, projectName='NewProject', langs=['pt-BR']):
    paths = self.generatePaths(projectName, langs)

    for path in paths:
      p = ''  
      for folder in path:
        p += '%s/' % (folder)
        if not os.path.exists(p):
          print('Creating directory %s' % p)
          os.mkdir(p)
