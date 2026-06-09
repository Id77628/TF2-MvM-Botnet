"""
Главная точка входа TF2 MvM Botnet приложения
"""
import sys
import logging
from ui.main_window import MainWindow
from PyQt5.QtWidgets import QApplication
from config import LOG_LEVEL, LOG_FORMAT

# Настройка логирования
logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)
logger = logging.getLogger(__name__)

def main():
    """Запуск приложения"""
    logger.info("Запуск TF2 MvM Botnet...")
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
