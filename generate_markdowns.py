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


def get_branch(path: str):
    return (
        subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=path)
        .decode("utf-8")
        .rstrip()
    )


def generate_source_url(source: str, branch: str, module: list[str], extenstion: str):

    url = (
        source
        + "/blob/"
        + branch
        + "/"
        + "/".join(module.split("."))
        + "."
        + extenstion
    )
    return url


def prepend_gatsby_header(
    file_path: str,
    title: str,
    slug: str,
    app: str,
    module: str,
    source: str,
    version: str,
):
    """
    Adds title, description and slug to the file.
    """
    with open(file_path, "w") as out_file:
        header = f"---\ntitle: {title}\nslug: {slug}\napp: {app}\nmodule: {module}\nsource: {source}\nversion: {version}\n---\n"
        out_file.write(header)

    return


def concat_files(source_file: str, target_file: str):
    with open(target_file, "a", encoding="utf-8") as outfile:
        if os.path.exists(source_file):
            with open(source_file, encoding="utf8") as infile:
                for line in infile:
                    outfile.write(line)
        else:
            logging.warning("File %s does not exist.", source_file)


def generate_additional_docs_from_directory(
    app,
    path,
    additional_directories,
    output_directory,
    doc_ignore_file_path,
    source,
    version,
):
    ignore_files = get_doc_ignore_file_list(doc_ignore_file_path)
    branch = get_branch(path)

    for additional_directory in additional_directories:
        directory_path = additional_directory["path"]

        if not os.path.isdir(output_directory):
            os.makedirs(output_directory, exist_ok=True)

        for markdown_file_path in Path(directory_path).rglob("*.md"):

            module_name = markdown_file_path.stem
            relative_path = os.path.relpath(
                str(markdown_file_path.parent), directory_path
            )

            module_path = "" if relative_path == "." else relative_path
            module = ".".join(os.path.join(module_path, module_name).split(os.sep))

            out_dir = os.path.join(output_directory, relative_path)

            can_be_ignored = False
            for ignore in ignore_files:
                if fnmatch.fnmatch(
                    os.path.join(module_path, markdown_file_path.name), ignore
                ):
                    can_be_ignored = True
                    break

            if can_be_ignored:
                logging.info("Ignoring markdown: %s", str(markdown_file_path))
                continue

            logging.info("Adding markdown: %s", str(markdown_file_path))

            if not os.path.isdir(out_dir):
                os.makedirs(out_dir)

            out_file = os.path.join(out_dir, markdown_file_path.name)

            url = generate_source_url(source, branch, module, "md")
            slug = "/".join(module.split(".")) + ".md"
            prepend_gatsby_header(
                out_file, markdown_file_path.name, slug, app, module, url, version
            )
            concat_files(str(markdown_file_path), out_file)
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


def get_doc_ignore_file_list(doc_ignore_path: str):
    ignore_files = []
    if os.path.isfile(doc_ignore_path):
        with open(doc_ignore_path) as doc_ignore_file:
            ignore_files = [line.rstrip("\n") for line in doc_ignore_file]
    else:
        logging.warning("File [%s] not found", doc_ignore_path)
    return ignore_files


def filter_modules(path: str, module_list: list[str], doc_ignore_path: str):
    """
    The function removes the modules that are found in `ignore_files`
    """

    matches = set()
    ignore_files = get_doc_ignore_file_list(doc_ignore_path)
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
    app: str,
    path: str,
    output_dir: str,
    doc_ignore_path: str,
    modules,
    source: str,
    version: str,
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

    if os.path.isdir(output_dir):
        shutil.rmtree(output_dir)

    branch = get_branch(path)

    for i in tqdm(range(len(markdowns_to_generate))):

        title = markdowns_to_generate[i].split(".")[-1]
        file_name = title + ".md"

        out_d = os.path.join(output_dir, *markdowns_to_generate[i].split(".")[:-1])

        if not os.path.isdir(out_d):
            os.makedirs(out_d, exist_ok=True)

        file_path = os.path.join(out_d, file_name)
        slug = "/".join(markdowns_to_generate[i].split("."))

        url = generate_source_url(source, branch, slug, "py")

        prepend_gatsby_header(
            file_path, title, slug, app, markdowns_to_generate[i], url, version
        )

        module_path = markdowns_to_generate[i]

        with open(file_path, "a") as fp:
            subprocess.call(
                ["pydoc-markdown", "-I", path, "-m", module_path, config], stdout=fp
            )


markdown_repos = {
    "aquarius": {
        "additional_directories": [],
        "docignore_file_path": "submodules/aquarius/.docignore",
        "path": "submodules/aquarius",
        "output_dir": os.path.join("markdowns", "aquarius"),
        "app": "aquarius",
        "markdown_path": [],
        "source": "https://github.com/oceanprotocol/aquarius",
        "version": "2.2.11",
    },
    "ocean.py": {
        "docignore_file_path": "submodules/ocean.py/.docignore",
        "path": "submodules/ocean.py",
        "output_dir": os.path.join("markdowns", "ocean-py"),
        "app": "ocean.py",
        "additional_files": [],
        "markdown_path": [
            {
                "path": os.path.join("submodules", "ocean.py"),
            }
        ],
        "source": "https://github.com/oceanprotocol/ocean.py",
        "version": "0.5.22",
    },
    "provider": {
        "additional_directories": [],
        "docignore_file_path": "submodules/provider/.docignore",
        "path": "submodules/provider",
        "output_dir": os.path.join("markdowns", "provider"),
        "app": "provider",
        "markdown_path": [],
        "source": "https://github.com/oceanprotocol/provider",
        "version": "0.4.9",
    },
    "ocean-subgraph": {
        "additional_directories": [],
        "docignore_file_path": "submodules/ocean-subgraph/.docignore",
        "path": "submodules/ocean-subgraph",
        "output_dir": os.path.join("markdowns", "ocean-subgraph"),
        "app": "ocean-subgraph",
        "markdown_path": [
            {
                "path": os.path.join("submodules", "ocean-subgraph"),
            }
        ],
        "source": "https://github.com/oceanprotocol/ocean-subgraph",
        "version": "1.1.1",
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
            markdown_repo["source"],
            markdown_repo["version"],
        )

        generate_additional_docs_from_directory(
            markdown_repo["app"],
            markdown_repo["path"],
            markdown_repo["markdown_path"],
            markdown_repo["output_dir"],
            markdown_repo["docignore_file_path"],
            markdown_repo["source"],
            markdown_repo["version"],
        )
