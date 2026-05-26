"""
Comparador Inteligente de Planilhas
Ponto de entrada principal do aplicativo
"""

import sys
import os

# Adiciona o diretório raiz ao path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont, QFontDatabase

from app.ui.splash_screen import SplashScreen
from app.ui.main_window import MainWindow
from app.core.settings import AppSettings


def main():
    # Habilita DPI alto
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    
    app = QApplication(sys.argv)
    app.setApplicationName("Comparador Inteligente de Planilhas")
    app.setApplicationVersion("1.0.0")
    app.setOrganizationName("SmartCompare")
    
    # Aplica stylesheet global
    settings = AppSettings()
    app.setStyleSheet(get_global_stylesheet(settings.theme))
    
    # Exibe splash screen
    splash = SplashScreen()
    splash.show()
    app.processEvents()
    
    # Cria janela principal
    window = MainWindow(settings)
    
    def finish_splash():
        splash.close()
        window.show()
        window.activateWindow()
    
    QTimer.singleShot(2500, finish_splash)
    
    sys.exit(app.exec())


def get_global_stylesheet(theme: str) -> str:
    """Retorna o stylesheet global baseado no tema."""
    if theme == "dark":
        return """
            QApplication {
                font-family: 'Segoe UI', sans-serif;
            }
            QToolTip {
                background-color: #1e2433;
                color: #e2e8f0;
                border: 1px solid #3d4663;
                border-radius: 6px;
                padding: 6px 10px;
                font-size: 12px;
            }
            QScrollBar:vertical {
                background: #1a1f2e;
                width: 8px;
                border-radius: 4px;
            }
            QScrollBar::handle:vertical {
                background: #3d4663;
                border-radius: 4px;
                min-height: 30px;
            }
            QScrollBar::handle:vertical:hover {
                background: #5b6a99;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
            QScrollBar:horizontal {
                background: #1a1f2e;
                height: 8px;
                border-radius: 4px;
            }
            QScrollBar::handle:horizontal {
                background: #3d4663;
                border-radius: 4px;
                min-width: 30px;
            }
            QScrollBar::handle:horizontal:hover {
                background: #5b6a99;
            }
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
                width: 0px;
            }
        """
    else:
        return """
            QToolTip {
                background-color: #f8fafc;
                color: #1e293b;
                border: 1px solid #cbd5e1;
                border-radius: 6px;
                padding: 6px 10px;
                font-size: 12px;
            }
            QScrollBar:vertical {
                background: #f1f5f9;
                width: 8px;
                border-radius: 4px;
            }
            QScrollBar::handle:vertical {
                background: #cbd5e1;
                border-radius: 4px;
                min-height: 30px;
            }
            QScrollBar::handle:vertical:hover {
                background: #94a3b8;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
        """


if __name__ == "__main__":
    main()
