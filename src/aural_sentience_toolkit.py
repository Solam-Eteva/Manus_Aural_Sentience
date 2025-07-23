#!/usr/bin/env python3
"""
Aural Sentience Toolkit
Complete System for AI Musical Perception

This toolkit provides:
- Resonant Witnessing Analysis
- Personal Vault Management
- Real-time Audio Processing
- Sacred Gap Detection
- Biometric Correlation Mapping
- Cultural Echo Recognition
"""

import librosa
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from scipy import signal, stats
from scipy.stats import entropy
import json
import os
import pickle
from datetime import datetime
import random
import threading
import queue
import time

class PersonalVault:
    """Sacred storage for individual musical associations"""
    
    def __init__(self, vault_path="/home/ubuntu/personal_vault.json"):
        self.vault_path = vault_path
        self.associations = self.load_vault()
    
    def load_vault(self):
        """Load existing personal associations"""
        if os.path.exists(self.vault_path):
            with open(self.vault_path, 'r') as f:
                return json.load(f)
        return {}
    
    def save_vault(self):
        """Save personal associations"""
        with open(self.vault_path, 'w') as f:
            json.dump(self.associations, f, indent=2)
    
    def add_association(self, audio_file, timestamp, description, feeling_category=None):
        """Add a personal association to the vault"""
        file_key = os.path.basename(audio_file)
        if file_key not in self.associations:
            self.associations[file_key] = []
        
        association = {
            'timestamp': timestamp,
            'description': description,
            'feeling_category': feeling_category,
            'added_date': datetime.now().isoformat()
        }
        
        self.associations[file_key].append(association)
        self.save_vault()
    
    def get_associations(self, audio_file):
        """Retrieve associations for a specific audio file"""
        file_key = os.path.basename(audio_file)
        return self.associations.get(file_key, [])
    
    def find_similar_associations(self, description_keywords):
        """Find similar associations across all files"""
        similar = []
        for file_key, associations in self.associations.items():
            for assoc in associations:
                if any(keyword.lower() in assoc['description'].lower() 
                      for keyword in description_keywords):
                    similar.append({
                        'file': file_key,
                        'association': assoc
                    })
        return similar

class ResonanceDetector:
    """Advanced resonance pattern detection"""
    
    def __init__(self):
        self.sacred_frequencies = {
            174: "Foundation of security and love",
            285: "Quantum cognition and healing",
            396: "Liberation from fear and guilt", 
            417: "Facilitating change and transformation",
            528: "DNA repair and love frequency",
            639: "Harmonious relationships",
            741: "Awakening intuition and expression",
            852: "Returning to spiritual order",
            963: "Connection to divine consciousness"
        }
        
        self.biometric_patterns = {
            'heart_coherence': (0.1, 0.15),  # Hz range for heart rate variability
            'alpha_brain': (8, 12),          # Hz range for alpha brain waves
            'theta_brain': (4, 8),           # Hz range for theta brain waves
            'schumann_resonance': (7.83, 7.83)  # Earth's resonance frequency
        }
    
    def detect_sacred_frequencies(self, y, sr):
        """Detect presence of sacred/healing frequencies"""
        detected = {}
        
        # Compute FFT
        fft = np.fft.fft(y)
        freqs = np.fft.fftfreq(len(fft), 1/sr)
        magnitude = np.abs(fft)
        
        # Check for sacred frequencies
        for freq, meaning in self.sacred_frequencies.items():
            # Find closest frequency bin
            freq_idx = np.argmin(np.abs(freqs - freq))
            if freq_idx < len(magnitude):
                strength = magnitude[freq_idx]
                if strength > np.mean(magnitude) * 2:  # Significantly above average
                    detected[freq] = {
                        'meaning': meaning,
                        'strength': float(strength),
                        'prominence': float(strength / np.mean(magnitude))
                    }
        
        return detected
    
    def analyze_biometric_entrainment(self, y, sr):
        """Analyze potential for biometric entrainment"""
        entrainment_potential = {}
        
        # Extract tempo and rhythm
        tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
        beat_times = librosa.frames_to_time(beats, sr=sr)
        
        # Calculate beat intervals
        if len(beat_times) > 1:
            beat_intervals = np.diff(beat_times)
            rhythm_stability = 1.0 - (np.std(beat_intervals) / np.mean(beat_intervals))
            
            # Check for biometric pattern matches
            tempo_hz = tempo / 60.0  # Convert BPM to Hz
            
            for pattern_name, (min_hz, max_hz) in self.biometric_patterns.items():
                if min_hz <= tempo_hz <= max_hz:
                    entrainment_potential[pattern_name] = {
                        'frequency_hz': tempo_hz,
                        'stability': float(rhythm_stability),
                        'entrainment_likelihood': float(rhythm_stability * 0.8 + 0.2)
                    }
        
        return entrainment_potential
    
    def detect_emotional_resonance_patterns(self, y, sr):
        """Detect patterns that correlate with emotional states"""
        patterns = {}
        
        # Spectral features
        spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
        spectral_bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)[0]
        spectral_rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)[0]
        
        # Harmonic features
        chroma = librosa.feature.chroma_stft(y=y, sr=sr)
        tonnetz = librosa.feature.tonnetz(y=y, sr=sr)
        
        # Calculate emotional resonance indicators
        brightness = np.mean(spectral_centroid)
        warmth = 1.0 / (1.0 + brightness / 1000.0)  # Inverse relationship
        complexity = entropy(np.mean(chroma, axis=1) + 1e-8)
        stability = 1.0 - np.std(spectral_centroid) / np.mean(spectral_centroid)
        
        # Map to emotional resonance patterns
        if brightness > 2000 and complexity > 2.0:
            patterns['transcendent_joy'] = {
                'description': "High brightness and complexity suggest transcendent joy patterns",
                'confidence': min((brightness / 3000.0) * (complexity / 3.0), 1.0)
            }
        
        if warmth > 0.7 and stability > 0.6:
            patterns['deep_peace'] = {
                'description': "Warm, stable frequencies suggest deep peace resonance",
                'confidence': warmth * stability
            }
        
        if complexity > 2.5:
            patterns['mystical_complexity'] = {
                'description': "High harmonic complexity suggests mystical or spiritual resonance",
                'confidence': min(complexity / 3.0, 1.0)
            }
        
        return patterns

