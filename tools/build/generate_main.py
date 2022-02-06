#!/usr/bin/env python3
"""
Generates a complete main file that includes all teaching modules.
"""
import typing as tp
from argparse import ArgumentParser
from pathlib import Path


def is_placeholder(module_file: Path) -> bool:
    """
    Checks if a given module file is only a placeholder.

    Args:
        module_file: that should be checked
    """
    with open(module_file, "r", encoding="UTF-8") as module:
        for line in module.readlines()[:7]:
            if line.startswith("This topic is currently under construction"):
                return True

    return False


def inject_teaching_modules(main_file: tp.TextIO, module_folder: Path) -> None:
    """
    Injects '__INCLUDE__(module/file/path.md)' markers into the main file for
    all modules found in the given module folder.

    Args:
        main_file: where generated input is written to
        module_folder: location of the teaching module folder
    """
    for module in module_folder.glob('**/*.md'):
        if not is_placeholder(module):
            main_file.write(f"__INCLUDE__({module})\n\n")


def generate_main(raw_main_filepath: Path, output_filepath: Path,
                  module_folder: Path) -> None:
    """
    Generate a complete main file that includes all teaching modules.

    Args:
        raw_main: file that will be processed
        output_filename: where generated input should be written
        module_folder: location of the teaching module folder
    """
    with open(raw_main_filepath, "r", encoding="UTF-8") as raw_main, open(
            output_filepath, "w", encoding="UTF-8") as generated_main_file:

        for line in raw_main.readlines():
            if line.startswith("INJECT_TEACHING_MODULES"):
                inject_teaching_modules(generated_main_file, module_folder)
            else:
                generated_main_file.write(line)


def main():
    """Parse inputs and kick of main generation."""
    parser = ArgumentParser("topic_updater")
    parser.add_argument("--raw",
                        type=Path,
                        help="The raw main file to process.")
    parser.add_argument("--out",
                        type=Path,
                        help="Output filename for the generated main.")
    parser.add_argument("--module-folder",
                        type=Path,
                        help="Path to the module folder.")

    args = parser.parse_args()

    generate_main(args.raw, args.out, args.module_folder)


if __name__ == "__main__":
    main()
