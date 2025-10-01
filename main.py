"""
AtHome Video Streamer - Main Entry Point
Launches the video streaming application
"""

import sys
import logging
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent / "📹 VIDEO STREAMER"))
sys.path.insert(0, str(Path(__file__).parent / "🔐 SÉCURITÉ & CONFIG"))

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger('AtHomeMain')

def main():
    """Main entry point"""
    try:
        from streamer_app import VideoStreamer
        
        logger.info("Starting AtHome Video Streamer")
        app = VideoStreamer()
        app.window.mainloop()
        
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
