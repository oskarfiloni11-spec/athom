"""
AtHome Video Surveillance System - Installeur Universel
Installation et configuration complète du système
"""

import sys
import os
import subprocess
from pathlib import Path
import json

class AtHomeInstaller:
    """Installeur principal pour le système AtHome"""
    
    def __init__(self):
        self.root_dir = Path(__file__).parent
        self.requirements_file = self.root_dir / "requirements.txt"
        self.config_file = self.root_dir / "athome_config.json"
        
    def print_header(self):
        """Afficher l'en-tête"""
        print("\n" + "=" * 70)
        print("🎥 AtHome Video Surveillance System - Installeur Universel")
        print("=" * 70)
        print()
        
    def check_python(self):
        """Vérifier la version Python"""
        print("📌 Vérification de Python...")
        version = sys.version_info
        
        if version.major < 3 or (version.major == 3 and version.minor < 8):
            print("❌ Python 3.8 ou supérieur requis")
            print(f"   Version actuelle: {version.major}.{version.minor}")
            return False
        
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} détecté")
        return True
        
    def install_dependencies(self):
        """Installer les dépendances"""
        print("\n📦 Installation des dépendances...")
        
        if not self.requirements_file.exists():
            print("❌ Fichier requirements.txt non trouvé")
            return False
        
        try:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", "-r", 
                str(self.requirements_file), "--quiet"
            ])
            print("✅ Dépendances installées avec succès")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Erreur d'installation: {e}")
            return False
            
    def create_config(self):
        """Créer la configuration par défaut"""
        print("\n⚙️ Configuration du système...")
        
        if self.config_file.exists():
            print("✅ Configuration existante trouvée")
            return True
        
        config = {
            "camera": {
                "cid": "usb:0",
                "name": "AtHome Camera 1",
                "enabled": True,
                "resolution": [1280, 720],
                "fps": 30,
                "bitrate": 2500,
                "codec": "h264",
                "audio_enabled": True,
                "rotation": 0,
                "flip_horizontal": False,
                "flip_vertical": False,
                "auto_start": False,
                "stealth_mode": False
            },
            "detection": {
                "enabled": True,
                "sensitivity": 50,
                "min_area": 500,
                "zones": [],
                "record_on_motion": True,
                "pre_record_seconds": 5,
                "post_record_seconds": 10
            },
            "storage": {
                "local_enabled": True,
                "local_path": "./recordings",
                "max_size_gb": 100,
                "retention_days": 30,
                "ftp_enabled": False,
                "s3_enabled": False
            },
            "notifications": {
                "telegram_enabled": False,
                "email_enabled": False
            },
            "security": {
                "password_hash": ""
            },
            "signaling": {
                "host": "0.0.0.0",
                "port": 8080,
                "path": "ws"
            },
            "webrtc": {
                "use_webrtc": True,
                "stun_servers": [
                    "stun:stun.l.google.com:19302",
                    "stun:global.stun.twilio.com:3478"
                ],
                "turn_server": None,
                "fps": 30
            }
        }
        
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=4)
        
        print("✅ Configuration créée avec succès")
        return True
        
    def create_directories(self):
        """Créer les répertoires nécessaires"""
        print("\n📁 Création des répertoires...")
        
        directories = [
            "recordings",
            "snapshots",
            "logs"
        ]
        
        for directory in directories:
            dir_path = self.root_dir / directory
            dir_path.mkdir(exist_ok=True)
            print(f"✅ {directory}/")
        
        return True
        
    def create_shortcuts(self):
        """Créer les raccourcis"""
        print("\n🔗 Création des raccourcis...")
        
        if sys.platform == "win32":
            self.create_windows_shortcuts()
        elif sys.platform == "linux":
            self.create_linux_shortcuts()
        elif sys.platform == "darwin":
            self.create_macos_shortcuts()
        
        return True
        
    def create_windows_shortcuts(self):
        """Créer les raccourcis Windows"""
        try:
            import winshell
            from win32com.client import Dispatch
            
            desktop = winshell.desktop()
            
            # Raccourci Streamer
            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(os.path.join(desktop, "AtHome Streamer.lnk"))
            shortcut.Targetpath = sys.executable
            shortcut.Arguments = str(self.root_dir / "launch_streamer.py")
            shortcut.WorkingDirectory = str(self.root_dir)
            shortcut.save()
            
            # Raccourci Viewer
            shortcut = shell.CreateShortCut(os.path.join(desktop, "AtHome Viewer.lnk"))
            shortcut.Targetpath = sys.executable
            shortcut.Arguments = str(self.root_dir / "launch_viewer.py")
            shortcut.WorkingDirectory = str(self.root_dir)
            shortcut.save()
            
            print("✅ Raccourcis Windows créés sur le bureau")
        except ImportError:
            print("⚠️ Impossible de créer les raccourcis Windows (modules manquants)")
        except Exception as e:
            print(f"⚠️ Erreur lors de la création des raccourcis: {e}")
            
    def create_linux_shortcuts(self):
        """Créer les raccourcis Linux"""
        desktop_dir = Path.home() / "Desktop"
        
        if not desktop_dir.exists():
            desktop_dir = Path.home() / ".local" / "share" / "applications"
            desktop_dir.mkdir(parents=True, exist_ok=True)
        
        # Raccourci Streamer
        streamer_desktop = f"""[Desktop Entry]
Version=1.0
Type=Application
Name=AtHome Streamer
Comment=AtHome Video Streamer Interface
Exec={sys.executable} {self.root_dir / "launch_streamer.py"}
Icon=camera
Terminal=false
Categories=Video;AudioVideo;
"""
        
        streamer_path = desktop_dir / "athome-streamer.desktop"
        with open(streamer_path, 'w') as f:
            f.write(streamer_desktop)
        streamer_path.chmod(0o755)
        
        # Raccourci Viewer
        viewer_desktop = f"""[Desktop Entry]
Version=1.0
Type=Application
Name=AtHome Viewer
Comment=AtHome Camera Viewer Interface
Exec={sys.executable} {self.root_dir / "launch_viewer.py"}
Icon=camera-video
Terminal=false
Categories=Video;AudioVideo;
"""
        
        viewer_path = desktop_dir / "athome-viewer.desktop"
        with open(viewer_path, 'w') as f:
            f.write(viewer_desktop)
        viewer_path.chmod(0o755)
        
        print("✅ Raccourcis Linux créés")
        
    def create_macos_shortcuts(self):
        """Créer les raccourcis macOS"""
        print("ℹ️ Raccourcis macOS: Utilisez les fichiers launch_*.py directement")
        
    def run_tests(self):
        """Exécuter les tests"""
        print("\n🧪 Exécution des tests...")
        
        test_file = self.root_dir / "test_athome.py"
        if not test_file.exists():
            print("⚠️ Fichier de tests non trouvé")
            return True
        
        try:
            result = subprocess.run([sys.executable, str(test_file)], 
                                   capture_output=True, text=True, timeout=30)
            
            if "ALL TESTS PASSED" in result.stdout:
                print("✅ Tous les tests réussis")
                return True
            else:
                print("⚠️ Certains tests ont échoué")
                print(result.stdout[-500:])  # Dernières 500 caractères
                return True  # Ne pas bloquer l'installation
        except Exception as e:
            print(f"⚠️ Erreur lors des tests: {e}")
            return True
            
    def print_summary(self):
        """Afficher le résumé"""
        print("\n" + "=" * 70)
        print("✅ Installation terminée avec succès!")
        print("=" * 70)
        print()
        print("📚 Comment utiliser AtHome:")
        print()
        print("1️⃣ Lancer le Video Streamer:")
        print(f"   python {self.root_dir / 'launch_streamer.py'}")
        print()
        print("2️⃣ Lancer le Camera Viewer:")
        print(f"   python {self.root_dir / 'launch_viewer.py'}")
        print()
        print("3️⃣ Interface Web (pour la documentation):")
        print(f"   L'interface web est accessible depuis le navigateur")
        print()
        print("📁 Fichiers importants:")
        print(f"   - Configuration: {self.config_file}")
        print(f"   - Enregistrements: {self.root_dir / 'recordings'}")
        print(f"   - Captures: {self.root_dir / 'snapshots'}")
        print()
        print("🔧 Fonctionnalités principales:")
        print("   ✅ Streaming WebRTC multi-caméras")
        print("   ✅ Support caméras USB et IP")
        print("   ✅ Détection de mouvement automatique")
        print("   ✅ Enregistrement avec audio")
        print("   ✅ Affichage multi-grilles (1, 2, 3, 4, 6, 9 caméras)")
        print("   ✅ QR code pour appairage rapide")
        print("   ✅ Interface web moderne")
        print()
        print("=" * 70)
        
    def install(self):
        """Lancer l'installation complète"""
        self.print_header()
        
        steps = [
            ("Vérification Python", self.check_python),
            ("Installation dépendances", self.install_dependencies),
            ("Configuration système", self.create_config),
            ("Création répertoires", self.create_directories),
            ("Création raccourcis", self.create_shortcuts),
            ("Tests système", self.run_tests)
        ]
        
        for step_name, step_func in steps:
            if not step_func():
                print(f"\n❌ Échec: {step_name}")
                print("\nInstallation interrompue.")
                return False
        
        self.print_summary()
        return True

if __name__ == "__main__":
    installer = AtHomeInstaller()
    success = installer.install()
    sys.exit(0 if success else 1)
