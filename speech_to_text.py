import speech_recognition as sr

def continuous_transcription():
    recognizer = sr.Recognizer()
    # Adjust this if the script stops too early or waits too long
    recognizer.pause_threshold = 0.8 

    with sr.Microphone() as source:
        print(">>> Calibrating for background noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print(">>> Continuous listening enabled. (Say 'Stop' to exit)")

        while True:
            try:
                print("\nListening...")
                audio_data = recognizer.listen(source, timeout=None)
                
                # Transcribe the snippet
                text = recognizer.recognize_google(audio_data)
                print(f"Captured: {text}")

                # Check for exit keyword
                if "stop" in text.lower() or "exit" in text.lower():
                    print(">>> Shutting down. Goodbye!")
                    break

            except sr.UnknownValueError:
                # This happens if you don't speak or it's just noise
                print("... (no speech detected) ...")
            except sr.RequestError:
                print(">>> Error: Check your internet connection.")
                break
            except KeyboardInterrupt:
                print("\n>>> Manual stop detected.")
                break

if __name__ == "__main__":
    continuous_transcription()
