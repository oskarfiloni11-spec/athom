"""
Module Helper for AtHome Imports
Simplifies importing modules after reorganization
"""

import sys
from pathlib import Path

def setup_athome_imports():
    """Configure imports for AtHome"""
    current_dir = Path(__file__).parent
    
    module_dirs = [
        "📹 VIDEO STREAMER",
        "🖥️ CAMERA VIEWER", 
        "🔐 SÉCURITÉ & CONFIG",
        "🔍 DÉTECTION & ANALYSE", 
        "📢 NOTIFICATIONS",
        "💾 STOCKAGE",
        "🌐 SERVEUR DE SIGNALISATION",
        "🌐 INTERFACE WEB"
    ]
    
    if str(current_dir) not in sys.path:
        sys.path.insert(0, str(current_dir))
    
    for module_dir in module_dirs:
        module_path = current_dir / module_dir
        if module_path.exists() and str(module_path) not in sys.path:
            sys.path.insert(0, str(module_path))

setup_athome_imports()
