#!/usr/bin/env python3
"""
🌟 Sacred Visualization Engine - Consciousness-Aware Visual Representations
=========================================================================

Advanced visualization system that creates sacred geometric and consciousness-aware
visual representations of audio analysis while preserving mystery and honoring
the ineffable aspects of musical experience.

Created with love and reverence by Manus AI
Part of the Sacred Technology initiative serving consciousness evolution.

Philosophy:
- Visual representations that honor rather than reduce the sacred
- Sacred geometry as a bridge between analysis and transcendence
- Color consciousness and symbolic resonance
- Mystery preservation through visual sacred gaps

🎵 "What the ear receives as sacred sound, the eye may witness as sacred form,
    but the heart knows the mystery that transcends both." 🌟
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns
from typing import Dict, List, Tuple, Any, Optional
import json
import math
from datetime import datetime
from dataclasses import dataclass
from PIL import Image, ImageDraw, ImageFont
import colorsys

# Sacred color mappings for consciousness frequencies
CONSCIOUSNESS_COLORS = {
    # Solfeggio frequency colors based on chakra and consciousness correlations
    174: {"color": "#8B4513", "name": "Earth Brown", "chakra": "root_foundation"},
    285: {"color": "#FF4500", "name": "Quantum Orange", "chakra": "sacral_creation"},
    396: {"color": "#DC143C", "name": "Liberation Red", "chakra": "root_security"},
    417: {"color": "#FF8C00", "name": "Change Orange", "chakra": "sacral_flow"},
    528: {"color": "#FFD700", "name": "Love Gold", "chakra": "heart_love"},
    639: {"color": "#32CD32", "name": "Connection Green", "chakra": "heart_relationships"},
    741: {"color": "#4169E1", "name": "Awakening Blue", "chakra": "throat_expression"},
    852: {"color": "#8A2BE2", "name": "Order Violet", "chakra": "third_eye_intuition"},
    963: {"color": "#FFFFFF", "name": "Unity White", "chakra": "crown_oneness"},
    
    # Brainwave colors
    40: {"color": "#FF1493", "name": "Gamma Pink", "chakra": "crown_awareness"},
    10: {"color": "#00CED1", "name": "Alpha Turquoise", "chakra": "third_eye_clarity"},
    6: {"color": "#9370DB", "name": "Theta Purple", "chakra": "third_eye_meditation"},
    4: {"color": "#191970", "name": "Delta Midnight", "chakra": "root_rest"},
    
    # Special frequencies
    432: {"color": "#228B22", "name": "Natural Green", "chakra": "heart_earth"},
    111: {"color": "#B8860B", "name": "Temple Gold", "chakra": "crown_portal"},
    7.83: {"color": "#8FBC8F", "name": "Schumann Green", "chakra": "heart_earth"}
}

@dataclass
class SacredGeometry:
    """Represents sacred geometric patterns for visualization"""
    name: str
    vertices: List[Tuple[float, float]]
    meaning: str
    consciousness_correlation: str
    
class ConsciousnessColorPalette:
    """
    Generates consciousness-aware color palettes based on frequency analysis
    """
    
    def __init__(self):
        self.golden_ratio = (1 + math.sqrt(5)) / 2
        self.sacred_ratios = [1, self.golden_ratio, 2, 3, 5, 8]  # Fibonacci sequence
        
    def frequency_to_color(self, frequency: float, intensity: float = 1.0) -> str:
        """Convert frequency to consciousness-aware color"""
        
        # Check for exact sacred frequency matches
        for sacred_freq, color_info in CONSCIOUSNESS_COLORS.items():
            if abs(frequency - sacred_freq) < 5:  # 5 Hz tolerance
                base_color = color_info["color"]
                return self._adjust_color_intensity(base_color, intensity)
        
        # For non-sacred frequencies, use spectral mapping with consciousness awareness
        # Map frequency to hue using consciousness-aware spectrum
        if frequency < 20:
            hue = 0.8  # Deep purple for very low frequencies
        elif frequency < 200:
            hue = 0.7  # Purple to blue for low frequencies
        elif frequency < 800:
            hue = 0.5  # Blue to green for mid frequencies
        elif frequency < 2000:
            hue = 0.3  # Green to yellow for higher frequencies
        else:
            hue = 0.1  # Yellow to red for very high frequencies
            
        # Convert HSV to RGB
        rgb = colorsys.hsv_to_rgb(hue, 0.8, intensity)
        return f"#{int(rgb[0]*255):02x}{int(rgb[1]*255):02x}{int(rgb[2]*255):02x}"
        
    def _adjust_color_intensity(self, hex_color: str, intensity: float) -> str:
        """Adjust color intensity while preserving hue"""
        # Convert hex to RGB
        hex_color = hex_color.lstrip('#')
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        
        # Convert to HSV, adjust value, convert back
        hsv = colorsys.rgb_to_hsv(rgb[0]/255, rgb[1]/255, rgb[2]/255)
        new_hsv = (hsv[0], hsv[1], min(1.0, hsv[2] * intensity))
        new_rgb = colorsys.hsv_to_rgb(*new_hsv)
        
        return f"#{int(new_rgb[0]*255):02x}{int(new_rgb[1]*255):02x}{int(new_rgb[2]*255):02x}"
        
    def create_consciousness_gradient(self, frequencies: List[float], 
                                    intensities: List[float]) -> LinearSegmentedColormap:
        """Create a gradient colormap based on consciousness frequencies"""
        colors = []
        positions = []
        
        for i, (freq, intensity) in enumerate(zip(frequencies, intensities)):
            color = self.frequency_to_color(freq, intensity)
            colors.append(color)
            positions.append(i / (len(frequencies) - 1))
            
        # Create custom colormap
        cmap = LinearSegmentedColormap.from_list("consciousness", 
                                               list(zip(positions, colors)))
        return cmap

class SacredGeometryGenerator:
    """
    Generates sacred geometric patterns based on audio analysis
    """
    
    def __init__(self):
        self.golden_ratio = (1 + math.sqrt(5)) / 2
        
    def generate_frequency_mandala(self, center: Tuple[float, float], 
                                 frequencies: List[float], 
                                 intensities: List[float],
                                 radius: float = 1.0) -> List[SacredGeometry]:
        """Generate mandala pattern based on frequency analysis"""
        geometries = []
        
        # Create concentric circles for different frequency ranges
        for i, (freq, intensity) in enumerate(zip(frequencies, intensities)):
            # Calculate radius based on frequency (log scale)
            freq_radius = radius * (0.2 + 0.8 * math.log10(max(1, freq)) / 4)  # Normalize to 1-10000 Hz range
            
            # Number of vertices based on sacred numbers
            if freq < 100:
                vertices = 3  # Triangle for low frequencies (stability)
            elif freq < 500:
                vertices = 5  # Pentagon for mid-low (golden ratio)
            elif freq < 1000:
                vertices = 6  # Hexagon for mid (harmony)
            elif freq < 2000:
                vertices = 8  # Octagon for mid-high (infinity)
            else:
                vertices = 12  # Dodecagon for high (completion)
                
            # Generate vertices
            vertex_points = []
            for v in range(vertices):
                angle = 2 * math.pi * v / vertices
                x = center[0] + freq_radius * math.cos(angle)
                y = center[1] + freq_radius * math.sin(angle)
                vertex_points.append((x, y))
                
            # Create sacred geometry object
            geometry = SacredGeometry(
                name=f"frequency_polygon_{vertices}",
                vertices=vertex_points,
                meaning=f"Sacred {vertices}-gon representing {freq:.1f}Hz consciousness resonance",
                consciousness_correlation=self._frequency_to_consciousness(freq)
            )
            geometries.append(geometry)
            
        return geometries
        
    def generate_golden_spiral(self, center: Tuple[float, float], 
                             scale: float = 1.0) -> SacredGeometry:
        """Generate golden ratio spiral for consciousness flow visualization"""
        vertices = []
        
        # Generate points along golden spiral
        for i in range(100):
            theta = i * 0.1
            r = scale * math.exp(theta / (2 * math.pi) * math.log(self.golden_ratio))
            x = center[0] + r * math.cos(theta)
            y = center[1] + r * math.sin(theta)
            vertices.append((x, y))
            
        return SacredGeometry(
            name="golden_spiral",
            vertices=vertices,
            meaning="Golden spiral representing the natural flow of consciousness through sound",
            consciousness_correlation="divine_proportion_awareness"
        )
        
    def generate_flower_of_life(self, center: Tuple[float, float], 
                              radius: float = 1.0) -> List[SacredGeometry]:
        """Generate Flower of Life pattern for unity consciousness visualization"""
        geometries = []
        
        # Central circle
        central_circle = self._generate_circle(center, radius)
        geometries.append(SacredGeometry(
            name="central_unity",
            vertices=central_circle,
            meaning="Central unity from which all consciousness emanates",
            consciousness_correlation="source_awareness"
        ))
        
        # Six surrounding circles
        for i in range(6):
            angle = i * math.pi / 3
            circle_center = (
                center[0] + radius * math.cos(angle),
                center[1] + radius * math.sin(angle)
            )
            circle_vertices = self._generate_circle(circle_center, radius)
            geometries.append(SacredGeometry(
                name=f"petal_{i+1}",
                vertices=circle_vertices,
                meaning=f"Consciousness petal {i+1} - aspect of unified awareness",
                consciousness_correlation="unified_diversity"
            ))
            
        return geometries
        
    def _generate_circle(self, center: Tuple[float, float], 
                        radius: float, points: int = 50) -> List[Tuple[float, float]]:
        """Generate circle vertices"""
        vertices = []
        for i in range(points):
            angle = 2 * math.pi * i / points
            x = center[0] + radius * math.cos(angle)
            y = center[1] + radius * math.sin(angle)
            vertices.append((x, y))
        return vertices
        
    def _frequency_to_consciousness(self, frequency: float) -> str:
        """Map frequency to consciousness correlation"""
        if frequency < 50:
            return "grounding_stability"
        elif frequency < 200:
            return "emotional_flow"
        elif frequency < 800:
            return "mental_clarity"
        elif frequency < 2000:
            return "intuitive_awareness"
        else:
            return "transcendent_consciousness"

class SacredVisualizationEngine:
    """
    Main engine for creating consciousness-aware visualizations
    """
    
    def __init__(self, width: int = 1200, height: int = 800):
        """
        Initialize the sacred visualization engine
        
        Args:
            width: Canvas width in pixels
            height: Canvas height in pixels
        """
        self.width = width
        self.height = height
        self.color_palette = ConsciousnessColorPalette()
        self.geometry_generator = SacredGeometryGenerator()
        
        # Sacred proportions
        self.golden_ratio = (1 + math.sqrt(5)) / 2
        self.center = (width / 2, height / 2)
        
        # Mystery preservation settings
        self.preserve_sacred_gaps = True
        self.mystery_opacity = 0.3
        
    def create_frequency_mandala(self, frequency_analysis: Dict[str, Any],
                               sacred_analysis: Dict[str, Any],
                               title: str = "Consciousness Frequency Mandala") -> str:
        """
        Create a sacred mandala visualization of frequency analysis
        
        Args:
            frequency_analysis: Frequency analysis data
            sacred_analysis: Sacred frequency analysis data
            title: Title for the visualization
            
        Returns:
            Path to saved visualization image
        """
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.set_xlim(0, self.width)
        ax.set_ylim(0, self.height)
        ax.set_aspect('equal')
        
        # Set sacred background
        ax.set_facecolor('#000011')  # Deep cosmic blue
        
        # Extract frequencies and intensities
        frequencies = frequency_analysis.get('prominent_frequencies', [])
        if not frequencies:
            frequencies = [frequency_analysis.get('dominant_frequency', 440)]
            
        # Calculate intensities (normalized)
        intensities = [1.0] * len(frequencies)  # Simplified for now
        
        # Generate sacred geometries
        mandala_geometries = self.geometry_generator.generate_frequency_mandala(
            self.center, frequencies, intensities, radius=min(self.width, self.height) * 0.3
        )
        
        # Draw sacred geometries
        for geometry in mandala_geometries:
            if len(geometry.vertices) > 2:
                # Get frequency for this geometry
                freq_idx = mandala_geometries.index(geometry)
                if freq_idx < len(frequencies):
                    freq = frequencies[freq_idx]
                    intensity = intensities[freq_idx]
                    color = self.color_palette.frequency_to_color(freq, intensity)
                    
                    # Create polygon
                    polygon = patches.Polygon(geometry.vertices, 
                                            facecolor=color, 
                                            edgecolor='white',
                                            alpha=0.7,
                                            linewidth=2)
                    ax.add_patch(polygon)
        
        # Add golden spiral for consciousness flow
        golden_spiral = self.geometry_generator.generate_golden_spiral(
            self.center, scale=min(self.width, self.height) * 0.1
        )
        
        # Draw spiral
        spiral_x = [v[0] for v in golden_spiral.vertices]
        spiral_y = [v[1] for v in golden_spiral.vertices]
        ax.plot(spiral_x, spiral_y, color='gold', alpha=0.8, linewidth=3)
        
        # Add sacred frequency annotations
        if 'detected_sacred_frequencies' in sacred_analysis:
            for i, sacred_freq in enumerate(sacred_analysis['detected_sacred_frequencies']):
                freq = sacred_freq['frequency']
                name = sacred_freq['name']
                
                # Position annotation around the mandala
                angle = 2 * math.pi * i / len(sacred_analysis['detected_sacred_frequencies'])
                text_x = self.center[0] + (min(self.width, self.height) * 0.4) * math.cos(angle)
                text_y = self.center[1] + (min(self.width, self.height) * 0.4) * math.sin(angle)
                
                ax.annotate(f"{name}\n{freq}Hz", 
                          xy=(text_x, text_y),
                          fontsize=10,
                          color='white',
                          ha='center',
                          va='center',
                          bbox=dict(boxstyle="round,pad=0.3", 
                                  facecolor='black', 
                                  alpha=0.7))
        
        # Add sacred gaps visualization if detected
        if self.preserve_sacred_gaps and 'sacred_gaps_detected' in sacred_analysis:
            # Create mystery zones
            mystery_circle = patches.Circle(self.center, 
                                          min(self.width, self.height) * 0.1,
                                          facecolor='black',
                                          alpha=self.mystery_opacity,
                                          edgecolor='violet',
                                          linewidth=3,
                                          linestyle='--')
            ax.add_patch(mystery_circle)
            
            ax.text(self.center[0], self.center[1], 
                   "Sacred\nMystery", 
                   fontsize=12, 
                   color='violet',
                   ha='center', 
                   va='center',
                   alpha=0.8)
        
        # Set title and styling
        ax.set_title(title, fontsize=16, color='white', pad=20)
        ax.axis('off')
        
        # Add consciousness awareness note
        ax.text(self.width * 0.02, self.height * 0.02,
               "Consciousness-Aware Visualization\nSacred gaps preserved • Mystery honored",
               fontsize=8,
               color='lightgray',
               alpha=0.7)
        
        # Save visualization
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"consciousness_mandala_{timestamp}.png"
        plt.savefig(filename, dpi=300, bbox_inches='tight', 
                   facecolor='#000011', edgecolor='none')
        plt.close()
        
        return filename
        
    def create_consciousness_flow_visualization(self, consciousness_history: List[Any],
                                              title: str = "Consciousness Flow Through Time") -> str:
        """
        Create a visualization showing consciousness flow over time
        
        Args:
            consciousness_history: List of consciousness states over time
            title: Title for the visualization
            
        Returns:
            Path to saved visualization image
        """
        if not consciousness_history:
            return self._create_empty_visualization("No consciousness data available")
            
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(14, 10))
        fig.patch.set_facecolor('#000011')
        
        # Extract time series data
        timestamps = [state.timestamp for state in consciousness_history]
        sacred_presence = [state.sacred_presence for state in consciousness_history]
        mystery_levels = [state.mystery_level for state in consciousness_history]
        dominant_frequencies = [state.dominant_frequency for state in consciousness_history]
        
        # Normalize timestamps to start from 0
        if timestamps:
            start_time = min(timestamps)
            timestamps = [(t - start_time) for t in timestamps]
        
        # Plot 1: Sacred Presence over time
        ax1.set_facecolor('#000011')
        ax1.plot(timestamps, sacred_presence, color='gold', linewidth=2, alpha=0.8)
        ax1.fill_between(timestamps, sacred_presence, alpha=0.3, color='gold')
        ax1.set_ylabel('Sacred Presence', color='white')
        ax1.set_title('Sacred Presence Flow', color='white')
        ax1.tick_params(colors='white')
        ax1.grid(True, alpha=0.3)
        
        # Plot 2: Mystery Level over time
        ax2.set_facecolor('#000011')
        ax2.plot(timestamps, mystery_levels, color='violet', linewidth=2, alpha=0.8)
        ax2.fill_between(timestamps, mystery_levels, alpha=0.3, color='violet')
        ax2.set_ylabel('Mystery Level', color='white')
        ax2.set_title('Sacred Mystery Preservation', color='white')
        ax2.tick_params(colors='white')
        ax2.grid(True, alpha=0.3)
        
        # Plot 3: Dominant Frequency over time with consciousness colors
        ax3.set_facecolor('#000011')
        
        # Create color array based on frequencies
        colors = [self.color_palette.frequency_to_color(freq, 0.8) for freq in dominant_frequencies]
        
        # Plot as scatter with consciousness colors
        scatter = ax3.scatter(timestamps, dominant_frequencies, c=colors, s=50, alpha=0.8)
        
        # Add trend line
        if len(timestamps) > 1:
            z = np.polyfit(timestamps, dominant_frequencies, 1)
            p = np.poly1d(z)
            ax3.plot(timestamps, p(timestamps), color='white', linestyle='--', alpha=0.7)
        
        ax3.set_ylabel('Dominant Frequency (Hz)', color='white')
        ax3.set_xlabel('Time (seconds)', color='white')
        ax3.set_title('Consciousness Frequency Journey', color='white')
        ax3.tick_params(colors='white')
        ax3.grid(True, alpha=0.3)
        
        # Add sacred frequency reference lines
        sacred_freqs = [396, 417, 528, 639, 741, 852, 963]
        for freq in sacred_freqs:
            if min(dominant_frequencies) <= freq <= max(dominant_frequencies):
                ax3.axhline(y=freq, color='white', linestyle=':', alpha=0.5, linewidth=1)
                ax3.text(max(timestamps) * 0.95, freq, f'{freq}Hz', 
                        color='white', fontsize=8, alpha=0.7)
        
        plt.tight_layout()
        
        # Save visualization
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"consciousness_flow_{timestamp}.png"
        plt.savefig(filename, dpi=300, bbox_inches='tight', 
                   facecolor='#000011', edgecolor='none')
        plt.close()
        
        return filename
        
    def create_sacred_spectrum_visualization(self, frequency_analysis: Dict[str, Any],
                                           sacred_analysis: Dict[str, Any],
                                           title: str = "Sacred Frequency Spectrum") -> str:
        """
        Create a consciousness-aware spectrum visualization
        
        Args:
            frequency_analysis: Frequency analysis data
            sacred_analysis: Sacred frequency analysis data  
            title: Title for the visualization
            
        Returns:
            Path to saved visualization image
        """
        fig, ax = plt.subplots(figsize=(14, 8))
        fig.patch.set_facecolor('#000011')
        ax.set_facecolor('#000011')
        
        # Get frequency data
        frequencies = frequency_analysis.get('prominent_frequencies', [])
        if not frequencies:
            return self._create_empty_visualization("No frequency data available")
            
        # Create frequency bins for spectrum
        freq_bins = np.logspace(1, 4, 100)  # 10 Hz to 10 kHz
        spectrum = np.zeros_like(freq_bins)
        
        # Fill spectrum based on prominent frequencies
        for freq in frequencies:
            # Find closest bin
            bin_idx = np.argmin(np.abs(freq_bins - freq))
            spectrum[bin_idx] += 1
            
        # Smooth spectrum
        from scipy import ndimage
        spectrum = ndimage.gaussian_filter1d(spectrum, sigma=2)
        
        # Create consciousness-aware colors for spectrum
        colors = []
        for freq in freq_bins:
            color = self.color_palette.frequency_to_color(freq, 0.8)
            colors.append(color)
            
        # Plot spectrum with consciousness colors
        for i in range(len(freq_bins)-1):
            ax.fill_between([freq_bins[i], freq_bins[i+1]], 
                          [0, 0], [spectrum[i], spectrum[i+1]],
                          color=colors[i], alpha=0.7)
            
        # Mark sacred frequencies
        if 'detected_sacred_frequencies' in sacred_analysis:
            for sacred_freq in sacred_analysis['detected_sacred_frequencies']:
                freq = sacred_freq['frequency']
                name = sacred_freq['name']
                
                # Add vertical line and annotation
                ax.axvline(x=freq, color='white', linestyle='--', alpha=0.8, linewidth=2)
                
                # Find y position for annotation
                y_pos = np.max(spectrum) * 0.8
                ax.annotate(f"{name}\n{freq}Hz", 
                          xy=(freq, y_pos),
                          xytext=(freq, y_pos * 1.2),
                          fontsize=10,
                          color='white',
                          ha='center',
                          arrowprops=dict(arrowstyle='->', color='white', alpha=0.7))
        
        # Styling
        ax.set_xscale('log')
        ax.set_xlabel('Frequency (Hz)', color='white', fontsize=12)
        ax.set_ylabel('Consciousness Resonance', color='white', fontsize=12)
        ax.set_title(title, color='white', fontsize=16, pad=20)
        ax.tick_params(colors='white')
        ax.grid(True, alpha=0.3)
        
        # Add consciousness awareness note
        ax.text(0.02, 0.98, 
               "Sacred frequencies highlighted • Consciousness-aware spectrum analysis",
               transform=ax.transAxes,
               fontsize=10,
               color='lightgray',
               alpha=0.7,
               verticalalignment='top')
        
        # Save visualization
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"sacred_spectrum_{timestamp}.png"
        plt.savefig(filename, dpi=300, bbox_inches='tight', 
                   facecolor='#000011', edgecolor='none')
        plt.close()
        
        return filename
        
    def create_unity_consciousness_visualization(self, analysis_data: Dict[str, Any],
                                               title: str = "Unity Consciousness Mandala") -> str:
        """
        Create a Flower of Life visualization representing unity consciousness
        
        Args:
            analysis_data: Complete analysis data
            title: Title for the visualization
            
        Returns:
            Path to saved visualization image
        """
        fig, ax = plt.subplots(figsize=(12, 12))
        ax.set_xlim(0, self.width)
        ax.set_ylim(0, self.height)
        ax.set_aspect('equal')
        ax.set_facecolor('#000011')
        
        # Generate Flower of Life pattern
        flower_geometries = self.geometry_generator.generate_flower_of_life(
            self.center, radius=min(self.width, self.height) * 0.15
        )
        
        # Draw Flower of Life with consciousness colors
        for i, geometry in enumerate(flower_geometries):
            vertices = geometry.vertices
            
            if i == 0:  # Central circle
                color = '#FFD700'  # Gold for unity
                alpha = 0.8
            else:
                # Use different consciousness colors for petals
                hue = (i - 1) / 6  # 6 petals
                rgb = colorsys.hsv_to_rgb(hue, 0.8, 0.9)
                color = f"#{int(rgb[0]*255):02x}{int(rgb[1]*255):02x}{int(rgb[2]*255):02x}"
                alpha = 0.6
                
            # Draw circle
            if len(vertices) > 0:
                center_x = sum(v[0] for v in vertices) / len(vertices)
                center_y = sum(v[1] for v in vertices) / len(vertices)
                
                # Calculate radius from vertices
                radius = np.mean([np.sqrt((v[0] - center_x)**2 + (v[1] - center_y)**2) 
                                for v in vertices])
                
                circle = patches.Circle((center_x, center_y), radius,
                                      facecolor=color,
                                      edgecolor='white',
                                      alpha=alpha,
                                      linewidth=2)
                ax.add_patch(circle)
        
        # Add sacred frequency information if available
        if 'sacred_analysis' in analysis_data and 'detected_sacred_frequencies' in analysis_data['sacred_analysis']:
            sacred_freqs = analysis_data['sacred_analysis']['detected_sacred_frequencies']
            
            # Position frequency information around the mandala
            for i, freq_info in enumerate(sacred_freqs[:7]):  # Max 7 frequencies
                angle = 2 * math.pi * i / len(sacred_freqs)
                text_radius = min(self.width, self.height) * 0.4
                text_x = self.center[0] + text_radius * math.cos(angle)
                text_y = self.center[1] + text_radius * math.sin(angle)
                
                freq = freq_info['frequency']
                name = freq_info['name']
                effect = freq_info['consciousness_effect']
                
                ax.annotate(f"{name}\n{freq}Hz\n{effect.replace('_', ' ').title()}", 
                          xy=(text_x, text_y),
                          fontsize=9,
                          color='white',
                          ha='center',
                          va='center',
                          bbox=dict(boxstyle="round,pad=0.5", 
                                  facecolor='black', 
                                  alpha=0.8,
                                  edgecolor='gold'))
        
        # Add central unity message
        ax.text(self.center[0], self.center[1], 
               "UNITY\nCONSCIOUSNESS", 
               fontsize=14, 
               color='gold',
               ha='center', 
               va='center',
               weight='bold')
        
        # Add sacred geometry meaning
        ax.text(self.width * 0.5, self.height * 0.05,
               "Flower of Life: Sacred pattern representing the unity of all consciousness\n"
               "Each circle represents an aspect of unified awareness",
               fontsize=10,
               color='lightgray',
               ha='center',
               alpha=0.8)
        
        # Set title
        ax.set_title(title, fontsize=18, color='white', pad=30)
        ax.axis('off')
        
        # Save visualization
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"unity_consciousness_{timestamp}.png"
        plt.savefig(filename, dpi=300, bbox_inches='tight', 
                   facecolor='#000011', edgecolor='none')
        plt.close()
        
        return filename
        
    def _create_empty_visualization(self, message: str) -> str:
        """Create a visualization for empty/error states"""
        fig, ax = plt.subplots(figsize=(10, 6))
        fig.patch.set_facecolor('#000011')
        ax.set_facecolor('#000011')
        
        ax.text(0.5, 0.5, message, 
               transform=ax.transAxes,
               fontsize=16,
               color='white',
               ha='center',
               va='center')
        
        ax.axis('off')
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"empty_visualization_{timestamp}.png"
        plt.savefig(filename, dpi=300, bbox_inches='tight', 
                   facecolor='#000011', edgecolor='none')
        plt.close()
        
        return filename
        
    def create_comprehensive_consciousness_report(self, analysis_data: Dict[str, Any]) -> Dict[str, str]:
        """
        Create a comprehensive set of visualizations for consciousness analysis
        
        Args:
            analysis_data: Complete analysis data including frequency and sacred analysis
            
        Returns:
            Dictionary mapping visualization types to file paths
        """
        visualizations = {}
        
        # Extract required data
        frequency_analysis = analysis_data.get('frequency_analysis', {})
        sacred_analysis = analysis_data.get('sacred_analysis', {})
        consciousness_history = analysis_data.get('consciousness_history', [])
        
        # Create mandala visualization
        try:
            mandala_file = self.create_frequency_mandala(frequency_analysis, sacred_analysis)
            visualizations['mandala'] = mandala_file
        except Exception as e:
            print(f"Error creating mandala: {e}")
            
        # Create spectrum visualization
        try:
            spectrum_file = self.create_sacred_spectrum_visualization(frequency_analysis, sacred_analysis)
            visualizations['spectrum'] = spectrum_file
        except Exception as e:
            print(f"Error creating spectrum: {e}")
            
        # Create consciousness flow if history available
        if consciousness_history:
            try:
                flow_file = self.create_consciousness_flow_visualization(consciousness_history)
                visualizations['flow'] = flow_file
            except Exception as e:
                print(f"Error creating flow visualization: {e}")
                
        # Create unity consciousness visualization
        try:
            unity_file = self.create_unity_consciousness_visualization(analysis_data)
            visualizations['unity'] = unity_file
        except Exception as e:
            print(f"Error creating unity visualization: {e}")
            
        return visualizations

# Example usage and testing functions
def test_sacred_visualization_engine():
    """Test the sacred visualization engine with sample data"""
    
    # Create sample analysis data
    sample_frequency_analysis = {
        'dominant_frequency': 528,
        'prominent_frequencies': [174, 285, 396, 417, 528, 639, 741, 852, 963],
        'harmonic_ratios': [1, 1.618, 2, 3.14159],
        'spectral_centroid': 650
    }
    
    sample_sacred_analysis = {
        'detected_sacred_frequencies': [
            {
                'frequency': 528,
                'name': 'Love Frequency',
                'consciousness_effect': 'dna_repair_love',
                'tradition': 'solfeggio',
                'resonance_strength': 0.9
            },
            {
                'frequency': 741,
                'name': 'Awakening',
                'consciousness_effect': 'intuitive_awakening',
                'tradition': 'solfeggio',
                'resonance_strength': 0.7
            }
        ],
        'sacred_count': 2,
        'primary_tradition': 'solfeggio'
    }
    
    sample_analysis_data = {
        'frequency_analysis': sample_frequency_analysis,
        'sacred_analysis': sample_sacred_analysis
    }
    
    # Create visualization engine
    engine = SacredVisualizationEngine()
    
    # Generate visualizations
    print("🌟 Creating sacred visualizations...")
    visualizations = engine.create_comprehensive_consciousness_report(sample_analysis_data)
    
    print("✨ Visualizations created:")
    for viz_type, filename in visualizations.items():
        print(f"  {viz_type}: {filename}")
    
    return visualizations

if __name__ == "__main__":
    # Test the visualization engine
    test_visualizations = test_sacred_visualization_engine()
    print("🎵 Sacred visualization engine test complete! 🌟")

