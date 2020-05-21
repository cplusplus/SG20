"""
Small tool for generating and fixing teaching topics.

Verify if the layout of all topics matches the skeleton.
> ./topic_updater.py --check

Update all topic files according to the skeleton.
> ./topic_updater.py --update

Update a specific topic file according to the skeleton.
> ./topic_updater.py --update functions/user-defined-literals.md
"""

import os
import typing as tp
from argparse import ArgumentParser
from copy import copy
from pathlib import Path


def _cli_yn_choice(question: str, default: str = 'y') -> bool:
    """Ask the user to make a y/n decision on the cli."""
    choices = 'Y/n' if default.lower() in ('y', 'yes') else 'y/N'
    choice: str = str(
        input("{message} ({choices}) ".format(message=question,
                                              choices=choices)))
    values: tp.Union[tp.Tuple[str, str],
                     tp.Tuple[str, str,
                              str]] = ('y', 'yes',
                                       '') if choices == 'Y/n' else ('y',
                                                                     'yes')
    return choice.strip().lower() in values


class SectionHeading:
    """ A header of section in the topic document.  """
    def __init__(self, title_text: str) -> None:
        self.__title_text = title_text
        self.__meta_text: tp.List[str] = []

    @property
    def header_text(self) -> str:
        """Text of the section header."""
        return self.__title_text

    @property
    def meta_text(self) -> tp.List[str]:
        """Meta text of the section, represented in italics."""
        return self.__meta_text

    def append_meta_text(self, meta_text_line: str) -> None:
        """
        Append a line to the meta text section of this section heading.

        Args:
            meta_text_line: new meta text line to append
        """
        self.__meta_text.append(meta_text_line)

    def convert_meta_text_to_lines(self) -> tp.List[str]:
        """
        Convert the sections meta text into separate lines for the document.
        """
        heading_lines = []
        heading_lines.append(os.linesep)

        meta_text = "".join(self.meta_text)
        # Guarantee exactly one empty line after meta text
        meta_text = meta_text.rstrip() + os.linesep * 2
        heading_lines.append(meta_text)

        return heading_lines

    def __str__(self) -> str:
        heading_text = f"{self.header_text}\n{''.join(self.meta_text)}"
        return heading_text


class Skeleton:
    """
    The topic skeleton which defines the layout and meta text of a topic file.
    """
    def __init__(self, skeleton_file_path: Path) -> None:
        self.__skeleton_file_path = skeleton_file_path
        self.__headings: tp.List[SectionHeading] = []
        self.__parse_headings()

    @property
    def headings(self) -> tp.List[SectionHeading]:
        """All headings in this skeleton."""
        return self.__headings

    def lookup_heading(self, start_heading_line: str) -> SectionHeading:
        """
        Looks up a heading from the skeleton.

        Args:
            start_heading_line: start of full string of the heading line

        Returns: the section heading that starts like the heading line
        """
        for heading in self.headings:
            if start_heading_line.startswith(
                    heading.header_text.split(":")[0]):
                return heading
        raise LookupError(
            f"Could not find heading that starts with: {start_heading_line}")

    def get_title_heading(self) -> SectionHeading:
        """ The Title heading of the document. """
        if not self.headings[0].header_text.startswith("# "):
            raise AssertionError(
                "First heading in the skeleton was not the title.")
        return self.headings[0]

    def check_if_topic_file_matches(self, topic_file_path: Path) -> bool:
        """
        Checks if the topic file headings and meta text matches the skeleton.
        Prints the differences between the topic file and the skeleton, if a
        miss mach is detected.

        Args:
            topic_file_path: path to the topic file to check

        Returns: `True` if the topic matches, otherwise, `False`
        """
        with open(topic_file_path, "r") as topic_file:
            current_heading_iter = iter(self.headings)
            current_heading = None
            expected_meta_text: tp.List[str] = []

            for line in topic_file.readlines():
                if line.startswith("#"):
                    if current_heading is not None and expected_meta_text:
                        print("Found missing italics:")
                        print(f"Expected: {expected_meta_text[0]}")
                        return False

                    current_heading = next(current_heading_iter)
                    expected_meta_text = copy(current_heading.meta_text)
                if line.startswith("_"):
                    if not expected_meta_text:
                        print("Did not expect further italics but found:")
                        print(line)
                        return False

                    if line == expected_meta_text[0]:
                        expected_meta_text.pop(0)
                    else:
                        print("Found italics text did not match the skeleton:")
                        print(f"Found:\n{line}")
                        print(f"Expected:\n{expected_meta_text[0]}")
                        return False

            return True

    def update_topic_meta_text(self, topic_file_path: Path) -> None:
        """
        Update the meta text of a topic file according to this skeleton.

        Args:
            topic_file_path: path to the topic file
        """
        doc_lines = []
        headings_iter = iter(self.headings)

        with open(topic_file_path, "r") as topic_file:
            emitting_doc_text = True
            for line in topic_file.readlines():
                if line.startswith("##"):
                    next_heading = next(headings_iter)
                    current_heading = self.lookup_heading(line.split(":")[0])

                    # Add headers that are completely missing
                    while (current_heading.header_text !=
                           next_heading.header_text):
                        print(f"Could not find section "
                              f"({next_heading.header_text}) before section "
                              f"({current_heading.header_text}).")
                        if _cli_yn_choice("Should I insert it before?"):
                            doc_lines.append(next_heading.header_text)
                            doc_lines.extend(
                                next_heading.convert_meta_text_to_lines())

                        next_heading = next(headings_iter)

                    emitting_doc_text = False

                    # Write out heading
                    doc_lines.append(line)
                    doc_lines.extend(
                        current_heading.convert_meta_text_to_lines())

                elif line.startswith("#"):
                    # Verify that the title heading has correct meta text
                    emitting_doc_text = False
                    next_heading = next(headings_iter)
                    doc_lines.append(line)
                    doc_lines.extend(
                        self.get_title_heading().convert_meta_text_to_lines())
                elif line.startswith("_") or line.strip().endswith("_"):
                    # Ignore meta lines
                    continue
                elif emitting_doc_text or line != "\n":
                    # Skip new lines if we aren't emitting normal document text
                    emitting_doc_text = True
                    doc_lines.append(line)

        # Add missing section headings at the end
        try:
            while True:
                next_heading = next(headings_iter)
                doc_lines.append(next_heading.header_text + os.linesep)
                doc_lines.extend(next_heading.convert_meta_text_to_lines())
        except StopIteration:
            pass

        # Remove excessive newlines
        doc_lines[-1] = doc_lines[-1].rstrip() + os.linesep

        with open(topic_file_path, "w") as tmp_file:
            for line in doc_lines:
                tmp_file.write(line)

    def __parse_headings(self) -> None:
        with open(self.__skeleton_file_path, "r") as skeleton_file:
            for line in skeleton_file.readlines():
                if line.startswith("#"):
                    self.headings.append(SectionHeading(line.strip()))
                elif line.startswith("_") or line.strip().endswith("_"):
                    if not self.headings:
                        raise AssertionError(
                            "Found italics skeleton text before first heading."
                        )
                    self.headings[-1].append_meta_text(line)

    def __str__(self) -> str:
        skeleton_text = ""
        for heading in self.headings:
            skeleton_text += str(heading) + "\n"
        return skeleton_text


