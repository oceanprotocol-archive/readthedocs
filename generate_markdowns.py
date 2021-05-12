"""
Usage: python generate_markdowns.py
"""
import argparse
import fnmatch
import logging
import os
import shutil
import sys
import subprocess
from pkgutil import iter_modules
from pathlib import Path
from setuptools import find_packages
from tqdm import tqdm

parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument(
    "-l",
    "--list",
    nargs="+",
    help="<Required> List of app e.g ocean.py provider aquarius",
    required=True,
)

parser.add_argument(
    "-m", "--modules", nargs="+", help="<optional> List of modules", required=False
)
parser.add_argument(
    "-v", "--verbose", help="increase output verbosity", action="store_true"
)

args = parser.parse_args()

if args.verbose:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)


def prepend_gatsby_header(file_path, title, slug, app, module):
    """
    Adds title, description and slug to the file.
    """

    with open(file_path, "w") as out_file:
        header = "---\ntitle: {0}\nslug: {1}\napp: {2}\nmodule: {3}\n---\n".format(
            title, slug, app, module
        )
        out_file.write(header)

    return


def generate_additional_docs(app, additional_files):
    for additioanl_file in additional_files:
        file_path = additioanl_file["path"]
        output_file = additioanl_file["output_file"]
        slug = additioanl_file["slug"]
        module = additioanl_file["module"]
        title = module.split(".")[-1]
        prepend_gatsby_header(output_file, title, slug, app, module)

        with open(output_file, "a", encoding="utf-8") as outfile:
            if os.path.exists(file_path):
                with open(file_path, encoding="utf8") as infile:
                    for line in infile:
                        outfile.write(line)
            else:
                logging.warning("File %s does not exist.", file_path)
        # os.system("cat {0} >> {1}".format(file_path, output_file))


def find_modules(path):
    """
    Funtion to list all the modules in a repository.
    """
    modules = set()
    packages = find_packages(path)
    for pkg in packages:
        modules.add(pkg)
        pkgpath = path + "/" + pkg.replace(".", "/")
        if sys.version_info.major == 2 or (
            sys.version_info.major == 3 and sys.version_info.minor < 6
        ):
            for _, name, ispkg in iter_modules([pkgpath]):
                if not ispkg:
                    modules.add(pkg + "." + name)
        else:
            for info in iter_modules([pkgpath]):
                if not info.ispkg:
                    modules.add(pkg + "." + info.name)
    return modules


def filter_modules(path: str, module_list: list[str], doc_ignore_path: str):
    """
    The function removes the modules that are found in `ignore_files`
    """
    ignore_files = []
    if os.path.isfile(doc_ignore_path):
        with open(doc_ignore_path) as doc_ignore_file:
            ignore_files = [line.rstrip("\n") for line in doc_ignore_file]
    else:
        logging.warning("File [%s] not found", doc_ignore_path)

    matches = set()

    for module in module_list:
        for ignore in ignore_files:
            file_path = os.path.join(*module.split("."))
            if fnmatch.fnmatch(file_path, ignore):
                matches.add(module)

    directories = set()
    for module in module_list:
        module_path = os.path.join(path, *module.split("."))
        if os.path.isdir(module_path):
            directories.add(module)

    logging.debug("Modules to be ignored: [%s]", ", ".join(matches))
    logging.debug(
        "Following modules are directories and will be ignored: [%s]",
        ", ".join(directories),
    )

    result = list(set(module_list) - matches.union(directories))

    logging.debug("Modules found: [%s]", ", ".join(matches))

    return result


def generate_markdowns(
    app: str, path: str, output_dir: str, doc_ignore_path: str, modules
):
    """
    Iterates over each repository to build the .md files.
    """
    logging.info("Generating markdowns for [%s]", path)
    result = list(find_modules(path))
    if modules:
        result = list(set(result) & set(modules))

    markdowns_to_generate = filter_modules(path, result, doc_ignore_path)

    config = ""
    with open("config.txt", "r") as f:
        config = f.read()

    output_dir_path = os.path.join("markdowns", output_dir)
    if os.path.isdir(output_dir_path):
        shutil.rmtree(output_dir_path)

    Path("markdowns/{0}/".format(output_dir)).mkdir(parents=True, exist_ok=True)

    for i in tqdm(range(len(markdowns_to_generate))):

        title = markdowns_to_generate[i].split(".")[-1]
        file_name = title + ".md"

        file_path = "markdowns/{0}/{1}".format(output_dir, file_name)
        slug = "/read-the-docs/" + output_dir + "/" + title

        prepend_gatsby_header(file_path, title, slug, app, markdowns_to_generate[i])

        module_path = markdowns_to_generate[i]

        with open(file_path, "a") as fp:
            subprocess.Popen(
                ["pydoc-markdown", "-I", path, "-m", module_path, config], stdout=fp
            )


markdown_repos = {
    "aquarius": {
        "additional_files": [],
        "docignore_file_path": "submodules/aquarius/.docignore",
        "path": "submodules/aquarius/ocean_lib",
        "output_dir": "aquarius",
        "app": "aquarius",
    },
    "ocean.py": {
        "docignore_file_path": "submodules/ocean.py/.docignore",
        "path": "submodules/ocean.py",
        "output_dir": "ocean-py",
        "app": "ocean.py",
        "additional_files": [
            {
                "path": os.path.join("submodules", "ocean.py", "README.md"),
                "slug": "/read-the-docs/ocean-py/readme",
                "module": "introduction.readme",
                "output_file": os.path.join("markdowns", "ocean-py", "Readme.md"),
            },
            {
                "path": os.path.join(
                    "submodules", "ocean.py", "READMEs", "overview.md"
                ),
                "slug": "/read-the-docs/ocean-py/overview",
                "module": "introduction.overview",
                "output_file": os.path.join("markdowns", "ocean-py", "overview.md"),
            },
        ],
    },
    "provider": {
        "additional_files": [],
        "docignore_file_path": "submodules/provider/.docignore",
        "path": "submodules/provider/ocean_lib",
        "output_dir": "provider",
        "app": "provider",
    },
}


if __name__ == "__main__":

    markdowns_to_be_generated = list(set(args.list) & set(markdown_repos.keys()))

    modules = None
    if args.modules:
        modules = list(set(args.modules))
        logging.info("Modules %s", modules)

    logging.info("Starting to generate markdowns for %s", markdowns_to_be_generated)

    for repository_info in markdowns_to_be_generated:
        markdown_repo = markdown_repos[repository_info]
        generate_markdowns(
            markdown_repo["app"],
            markdown_repo["path"],
            markdown_repo["output_dir"],
            markdown_repo["docignore_file_path"],
            modules,
        )

        generate_additional_docs(
            markdown_repo["app"], markdown_repo["additional_files"]
        )
