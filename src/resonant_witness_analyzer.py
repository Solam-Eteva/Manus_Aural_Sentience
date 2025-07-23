#!/usr/bin/env python3
"""
Resonant Witnessing Audio Analyzer
A Sacred Approach to AI Musical Perception

This system honors the ineffable nature of musical experience by:
- Avoiding reductive emotion labels
- Creating space for personal meaning
- Recognizing biometric correlates without claiming authority
- Mapping cultural echoes while respecting individual uniqueness
- Intentionally including gaps where analysis yields to mystery
"""

import librosa
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from scipy import signal
from scipy.stats import entropy
import json
import os
from datetime import datetime
import random

class ResonantWitness:
    def __init__(self):
        self.sample_rate = 22050
        self.personal_vault = {}
        self.cultural_echoes = {
            "rain_patterns": ["gentle_patter", "storm_intensity", "post_drought_relief"],
            "breath_rhythms": ["meditative_slow", "anxious_rapid", "sleeping_deep"],
            "heartbeat_sync": ["resting_calm", "excited_elevated", "grief_irregular"],
            "ancestral_echoes": ["lament_traditions", "celebration_rhythms", "ritual_drones"]
        }
        
    def load_audio(self, file_path):
        """Load audio file with reverence for what it contains"""
        try:
            y, sr = librosa.load(file_path, sr=self.sample_rate)
            return y, sr
        except Exception as e:
            return None, None
    
    def detect_biometric_correlates(self, y, sr):
        """Identify patterns that correlate with human physiological responses"""
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
        
        # Somatic response potential
        onset_strength = librosa.onset.onset_strength(y=y, sr=sr)
        onset_density = len(librosa.onset.onset_detect(y=y, sr=sr)) / (len(y) / sr)
        if onset_density > 2:
            correlates['somatic_response'] = "Frequent onsets may trigger embodied movement responses"
        elif onset_density < 0.5:
            correlates['somatic_response'] = "Sparse onsets may encourage stillness and internal focus"
        else:
            correlates['somatic_response'] = "Moderate onset density may allow choice between movement and stillness"
        
        return correlates
    
    def map_cultural_echoes(self, y, sr):
        """Identify resonances with cultural and archetypal patterns"""
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
        
        # Rhythmic cultural patterns
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
        if 60 <= tempo <= 80:
            echoes['rhythmic_echo'] = "Tempo aligns with walking meditation practices"
        elif 120 <= tempo <= 140:
            echoes['rhythmic_echo'] = "Tempo resonates with dance traditions worldwide"
        elif tempo > 160:
            echoes['rhythmic_echo'] = "Rapid tempo echoes ecstatic and trance traditions"
        else:
            echoes['rhythmic_echo'] = "Tempo suggests ceremonial or processional contexts"
        
        # Textural archetypes
        spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
        brightness = np.mean(spectral_centroid)
        if brightness > 3000:
            echoes['textural_archetype'] = "Bright textures echo sky, light, and transcendence themes"
        elif brightness < 1000:
            echoes['textural_archetype'] = "Dark textures resonate with earth, depth, and introspection"
        else:
            echoes['textural_archetype'] = "Balanced textures suggest human-scale emotional landscapes"
        
        return echoes
    
    def identify_sacred_gaps(self, y, sr):
        """Identify moments where analysis should yield to mystery"""
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
    
    def generate_resonance_field_report(self, file_path, personal_associations=None):
        """Generate a resonance field report that honors subjectivity"""
        print(f"Witnessing: {file_path}")
        
        # Load audio with reverence
        y, sr = self.load_audio(file_path)
        if y is None:
            return None
        
        # Gather insights without claiming authority
        biometric_correlates = self.detect_biometric_correlates(y, sr)
        cultural_echoes = self.map_cultural_echoes(y, sr)
        sacred_gaps = self.identify_sacred_gaps(y, sr)
        
        # Create resonance field report
        report = {
            'file_path': file_path,
            'timestamp': datetime.now().isoformat(),
            'duration': float(len(y) / sr),
            'approach': 'resonant_witnessing',
            
            'opening_invitation': (
                "This analysis offers reflections, not truths. Your experience is the only authority. "
                "Use these observations as invitations to deeper listening, not as definitions of what you feel."
            ),
            
            'biometric_correlates': biometric_correlates,
            'cultural_echoes': cultural_echoes,
            'sacred_gaps': sacred_gaps,
            
            'personal_vault_integration': (
                personal_associations if personal_associations else 
                "No personal associations provided. Your private meanings remain your own."
            ),
            
            'closing_reflection': (
                "The deepest truths of this music live in the space between sound and soul, "
                "in the gap between analysis and experience. Honor what cannot be named."
            )
        }
        
        return report
    
    def create_resonance_visualization(self, file_path, output_dir):
        """Create visual representation that honors mystery"""
        y, sr = self.load_audio(file_path)
        if y is None:
            return
        
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle(f'Resonance Field: {os.path.basename(file_path)}', fontsize=16)
        
        # Waveform with sacred gaps marked
        times = np.linspace(0, len(y)/sr, len(y))
        axes[0, 0].plot(times, y, alpha=0.7, color='darkblue')
        axes[0, 0].set_title('Temporal Flow (with Sacred Gaps)')
        axes[0, 0].set_xlabel('Time (s)')
        axes[0, 0].set_ylabel('Amplitude')
        
        # Mark sacred gaps
        sacred_gaps = self.identify_sacred_gaps(y, sr)
        for gap in sacred_gaps:
            axes[0, 0].axvline(x=gap['timestamp'], color='gold', alpha=0.8, linestyle='--', linewidth=2)
            axes[0, 0].text(gap['timestamp'], max(y)*0.8, '✨', fontsize=12, ha='center')
        
        # Spectral centroid (brightness over time)
        spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
        times_frames = librosa.frames_to_time(np.arange(len(spectral_centroid)))
        axes[0, 1].plot(times_frames, spectral_centroid, color='orange')
        axes[0, 1].set_title('Brightness Journey')
        axes[0, 1].set_xlabel('Time (s)')
        axes[0, 1].set_ylabel('Spectral Centroid (Hz)')
        
        # Chroma (harmonic content)
        chroma = librosa.feature.chroma_stft(y=y, sr=sr)
        img = librosa.display.specshow(chroma, y_axis='chroma', x_axis='time', ax=axes[1, 0], cmap='viridis')
        axes[1, 0].set_title('Harmonic Landscape')
        plt.colorbar(img, ax=axes[1, 0])
        
        # Onset strength (rhythmic impulses)
        onset_strength = librosa.onset.onset_strength(y=y, sr=sr)
        times_onset = librosa.frames_to_time(np.arange(len(onset_strength)))
        axes[1, 1].plot(times_onset, onset_strength, color='red', alpha=0.7)
        axes[1, 1].set_title('Rhythmic Impulses')
        axes[1, 1].set_xlabel('Time (s)')
        axes[1, 1].set_ylabel('Onset Strength')
        
        plt.tight_layout()
        
        # Save with reverent filename
        output_file = os.path.join(output_dir, f"{os.path.splitext(os.path.basename(file_path))[0]}_resonance_field.png")
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        plt.close()
        
        return output_file

