'''
Usage: python generate_markdowns.py
'''
import argparse
import fnmatch
import logging
import os
import sys
import subprocess
from pkgutil import iter_modules
from pathlib import Path
from setuptools import find_packages
from tqdm import tqdm

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-l','--list', nargs='+', help='<Required> Set flag', required=True)
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")

args = parser.parse_args()

if args.verbose:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)


def prepend_gatsby_header(file_path, title, slug, section, sub_section, module):
    '''
    Adds title, description and slug to the file.
    '''

    with open(file_path, 'w') as out_file:
        header = '---\ntitle: {0}\nslug: {1}\nsection: {2}\nsub_section: {3}\nmodule: {4}\n---\n' \
            .format(title, slug, section, sub_section, module)
        out_file.write(header)

    return

def generate_additional_docs(section, additional_files):
    for additioanl_file in additional_files:
        file_path = additioanl_file['path']
        output_file = additioanl_file['output_file']
        slug = additioanl_file['slug']
        sub_section = additioanl_file['sub_section']
        title = sub_section
        module = additioanl_file['module']
        prepend_gatsby_header(output_file, title, slug, section, sub_section, module)

        with open(output_file, 'a', encoding="utf-8") as outfile:
            if (os.path.exists(file_path)):
                with open(file_path, encoding='utf8') as infile:
                    for line in infile:
                        outfile.write(line)
            else:
                logging.warning("File %s does not exist.", file_path)
        # os.system("cat {0} >> {1}".format(file_path, output_file))

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

def filter_modules(module_list:[str], doc_ignore_path: str):
    '''
    The function removes the modules that are found in `ignore_files`
    '''
    ignore_files = []
    if os.path.isfile(doc_ignore_path):
        with open(doc_ignore_path) as doc_ignore_file:
            ignore_files = [line.rstrip('\n') for line in doc_ignore_file]
    else:
        logging.warning("File [%s] not found", doc_ignore_path)

    matches = set()

    for module in module_list:
        for ignore in ignore_files:
            file_path =  os.path.join(*module.split('.'))
            if fnmatch.fnmatch(file_path, ignore):
                matches.add(module)
    
    logging.debug('Modules to be ignored: [%s]', ", ".join(matches))

    result = list(set(module_list) - matches)
    return result

def generate_markdowns(section_name: str, path: str, output_dir: str, doc_ignore_path: str, generate_markdown: bool):
    '''
    Iterates over each repository to build the .md files.
    '''
    logging.info("Generating markdowns for [%s]", path)
    result = list(find_modules(path))
    # result2 = list(find_modules2(path))

    markdowns_to_generate = filter_modules(result, doc_ignore_path)

    config = ''
    with open("config.txt", "r") as f:
        config = f.read()

    # markdowns_to_generate = [markdowns_to_generate[0]]
    for i in tqdm(range(len(markdowns_to_generate))):

        title = markdowns_to_generate[i].split('.')[-1]
        file_name = title + '.md'
        Path("markdowns/{0}/".format(output_dir)).mkdir(parents=True, exist_ok=True)

        file_path = 'markdowns/{0}/{1}'.format(output_dir, file_name)
        slug = '/read-the-docs/' + output_dir + '/' + title

        module_path = markdowns_to_generate[i].split('.')
        sub_section_name =  module_path[-2] if len(module_path) > 1 else module_path[-1]

        prepend_gatsby_header(file_path, title, slug, section_name, sub_section_name, markdowns_to_generate[i])

        module_path = markdowns_to_generate[i]
        command = '''pydoc-markdown -I {0} -m {1} '{2}' >> {3}''' \
                    .format(path, module_path, config, file_path)
        
        if generate_markdown:
            with open(file_path, 'a') as fp:
                subprocess.call(['pydoc-markdown', '-I', path, '-m', module_path, config], stdout=fp)

markdown_repos = {'aquarius': {'additional_files':[], 'docignore_file_path': 'aquarius/.docignore','path':'aquarius/ocean_lib', 'output_dir': 'aquarius', 'section': 'aquarius'},
            'ocean.py': {'docignore_file_path': 'ocean.py/.docignore','path':'ocean.py', 'output_dir': 'ocean-py', 'section': 'ocean.py',
            'additional_files': [
                {'path': os.path.join('ocean.py','README.md'),
                'slug': '/read-the-docs/ocean-py/readme',
                'sub_section': 'Overview',
                'module': 'introduction',
                'output_file' : os.path.join('markdowns','ocean-py','Readme.md')
                },
                {'path': os.path.join('ocean.py','READMEs','overview.md'),
                'slug': '/read-the-docs/ocean-py/overview',
                'sub_section': 'Overview',
                'module': 'overview',
                'output_file' : os.path.join('markdowns','ocean-py','overview.md')
                }
        ]},
        'provider': {'additional_files':[], 'docignore_file_path': 'provider/.docignore','path':'provider/ocean_lib', 'output_dir': 'provider', 'section': 'provider'}}


if __name__ == '__main__':

    markdowns_to_be_generated = list(set(args.list) & set(markdown_repos.keys()))
    logging.info("Starting to generate markdowns for %s", markdowns_to_be_generated)

    for repository_info in markdowns_to_be_generated:
        markdown_repo = markdown_repos[repository_info]
        generate_markdowns(markdown_repo['section'], markdown_repo['path'], markdown_repo['output_dir'],
                            markdown_repo['docignore_file_path'], True)
  
        generate_additional_docs(markdown_repo['section'],markdown_repo['additional_files'])
