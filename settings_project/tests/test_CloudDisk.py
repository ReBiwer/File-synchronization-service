import unittest
from settings_project.types_project.type_info_yandex_disk import ResponseStatus
from settings_project.working_directories.cloud_dir import CloudDir


class TestCloudDisk(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.testedCloudDisk = CloudDir()
        cls.HTTP_code_200 = ResponseStatus(200)

    def test_get_info_cloud_disk(self):
        _, res_code_status = self.testedCloudDisk.get_info_cloud_disk()
        self.assertEqual(res_code_status, self.HTTP_code_200)
