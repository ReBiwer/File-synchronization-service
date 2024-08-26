import unittest
from types_project.type_response import ResponseStatus
from yandex_disk import CloudDisk


class TestCloudDisk(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.testedCloudDisk = CloudDisk()
        cls.HTTP_code_200 = ResponseStatus(200)

    def test_get_info_cloud_disk(self):
        _, res_code_status = self.testedCloudDisk.get_info_cloud_disk()
        self.assertEqual(res_code_status, self.HTTP_code_200)

