import unittest
from unittest.mock import patch, mock_open
from vox_bridge.utils.translate import translate_text, translate_cli, download_model

class TestTranslateUtils(unittest.TestCase):

    @patch('vox_bridge.utils.translate.package.update_package_index')
    @patch('vox_bridge.utils.translate.package.get_available_packages')
    @patch('vox_bridge.utils.translate.package.install_from_path')
    @patch('vox_bridge.utils.translate.translate.translate')
    def test_translate_text(self, mock_translate, mock_install, mock_get_packages, mock_update_index):
        # Setup mock behavior
        mock_translate.return_value = "This is a test."
        mock_get_packages.return_value = [MockPackage()]
        # Use mock_open to simulate file operations
        with patch("builtins.open", mock_open(read_data="यह एक परीक्षण है।")) as mock_file:
            translate_text("hi_text.txt", "en_text.txt")
            # Add assertion for opening file for reading if applicable
            # mock_file.assert_called_with("hi_text.txt", "r", encoding="utf-8")
            # Add assertion for file open call arguments
            mock_file.assert_called_with("en_text.txt", "w", encoding="utf-8")
            mock_file().write.assert_called_once_with("This is a test.")

    @patch('vox_bridge.utils.translate.package.update_package_index')
    @patch('vox_bridge.utils.translate.package.get_available_packages')
    @patch('vox_bridge.utils.translate.package.install_from_path')
    @patch('vox_bridge.utils.translate.translate.translate')
    def test_translate_cli(self, mock_translate, mock_install, mock_get_packages, mock_update_index):
        # Setup mock behavior
        input_text = "यह एक परीक्षण है।"
        expected_translation = "This is a test."
        mock_translate.return_value = expected_translation
        mock_get_packages.return_value = [MockPackage()]

        translation = translate_cli(input_text)
        self.assertEqual(translation, expected_translation)

    @patch('vox_bridge.utils.translate.package.update_package_index')
    @patch('vox_bridge.utils.translate.package.get_available_packages')
    @patch('vox_bridge.utils.translate.package.install_from_path')
    def test_download_model(self, mock_install, mock_get_packages, mock_update_index):
        mock_get_packages.return_value = [MockPackage()]
        download_model()
        # Assert that install_from_path is called with the correct path
        mock_install.assert_called_once_with("path/to/downloaded/package")
        # Additionally, assert that the other functions are called as expected
        mock_update_index.assert_called_once()
        mock_get_packages.assert_called_once()

class MockPackage:
    def __init__(self):
        self.from_code = "hi"
        self.to_code = "en"

    def download(self):
        return "path/to/downloaded/package"

if __name__ == '__main__':
    unittest.main()
