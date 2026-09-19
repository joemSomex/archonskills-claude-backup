import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).parents[1] / "scripts" / "obsidian_memory.py"


class ObsidianMemoryCliTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.vault = Path(self.tmp.name) / "Vault"

    def tearDown(self):
        self.tmp.cleanup()

    def run_cli(self, *args, expected=0):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--vault", str(self.vault), *args],
            text=True,
            capture_output=True,
        )
        self.assertEqual(result.returncode, expected, result.stderr)
        return result

    def test_save_creates_structured_markdown_in_memory_folder(self):
        result = self.run_cli(
            "save",
            "Database Decision",
            "Use PostgreSQL for the primary store.",
            "--source",
            "user request",
        )
        payload = json.loads(result.stdout)
        note = self.vault / payload["path"]
        self.assertEqual(note.parent, self.vault / "Memory")
        text = note.read_text()
        self.assertIn("title: Database Decision", text)
        self.assertIn("source: user request", text)
        self.assertIn("Use PostgreSQL for the primary store.", text)

    def test_save_uses_a_new_filename_instead_of_overwriting(self):
        first = json.loads(self.run_cli("save", "Same title", "first").stdout)
        second = json.loads(self.run_cli("save", "Same title", "second").stdout)
        self.assertNotEqual(first["path"], second["path"])
        self.assertEqual(len(list((self.vault / "Memory").glob("*.md"))), 2)

    def test_search_is_case_insensitive_and_returns_relative_paths(self):
        self.run_cli("save", "API Choice", "Adopt FastAPI for the service.")
        payload = json.loads(self.run_cli("search", "fastapi").stdout)
        self.assertEqual(payload["count"], 1)
        self.assertTrue(payload["results"][0]["path"].startswith("Memory/"))
        self.assertIn("FastAPI", payload["results"][0]["snippet"])

    def test_recall_ranks_multiword_relevance_and_honors_limit(self):
        expected = json.loads(
            self.run_cli(
                "save",
                "API Framework Decision",
                "We chose FastAPI for the backend service.",
            ).stdout
        )
        self.run_cli("save", "Database Decision", "Use PostgreSQL for persistence.")

        payload = json.loads(
            self.run_cli("recall", "our API framework decision", "--limit", "1").stdout
        )

        self.assertEqual(payload["count"], 1)
        self.assertEqual(payload["results"][0]["path"], expected["path"])
        self.assertGreater(payload["results"][0]["score"], 0)
        self.assertIn("FastAPI", payload["results"][0]["snippet"])

    def test_recall_rejects_query_without_meaningful_terms(self):
        result = self.run_cli("recall", "what is the", expected=2)
        self.assertIn("meaningful search term", result.stderr)

    def test_recent_returns_newest_note_first_and_honors_limit(self):
        older = json.loads(self.run_cli("save", "Older", "old content").stdout)
        newer = json.loads(self.run_cli("save", "Newer", "new content").stdout)
        os.utime(self.vault / older["path"], (100, 100))
        os.utime(self.vault / newer["path"], (200, 200))

        payload = json.loads(self.run_cli("recent", "--limit", "1").stdout)

        self.assertEqual(payload["count"], 1)
        self.assertEqual(payload["results"][0]["path"], newer["path"])

    def test_get_rejects_path_traversal(self):
        result = self.run_cli("get", "../outside.md", expected=2)
        self.assertIn("inside the Memory folder", result.stderr)

    def test_empty_content_is_rejected(self):
        result = self.run_cli("save", "Empty", "   ", expected=2)
        self.assertIn("content must not be empty", result.stderr)


if __name__ == "__main__":
    unittest.main()
