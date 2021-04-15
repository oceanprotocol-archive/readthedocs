'''
Usage: python generate_markdowns.py
'''
import sys
import os
from pkgutil import iter_modules
from pathlib import Path
from setuptools import find_packages
from tqdm import tqdm

def prepend_gatsby_header(file_path, title, slug, section, sub_section):
    '''
    Adds title, description and slug to the file.
    '''

    with open(file_path, 'w') as out_file:
        header = '---\ntitle: {0}\nslug: {1}\nsection: {2}\nsub_section: {3}\n---\n'.format(title, slug, section, sub_section)
        out_file.write(header)

    return

def find_modules(path):
    '''
    Funtion to list all the modules in a repository.
    '''
    modules = set()
    packages =  find_packages(path)
    for pkg in packages:
        modules.add(pkg)
        pkgpath = path + '/' + pkg.replace('.', '/')
        if sys.version_info.major == 2 or (sys.version_info.major == 3 and sys.version_info.minor < 6):
            for _, name, ispkg in iter_modules([pkgpath]):
                if not ispkg:
                    modules.add(pkg + '.' + name)
        else:
            for info in iter_modules([pkgpath]):
                if not info.ispkg:
                    modules.add(pkg + '.' + info.name)
    return modules

def find_modules2(path):
    '''
    Funtion to list all the modules in a repository.
    '''
    modules = []
    packages =  find_packages(path)
    for pkg in packages:
        # modules[pkg] = []
        pkgpath = path + '/' + pkg.replace('.', '/')
        if sys.version_info.major == 2 or (sys.version_info.major == 3 and sys.version_info.minor < 6):
            for _, name, ispkg in iter_modules([pkgpath]):
                if not ispkg:
                    modules.append({'package':pkg,'module':name})
        else:
            for info in iter_modules([pkgpath]):
                if not info.ispkg:
                    modules.append({'package':pkg,'module':info.name})
    return modules

def generate_markdowns(section_name, path, output_dir):
    '''
    Iterates over each repository to build the .md files.
    '''
    print("Generating markdowns for [{0}]".format(path))
    result = list(find_modules(path))
    result2 = list(find_modules2(path))

    skip_list = ['test']

    markdowns_to_generate = []

    for i in result2:
        for skip_word in skip_list:
            if not (i['package'] + '.'+ i['module']).find(skip_word) != -1:
                markdowns_to_generate.append(i)


    for i in tqdm(range(len(markdowns_to_generate))):

        title = markdowns_to_generate[i]['module'].replace('.', '-')
        file_name = title + '.md'
        Path("markdowns/{0}/".format(output_dir)).mkdir(parents=True, exist_ok=True)

        file_path = 'markdowns/{0}/{1}'.format(output_dir, file_name)
        slug = '/read-the-docs/' + output_dir + '/' + title
        sub_section_name =  markdowns_to_generate[i]['package']
        prepend_gatsby_header(file_path, title, slug, section_name, sub_section_name)

        module_path = markdowns_to_generate[i]['package'] + '.' + markdowns_to_generate[i]['module']
        command = 'pydoc-markdown -I {0} -m {1} >> {2}' \
                    .format(path, module_path, file_path)

        os.system(command)

markdown_repos = [{'path':'aquarius/ocean_lib', 'output_dir': 'aquarius', 'section': 'aquarius'},
            {'path':'ocean.py/ocean_lib', 'output_dir': 'ocean-py', 'section': 'ocean.py'},
            {'path':'provider/ocean_lib', 'output_dir': 'provider', 'section': 'provider'}]

for markdown_repo in markdown_repos:
    generate_markdowns(markdown_repo['section'],markdown_repo['path'], markdown_repo['output_dir'])