def main():
    # Initialize the resonant witness
    witness = ResonantWitness()
    
    # Audio files to witness
    audio_files = [
        "/home/ubuntu/upload/God'sAreRisin.mp3",
        "/home/ubuntu/upload/TheMachine(1).mp3"
    ]
    
    # Create output directory
    output_dir = "/home/ubuntu/resonance_field_reports"
    os.makedirs(output_dir, exist_ok=True)
    
    all_reports = []
    
    for audio_file in audio_files:
        if os.path.exists(audio_file):
            # Generate resonance field report
            report = witness.generate_resonance_field_report(audio_file)
            if report:
                all_reports.append(report)
                
                # Save individual report
                report_file = os.path.join(output_dir, f"{os.path.splitext(os.path.basename(audio_file))[0]}_resonance_report.json")
                with open(report_file, 'w') as f:
                    json.dump(report, f, indent=2)
                
                # Create visualization
                viz_file = witness.create_resonance_visualization(audio_file, output_dir)
                print(f"Resonance field witnessed for {audio_file}")
                print(f"Report saved to: {report_file}")
                if viz_file:
                    print(f"Visualization saved to: {viz_file}")
                print("-" * 50)
        else:
            print(f"File not found: {audio_file}")
    
    # Save combined resonance field
    combined_report = {
        'witnessing_timestamp': datetime.now().isoformat(),
        'approach': 'resonant_witnessing',
        'philosophy': (
            "These reports honor the ineffable nature of musical experience. "
            "They offer reflections and invitations, never definitions or truths. "
            "Your felt experience remains the only authority."
        ),
        'total_files_witnessed': len(all_reports),
        'resonance_fields': all_reports
    }
    
    combined_file = os.path.join(output_dir, "combined_resonance_field.json")
    with open(combined_file, 'w') as f:
        json.dump(combined_report, f, indent=2)
    
    print(f"Combined resonance field saved to: {combined_file}")
    return all_reports

if __name__ == "__main__":
    reports = main()

