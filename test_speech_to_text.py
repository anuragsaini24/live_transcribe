import contextlib
import io
import unittest
from unittest.mock import patch

import speech_to_text


class ContinuousTranscriptionTests(unittest.TestCase):
    def run_transcription(self, *, recognition_responses=None, listen_side_effect=None):
        output = io.StringIO()
        with patch.object(
            speech_to_text.sr, "Recognizer"
        ) as recognizer_class, patch.object(
            speech_to_text.sr, "Microphone"
        ) as microphone_class, contextlib.redirect_stdout(output):
            recognizer = recognizer_class.return_value
            recognizer.listen.side_effect = listen_side_effect
            recognizer.recognize_google.side_effect = recognition_responses

            speech_to_text.continuous_transcription()

        return recognizer, microphone_class, output.getvalue()

    def test_transcribes_until_stop_keyword(self):
        recognizer, microphone_class, output = self.run_transcription(
            recognition_responses=["Please stop now"]
        )

        microphone_class.assert_called_once_with()
        recognizer.adjust_for_ambient_noise.assert_called_once_with(
            microphone_class.return_value.__enter__.return_value,
            duration=1,
        )
        self.assertIn("Captured: Please stop now", output)
        self.assertIn("Shutting down", output)

    def test_continues_after_unrecognized_speech(self):
        _, _, output = self.run_transcription(
            recognition_responses=[
                speech_to_text.sr.UnknownValueError(),
                "exit",
            ]
        )

        self.assertIn("no speech detected", output)
        self.assertIn("Captured: exit", output)

    def test_stops_on_recognition_request_error(self):
        _, _, output = self.run_transcription(
            recognition_responses=[
                speech_to_text.sr.RequestError("network unavailable")
            ]
        )

        self.assertIn("Check your internet connection", output)

    def test_stops_on_keyboard_interrupt(self):
        _, _, output = self.run_transcription(
            listen_side_effect=KeyboardInterrupt
        )

        self.assertIn("Manual stop detected", output)


if __name__ == "__main__":
    unittest.main()
