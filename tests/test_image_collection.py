import pytest
from .context import picpick
from picpick.imagecollection import ImageCollection

TEST_FOLDER = './tests/test_data'
JPG_FILE = 'test_image_keyboard.jpg'
PNG_FILE = 'test_image_tv.png'
SUBDIR_FILE = 'data_in_subdir/test_image_chill_out.jpg'

def test_finds_jpg():
    ic = ImageCollection(TEST_FOLDER)
    assert JPG_FILE in ic.pictures, "Collection should include jpg file"

def test_finds_png():
    ic = ImageCollection(TEST_FOLDER)
    assert PNG_FILE in ic.pictures, "Collection should include png file"

def test_finds_recursively():
    ic = ImageCollection(TEST_FOLDER)
    assert SUBDIR_FILE in ic.pictures, "Collection should include file from subdir"
