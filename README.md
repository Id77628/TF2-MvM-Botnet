# TF2 MvM Botnet

Система автоматизированных ботов для Team Fortress 2 Mann vs Machine режима.

## Описание

Проект реализует систему многоботовой автоматизации для игры в режим MvM (Mann vs Machine) в Team Fortress 2. Боты могут:

- Автоматически присоединяться к серверам
- Выбирать классы и миссии
- Взаимодействовать между собой (главный бот приглашает подчинённых)
- Навигировать по карте
- Вести боевые операции против врагов

## Архитектура

```
TF2-MvM-Botnet/
├── ui/                    # Графический интерфейс
│   ├── main_window.py    # Главное окно приложения
│   └── controls.py       # UI компоненты
├── bot/                   # Ядро ботов
│   ├── bot_manager.py    # Управление ботами
│   ├── tf2_bot.py        # Базовый класс бота
│   └── bot_roles.py      # Роли и классы ботов
├── game/                  # Игровая логика
│   ├── game_state.py     # Состояние игры
│   ├── missions.py       # Миссии и карты
│   ├── enemies.py        # Враги MvM
│   └── classes.py        # Классы TF2
├── navigation/            # Навигация
│   ├── navmesh.py        # NavMesh парсер
│   └── pathfinding.py    # Поиск пути
├── input/                 # Управление вводом
│   ├── mouse_controller.py
│   ├── keyboard_controller.py
│   └── console.py        # Работа с консолью
├── data/                  # Статические данные
│   ├── missions.json     # Описание миссий
│   ├── enemies.json      # Враги и их характеристики
│   └── maps.json         # Карты и координаты
└── config.py             # Конфигурация
```

## Зависимости

- Python 3.8+
- PyAutoGUI - управление мышью и клавиатурой
- PyQt5 - графический интерфейс
- NumPy - для математических вычислений
- OpenCV - обработка изображений (опционально)

## Установка

```bash
pip install pyautogui pyqt5 numpy opencv-python
```

## Использование

```bash
python main.py
```

## Ссылки на вспомогательные проекты

- [TF2-MvM-Defender-TFBots](https://github.com/OfficerSpy/TF2-MvM-Defender-TFBots) - логика поведения ботов
- [sigsegv-mvm/population](https://github.com/sigsegv-mvm/population) - базы данных миссий и врагов
- [NavMeshes](https://github.com/Arcelis0/NavMeshes) - карты навигации
- [tf-navmesh](https://github.com/jiimjaam/tf-navmesh) - инструменты для работы с NavMesh
