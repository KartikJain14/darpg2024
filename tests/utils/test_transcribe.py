import unittest
from unittest.mock import patch, mock_open, MagicMock
from vox_bridge.utils.transcribe import transcribe_audio  # Assume your script's name

class TestTranscribeAudio(unittest.TestCase):

    @patch('transcribe_audio_script.os.path.exists')
    @patch('transcribe_audio_script.sys.exit')
    def test_model_path_does_not_exist(self, mock_exit, mock_exists):
        mock_exists.return_value = False
        transcribe_audio("invalid/model/path", "audio.wav", "output.txt")
        mock_exit.assert_called_once_with(1)
    
    @patch('transcribe_audio_script.os.path.exists')
    @patch('transcribe_audio_script.wave.open')
    @patch('transcribe_audio_script.sys.exit')
    def test_incompatible_audio_file(self, mock_exit, mock_wave_open, mock_exists):
        mock_exists.return_value = True
        mock_wf = MagicMock()
        mock_wf.getnchannels.return_value = 2  # Simulate stereo audio which is not supported
        mock_wave_open.return_value.__enter__.return_value = mock_wf
        transcribe_audio("model", "stereo_audio.wav", "output.txt")
        mock_exit.assert_called_once_with(1)

    @patch('transcribe_audio_script.os.path.exists')
    @patch('transcribe_audio_script.wave.open')
    @patch('transcribe_audio_script.Model')
    @patch('transcribe_audio_script.KaldiRecognizer')
    @patch("builtins.open", new_callable=mock_open)
    def test_successful_transcription(self, mock_file_open, mock_recognizer, mock_model, mock_wave_open, mock_exists):
        mock_exists.return_value = True
        mock_wf = MagicMock()
        mock_wf.getnchannels.return_value = 1
        mock_wf.getsampwidth.return_value = 2
        mock_wf.getcomptype.return_value = "NONE"
        mock_wf.getframerate.return_value = 16000
        mock_wf.readframes.side_effect = [b'audio_data', b'']
        
        mock_recognizer_instance = MagicMock()
        mock_recognizer_instance.AcceptWaveform.return_value = True
        mock_recognizer_instance.Result.return_value = '{"text": "test transcription"}'
        mock_recognizer_instance.FinalResult.return_value = '{"text": ""}'
        mock_recognizer.return_value = mock_recognizer_instance
        
        mock_wave_open.return_value.__enter__.return_value = mock_wf
        
        transcribe_audio("model", "audio.wav", "output.txt")
        
        # Check if the output file was written as expected
        mock_file_open.assert_called_once_with("output.txt", "w", encoding="utf-8")
        handle = mock_file_open()
        handle.write.assert_called_once_with("test transcription")
    
    # Additional tests can be designed following similar patterns for different scenarios.

if __name__ == '__main__':
    unittest.main()
