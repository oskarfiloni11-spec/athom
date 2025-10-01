"""
AtHome Camera Viewer - Launcher
Lance l'interface moderne de visualisation multi-caméras
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "🖥️ CAMERA VIEWER"))
sys.path.insert(0, str(Path(__file__).parent / "🔐 SÉCURITÉ & CONFIG"))

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

if __name__ == "__main__":
    from modern_viewer_gui import ModernViewerGUI
    
    print("=" * 60)
    print("🖥️ AtHome Camera Viewer - Interface Moderne")
    print("=" * 60)
    print()
    
    app = ModernViewerGUI()
    app.run()
