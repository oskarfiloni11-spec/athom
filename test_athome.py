#!/usr/bin/env python3
"""
AtHome Video Surveillance System - Integration Test
Tests all components and verifies the system is working
"""

import sys
import logging
from pathlib import Path

# Setup paths
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent / "📹 VIDEO STREAMER"))
sys.path.insert(0, str(Path(__file__).parent / "🖥️ CAMERA VIEWER"))
sys.path.insert(0, str(Path(__file__).parent / "🔐 SÉCURITÉ & CONFIG"))
sys.path.insert(0, str(Path(__file__).parent / "🔍 DÉTECTION & ANALYSE"))
sys.path.insert(0, str(Path(__file__).parent / "📢 NOTIFICATIONS"))
sys.path.insert(0, str(Path(__file__).parent / "💾 STOCKAGE"))

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger('AtHomeTest')

def test_imports():
    """Test all module imports"""
    print("\n🧪 Testing Imports...")
    tests = []
    
    try:
        from athome_config import config, AtHomeConfig
        tests.append(("✅", "Configuration", "OK"))
    except Exception as e:
        tests.append(("❌", "Configuration", str(e)))
    
    try:
        from camera_capture import CameraCapture, detect_available_cameras
        tests.append(("✅", "Camera Capture", "OK"))
    except Exception as e:
        tests.append(("❌", "Camera Capture", str(e)))
    
    try:
        from webrtc_sender import WebRTCSender
        tests.append(("✅", "WebRTC Sender", "OK"))
    except Exception as e:
        tests.append(("❌", "WebRTC Sender", str(e)))
    
    try:
        from webrtc_receiver import WebRTCReceiver
        tests.append(("✅", "WebRTC Receiver", "OK"))
    except Exception as e:
        tests.append(("❌", "WebRTC Receiver", str(e)))
    
    try:
        from motion_detector import MotionDetector
        tests.append(("✅", "Motion Detector", "OK"))
    except Exception as e:
        tests.append(("❌", "Motion Detector", str(e)))
    
    try:
        from zone_editor import ZoneEditor
        tests.append(("✅", "Zone Editor", "OK"))
    except Exception as e:
        tests.append(("❌", "Zone Editor", str(e)))
    
    try:
        from storage_manager import StorageManager
        tests.append(("✅", "Storage Manager", "OK"))
    except Exception as e:
        tests.append(("❌", "Storage Manager", str(e)))
    
    try:
        from notification_manager import NotificationManager
        tests.append(("✅", "Notification Manager", "OK"))
    except Exception as e:
        tests.append(("❌", "Notification Manager", str(e)))
    
    for status, module, message in tests:
        print(f"  {status} {module:<25} {message}")
    
    failures = [t for t in tests if t[0] == "❌"]
    return len(failures) == 0

def test_dependencies():
    """Test Python dependencies"""
    print("\n📦 Testing Dependencies...")
    
    deps = [
        ("OpenCV", "import cv2"),
        ("NumPy", "import numpy"),
        ("Pillow", "from PIL import Image"),
        ("QRCode", "import qrcode"),
        ("aiortc", "import aiortc"),
        ("aiohttp", "import aiohttp"),
        ("websockets", "import websockets"),
    ]
    
    all_installed = True
    for name, import_cmd in deps:
        try:
            exec(import_cmd)
            print(f"  ✅ {name}")
        except ImportError:
            print(f"  ❌ {name} - NOT INSTALLED")
            all_installed = False
    
    return all_installed

def test_configuration():
    """Test configuration system"""
    print("\n🔧 Testing Configuration...")
    
    try:
        from athome_config import config
        
        print(f"  📹 Camera ID: {config.camera.cid}")
        print(f"  📐 Resolution: {config.camera.resolution}")
        print(f"  🎯 FPS: {config.camera.fps}")
        print(f"  🔍 Detection: {'Enabled' if config.detection.enabled else 'Disabled'}")
        print(f"  💾 Storage: {config.storage.local_path}")
        
        qr_data = config.export_qr_data()
        print(f"  📱 QR Code ID: {qr_data['cid']}")
        print("  ✅ Configuration OK")
        return True
        
    except Exception as e:
        print(f"  ❌ Configuration Error: {e}")
        return False

