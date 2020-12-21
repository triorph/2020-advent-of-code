import unittest
from .day19 import RuleCheckerDay19


class TestRuleCheckerDay19(unittest.TestCase):
    def test_day_a(self):
        d19a = RuleCheckerDay19("example_data.txt")
        self.assertTrue(d19a.evaluate_rule_zero("ababbb"))
        self.assertTrue(d19a.evaluate_rule_zero("abbbab"))
        self.assertFalse(d19a.evaluate_rule_zero("bababa"))
        self.assertFalse(d19a.evaluate_rule_zero("aaabbb"))
        self.assertFalse(d19a.evaluate_rule_zero("aaaabbb"))
        print(d19a._data)
        self.assertEqual(d19a.day_a(), 2)

    def test_day_b(self):
        d19b = RuleCheckerDay19("example_datab.txt")
        self.assertEqual(d19b.day_a(), 3)
        d19b.add_day_b_rules()
        self.assertTrue(d19b.evaluate_rule_zero("bbabbbbaabaabba"))
        self.assertTrue(d19b.evaluate_rule_zero("babbbbaabbbbbabbbbbbaabaaabaaa"))
        self.assertTrue(
            d19b.evaluate_rule_zero("aaabbbbbbaaaabaababaabababbabaaabbababababaaa")
        )
        self.assertTrue(d19b.evaluate_rule_zero("bbbbbbbaaaabbbbaaabbabaaa"))
        self.assertTrue(d19b.evaluate_rule_zero("bbbababbbbaaaaaaaabbababaaababaabab"))
        self.assertTrue(d19b.evaluate_rule_zero("ababaaaaaabaaab"))
        self.assertTrue(d19b.evaluate_rule_zero("ababaaaaabbbaba"))
        self.assertTrue(d19b.evaluate_rule_zero("baabbaaaabbaaaababbaababb"))
        self.assertTrue(d19b.evaluate_rule_zero("abbbbabbbbaaaababbbbbbaaaababb"))
        self.assertTrue(d19b.evaluate_rule_zero("aaaaabbaabaaaaababaa"))
        self.assertTrue(d19b.evaluate_rule_zero("aaaabbaabbaaaaaaabbbabbbaaabbaabaaa"))
        self.assertTrue(
            d19b.evaluate_rule_zero("aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba")
        )
        self.assertEqual(d19b.day_b(), 12)