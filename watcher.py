from typing import Optional
import os
import pathlib
import time
import hashlib
import argparse
import subprocess


def parse_arguments() -> tuple[list[str], int, bool]:
    parser = argparse.ArgumentParser(
        description="On file change run mypy and format with black"
    )
    parser.add_argument(
        "file_name", metavar="str", nargs="+", type=str, help="files to reformat"
    )
    parser.add_argument(
        "--watch_time",
        metavar="int",
        type=int,
        default=2,
        help="poll time for file changes",
    )
    parser.add_argument(
        "--recursive",
        metavar="bool",
        type=bool,
        default=False,
        help="recursively check directories",
    )
    args = parser.parse_args()
    return args.file_name, args.watch_time, args.recursive


def get_files_in_folder(
    root_dir: str, extension: str = "*.py", recursive: bool = False
) -> list[str]:
    root_path = pathlib.Path(root_dir)
    if recursive:
        file_names = [str(f) for f in root_path.rglob(extension)]
    else:
        file_names = [str(f) for f in root_path.glob(extension)]
    return file_names


def main() -> None:
    file_names, watch_time, recursive = parse_arguments()
    checker = {}
    for file_name in file_names:
        if os.path.isdir(file_name):
            dir_files = get_files_in_folder(file_name, recursive=recursive)
            for dir_file in dir_files:
                checker[dir_file] = ""
        elif file_name.endswith(".py"):
            checker[file_name] = ""
        else:
            raise NotImplementedError("Only py files supported")
    if len(checker) == 0:
        raise ValueError("No py files found")
    while True:  # Watch files for changes
        for file_name, contents in checker.items():
            with open(file_name, "rb") as fd:
                dat = fd.read()
                new_contents = hashlib.md5(dat).hexdigest()
                if new_contents != contents:
                    print(f"{file_name} change detected")
                    black_task = subprocess.Popen(["black", file_name])
                    black_task.wait()
                    mypy_task = subprocess.Popen(["mypy", file_name])
                    mypy_task.wait()
                    checker[file_name] = new_contents
        time.sleep(watch_time)


if __name__ == "__main__":
    main()
