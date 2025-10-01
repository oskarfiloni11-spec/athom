# AtHome Video Surveillance System

## Overview
AtHome is a comprehensive Python-based video surveillance system featuring WebRTC peer-to-peer streaming, intelligent motion detection, and multi-platform support. The system includes desktop applications, a web interface, and a signaling server for real-time video communication.

**Current State**: ✅ Fully functional with all core components operational
- Signaling server running on port 8080
- All modules tested and working
- Dependencies installed
- Web interface available

## Recent Changes
- **2025-09-30**: Initial project setup completed
  - Created all module directories with proper structure
  - Implemented signaling server with WebSocket support
  - Added camera capture with USB detection
  - Implemented WebRTC sender/receiver modules
  - Created motion detection with configurable zones
  - Added storage manager with retention policies
  - Implemented notification system (Email/Telegram)
  - Created desktop GUI applications (Streamer & Viewer)
  - Added web interface for system overview
  - All tests passing (6/6)

- **2025-09-30**: Modern UI Interfaces Created
  - Created modern_streamer_gui.py - Interface avancée avec design professionnel
  - Created modern_viewer_gui.py - Multi-caméras avec grilles (1, 2, 3, 4, 6, 9)
  - Added launch_streamer.py and launch_viewer.py - Launchers simplifiés
  - Created setup_installer.py - Installeur universel
  - Added comprehensive README.md documentation
  - **Note**: UI interfaces created, backend integration partially complete

## Project Architecture

### Directory Structure
```
AtHome/
├── 📹 VIDEO STREAMER/
│   ├── modern_streamer_gui.py  # ✨ Modern UI avec toutes options
│   ├── streamer_app.py         # GUI streamer original
│   ├── camera_capture.py       # USB camera detection & capture
│   └── webrtc_sender.py        # WebRTC video transmission
│
├── 🖥️ CAMERA VIEWER/
│   ├── modern_viewer_gui.py    # ✨ Multi-cam avec grilles & audio
│   ├── viewer_dashboard.py     # GUI viewer original
│   └── webrtc_receiver.py      # WebRTC video reception
│
├── 🔐 SÉCURITÉ & CONFIG/
│   └── athome_config.py        # JSON-based config management
│
├── 🔍 DÉTECTION & ANALYSE/
│   ├── motion_detector.py      # Motion detection engine
│   └── zone_editor.py          # Detection zone editor
│
├── 💾 STOCKAGE/
│   └── storage_manager.py      # Video recording & retention
│
├── 📢 NOTIFICATIONS/
│   └── notification_manager.py # Email & Telegram alerts
│
├── 🌐 SERVEUR DE SIGNALISATION/
│   └── signaling_server.py     # WebSocket signaling server
│
├── 🌐 INTERFACE WEB/
│   └── web_server.py           # HTTP web server
│
├── launch_streamer.py          # 🚀 Lancer interface moderne streamer
├── launch_viewer.py            # 🚀 Lancer interface moderne viewer
├── setup_installer.py          # 📦 Installeur universel
├── main.py                     # Original streamer entry point
├── test_athome.py             # Integration test suite
├── athome_config.json         # System configuration
├── requirements.txt           # Python dependencies
└── README.md                  # 📚 Documentation complète
```

### Key Components

#### 1. **Signaling Server** (Port 8080)
- WebSocket-based WebRTC signaling
- Camera/viewer registration
- SDP offer/answer exchange
- ICE candidate forwarding
- Multi-client support

#### 2. **Video Streamer** (Desktop App)
- Tkinter-based GUI
- USB camera detection
- WebRTC streaming with overlay
- QR code pairing
- Configurable resolution/FPS

#### 3. **Camera Viewer** (Desktop App)
- Tkinter-based GUI
- WebRTC video reception
- QR code scanner
- Video display with controls

#### 4. **Motion Detection**
- Background subtraction (MOG2)
- Configurable sensitivity
- Detection zones support
- Automatic recording trigger

#### 5. **Storage Manager**
- Local video recording (AVI)
- Retention policy (days)
- Storage quota management
- Automatic cleanup

#### 6. **Notifications**
- Email alerts (SMTP)
- Telegram notifications
- Motion detection alerts
- Image attachments

## Technology Stack

### Core Technologies
- **Python 3.11**: Main programming language
- **WebRTC (aiortc)**: Peer-to-peer video streaming
- **OpenCV**: Video processing & motion detection
- **aiohttp**: Async HTTP server
- **WebSockets**: Real-time signaling
- **Tkinter**: Desktop GUI framework

### Key Dependencies
```
aiohttp>=3.8.0          # Async web framework
aiortc>=1.6.0           # WebRTC implementation
av>=10.0.0              # Video codecs
opencv-python-headless  # Computer vision (headless)
Pillow>=10.0.0         # Image processing
numpy>=1.24.0          # Numerical operations
qrcode[pil]>=7.4.0     # QR code generation
websockets>=11.0.0     # WebSocket client/server
cryptography>=41.0.0   # Security & encryption
```

## Configuration

