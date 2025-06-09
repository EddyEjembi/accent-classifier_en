import os
from utils.video_processor import VideoProcessor
from utils.audio_extractor import AudioExtractor
from utils.accent_classifier import AccentClassifier

# Initialize components
def load_models():
    return {
        'video_processor': VideoProcessor(),
        'audio_extractor': AudioExtractor(),
        'accent_classifier': AccentClassifier()
    }

def process_video(url):
    models = load_models()
    
    # Download video and extract audio
    print(f"Processing video from URL: {url}")
    audio_path = models['video_processor'].download_video(url)
    
    # Process audio to remove silence and prepare for classification
    print(f"Extracted audio saved at: {audio_path}")
    processed_audio_path = models['audio_extractor'].process_audio(audio_path)
    
    # Classify accent from processed audio
    print(f"Classifying accent from audio: {processed_audio_path}")
    result = models['accent_classifier'].classify_accent(processed_audio_path)
    result = models['accent_classifier'].classify_accent(url)

    # Clean up temporary files
    os.remove(audio_path)
    os.remove(processed_audio_path)

    return result

if __name__ == "__main__":
    video_url = "https://youtube.com/shorts/jtAUQ5dk81A?si=ZUmTir2vDcd6ASTa"  # Replace with a valid YouTube URL
    result = process_video(video_url)
    
    print("Accent Classification Result:")
    print(f"Accent: {result['accent']}")
    print(f"Confidence: {result['confidence']}%")
    print(f"Raw Prediction: {result['raw_prediction']}")
    print(f"Summary: {result['summary']}")