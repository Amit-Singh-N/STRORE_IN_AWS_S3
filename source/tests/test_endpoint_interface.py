import pytest
from endpoint_client.endpoint_interface import EndPointDownloader

class TestClass:
    def test_download_json(self):
        endpoint_object = EndPointDownloader()
        assert endpoint_object.download_json() == 1


    def test_download_json_exception(self):
        endpoint_object = EndPointDownloader()
        endpoint_object.file_name="abcd"
        assert endpoint_object.download_json() == pytest.raises(SystemExit)
# test_download_json_exception()
#test_download_json()

