import pytest
import os.path
import shutil
import time
from .context import picpick
import picpick.picpickapp as ppa

class TestPicPickApp:

    def setup_class(self):
        print("setting up for tests")
        self._build_test_image_folder(self)

        ppa.app.config['TESTING'] = True
        self.client = ppa.app.test_client()

    def _build_test_image_folder(self):
        # Will set up a directory structure of test images
        self.test_folder = "/tmp/picpick_test/" + str(int(time.time()))
        print("Building test image folder at: " + self.test_folder)

        test_image_filename = './tests/test_data/test_image_keyboard.jpg'
        assert os.path.isfile(test_image_filename), "Could not find test image"

        self.images_folder = self.test_folder + "/images"
        if not os.path.exists(self.images_folder):
            os.makedirs(self.images_folder)

        for i in range(20):
            dst = self.images_folder + "/test_image_" + str(i) + ".jpg"
            shutil.copyfile(test_image_filename, dst)

    def teardown_class(self):
        assert os.path.isdir(self.test_folder), "Could not find test folder to delete it."
        shutil.rmtree(self.test_folder)

    def test_against_server(self):
        rv = self.client.get('/TestProject/Pics/test_pic.jpg')
        msg = rv.get_data().decode("utf-8")
        assert 'Hello tester' in msg




