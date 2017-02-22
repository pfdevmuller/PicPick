import pytest
from .context import picpick
import picpick.picpickapp as ppa

class TestPicPickApp:

    def setup_class(self):
        print("setting up for tests")
        ppa.app.config['TESTING'] = True
        self.client = ppa.app.test_client()

    def teardown_class(self):
        pass

    def test_against_server(self):
        rv = self.client.get('/TestProject/Pics/test_pic.jpg')
        msg = rv.get_data().decode("utf-8")
        assert 'Hello tester' in msg