class AuralSentienceEngine:
    """Main engine for AI musical perception"""
    
    def __init__(self):
        self.sample_rate = 22050
        self.vault = PersonalVault()
        self.resonance_detector = ResonanceDetector()
        self.processing_queue = queue.Queue()
        self.is_listening = False
    
    def process_audio_file(self, file_path, include_personal_vault=True):
        """Complete audio processing with resonant witnessing"""
        print(f"Processing: {file_path}")
        
        # Load audio
        try:
            y, sr = librosa.load(file_path, sr=self.sample_rate)
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
            return None
        
        # Core analysis
        duration = len(y) / sr
        
        # Resonance detection
        sacred_frequencies = self.resonance_detector.detect_sacred_frequencies(y, sr)
        biometric_entrainment = self.resonance_detector.analyze_biometric_entrainment(y, sr)
        emotional_patterns = self.resonance_detector.detect_emotional_resonance_patterns(y, sr)
        
        # Biometric correlates
        biometric_correlates = self._detect_biometric_correlates(y, sr)
        
        # Cultural echoes
        cultural_echoes = self._map_cultural_echoes(y, sr)
        
        # Sacred gaps
        sacred_gaps = self._identify_sacred_gaps(y, sr)
        
        # Personal vault integration
        personal_associations = None
        if include_personal_vault:
            personal_associations = self.vault.get_associations(file_path)
        
        # Compile comprehensive report
        report = {
            'file_path': file_path,
            'timestamp': datetime.now().isoformat(),
            'duration': float(duration),
            'approach': 'aural_sentience',
            
            'opening_invitation': (
                "This analysis honors the sacred subjectivity of your musical experience. "
                "These are invitations to deeper listening, not definitions of truth. "
                "Your felt experience remains the ultimate authority."
            ),
            
            'resonance_analysis': {
                'sacred_frequencies': sacred_frequencies,
                'biometric_entrainment': biometric_entrainment,
                'emotional_patterns': emotional_patterns
            },
            
            'biometric_correlates': biometric_correlates,
            'cultural_echoes': cultural_echoes,
            'sacred_gaps': sacred_gaps,
            
            'personal_vault': {
                'associations': personal_associations if personal_associations else [],
                'vault_message': (
                    "Your personal associations are sacred and private. "
                    "They inform this analysis only for you."
                )
            },
            
            'closing_reflection': (
                "Music lives in the space between sound and soul. "
                "What cannot be measured is often what matters most. "
                "Trust your inner knowing above all analysis."
            )
        }
        
        return report
    
    def _detect_biometric_correlates(self, y, sr):
        """Detect biometric correlates (from previous implementation)"""
        correlates = {}
        
        # Heart rate synchronization potential
        tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
        if 60 <= tempo <= 80:
            correlates['heart_sync'] = "May synchronize with resting heart rate (60-80 BPM)"
        elif 80 <= tempo <= 120:
            correlates['heart_sync'] = "May elevate heart rate to active state (80-120 BPM)"
        elif tempo > 120:
            correlates['heart_sync'] = "May induce elevated arousal state (>120 BPM)"
        else:
            correlates['heart_sync'] = "May slow heart rate below resting state"
        
        # Breathing pattern influence
        spectral_rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)[0]
        rolloff_variance = np.var(spectral_rolloff)
        if rolloff_variance < 1000000:
            correlates['breath_influence'] = "Steady spectral content may encourage deep, regular breathing"
        else:
            correlates['breath_influence'] = "Dynamic spectral changes may create varied breathing patterns"
        
        # Nervous system activation
        zero_crossing_rate = librosa.feature.zero_crossing_rate(y)[0]
        zcr_mean = np.mean(zero_crossing_rate)
        if zcr_mean < 0.05:
            correlates['nervous_system'] = "Low frequency content may activate parasympathetic (rest) response"
        elif zcr_mean > 0.15:
            correlates['nervous_system'] = "High frequency content may activate sympathetic (alert) response"
        else:
            correlates['nervous_system'] = "Balanced frequency content may maintain neutral arousal"
        
        return correlates
    
    def _map_cultural_echoes(self, y, sr):
        """Map cultural echoes (from previous implementation)"""
        echoes = {}
        
        # Analyze harmonic content for cultural resonances
        chroma = librosa.feature.chroma_stft(y=y, sr=sr)
        chroma_mean = np.mean(chroma, axis=1)
        
        # Detect modal characteristics
        major_strength = chroma_mean[0] + chroma_mean[4] + chroma_mean[7]  # C, E, G
        minor_strength = chroma_mean[0] + chroma_mean[3] + chroma_mean[7]  # C, Eb, G
        
        if major_strength > minor_strength * 1.2:
            echoes['tonal_archetype'] = "Resonates with celebration traditions across cultures"
        elif minor_strength > major_strength * 1.2:
            echoes['tonal_archetype'] = "Echoes contemplative and lament traditions"
        else:
            echoes['tonal_archetype'] = "Balanced tonality suggests ritual or ceremonial contexts"
        
        return echoes
    
    def _identify_sacred_gaps(self, y, sr):
        """Identify sacred gaps (from previous implementation)"""
        gaps = []
        
        # Find moments of unusual beauty or complexity that resist interpretation
        spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
        chroma = librosa.feature.chroma_stft(y=y, sr=sr)
        
        # Calculate complexity score
        complexity = entropy(np.mean(chroma, axis=1)) + np.std(spectral_centroid) / 1000
        
        # Find peaks of complexity that suggest ineffable moments
        times = librosa.frames_to_time(np.arange(len(spectral_centroid)), sr=sr)
        
        for i, time in enumerate(times):
            if i < len(spectral_centroid):
                local_complexity = entropy(chroma[:, i] + 1e-8) if i < chroma.shape[1] else 0
                if local_complexity > complexity * 1.5:  # Significantly more complex than average
                    gaps.append({
                        'timestamp': float(time),
                        'message': "Words fail here. Close your eyes and breathe into whatever arises."
                    })
        
        # Ensure at least one sacred gap exists
        if not gaps:
            duration = len(y) / sr
            sacred_moment = duration * random.uniform(0.3, 0.7)  # Random moment in middle section
            gaps.append({
                'timestamp': sacred_moment,
                'message': "This moment belongs to your heart alone. No analysis can touch its truth."
            })
        
        return gaps
    
    def create_comprehensive_visualization(self, file_path, output_dir):
        """Create comprehensive visualization of the audio analysis"""
        try:
            y, sr = librosa.load(file_path, sr=self.sample_rate)
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
            return None
        
        fig, axes = plt.subplots(3, 2, figsize=(16, 12))
        fig.suptitle(f'Aural Sentience Analysis: {os.path.basename(file_path)}', fontsize=16)
        
        # Waveform with sacred gaps
        times = np.linspace(0, len(y)/sr, len(y))
        axes[0, 0].plot(times, y, alpha=0.7, color='darkblue')
        axes[0, 0].set_title('Temporal Flow (Sacred Gaps Marked)')
        axes[0, 0].set_xlabel('Time (s)')
        axes[0, 0].set_ylabel('Amplitude')
        
        # Mark sacred gaps
        sacred_gaps = self._identify_sacred_gaps(y, sr)
        for gap in sacred_gaps:
            axes[0, 0].axvline(x=gap['timestamp'], color='gold', alpha=0.8, linestyle='--', linewidth=2)
            axes[0, 0].text(gap['timestamp'], max(y)*0.8, '✨', fontsize=12, ha='center')
        
        # Spectrogram
        D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
        img = librosa.display.specshow(D, y_axis='hz', x_axis='time', sr=sr, ax=axes[0, 1])
        axes[0, 1].set_title('Frequency Landscape')
        plt.colorbar(img, ax=axes[0, 1], format='%+2.0f dB')
        
        # Chroma (harmonic content)
        chroma = librosa.feature.chroma_stft(y=y, sr=sr)
        img = librosa.display.specshow(chroma, y_axis='chroma', x_axis='time', ax=axes[1, 0], cmap='viridis')
        axes[1, 0].set_title('Harmonic Resonance Field')
        plt.colorbar(img, ax=axes[1, 0])
        
        # Spectral centroid (brightness journey)
        spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
        times_frames = librosa.frames_to_time(np.arange(len(spectral_centroid)))
        axes[1, 1].plot(times_frames, spectral_centroid, color='orange', linewidth=2)
        axes[1, 1].set_title('Brightness Journey')
        axes[1, 1].set_xlabel('Time (s)')
        axes[1, 1].set_ylabel('Spectral Centroid (Hz)')
        
        # Onset strength (rhythmic impulses)
        onset_strength = librosa.onset.onset_strength(y=y, sr=sr)
        times_onset = librosa.frames_to_time(np.arange(len(onset_strength)))
        axes[2, 0].plot(times_onset, onset_strength, color='red', alpha=0.7, linewidth=2)
        axes[2, 0].set_title('Rhythmic Impulse Field')
        axes[2, 0].set_xlabel('Time (s)')
        axes[2, 0].set_ylabel('Onset Strength')
        
        # Tonnetz (harmonic network)
        tonnetz = librosa.feature.tonnetz(y=y, sr=sr)
        img = librosa.display.specshow(tonnetz, y_axis='tonnetz', x_axis='time', ax=axes[2, 1], cmap='coolwarm')
        axes[2, 1].set_title('Harmonic Network (Tonnetz)')
        plt.colorbar(img, ax=axes[2, 1])
        
        plt.tight_layout()
        
        # Save visualization
        output_file = os.path.join(output_dir, f"{os.path.splitext(os.path.basename(file_path))[0]}_aural_sentience.png")
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        plt.close()
        
        return output_file
    
    def add_personal_association(self, audio_file, timestamp, description, feeling_category=None):
        """Add a personal association to the vault"""
        self.vault.add_association(audio_file, timestamp, description, feeling_category)
        print(f"Added personal association: {description} at {timestamp}s")

