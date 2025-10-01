"""
AtHome Video Streamer - Launcher
Lance l'interface moderne de streaming vidéo
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "📹 VIDEO STREAMER"))
sys.path.insert(0, str(Path(__file__).parent / "🔐 SÉCURITÉ & CONFIG"))

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

if __name__ == "__main__":
    from modern_streamer_gui import ModernStreamerGUI
    
    print("=" * 60)
    print("🎥 AtHome Video Streamer - Interface Moderne")
    print("=" * 60)
    print()
    
    app = ModernStreamerGUI()
    app.run()
