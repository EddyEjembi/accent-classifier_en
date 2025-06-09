
# English Accent Classifier

A simple [web application](https://accent-classifieren.streamlit.app/) that analyzes English accents from video URLs using state-of-the-art speech and machine learning models.

## Application Features

- **Multi-Platform Support**: Works with YouTube, Loom, and direct MP4 video links
- **Real-time Processing**: Download, extract, and analyze audio from videos automatically
- **High Accuracy**: Uses pre-trained Wav2Vec2 models optimized for English accent classification
- **User-friendly Interface**: A simple and clean Streamlit web interface with progress tracking
- **Comprehensive Analysis**: Provides confidence scores and detailed accent breakdowns

## Application Demo

![Demo of the application running.](./assets/Streamlit%20-%20Google%20Chrome%202025-06-09%2018-08-16.gif)

The application processes videos through three main stages:
1. **Video Download**: Extracts audio from video URLs using `yt-dlp` package.
2. **Audio Processing**: Cleans and preprocesses audio for optimal classification
3. **Accent Classification**: Analyzes speech patterns using advanced ML models

## Installation

### Prerequisites

- Python 3.8+
- FFmpeg (for audio processing)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/eddyejembi/accent-classifier_en.git
   cd accent-classifier_en
   ```

2. **Create virtual environment**
   ```bash
   # Bash
   python -m venv accentclasify
   
   # Windows
   accentclasify\Scripts\activate
   
   # macOS/Linux
   source accentclasify/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install FFmpeg**
   
   **Windows:**
   - Download from [FFmpeg.org](https://ffmpeg.org/download.html)
   - Or use Chocolatey: `choco install ffmpeg`
   
   **macOS:**
   ```bash
   brew install ffmpeg
   ```
   
   **Linux:**
   ```bash
   sudo apt update
   sudo apt install ffmpeg
   ```

## Project Structure

```
accent-classifier_en/
├── .streamlit/
│   └── config.toml              # Streamlit configuration
├── utils/
│   ├── __init__.py
│   ├── video_processor.py       # Video downloading and audio extraction
│   ├── audio_extractor.py       # Audio preprocessing and cleaning
│   └── accent_classifier.py     # ML model for accent classification
├── tests/
│   ├── __init__.py
│   └── test.py                  # Unit tests and validation
├── temp_downloads/              # Temporary storage for processed files
├── pretrained_models/           # Cached ML models
├── app.py                       # Main Streamlit application
├── requirements.txt             # Python dependencies
└── README.md                    # Project Documentation
```

## Application Usage

### Run the Streamlit Application
```bash
streamlit run app.py
```

### Testing: Individual Components, general pipeline and project workflow
```bash
python -m tests.test
```

## Web Interface

1. **Open your browser** to the displayed URL (typically `http://localhost:8501`)
2. **Enter a video URL** in the input field:
   - YouTube: `https://www.youtube.com/watch?v=VIDEO_ID`
   - Loom: `https://www.loom.com/share/VIDEO_ID`
   - Direct MP4: `https://example.com/video.mp4`
3. **Click "Analyze Accent"** to start processing
4. **View Results**: See detected accent, confidence score, and analysis summary

## Technical Details

### Architecture

The application follows a modular architecture with three main components:

#### 1. Video Processor (`utils/video_processor.py`)
- Uses [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) for robust video downloading
- Extracts audio in WAV format at 16kHz sample rate
  + Reason: The model was trained on this sample rate.
- Handles multiple video platforms and formats
- Implements error handling for network issues

#### 2. Audio Extractor (`utils/audio_extractor.py`)
- Leverages `librosa` for audio preprocessing
- Removes silence and normalizes audio levels
- Converts to standard format for ML models
- Optimizes audio quality for speech recognition

#### 3. Accent Classifier (`utils/accent_classifier.py`)
- Built on SpeechBrain's Wav2Vec2 architecture
- Uses pre-trained models from HuggingFace Hub
- Supports multiple English accent variations
- Provides confidence scores and detailed analysis

### Models Used

- **Base Model**: [`Jzuluaga/accent-id-commonaccent_ecapa`](https://huggingface.co/Jzuluaga/accent-id-commonaccent_ecapa)
- **Architecture**: ECAPA-TDNN architecture
- **Training Data**: CommonAccent dataset with English varieties
- **Supported Accents**: American, British, Australian, Canadian, Indian, and more.
- **Brief Description**: The model is a finetuned version of SpeechBrain's [`spkrec-ecapa-voxceleb (VoxCeleb)`](https://huggingface.co/speechbrain/spkrec-ecapa-voxceleb). It was finetuned to recognize various English accents. Further finetuning might be needed for production or using a different and more accurate model for production.

### Performance Optimizations

- **Caching**: The Model is loaded once and cached using Streamlit's `@st.cache_resource`
- **Batch Processing**: Efficient audio processing with librosa
- **Memory Management**: Automatic cleanup of temporary files after use.
- **Error Recovery**: Robust error handling with graceful degradation

## Supported Accents

The classifier can identify the following English accent categories:

- us
- england
- australia
- indian
- canada
- bermuda
- scotland
- african
- ireland
- newzealand
- wales
- malaysia
- philippines
- singapore
- hongkong
- southatlandtic



## Troubleshooting

### Common Issues

#### 1. Symlink Permission Error (Windows)
```
OSError: [WinError 1314] A required privilege is not held by the client
```
**Solution**: Enable Developer Mode in Windows Settings or run as Administrator

#### 2. FFmpeg Not Found
```
FileNotFoundError: [Errno 2] No such file or directory: 'ffmpeg'
```
**Solution**: Install FFmpeg and ensure it's in your system PATH. [Installation Guide](#Setup-Instructions)

#### 3. Model Download Issues
```
ConnectionError: Failed to download model
```
**Solution**: Check internet connection and ensure HuggingFace Hub access


### System Requirements
- **OS**: Windows 10/11, macOS 10.14+, or Linux
- **Python**: 3.8+
- **RAM**: 8GB minimum, 16GB recommended
- **Storage**: 5GB free space for models and temporary files
- **Network**: Broadband internet for video downloads

## Contributing

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit changes**: `git commit -m 'Add amazing feature'`
4. **Push to branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**


## Support

For questions, issues, or contributions, connect with me on any of these platform:

- 🐦[ X (Twitter)](https://x.com/eddyejembi)
- 💼[ LinkedIn](https://www.linkedin.com/in/eddyejembi/)
- 📬[ Mail](mailto:eddyejembi2018@gmail.com)