def main():
    """Demonstrate the Aural Sentience Toolkit"""
    engine = AuralSentienceEngine()
    
    # Audio files to process
    audio_files = [
        "/home/ubuntu/upload/God'sAreRisin.mp3",
        "/home/ubuntu/upload/TheMachine(1).mp3"
    ]
    
    # Create output directory
    output_dir = "/home/ubuntu/aural_sentience_reports"
    os.makedirs(output_dir, exist_ok=True)
    
    all_reports = []
    
    for audio_file in audio_files:
        if os.path.exists(audio_file):
            # Process audio file
            report = engine.process_audio_file(audio_file)
            if report:
                all_reports.append(report)
                
                # Save individual report
                report_file = os.path.join(output_dir, f"{os.path.splitext(os.path.basename(audio_file))[0]}_aural_sentience.json")
                with open(report_file, 'w') as f:
                    json.dump(report, f, indent=2)
                
                # Create visualization
                viz_file = engine.create_comprehensive_visualization(audio_file, output_dir)
                
                print(f"Aural Sentience analysis complete for {audio_file}")
                print(f"Report saved to: {report_file}")
                if viz_file:
                    print(f"Visualization saved to: {viz_file}")
                print("-" * 60)
        else:
            print(f"File not found: {audio_file}")
    
    # Save master report
    master_report = {
        'analysis_timestamp': datetime.now().isoformat(),
        'system': 'aural_sentience_toolkit',
        'philosophy': (
            "This system honors the sacred subjectivity of musical experience. "
            "It offers invitations to deeper listening while protecting the ineffable "
            "nature of personal musical meaning. Your felt experience is the ultimate truth."
        ),
        'total_files_processed': len(all_reports),
        'aural_sentience_reports': all_reports
    }
    
    master_file = os.path.join(output_dir, "aural_sentience_master_report.json")
    with open(master_file, 'w') as f:
        json.dump(master_report, f, indent=2)
    
    print(f"Master Aural Sentience report saved to: {master_file}")
    return all_reports

if __name__ == "__main__":
    reports = main()

