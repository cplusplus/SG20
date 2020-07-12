"""
Testing module for the topic_updater script. This modules tests whether the
abstractions, SectionHeading, Skeleton, which are  used in the script correctly
work.
"""
from itertools import dropwhile
from pathlib import Path
import copy
import os
import unittest

import mock

import topic_updater as tu

TEST_INPUTS = Path("tests/TEST_INPUTS/")


class TestSectionHeading(unittest.TestCase):
    """
    Tests the section heading class, which represents a specific secion heading
    in a topic markdown.
    """
    @classmethod
    def setUpClass(cls):
        """ Setup example section header. """
        cls.section_title = "## Section Title"
        cls.test_meta_text_line0 = "_ Some meta text _" + os.linesep
        cls.test_meta_text_line1 = "_ Another line meta text _" + os.linesep

        cls.new_heading = tu.SectionHeading(cls.section_title)
        cls.new_heading.append_meta_text(cls.test_meta_text_line0)

    def test_basic_construction(self):
        """ Checks if we setup the basic section header correclty. """
        new_heading = copy.deepcopy(self.new_heading)

        self.assertEqual(new_heading.header_text, self.section_title)
        self.assertEqual(new_heading.meta_text, [self.test_meta_text_line0])

        new_heading.append_meta_text(self.test_meta_text_line1)

        self.assertEqual(
            new_heading.meta_text,
            [self.test_meta_text_line0, self.test_meta_text_line1])

    def test_meta_text_to_line_conversion(self):
        """ Checks if we correctly generate meta text. """
        new_heading = copy.deepcopy(self.new_heading)
        new_heading.append_meta_text(self.test_meta_text_line1)

        meta_text_lines = new_heading.convert_meta_text_to_lines()

        self.assertEqual(meta_text_lines[0], os.linesep,
                         "First line should be only a linesep.")
        self.assertEqual(meta_text_lines[1], self.test_meta_text_line0)
        self.assertEqual(
            meta_text_lines[2], self.test_meta_text_line1 + os.linesep,
            "The last meta line should have an additional line separator")


class TestSkeleton(unittest.TestCase):
    """
    Tests the skeleton class which loads the topic skeleton from a file and
    parses it.
    """
    @classmethod
    def setUpClass(cls):
        """ Setup small test skeleton which contains all edge cases. """
        cls.test_skeleton = tu.Skeleton(TEST_INPUTS / "test_skeleton.md")

    def test_actual_skeleton_parse(self):
        """
        Checks that we can fully parse the actual skeleton.
        """
        offset_to_main_folder = "../../../"
        actual_skeleton = tu.Skeleton(TEST_INPUTS / offset_to_main_folder /
                                      "skeleton.md")

        self.assertEqual(actual_skeleton.get_title_heading().header_text,
                         "# Module name: topic name")
        headings = list(
            map(lambda heading: heading.header_text, actual_skeleton.headings))
        self.assertEqual(headings[0], "# Module name: topic name")
        self.assertEqual(headings[1], "## Overview")

        self.assertEqual(headings[-2], "### Points to cover")
        self.assertEqual(headings[-1], "## Advanced")

    def test_heading_lookup(self):
        """
        Checks if we can lookup different section headings in the skeleton.
        """
        section_with_user_content = self.test_skeleton.lookup_heading(
            "## Section with user content:")
        missing_mid = self.test_skeleton.lookup_heading(
            "## Missing mid section")

        self.assertEqual(section_with_user_content.header_text,
                         "## Section with user content: provided by the user")
        self.assertEqual(
            section_with_user_content.meta_text[0].rstrip(),
            "_ Example section where user text is in the header _")

        self.assertEqual(missing_mid.header_text, "## Missing mid section")
        self.assertEqual(
            missing_mid.meta_text[0].rstrip(),
            "_ This section could be missing in the middle of the topics _")

    def test_title_heading_lookup(self):
        """
        Checks if we get the correct title heading from the test skeleton.
        """
        self.assertEqual(self.test_skeleton.get_title_heading().header_text,
                         "# Main Title")
        self.assertEqual(
            self.test_skeleton.get_title_heading().meta_text[0],
            "_Skeleton instructions are typeset in italic text._" + os.linesep)

    def test_that_meta_text_with_linebreaks_inbetween_meta_markers_parse(self):
        """
        Checks that we correctly parse meta text that stretches over multiple
        lines.
        """
        multi_line_meta_heading = self.test_skeleton.lookup_heading(
            "## Meta text with line breaks")

        self.assertEqual(multi_line_meta_heading.meta_text[0],
                         "_ Some text here" + os.linesep)
        self.assertEqual(multi_line_meta_heading.meta_text[1],
                         "some after the line break _" + os.linesep)


