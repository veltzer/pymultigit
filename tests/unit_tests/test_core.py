"""Behavioural tests for pymultigit's pure helpers."""

import os
import tempfile
import unittest

from pymultigit import core


class IsGitFolderTests(unittest.TestCase):
    def test_directory_with_git_subdir_is_git_folder(self):
        with tempfile.TemporaryDirectory() as d:
            os.mkdir(os.path.join(d, ".git"))
            self.assertTrue(core.is_git_folder(d))

    def test_directory_without_git_subdir_is_not(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertFalse(core.is_git_folder(d))

    def test_nonexistent_path_is_not(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertFalse(core.is_git_folder(os.path.join(d, "nope")))

    def test_git_as_file_not_dir_is_not(self):
        # a submodule's ".git" is a file, not a directory; that must not count
        with tempfile.TemporaryDirectory() as d:
            with open(os.path.join(d, ".git"), "w", encoding="utf-8"):
                pass
            self.assertFalse(core.is_git_folder(d))