def check_skeletons(skeleton: Skeleton,
                    topic_paths: tp.Iterator[Path]) -> None:
    """
    Check of the topics files match the skeleton.

    Args:
        skeleton: base skeleton to compare the topics against
        topic_paths: list of paths to topic files
    """
    for topic_path in topic_paths:
        if skeleton.check_if_topic_file_matches(topic_path):
            print(f"All meta-text in {topic_path} matched the skeleton.")


def update_skeletons(skeleton: Skeleton,
                     topic_paths: tp.Iterator[Path]) -> None:
    """
    Update the topics files to match the skeleton.

    Args:
        skeleton: base skeleton, used as a ground truth
        topic_paths: list of paths to topic files
    """
    for path in topic_paths:
        skeleton.update_topic_meta_text(path)


def main() -> None:
    """ Driver function for the topic fixer tool.  """
    parser = ArgumentParser("topic_updater")
    parser.add_argument("--check",
                        action="store_true",
                        default=False,
                        help="Check if the topic files match the skeleton.")
    parser.add_argument("--update",
                        action="store_true",
                        default=False,
                        help="Update topic files according to the skeleton.")
    parser.add_argument("--skeleton-file",
                        type=Path,
                        default=Path("skeleton.md"),
                        help="Provide alternative skeleton file.")
    parser.add_argument("topic_paths",
                        nargs="*",
                        default=None,
                        type=Path,
                        help="List of paths to topic files, if no paths "
                        "are provided all topic files are used.")

    args = parser.parse_args()

    if not args.skeleton_file.exists():
        print(f"Could not find skeleton file {args.skeleton_file}")
        return
    skeleton = Skeleton(args.skeleton_file)

    if not args.topic_paths:

        def exclude_non_topic_files(path: Path) -> bool:
            return not (path.name == "skeleton.md"
                        or str(path).startswith(".github"))

        topic_paths = filter(exclude_non_topic_files,
                             Path(".").glob("**/*.md"))
    else:
        topic_paths = args.topic_paths

    # Verify that all topic paths exist
    for topic_path in topic_paths:
        if not topic_path.exists():
            print(f"Could not find topic file {topic_path}")
            return

    if args.check:
        check_skeletons(skeleton, topic_paths)
    elif args.update:
        update_skeletons(skeleton, topic_paths)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
