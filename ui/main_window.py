"""
Главное окно приложения TF2 MvM Botnet
"""

import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QToggleButton, QListWidget, QListWidgetItem, QPushButton,
    QSpinBox, QGroupBox, QGridLayout
)
from PyQt5.QtCore import Qt, pyqtSignal, QThread
from PyQt5.QtGui import QFont, QColor
import config


class MainWindow(QMainWindow):
    """Главное окно приложения"""
    
    # Сигналы для управления ботами
    start_bots = pyqtSignal()
    stop_bots = pyqtSignal()
    server_type_changed = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """Инициализация интерфейса"""
        self.setWindowTitle('TF2 MvM Botnet')
        self.setGeometry(100, 100, config.UI_WINDOW_WIDTH, config.UI_WINDOW_HEIGHT)
        
        # Установка белого фона
        self.setStyleSheet(f"background-color: {config.UI_BACKGROUND_COLOR};")
        
        # Главный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Главная раскладка
        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # Заголовок
        title = QLabel('TF2 MvM Ботнет')
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title.setFont(title_font)
        main_layout.addWidget(title)
        
        # ===== СЕРВЕРЫ =====
        servers_group = QGroupBox('Выбор серверов')
        servers_layout = QHBoxLayout()
        
        # Переключатель локальные серверы
        self.local_toggle = self.create_toggle_button(
            'Локальные серверы для тестирования',
            True
        )
        self.local_toggle.clicked.connect(self.on_local_server_toggled)
        servers_layout.addWidget(self.local_toggle)
        
        # Переключатель серверы друга
        self.friend_toggle = self.create_toggle_button(
            'Серверы друга',
            False
        )
        self.friend_toggle.clicked.connect(self.on_friend_server_toggled)
        servers_layout.addWidget(self.friend_toggle)
        
        servers_group.setLayout(servers_layout)
        main_layout.addWidget(servers_group)
        
        # ===== УПРАВЛЕНИЕ БОТАМИ =====
        bots_group = QGroupBox('Управление ботами')
        bots_layout = QGridLayout()
        
        # Количество ботов
        bots_layout.addWidget(QLabel('Количество ботов:'), 0, 0)
        self.bot_count_spinbox = QSpinBox()
        self.bot_count_spinbox.setMinimum(1)
        self.bot_count_spinbox.setMaximum(config.MAX_BOTS)
        self.bot_count_spinbox.setValue(1)
        bots_layout.addWidget(self.bot_count_spinbox, 0, 1)
        
        # Главный бот (Leader toggle)
        self.leader_toggle = self.create_toggle_button(
            'Главный бот (Leader)',
            True
        )
        bots_layout.addWidget(self.leader_toggle, 1, 0, 1, 2)
        
        bots_group.setLayout(bots_layout)
        main_layout.addWidget(bots_group)
        
        # ===== СПИСОК БОТОВ =====
        bots_list_group = QGroupBox('Список активных ботов')
        bots_list_layout = QVBoxLayout()
        
        self.bots_list = QListWidget()
        self.bots_list.setMinimumHeight(150)
        bots_list_layout.addWidget(self.bots_list)
        
        bots_list_group.setLayout(bots_list_layout)
        main_layout.addWidget(bots_list_group)
        
        # ===== КНОПКИ ДЕЙСТВИЯ =====
        buttons_layout = QHBoxLayout()
        
        self.start_button = QPushButton('Запустить')
        self.start_button.setStyleSheet(
            "background-color: #4CAF50; color: white; font-weight: bold; padding: 10px;"
        )
        self.start_button.clicked.connect(self.on_start_clicked)
        buttons_layout.addWidget(self.start_button)
        
        self.stop_button = QPushButton('Остановить')
        self.stop_button.setStyleSheet(
            "background-color: #f44336; color: white; font-weight: bold; padding: 10px;"
        )
        self.stop_button.setEnabled(False)
        self.stop_button.clicked.connect(self.on_stop_clicked)
        buttons_layout.addWidget(self.stop_button)
        
        main_layout.addLayout(buttons_layout)
        
        # Растяжимое пространство
        main_layout.addStretch()
        
        central_widget.setLayout(main_layout)
        
    def create_toggle_button(self, text: str, checked: bool = False) -> QPushButton:
        """Создание кнопки-переключателя"""
        button = QPushButton(text)
        button.setCheckable(True)
        button.setChecked(checked)
        button.setMinimumHeight(40)
        
        self.update_toggle_style(button)
        return button
    
    def update_toggle_style(self, button: QPushButton):
        """Обновление стиля кнопки-переключателя"""
        if button.isChecked():
            button.setStyleSheet(
                "background-color: #2196F3; color: white; font-weight: bold; border-radius: 5px;"
            )
        else:
            button.setStyleSheet(
                "background-color: #e0e0e0; color: black; border-radius: 5px;"
            )
    
    def on_local_server_toggled(self):
        """Переключение на локальные серверы"""
        if self.local_toggle.isChecked():
            self.friend_toggle.setChecked(False)
            self.update_toggle_style(self.local_toggle)
            self.update_toggle_style(self.friend_toggle)
            self.server_type_changed.emit('local')
    
    def on_friend_server_toggled(self):
        """Переключение на серверы друга"""
        if self.friend_toggle.isChecked():
            self.local_toggle.setChecked(False)
            self.update_toggle_style(self.local_toggle)
            self.update_toggle_style(self.friend_toggle)
            self.server_type_changed.emit('friend')
    
    def on_start_clicked(self):
        """Нажатие кнопки 'Запустить'"""
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.start_bots.emit()
        self.add_bot_to_list("Запуск ботов...")
    
    def on_stop_clicked(self):
        """Нажатие кнопки 'Остановить'"""
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.stop_bots.emit()
        self.bots_list.clear()
    
    def add_bot_to_list(self, bot_name: str, status: str = 'connecting'):
        """Добавление бота в список"""
        item = QListWidgetItem(f"{bot_name} - {status}")
        self.bots_list.addItem(item)
    
    def update_bot_status(self, bot_name: str, status: str):
        """Обновление статуса бота"""
        for i in range(self.bots_list.count()):
            item = self.bots_list.item(i)
            if bot_name in item.text():
                item.setText(f"{bot_name} - {status}")
                break


def main():
    """Главная функция приложения"""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
