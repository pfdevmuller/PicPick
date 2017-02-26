import pytest
import os.path
import shutil
import time
import json
from .context import picpick
import picpick.picpickapp as ppa
from picpick.imagecollection import ImageCollection

class TestPicPickApp:

    TEST_PROJECT_NAME = 'TestProject'

    def setup_class(self):
        print("setting up for tests")
        self._build_test_image_folder(self)
        image_collection = ImageCollection(self.images_folder)
        ppa.set_image_collection(image_collection)

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

        for dst in self._get_test_image_paths(self, self.images_folder):
            shutil.copyfile(test_image_filename, dst)

    def _get_test_image_paths(self, images_folder):
        return [images_folder + "/test_image_" + str(i) + ".jpg" for i in range(20)]

    def teardown_class(self):
        assert os.path.isdir(self.test_folder), "Could not find test folder to delete it."
        shutil.rmtree(self.test_folder)

    def test_can_get_response_from_test_pic(self):
        response = self.client.get('/'+self.TEST_PROJECT_NAME+'/Pics/test_pic.jpg')
        msg = response.get_data().decode("utf-8")
        assert 'Hello tester' in msg


    def test_can_get_list_of_images(self):
        response = self.client.get('/'+self.TEST_PROJECT_NAME+'/Pics')
        msg = response.get_data().decode("utf-8")
        parsed = json.loads(msg)

        image_paths = self._get_test_image_paths(self.images_folder)
        # We expect paths relative to the image folder, so we trim that off here:
        expected = list(map(lambda path : path.replace(self.images_folder + '/', '', 1), image_paths))
        print("EXPECTED: " + str(expected))
        assert len(expected) > 1, 'Expected more than 1 path in test image path list'

        # TODO use a set here instead!
        assert sorted(parsed) == sorted(expected), "Expected picture list to match test folder contents"





