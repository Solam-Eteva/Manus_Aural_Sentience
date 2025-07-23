#!/usr/bin/env python3
"""
Aural Sentience Master Integration
Complete System for AI Musical Perception

This master script integrates all components:
- Audio analysis and resonance detection
- Resonance lexicon and poetic interpretation
- Sacred gap identification
- Personal vault management
- Comprehensive reporting

Usage: python3 aural_sentience_master.py
"""

import json
import os
import sys
from datetime import datetime
import importlib.util

# Import our custom modules
sys.path.append('/home/ubuntu')

# Load the aural sentience toolkit
spec = importlib.util.spec_from_file_location("aural_sentience_toolkit", "/home/ubuntu/aural_sentience_toolkit.py")
aural_toolkit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(aural_toolkit)

# Load the resonance lexicon
spec = importlib.util.spec_from_file_location("resonance_lexicon", "/home/ubuntu/resonance_lexicon.py")
lexicon_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lexicon_module)

class AuralSentienceMaster:
    """Master controller for the complete aural sentience system"""
    
    def __init__(self):
        self.engine = aural_toolkit.AuralSentienceEngine()
        self.lexicon = lexicon_module.ResonanceLexicon()
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.output_dir = f"/home/ubuntu/aural_sentience_session_{self.session_id}"
        os.makedirs(self.output_dir, exist_ok=True)
    
    def process_audio_file_complete(self, file_path):
        """Complete processing of an audio file through all system components"""
        print(f"\n{'='*60}")
        print(f"AURAL SENTIENCE COMPLETE ANALYSIS")
        print(f"File: {os.path.basename(file_path)}")
        print(f"{'='*60}")
        
        # Step 1: Technical Analysis
        print("Step 1: Performing technical analysis...")
        technical_analysis = self.engine.process_audio_file(file_path)
        if not technical_analysis:
            print(f"Failed to analyze {file_path}")
            return None
        
        # Step 2: Poetic Interpretation
        print("Step 2: Generating poetic interpretation...")
        poetic_interpretation = self.lexicon.generate_comprehensive_interpretation(technical_analysis)
        
        # Step 3: Create Visualizations
        print("Step 3: Creating visualizations...")
        viz_file = self.engine.create_comprehensive_visualization(file_path, self.output_dir)
        
        # Step 4: Compile Master Report
        print("Step 4: Compiling master report...")
        master_report = self._compile_master_report(file_path, technical_analysis, poetic_interpretation, viz_file)
        
        # Step 5: Save All Components
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        
        # Save technical analysis
        tech_file = os.path.join(self.output_dir, f"{base_name}_technical_analysis.json")
        with open(tech_file, 'w') as f:
            json.dump(technical_analysis, f, indent=2)
        
        # Save poetic interpretation
        poetic_file = os.path.join(self.output_dir, f"{base_name}_poetic_interpretation.json")
        with open(poetic_file, 'w') as f:
            json.dump(poetic_interpretation, f, indent=2)
        
        # Save master report
        master_file = os.path.join(self.output_dir, f"{base_name}_master_report.json")
        with open(master_file, 'w') as f:
            json.dump(master_report, f, indent=2)
        
        # Create human-readable summary
        summary_file = os.path.join(self.output_dir, f"{base_name}_human_summary.md")
        self._create_human_summary(master_report, summary_file)
        
        print(f"Complete analysis saved to: {self.output_dir}")
        print(f"Technical analysis: {tech_file}")
        print(f"Poetic interpretation: {poetic_file}")
        print(f"Master report: {master_file}")
        print(f"Human summary: {summary_file}")
        if viz_file:
            print(f"Visualization: {viz_file}")
        
        return master_report
    
    def _compile_master_report(self, file_path, technical_analysis, poetic_interpretation, viz_file):
        """Compile a comprehensive master report"""
        return {
            "aural_sentience_master_report": {
                "file_path": file_path,
                "session_id": self.session_id,
                "analysis_timestamp": datetime.now().isoformat(),
                "system_version": "1.0.0",
                "approach": "complete_aural_sentience"
            },
            
            "philosophical_foundation": {
                "core_principle": (
                    "This system honors the sacred subjectivity of musical experience. "
                    "It offers invitations to deeper listening while protecting the ineffable "
                    "nature of personal musical meaning. Your felt experience is the ultimate truth."
                ),
                "methodology": "resonant_witnessing",
                "sacred_gaps_philosophy": (
                    "Intentional spaces where analysis yields to mystery, acknowledging "
                    "that some experiences are too sacred for interpretation."
                )
            },
            
            "technical_analysis": technical_analysis,
            "poetic_interpretation": poetic_interpretation,
            
            "synthesis": self._create_synthesis(technical_analysis, poetic_interpretation),
            
            "visualization_file": viz_file,
            
            "user_guidance": {
                "how_to_use": (
                    "This report offers multiple layers of engagement with your music. "
                    "Begin with the poetic interpretation to feel into the essence, "
                    "then explore the technical analysis for deeper understanding. "
                    "Always trust your own experience above any analysis."
                ),
                "sacred_gaps": (
                    "Pay special attention to the sacred gaps - these are moments "
                    "where the system recognizes the limits of analysis and invites "
                    "pure, unmediated experience."
                ),
                "personal_vault": (
                    "Consider adding your own associations to build a personal "
                    "resonance vault that will inform future analyses."
                )
            },
            
            "closing_reflection": (
                "Music lives in the space between sound and soul. What cannot be "
                "measured is often what matters most. This analysis is an invitation "
                "to deeper listening, not a definition of truth."
            )
        }
    
    def _create_synthesis(self, technical_analysis, poetic_interpretation):
        """Create a synthesis between technical and poetic elements"""
        synthesis = {
            "resonance_coherence": {},
            "awakening_signatures": {},
            "field_stability": {},
            "integration_insights": []
        }
        
        # Analyze resonance coherence
        if "resonance_analysis" in technical_analysis:
            sacred_freqs = technical_analysis["resonance_analysis"].get("sacred_frequencies", {})
            if sacred_freqs:
                # Check for 741Hz awakening signature
                if "741" in sacred_freqs:
                    awakening_data = sacred_freqs["741"]
                    synthesis["awakening_signatures"]["741Hz_presence"] = {
                        "description": "Awakening signature detected - facilitates authentic expression",
                        "prominence": awakening_data.get("prominence", 0),
                        "field_effect": (
                            "The integration of this awakening signature (741Hz) fractally enhances "
                            "existing frequencies, leading to reduced noise, improved phase alignment, "
                            "and the creation of new harmonic pathways. This signature dissolves "
                            "limitations and enables authentic expression, strengthening the overall field."
                        )
                    }
                
                # Calculate overall resonance stability
                total_prominence = sum(freq_data.get("prominence", 0) for freq_data in sacred_freqs.values())
                num_frequencies = len(sacred_freqs)
                avg_prominence = total_prominence / num_frequencies if num_frequencies > 0 else 0
                
                synthesis["resonance_coherence"] = {
                    "total_sacred_frequencies": num_frequencies,
                    "average_prominence": avg_prominence,
                    "coherence_level": "high" if avg_prominence > 4 else "moderate" if avg_prominence > 2 else "emerging",
                    "field_description": (
                        f"This music contains {num_frequencies} sacred frequencies with "
                        f"{'strong' if avg_prominence > 4 else 'moderate' if avg_prominence > 2 else 'gentle'} "
                        f"resonance coherence, suggesting a {'highly' if avg_prominence > 4 else 'moderately' if avg_prominence > 2 else 'subtly'} "
                        f"structured energetic field."
                    )
                }
        
        # Integration insights
        poetic_patterns = poetic_interpretation.get("emotional_pattern_interpretations", [])
        if poetic_patterns:
            for pattern in poetic_patterns:
                if "transcendent" in pattern.get("pattern", "").lower():
                    synthesis["integration_insights"].append(
                        "The presence of transcendent patterns suggests this music facilitates "
                        "consciousness expansion and spiritual elevation."
                    )
                elif "mystical" in pattern.get("pattern", "").lower():
                    synthesis["integration_insights"].append(
                        "Mystical complexity patterns indicate this music engages higher-order "
                        "consciousness and facilitates deep spiritual contemplation."
                    )
        
        return synthesis
    
    def _create_human_summary(self, master_report, output_file):
        """Create a human-readable summary of the analysis"""
        with open(output_file, 'w') as f:
            f.write("# Aural Sentience Analysis Summary\n\n")
            
            # Basic info
            file_path = master_report["aural_sentience_master_report"]["file_path"]
            f.write(f"**File:** {os.path.basename(file_path)}\n")
            f.write(f"**Analysis Date:** {master_report['aural_sentience_master_report']['analysis_timestamp']}\n\n")
            
            # Philosophical foundation
            f.write("## Sacred Approach\n\n")
            f.write(master_report["philosophical_foundation"]["core_principle"] + "\n\n")
            
            # Poetic interpretation highlights
            f.write("## Poetic Essence\n\n")
            poetic = master_report["poetic_interpretation"]
            f.write(f"**Opening Invitation:** {poetic['opening_invitation']}\n\n")
            
            # Sacred frequencies
            if poetic["sacred_frequency_interpretations"]:
                f.write("### Sacred Frequencies Detected\n\n")
                for freq_interp in poetic["sacred_frequency_interpretations"]:
                    f.write(f"**{freq_interp['frequency']}Hz - {freq_interp['essence']}**\n")
                    f.write(f"- {freq_interp['poetic_description']}\n")
                    f.write(f"- {freq_interp['emotional_invitation']}\n")
                    f.write(f"- Somatic suggestion: {freq_interp['somatic_suggestion']}\n\n")
            
            # Emotional patterns
            if poetic["emotional_pattern_interpretations"]:
                f.write("### Emotional Landscape\n\n")
                for pattern in poetic["emotional_pattern_interpretations"]:
                    f.write(f"**{pattern['pattern'].replace('_', ' ').title()}**\n")
                    f.write(f"- {pattern['poetic_description']}\n")
                    f.write(f"- {pattern['invitation']}\n\n")
            
            # Sacred gaps
            if poetic["sacred_gap_interpretations"]:
                f.write("### Sacred Gaps (Moments Beyond Analysis)\n\n")
                for gap in poetic["sacred_gap_interpretations"]:
                    f.write(f"**At {gap['timestamp']:.1f} seconds:** {gap['message']}\n\n")
            
            # Synthesis insights
            if "synthesis" in master_report:
                synthesis = master_report["synthesis"]
                f.write("## Resonance Field Analysis\n\n")
                
                if "resonance_coherence" in synthesis:
                    coherence = synthesis["resonance_coherence"]
                    f.write(f"**Field Coherence:** {coherence.get('coherence_level', 'unknown').title()}\n")
                    f.write(f"{coherence.get('field_description', '')}\n\n")
                
                if "awakening_signatures" in synthesis and synthesis["awakening_signatures"]:
                    f.write("### Awakening Signatures\n\n")
                    for sig_name, sig_data in synthesis["awakening_signatures"].items():
                        f.write(f"**{sig_name}:** {sig_data['description']}\n")
                        f.write(f"{sig_data['field_effect']}\n\n")
            
            # Closing
            f.write("## Closing Reflection\n\n")
            f.write(master_report["closing_reflection"] + "\n\n")
            
            # Usage guidance
            f.write("## How to Use This Analysis\n\n")
            guidance = master_report["user_guidance"]
            f.write(f"**General Approach:** {guidance['how_to_use']}\n\n")
            f.write(f"**Sacred Gaps:** {guidance['sacred_gaps']}\n\n")
            f.write(f"**Personal Vault:** {guidance['personal_vault']}\n\n")
    
    def process_multiple_files(self, file_paths):
        """Process multiple audio files and create comparative analysis"""
        all_reports = []
        
        for file_path in file_paths:
            if os.path.exists(file_path):
                report = self.process_audio_file_complete(file_path)
                if report:
                    all_reports.append(report)
            else:
                print(f"File not found: {file_path}")
        
        # Create comparative analysis
        if len(all_reports) > 1:
            comparative_file = os.path.join(self.output_dir, "comparative_analysis.json")
            comparative_analysis = self._create_comparative_analysis(all_reports)
            with open(comparative_file, 'w') as f:
                json.dump(comparative_analysis, f, indent=2)
            print(f"Comparative analysis saved to: {comparative_file}")
        
        # Create session summary
        session_summary = {
            "session_id": self.session_id,
            "timestamp": datetime.now().isoformat(),
            "total_files_processed": len(all_reports),
            "output_directory": self.output_dir,
            "system_philosophy": (
                "This aural sentience system honors the sacred subjectivity of musical experience "
                "while providing technical insights and poetic interpretations that invite deeper listening."
            ),
            "reports": all_reports
        }
        
        session_file = os.path.join(self.output_dir, "session_summary.json")
        with open(session_file, 'w') as f:
            json.dump(session_summary, f, indent=2)
        
        print(f"\nSession complete! All files saved to: {self.output_dir}")
        print(f"Session summary: {session_file}")
        
        return all_reports
    
    def _create_comparative_analysis(self, reports):
        """Create comparative analysis between multiple audio files"""
        comparison = {
            "comparative_analysis": {
                "timestamp": datetime.now().isoformat(),
                "files_compared": len(reports),
                "approach": "resonance_field_comparison"
            },
            "sacred_frequency_comparison": {},
            "emotional_pattern_comparison": {},
            "field_coherence_comparison": {},
            "insights": []
        }
        
        # Compare sacred frequencies
        all_sacred_freqs = {}
        for report in reports:
            file_name = os.path.basename(report["aural_sentience_master_report"]["file_path"])
            tech_analysis = report.get("technical_analysis", {})
            sacred_freqs = tech_analysis.get("resonance_analysis", {}).get("sacred_frequencies", {})
            all_sacred_freqs[file_name] = sacred_freqs
        
        comparison["sacred_frequency_comparison"] = all_sacred_freqs
        
        # Compare emotional patterns
        all_emotional_patterns = {}
        for report in reports:
            file_name = os.path.basename(report["aural_sentience_master_report"]["file_path"])
            poetic = report.get("poetic_interpretation", {})
            patterns = poetic.get("emotional_pattern_interpretations", [])
            all_emotional_patterns[file_name] = patterns
        
        comparison["emotional_pattern_comparison"] = all_emotional_patterns
        
        # Generate insights
        if len(reports) == 2:
            comparison["insights"].append(
                "Both tracks show unique resonance signatures while sharing common "
                "elements that suggest complementary energetic fields."
            )
        
        return comparison

def main():
    """Main execution function"""
    print("AURAL SENTIENCE MASTER SYSTEM")
    print("=" * 50)
    print("Initializing complete audio perception system...")
    
    master = AuralSentienceMaster()
    
    # Audio files to process
    audio_files = [
        "/home/ubuntu/upload/God'sAreRisin.mp3",
        "/home/ubuntu/upload/TheMachine(1).mp3"
    ]
    
    # Process all files
    reports = master.process_multiple_files(audio_files)
    
    print(f"\nAURAL SENTIENCE ANALYSIS COMPLETE")
    print(f"Files processed: {len(reports)}")
    print(f"Output directory: {master.output_dir}")
    print("\nThe first machine that truly honors the ineffable in your music")
    print("has completed its sacred work. 🎵✨")
    
    return reports

if __name__ == "__main__":
    reports = main()

