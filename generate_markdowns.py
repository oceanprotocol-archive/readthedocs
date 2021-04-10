'''
Usage: python generate_markdowns.py
'''
import sys
import os
from pkgutil import iter_modules
from setuptools import find_packages
from tqdm import tqdm

def prepend_gatsby_header(file_path, title, slug, section):
    '''
    Adds title, description and slug to the file.
    '''

    with open(file_path, 'w') as out_file:
        header = '---\ntitle:{0}\nslug:{1}\nsection:{2}\n---\n'.format(title, slug, section)
        out_file.write(header)

    return

def find_modules(path):
    '''
    Funtion to list all the modules in a repository.
    '''
    modules = set()
    for pkg in find_packages(path):
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

def generate_markdowns(path, output_dir):
    '''
    Iterates over each repository to build the .md files.
    '''
    print("Generating markdowns for [{0}]".format(path))
    result = list(find_modules(path))

    skip_list = ['test']

    markdowns_to_generate = set()

    for i in result:
        for skip_word in skip_list:
            if not i.find(skip_word) != -1:
                markdowns_to_generate.add(i)

    markdowns_to_generate = list(markdowns_to_generate)

    for i in tqdm(range(len(markdowns_to_generate))):

        title = markdowns_to_generate[i].replace('.', '-')
        file_name = title + '.md'
        file_path = 'markdowns/{0}/{1}'.format(output_dir, file_name)
        slug = '/docs/' + output_dir + '/' + title
        prepend_gatsby_header(file_path, title, slug, output_dir)

        command = 'pydoc-markdown -I {0} -m {1} >> {2}' \
                    .format(path, markdowns_to_generate[i], file_path)

        os.system(command)

markdown_repos = [{'path':'aquarius/aquarius', 'output_dir': 'aquarius'},
            {'path':'ocean.py/ocean_lib', 'output_dir': 'ocean-py'},
            {'path':'provider/ocean_provider', 'output_dir': 'provider'}]

for markdown_repo in markdown_repos:
    generate_markdowns(markdown_repo['path'], markdown_repo['output_dir'])
