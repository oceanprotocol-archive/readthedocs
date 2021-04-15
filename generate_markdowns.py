'''
Usage: python generate_markdowns.py
'''
import sys
import argparse
from pkgutil import iter_modules
from pathlib import Path
from setuptools import find_packages
from tqdm import tqdm
import subprocess

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-l','--list', nargs='+', help='<Required> Set flag', required=True)
parser.add_argument('-P','--print-command', default=False, action=argparse.BooleanOptionalAction)

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

def generate_markdowns(section_name: str, path: str, output_dir: str, output_commad: bool, generate_markdown: bool):
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

    config = ''
    f = open("config.txt", "r")
    config = f.read()

    # markdowns_to_generate = [markdowns_to_generate[0]]
    for i in tqdm(range(len(markdowns_to_generate))):

        title = markdowns_to_generate[i]['module'].replace('.', '-')
        file_name = title + '.md'
        Path("markdowns/{0}/".format(output_dir)).mkdir(parents=True, exist_ok=True)

        file_path = 'markdowns/{0}/{1}'.format(output_dir, file_name)
        slug = '/read-the-docs/' + output_dir + '/' + title
        sub_section_name =  markdowns_to_generate[i]['package']
        prepend_gatsby_header(file_path, title, slug, section_name, sub_section_name)


        module_path = markdowns_to_generate[i]['package'] + '.' + markdowns_to_generate[i]['module']
        command = '''pydoc-markdown -I {0} -m {1} '{2}' >> {3}''' \
                    .format(path, module_path, config, file_path)
        if output_commad:
            print(command)

        if generate_markdown:
            with open(file_path, 'a') as fp:
                subprocess.call(['pydoc-markdown', '-I', path, '-m', module_path, config], stdout=fp)

markdown_repos = {'aquarius': {'path':'aquarius/ocean_lib', 'output_dir': 'aquarius', 'section': 'aquarius'},
            'ocean.py': {'path':'ocean.py', 'output_dir': 'ocean-py', 'section': 'ocean.py'},
        'provider': {'path':'provider/ocean_lib', 'output_dir': 'provider', 'section': 'provider'}}

if __name__ == '__main__':
    args = parser.parse_args()

    markdowns_to_be_generated = list(set(args.list) & set(markdown_repos.keys()))
    print("Starting to generate markdowns for {0}".format(markdowns_to_be_generated))

    for repository_info in markdowns_to_be_generated:
        markdown_repo = markdown_repos[repository_info]
        generate_markdowns(markdown_repo['section'], markdown_repo['path'],
                            markdown_repo['output_dir'], args.print_command, True)
