"""
"""

from pathlib import Path
import unittest
import io

import build.generate_main as gm

TEST_INPUTS = Path("tests/TEST_INPUTS/")


def _trim_include(line: str) -> str:
    return line[12:-1]


class TestMainGeneration(unittest.TestCase):
    """
    Tests the main generator functionallity that is used to automatically
    generate a complete main file with all modules.
    """
    def test_is_placeholder_actual_placeholder(self):
        """Check is_placeholder correctly identifies a placeholder file."""
        self.assertTrue(
            gm.is_placeholder(TEST_INPUTS / "test_modules" /
                              "test_placeholder.md"))

    def test_is_placeholder_does_not_identify_other_files(self):
        """Check is_placeholder does not identifies other files as
        placeholders."""
        self.assertFalse(
            gm.is_placeholder(TEST_INPUTS / "test_modules" /
                              "test_wrong_placeholder.md"))

    def test_that_inject_modules_correctly_injects_includes(self):
        """
        Checks that `inject_teaching_modules` correctly injects all available
        teaching modules into the given file.
        """
        output_buffer = io.StringIO()
        gm.inject_teaching_modules(output_buffer, TEST_INPUTS / "test_modules")

        generated_include_lines = [
            s for s in output_buffer.getvalue().splitlines() if s
        ]

        for include_line in generated_include_lines:
            self.assertTrue(include_line.startswith("__INCLUDE__("))
            self.assertTrue(include_line.endswith(")"))

        generated_include_lines = sorted(
            list(map(_trim_include, generated_include_lines)))

        self.assertEqual(
            generated_include_lines[0],
            "tests/TEST_INPUTS/test_modules/test_empty_module.md")
        self.assertEqual(
            generated_include_lines[1],
            "tests/TEST_INPUTS/test_modules/test_wrong_placeholder.md")
