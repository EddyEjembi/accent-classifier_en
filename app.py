import streamlit as st
import os
from utils.video_processor import VideoProcessor
from utils.audio_extractor import AudioExtractor
from utils.accent_classifier import AccentClassifier

# Initialize components
@st.cache_resource
def load_models():
    return {
        'video_processor': VideoProcessor(),
        'audio_extractor': AudioExtractor(),
        'accent_classifier': AccentClassifier()
    }

def main():
    st.title("🎯 Accent Classifier")
    st.write("Analyze accents from video URLs (Loom, YouTube, MP4 links)")
    
    # Load models
    models = load_models()
    
    # Input
    video_url = st.text_input("Enter Video URL:", placeholder="https://...")
    
    if st.button("Analyze Accent"):
        if not video_url:
            st.error("Please enter a video URL")
            return
            
        try:
            with st.spinner("Processing video..."):
                # Step 1: Download video
                st.info("📥 Downloading video...")
                audio_path = models['video_processor'].download_video(video_url)
                
                # Step 2: Process audio
                st.info("🎵 Processing audio...")
                processed_audio = models['audio_extractor'].process_audio(audio_path)
                
                # Step 3: Classify accent
                st.info("🔍 Classifying accent...")
                result = models['accent_classifier'].classify_accent(processed_audio)
                
                # Display results
                if 'error' not in result:
                    st.success("✅ Analysis Complete!")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Accent", result['accent'])
                    with col2:
                        st.metric("Confidence", f"{result['confidence']}%")
                    
                    st.info(result['summary'])
                    
                    # Clean up files
                    cleanup_files([audio_path, processed_audio])
                else:
                    st.error(f"Error: {result['error']}")
                    
        except Exception as e:
            st.error(f"Processing failed: {str(e)}")

    # Display GitHub link
    st.markdown("[GitHub Repository](https://github.com/EddyEjembi/accent-classifier_en)")

def cleanup_files(file_paths):
    """Remove temporary files"""
    for path in file_paths:
        try:
            if os.path.exists(path):
                os.remove(path)
        except:
            pass

if __name__ == "__main__":
    main()