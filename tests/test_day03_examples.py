"""Smoke tests for the Day 03 example scripts."""

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples" / "day03"


class Day03ExampleTests(unittest.TestCase):
    def run_example(self, filename: str) -> str:
        result = subprocess.run(
            [sys.executable, str(EXAMPLES / filename)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout

    def test_hello_world(self):
        self.assertEqual(self.run_example("hello_world.py"), "Hello World!\n")

    def test_print_basics_contains_expected_outputs(self):
        output = self.run_example("print_basics.py")
        self.assertGreaterEqual(output.count("Hello World!\n"), 2)
        self.assertIn("2026-10-24\n", output)
        self.assertIn("This is the first part and this is the second part.\n", output)
        self.assertIn("Age: 18\n", output)

    def test_comments_script_runs(self):
        output = self.run_example("comments.py")
        self.assertIn("Welcome to Python!\n", output)
        self.assertIn("This is a hashtag: #python\n", output)
        self.assertIn("Hello!\n", output)


if __name__ == "__main__":
    unittest.main()