class TestSkeletonTopicUpdates(unittest.TestCase):
    """
    Test skeleton topic update function. This test tries to cover different
    scenarios that could occure during topic updates and verifies that we
    handle them correctly.
    """
    @classmethod
    def setUpClass(cls):
        """ Setup small test skeleton which contains all edge cases. """
        cls.test_skeleton = tu.Skeleton(TEST_INPUTS / "test_skeleton.md")

    def test_not_to_override_user_provided_heading_text(self):
        """
        Checks that the update method does not override user provided text,
        which is part of some section headings.
        """
        topic_file_path = TEST_INPUTS / "user_content_heading_topic.md"
        with open(topic_file_path, "r") as topic_file:
            updated_topic_lines = self.test_skeleton.update_topic_meta_text(
                topic_file)

            start_test_scope_lines = list(
                dropwhile(
                    lambda line: not line.startswith(
                        "## Section with user content:"), updated_topic_lines))

            self.assertTrue(
                start_test_scope_lines[0].endswith(
                    " This is provided by the user" + os.linesep),
                "User provided content was modified")

    def test_that_we_dont_override_user_text_in_sections(self):
        """
        Checks that when we don't change user written text in section when
        updating the topic.
        """
        topic_file_path = TEST_INPUTS / "user_content_heading_topic.md"
        with open(topic_file_path, "r") as topic_file:
            updated_topic_lines = self.test_skeleton.update_topic_meta_text(
                topic_file)

            start_test_scope_lines = list(
                dropwhile(
                    lambda line: not line.startswith(
                        "Users can add different content here"),
                    updated_topic_lines))

            self.assertTrue(
                start_test_scope_lines[0].startswith(
                    "Users can add different content here."),
                "User provided content was modified")
            self.assertTrue(start_test_scope_lines[1].startswith("<table>"),
                            "User provided content was modified")
            self.assertTrue(start_test_scope_lines[2].startswith("</table>"),
                            "User provided content was modified")

    @mock.patch('topic_updater._cli_yn_choice')
    def test_if_missing_section_gets_added_to_the_end(self, mock_cli_yn):
        """
        Checks if a section that is missing at the end of the topic file gets
        automatically added.
        """
        mock_cli_yn.return_value = True
        topic_file_path = TEST_INPUTS / "missing_sections.md"
        with open(topic_file_path, "r") as topic_file:
            updated_topic_lines = self.test_skeleton.update_topic_meta_text(
                topic_file)

            self.assertEqual(
                updated_topic_lines[-3].rstrip(), "## Missing end section",
                "Missing section was not added to the end of the file.")
            self.assertEqual(
                updated_topic_lines[-1].rstrip(),
                "_ This section could be missing at the end of the document _")

    @mock.patch('topic_updater._cli_yn_choice')
    def test_if_missing_section_gets_added_in_the_middle(self, mock_cli_yn):
        """
        Checks if a section that is missing in the middle of the topic file
        gets added if the user wants it. The test assumes the user supplies
        yes as an answer.
        """
        mock_cli_yn.return_value = True
        topic_file_path = TEST_INPUTS / "missing_sections.md"
        with open(topic_file_path, "r") as topic_file:
            updated_topic_lines = self.test_skeleton.update_topic_meta_text(
                topic_file)

            # Reduces the topic lines to only contain sections and removes all
            # lines before the test scope, i.e., the section before the missing
            # section.
            start_test_scope_lines = list(
                filter(
                    lambda line: line.startswith("##"),
                    dropwhile(
                        lambda line: not line.startswith(
                            "## Section with user content"),
                        iter(updated_topic_lines))))

            # Verify that the previous section is correct
            self.assertTrue(
                start_test_scope_lines[0].startswith(
                    "## Section with user content"),
                "The section before the added missing section is wrong.")

            # Verify the section was inserted
            self.assertEqual(
                start_test_scope_lines[1].rstrip(), "## Missing mid section",
                "The missing section was not inserted correctly.")

            # Verify the next section is correct
            self.assertTrue(
                start_test_scope_lines[2].startswith(
                    "## Italics text should be updated"),
                "The section after the added missing section is wrong.")

    def test_that_meta_text_gets_updated(self):
        """
        Checks that meta text in the topic gets updated according to the
        skeleton.
        """
        topic_file_path = TEST_INPUTS / "fix_wrong_sections.md"
        with open(topic_file_path, "r") as topic_file:
            updated_topic_lines = self.test_skeleton.update_topic_meta_text(
                topic_file)

            topic_lines_starting_from_italics_section = list(
                dropwhile(
                    lambda line: not line.startswith(
                        "## Italics text should be updated"),
                    iter(updated_topic_lines)))
            self.assertEqual(
                topic_lines_starting_from_italics_section[0].rstrip(),
                "## Italics text should be updated",
                "Could not find italics section.")
            self.assertEqual(
                topic_lines_starting_from_italics_section[2].rstrip(),
                "_ Updated italics text. _")

    def test_topic_does_not_end_in_empty_line(self):
        """
        Checks that the update topic lines do not end with and empty line.
        """
        topic_file_path = TEST_INPUTS / "user_content_heading_topic.md"
        with open(topic_file_path, "r") as topic_file:
            updated_topic_lines = self.test_skeleton.update_topic_meta_text(
                topic_file)

            self.assertNotEqual(updated_topic_lines[-1], os.linesep)

    def test_newline_between_heading_and_meta_text(self):
        """
        Checks that we emit a newline between the heading and the meta text.
        """
        topic_file_path = TEST_INPUTS / "user_content_heading_topic.md"
        with open(topic_file_path, "r") as topic_file:
            updated_topic_lines = self.test_skeleton.update_topic_meta_text(
                topic_file)

            start_test_scope_lines = list(
                dropwhile(
                    lambda line: not line.startswith("## Section with user"),
                    updated_topic_lines))
            self.assertEqual(start_test_scope_lines[1], os.linesep,
                             "No newline between heading and meta text.")
            self.assertTrue(
                start_test_scope_lines[2].startswith("_ Example section"))
