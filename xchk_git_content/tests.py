import unittest
import regex
from django.test import TestCase
from unittest.mock import Mock, patch, MagicMock
from xchk_regex_strategies.strats import RegexCheck
from xchk_core.models import SubmissionV2
from xchk_core.templatetags.xchk_instructions import node_instructions_2_ul
from xchk_core.strats import StratInstructions, AT_LEAST_ONE_TEXT, ALL_OF_TEXT
from .contentviews import WhatIsGitView

class WhatIsGitRegexCheckTest(TestCase):

    def test_non_dutch_language_link(self):
        text = r"""https://git-scm.com/book/en/v2"""
        self.assertTrue(WhatIsGitView._incorrect_lang_regex.fullmatch(text))

    def test_non_link(self):
        text = r"""https://ubuntu.com"""
        self.assertFalse(WhatIsGitView._accepted_regex.match(text))

if __name__ == '__main__':
    unittest.main()
