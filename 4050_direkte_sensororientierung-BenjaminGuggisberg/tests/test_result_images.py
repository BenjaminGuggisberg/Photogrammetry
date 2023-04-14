import os
import unittest


class TestImageWriter(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.path = os.path.dirname(os.path.dirname(__file__))
        return super().setUpClass()

    def test_res_folder_exists(self):
        self.assertTrue(
            os.path.exists(os.path.join(self.path, 'res'))
            )

    def test_res_image_koll_exists(self):
        self.assertTrue(
            os.path.isfile(
                os.path.join(self.path,'res\object_points_koll.png')
                )
            )

    def test_res_image_proj_geom_exists(self):
        self.assertTrue(
            os.path.isfile(
                os.path.join(self.path,'res\object_points_proj_geometry.png')
                )
            )

if __name__ == "__main__":
    unittest.main()