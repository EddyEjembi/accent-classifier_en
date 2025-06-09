from speechbrain.pretrained.interfaces import foreign_class

ACCENT_MAPPING = {
    'us': 'American',
    'england': 'British',
    'australia': 'Australian',
    'indian': 'Indian',
    'canada': 'Canadian',
    'scotland': 'Scottish',
    'ireland': 'Irish',
    'wales': 'Welsh',
    'newzealand': 'New Zealand',
    'singapore': 'Singaporean',
    'malaysia': 'Malaysian',
    'philippines': 'Filipino',
    'hongkong': 'Hong Kong',
    'african': 'African',
    'bermuda': 'Bermudian',
    'southatlantic': 'South Atlantic'
}

class AccentClassifier:
    def __init__(self):
        # English accent classification model from SpeechBrain
        self.classifier = foreign_class(
            source="Jzuluaga/accent-id-commonaccent_xlsr-en-english", 
            pymodule_file="custom_interface.py", 
            classname="CustomEncoderWav2vec2Classifier"
        )
        
        # Accent mapping
        self.accent_mapping = ACCENT_MAPPING
    
    def classify_accent(self, audio_path):
        """
        Classify English accent from audio file extracted from a video URL.
        param:
            audio_path: Path to the audio file
        return: 
            Dictionary with accent, confidence, raw prediction, and summary
        """
        
        try:
            # Get prediction
            out_prob, score, index, text_lab = self.classifier.classify_file(audio_path)
            
            # Extract results
            raw_accent = text_lab[0] 
            confidence = float(score.max()) * 100  # Convert to percentage
            accent_name = self.accent_mapping.get(raw_accent, raw_accent.title())
            
            return {
                'accent': accent_name,
                'confidence': round(confidence, 2),
                'raw_prediction': raw_accent,
                'summary': f"Detected {accent_name} accent with {confidence:.1f}% confidence"
            }
            
        except Exception as e:
            return {
                'accent': 'Unknown',
                'confidence': 0,
                'error': str(e),
                'summary': 'Could not classify accent due to processing error'
            }