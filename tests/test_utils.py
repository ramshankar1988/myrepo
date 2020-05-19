import unittest

from tutor import utils


class UtilsTests(unittest.TestCase):
    def test_common_domain(self):
        self.assertEqual(
            "domain.com", utils.common_domain("sub1.domain.com", "sub2.domain.com")
        )
        self.assertEqual(
            "sub1.domain.com",
            utils.common_domain("sub1.domain.com", "sub2.sub1.domain.com"),
        )
        self.assertEqual("com", utils.common_domain("domain1.com", "domain2.com"))
        self.assertEqual(
            "domain.com", utils.common_domain("sub.domain.com", "ub.domain.com")
        )

    def test_reverse_host(self):
        self.assertEqual("com.google.www", utils.reverse_host("www.google.com"))

    def test_list_if(self):
        self.assertEqual('["cms"]', utils.list_if([("lms", False), ("cms", True)]))

    def test_encrypt_decrypt(self):
        password = "passw0rd"
        encrypted1 = utils.encrypt(password)
        encrypted2 = utils.encrypt(password)
        self.assertNotEqual(encrypted1, encrypted2)
        self.assertTrue(utils.verify_encrypted(encrypted1, password))
        self.assertTrue(utils.verify_encrypted(encrypted2, password))
