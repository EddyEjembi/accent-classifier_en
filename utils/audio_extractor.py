import librosa
import soundfile as sf

class AudioExtractor:
    def process_audio(self, audio_path):
        """
        Clean and prepare audio for classification
        """
        # Load audio file
        audio, sr = librosa.load(audio_path, sr=16000)
        
        # Remove silence from beginning and end
        audio_trimmed, _ = librosa.effects.trim(audio, top_db=20)
        
        # Save processed audio
        processed_path = audio_path.replace('.wav', '_processed.wav')
        sf.write(processed_path, audio_trimmed, sr)
        
        print(f"Processed audio saved to: {processed_path}")
        return processed_path
        