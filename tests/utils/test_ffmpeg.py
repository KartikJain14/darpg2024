import unittest
from unittest.mock import patch, MagicMock
from vox_bridge.utils.ffmpeg import convert_audio # Replace with the name of your module where convert_audio is defined

class TestConvertAudio(unittest.TestCase):

    @patch('your_module.ffmpeg.input')
    def test_convert_audio(self, mock_input):
        # Setup mocks
        mock_output = MagicMock()
        mock_input.return_value.output.return_value.overwrite_output.return_value.run = MagicMock()

        # Call the function to test
        convert_audio('input.mp3', 'output.wav')

        # Assertions to ensure ffmpeg was called correctly
        mock_input.assert_called_once_with('input.mp3')
        mock_input.return_value.output.assert_called_once_with('output.wav', acodec='pcm_s16le', ac=1, ar='16000', loglevel="quiet")
        mock_input.return_value.output.return_value.overwrite_output.assert_called_once()
        mock_input.return_value.output.return_value.overwrite_output.return_value.run.assert_called_once()

if __name__ == '__main__':
    unittest.main()
