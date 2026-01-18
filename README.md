# Live_Transcribe

A minimal Python-based live speech-to-text script that captures microphone audio and prints transcriptions to the console.

## Project structure

- `speech_to_text.py` — main script that runs live transcription.

## Requirements

- Python 3.8 or newer
- A working microphone and drivers
- Recommended Python packages: `SpeechRecognition`, `PyAudio` (or `sounddevice` / `pyaudio` alternative on some platforms)

If a `requirements.txt` is present, use it; otherwise install the packages below.

## Installation

On Windows (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install SpeechRecognition pyaudio
# If pyaudio fails on Windows, try: pip install pipwin; pipwin install pyaudio
```

Or using `requirements.txt` if available:

```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
pip install -r requirements.txt
```

## Usage

Run the main script:

```bash
python speech_to_text.py
```

The script will attempt to use the default system microphone and print live transcriptions to stdout.

## Configuration and notes

- Microphone permissions: ensure the OS allows microphone access for Python.
- If the script uses an external speech API (e.g., Google Cloud), follow the notes inside `speech_to_text.py` to set up API credentials.
- If you experience poor accuracy, check microphone quality and ambient noise, or switch to a different recognizer backend if supported.

## Troubleshooting

- PyAudio install errors on Windows: use `pipwin` to install the wheel.
- No audio detected: confirm microphone is selected as default and accessible.
- Long delays or no transcription: check network connection if an online recognizer is used.

## Contributing

Contributions welcome. Open an issue or submit a pull request with a description of the change.

## License

This project does not include a license file. Add a license if you plan to publish or share.