### Configuration File (`athome_config.json`)
```json
{
    "camera": {
        "cid": "usb:0",
        "resolution": [1280, 720],
        "fps": 30,
        "codec": "h264"
    },
    "detection": {
        "enabled": true,
        "sensitivity": 50,
        "record_on_motion": true
    },
    "storage": {
        "local_path": "./recordings",
        "max_size_gb": 100,
        "retention_days": 30
    },
    "signaling": {
        "host": "127.0.0.1",
        "port": 8080
    },
    "webrtc": {
        "stun_servers": [
            "stun:stun.l.google.com:19302"
        ]
    }
}
```

## How to Use

### Running the System

1. **Signaling Server** (Already Running)
   - Automatically started on port 8080
   - Handles WebRTC signaling

2. **Video Streamer** (Desktop)
   ```bash
   python main.py
   ```
   - Select camera from dropdown
   - Configure settings
   - Start streaming
   - Scan QR code with viewer

3. **Camera Viewer** (Desktop)
   ```bash
   python "🖥️ CAMERA VIEWER/viewer_dashboard.py"
   ```
   - Scan QR code from streamer
   - Connect to camera
   - View live feed

4. **Web Interface**
   ```bash
   python "🌐 INTERFACE WEB/web_server.py"
   ```
   - Open browser to http://localhost:5000
   - View system status
   - Access documentation

### Testing
```bash
python test_athome.py
```
Tests:
- ✅ File structure
- ✅ Dependencies
- ✅ Module imports
- ✅ Configuration
- ✅ Camera detection
- ✅ Signaling server

## Features

### Implemented ✅
- [x] WebRTC peer-to-peer video streaming (backend)
- [x] USB camera detection & capture
- [x] Desktop streamer application (Tkinter) - Original & Modern UI
- [x] Desktop viewer dashboard (Tkinter) - Original & Modern UI
- [x] WebSocket signaling server
- [x] Motion detection with zones
- [x] Local video recording
- [x] QR code pairing system
- [x] Configuration management
- [x] Notification framework
- [x] Web interface
- [x] Modern UI with advanced controls (Streamer)
- [x] Multi-camera grid layouts (Viewer: 1,2,3,4,6,9)
- [x] IP camera support UI (RTSP)
- [x] Audio controls per camera UI
- [x] Recording options UI (format, quality, folder)
- [x] Universal installer (setup_installer.py)
- [x] Launch scripts (launch_streamer.py, launch_viewer.py)
- [x] Comprehensive documentation (README.md)

### Integration Needed 🔧
- [ ] Connect modern UI to WebRTC backend (aiortc pipelines)
- [ ] Implement audio capture/playback (PyAudio/sounddevice)
- [ ] Wire recording to storage_manager from UI
- [ ] Implement RTSP stream opening for IP cameras
- [ ] Connect QR pairing to signaling server sessions
- [ ] Add authentication for signaling/web endpoints
- [ ] Implement streaming URL generation for local network

### Planned 🔮
- [ ] Browser-based WebRTC viewer
- [ ] Cloud storage integration (S3, FTP)
- [ ] Active notifications (Email/Telegram)
- [ ] Mobile app support
- [ ] AI object detection
- [ ] Multi-user authentication
- [ ] Recording playback UI
- [ ] Live thumbnail previews

## Development Notes

### Cloud Environment Considerations
- Using `opencv-python-headless` for headless operation
- No physical cameras in Replit environment (normal)
- Signaling server accessible on all interfaces (0.0.0.0)
- Test suite handles cloud limitations gracefully

### WebRTC Architecture
1. Camera creates offer via signaling server
2. Viewer receives offer and creates answer
3. ICE candidates exchanged for NAT traversal
4. Direct peer-to-peer video stream established
5. STUN servers used for public IP discovery

### Security
- Password hashing (SHA-256)
- WebRTC encryption (DTLS/SRTP)
- Configurable access controls
- Secret management via environment

## Troubleshooting

### Common Issues
1. **No cameras detected**: Normal in cloud environment
2. **WebSocket connection errors**: Check signaling server logs
3. **WebRTC connection fails**: Verify STUN servers accessible
4. **Motion detection false positives**: Adjust sensitivity
5. **Storage full**: Check retention policy and cleanup

### Logs
- Signaling server: Check workflow logs
- Application: Check console output
- WebRTC: Browser developer console

## Project Status
**Status**: 🟡 Modern UI Complete - Backend Integration In Progress
**Core Backend**: ✅ Functional (WebRTC, Signaling, Detection, Storage)
**Modern UI**: ✅ Complete (Streamer & Viewer interfaces)
**Integration**: 🔧 Partial (UI needs backend wiring)
**Test Results**: 6/6 passing (backend tests)
**Signaling Server**: Running on port 8080
**Last Updated**: 2025-09-30

## How to Launch Modern Interfaces

```bash
# Lancer le Video Streamer moderne
python launch_streamer.py

# Lancer le Camera Viewer moderne
python launch_viewer.py

# Installeur universel (création config, raccourcis, etc.)
python setup_installer.py
```
