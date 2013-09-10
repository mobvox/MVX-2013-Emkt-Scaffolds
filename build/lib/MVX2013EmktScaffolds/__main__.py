# _*_ coding: utf-8 _*_

from files import Files
from folders import Folders

import argparse

parser = argparse.ArgumentParser(description='Generates scaffolds of email marketing')
parser.add_argument('name', type=str, help='the name of the email marketing, something like \'MVX-2013-ProjectName\'')
parser.add_argument('--langs', type=str, nargs='+', metavar='L', help='the languages to be used, supported languages are \'[pt-BR, en, es]\'')
args = parser.parse_args()


files = Files()
folders = Folders()

def createProject(projectName, langs):
  folders.createProjectFolders(projectName=projectName, langs=langs)
  files.createProjectFiles(projectName=projectName, langs=langs)

langs = ['pt-BR'] if not args.langs else args.langs

if folders.folderExists(args.name):
  opt = raw_input('Folder \'%s\' alredy exists, do you want to overwrite it\'s contents? ' % args.name)
  opt = opt.lower()
  if opt == "y" or opt == "yes":
    createProject(projectName=args.name, langs=langs)
  elif opt == "n" or opt == "no":
    print 'Exiting...'
  else:
    print('Invalid option \'%s\'' % opt)
else:
  createProject(projectName=args.name, langs=langs)
