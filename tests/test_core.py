import unittest

from trafficlens import summarize_flows


class SummarizeFlowsTests(unittest.TestCase):
    def test_groups_records(self):
        rows = summarize_flows([
            {"protocol": "tcp", "source": "a", "destination": "b", "bytes": 20},
            {"protocol": "tcp", "source": "a", "destination": "b", "bytes": 30},
        ])
        self.assertEqual(rows[0]["bytes"], 50)

    def test_rejects_negative_bytes(self):
        with self.assertRaises(ValueError):
            summarize_flows([{"bytes": -1}])


if __name__ == "__main__":
    unittest.main()
