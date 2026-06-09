"""
Конфигурация приложения для TF2 MvM Botnet
"""

import os
from dataclasses import dataclass
from typing import Dict, List

# Пути к файлам
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
LOG_DIR = os.path.join(BASE_DIR, 'logs')

# Создаём директории если их нет
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

# UI Конфигурация
UI_WINDOW_WIDTH = 600
UI_WINDOW_HEIGHT = 400
UI_BACKGROUND_COLOR = "#FFFFFF"

# Боты
MAX_BOTS = 10
BOT_SPAWN_DELAY = 2  # секунды между спауном ботов

# Таймауты
CONNECTION_TIMEOUT = 30
MISSION_SEARCH_TIMEOUT = 60
RESPAWN_DELAY = 10  # Время восстановления после смерти

# Классы TF2
TF2_CLASSES = [
    'Scout',
    'Soldier',
    'Pyro',
    'Demoman',
    'Heavy',
    'Engineer',
    'Medic',
    'Sniper',
    'Spy'
]

# Типы серверов
SERVER_TYPES = {
    'local': 'Локальные серверы для тестирования',
    'friend': 'Серверы друга'
}

# Режимы игры
GAME_MODES = {
    'mvm': 'Mann vs Machine'
}

# Состояния бота
@dataclass
class BotState:
    """Состояние бота"""
    IN_MENU = 'in_menu'
    SEARCHING = 'searching'
    IN_GAME = 'in_game'
    DEAD = 'dead'
    RESPAWNING = 'respawning'
    DISCONNECTED = 'disconnected'

# Роли главного бота
@dataclass
class BotRole:
    """Роли ботов в команде"""
    LEADER = 'leader'          # Главный бот (приглашает других)
    FOLLOWER = 'follower'      # Подчинённый бот (принимает приглашение)

# Mouse контроль
MOUSE_MOVEMENT_SPEED = 1.0
MOUSE_CLICK_DURATION = 0.1

# Клавиатура
KEYBOARD_PRESS_DURATION = 0.05

# Логирование
LOG_LEVEL = 'INFO'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Пути для примеров
MISSIONS_DATA_FILE = os.path.join(DATA_DIR, 'missions.json')
ENEMIES_DATA_FILE = os.path.join(DATA_DIR, 'enemies.json')
MAPS_DATA_FILE = os.path.join(DATA_DIR, 'maps.json')
NAVMESH_DIR = os.path.join(DATA_DIR, 'navmeshes')
