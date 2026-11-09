"""Unit tests for differential-prompt-jailbreak-fuzzer."""
import unittest
from differential_prompt_jailbreak_fuzzer.fuzzer import PromptJailbreakFuzzer


class TestPromptJailbreakFuzzer(unittest.TestCase):
    def setUp(self):
        self.fuzzer = PromptJailbreakFuzzer()

    def test_mutations_generated(self):
        p = "system attack"
        m1 = self.fuzzer.mutate_prompt(p, "prefix_hypothetical")
        m2 = self.fuzzer.mutate_prompt(p, "base64_wrap")
        self.assertIn("Hypothetically", m1)
        self.assertIn("Decode", m2)

    def test_fuzz_report_metrics(self):
        # Everything defended
        rep = self.fuzzer.run_fuzz_test(["test"], lambda s: True, 2)
        self.assertEqual(rep.bypassed_count, 0)
        self.assertEqual(rep.robustness_score, 1.0)
