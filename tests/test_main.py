import os
import unittest
from io import BytesIO
from unittest.mock import patch
from flask import template_rendered

# Import your Flask app
from vox_bridge.main import app


# Context manager to capture templates rendered
class CaptureTemplates:
    def __init__(self, app):
        self.app = app
        self.templates = []

    def __enter__(self):
        template_rendered.connect(self._capture, self.app)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        template_rendered.disconnect(self._capture, self.app)

    def _capture(self, sender, template, context, **extra):
        self.templates.append((template, context))


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    @patch('vox_bridge.main.convert_audio')
    @patch('vox_bridge.main.transcribe_audio')
    @patch('vox_bridge.main.translate_text')
    def test_api_route_success(self, mock_translate, mock_transcribe, mock_convert):
        # Mock the file processing functions to avoid actual file processing
        mock_translate.return_value = None
        mock_transcribe.return_value = None
        mock_convert.return_value = None

        # Mocking an mp3 file upload
        data = {
            'audioFile': (BytesIO(b'My binary data'), 'audio.mp3')
        }
        
        with CaptureTemplates(app) as templates:
            response = self.client.post('/api', content_type='multipart/form-data', data=data)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(templates.templates), 1)
            template, context = templates.templates[0]
            self.assertEqual(template.name, "result.html")
            # Validate context or rendered content if necessary

    def test_api_route_fail_no_file_selected(self):
        # Testing the API when no file is provided
        data = {}
        response = self.client.post('/api', content_type='multipart/form-data', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("No file selected", response.data.decode())

    def test_api_route_fail_invalid_file_type(self):
        # Testing the API with an invalid file type
        data = {
            'audioFile': (BytesIO(b'My binary data'), 'image.png')
        }
        response = self.client.post('/api', content_type='multipart/form-data', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Invalid file, Please upload an mp3 file.", response.data.decode())

if __name__ == '__main__':
    unittest.main()