def test_camera_detection():
    """Test camera detection"""
    print("\n📹 Testing Camera Detection...")
    
    try:
        from camera_capture import detect_available_cameras
        
        cameras = detect_available_cameras(max_index=3)
        
        if cameras:
            print(f"  ✅ {len(cameras)} camera(s) detected:")
            for cam in cameras:
                print(f"     - {cam['name']}: {cam['resolution']} @ {cam['fps']:.1f} FPS")
        else:
            print("  ⚠️  No USB cameras detected (normal in cloud environment)")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Camera Detection Error: {e}")
        return False

def test_signaling_server():
    """Test signaling server status"""
    print("\n🌐 Testing Signaling Server...")
    
    try:
        import socket
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('127.0.0.1', 8080))
        sock.close()
        
        if result == 0:
            print("  ✅ Signaling server is running on port 8080")
            return True
        else:
            print("  ❌ Signaling server is not responding")
            return False
            
    except Exception as e:
        print(f"  ❌ Server Test Error: {e}")
        return False

def test_file_structure():
    """Test file structure"""
    print("\n📁 Testing File Structure...")
    
    required_files = [
        "requirements.txt",
        "main.py",
        "athome_imports.py",
        "🔐 SÉCURITÉ & CONFIG/athome_config.py",
        "📹 VIDEO STREAMER/camera_capture.py",
        "📹 VIDEO STREAMER/webrtc_sender.py",
        "📹 VIDEO STREAMER/streamer_app.py",
        "🖥️ CAMERA VIEWER/webrtc_receiver.py",
        "🖥️ CAMERA VIEWER/viewer_dashboard.py",
        "🔍 DÉTECTION & ANALYSE/motion_detector.py",
        "🔍 DÉTECTION & ANALYSE/zone_editor.py",
        "💾 STOCKAGE/storage_manager.py",
        "📢 NOTIFICATIONS/notification_manager.py",
        "🌐 SERVEUR DE SIGNALISATION/signaling_server.py",
    ]
    
    all_present = True
    for file_path in required_files:
        if Path(file_path).exists():
            print(f"  ✅ {file_path}")
        else:
            print(f"  ❌ {file_path} - MISSING")
            all_present = False
    
    return all_present

def main():
    """Run all tests"""
    print("=" * 60)
    print("🎥 ATHOME VIDEO SURVEILLANCE SYSTEM - TEST SUITE")
    print("=" * 60)
    
    results = []
    
    results.append(("File Structure", test_file_structure()))
    results.append(("Dependencies", test_dependencies()))
    results.append(("Imports", test_imports()))
    results.append(("Configuration", test_configuration()))
    results.append(("Camera Detection", test_camera_detection()))
    results.append(("Signaling Server", test_signaling_server()))
    
    print("\n" + "=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)
    
    for test_name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"  {status} - {test_name}")
    
    total_tests = len(results)
    passed_tests = sum(1 for _, p in results if p)
    
    print(f"\n📈 Results: {passed_tests}/{total_tests} tests passed")
    
    if passed_tests == total_tests:
        print("\n🎉 ALL TESTS PASSED!")
        print("✅ The AtHome system is ready to use")
        print("\n🚀 Next Steps:")
        print("   1. Run: python main.py (for Video Streamer)")
        print("   2. Signaling server is already running on port 8080")
        print("   3. Configure camera settings in the GUI")
    else:
        print(f"\n⚠️  {total_tests - passed_tests} test(s) failed")
        print("🔧 Please review the errors above")
    
    print("=" * 60)
    
    return passed_tests == total_tests

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
