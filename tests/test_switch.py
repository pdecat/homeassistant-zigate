"""Test zigate switch."""
import unittest


class TestSwitch(unittest.TestCase):
    def test_switch(self):
        from custom_components.zigate import switch  # noqa


if __name__ == '__main__':
    unittest.main()
