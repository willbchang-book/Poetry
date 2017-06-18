# -*- coding: utf-8 -*-
import os

def loop_files(path):
	for root, dirs, filenames in os.walk(path):
		for file_name in filenames:
			if ".md" in file_name:
				delete_dash(file_name)
        print(file_name)

def rename_title(file_name, index, title, suffix):
	if index == 0 and title != '':
		title = title.rstrip().replace('#', '').replace(' ', '')
		title += suffix
		return title

def rename_file(file_name):
	with open(file_name) as f:
		for index, line in enumerate(f):
			title = rename_title(file_name, index, line, '.md')
			os.rename(file_name, title)

def rename_path_files(path):
	for root, dirs, filenames in os.walk(path):
    for f in filenames:
      if isEnglish(f) and '.md' in f:
        rename_file(f)

def remove_empty_lines(file_name):
  """Overwrite the file, removing empty lines and lines that contain only whitespace."""
  with open(file_name, 'r+') as f:
    lines = f.readlines()
    f.seek(0)
    f.writelines(line for line in lines if line.strip())
    f.truncate()

def add_br_at_endline(arg):
  with open(file_name, 'r+') as f:
    lines = f.readlines()
    f.seek(0)
    f.writelines(line for line in lines if line.strip())
    f.truncate()

def delete_dash(file_name):
  with open(file_name, 'r+') as f:
    lines = f.readlines()
    f.seek(0)
    for line in lines:
      f.writelines(line.replace('---', ''))
    f.truncate()

def isEnglish(s):
  try:
    s.encode('ascii')
  except UnicodeEncodeError:
    return False
  else:
    return True


indir = '/Users/Will/Poetry/'
loop_files(indir)
