"""
Главное окно приложения "Медиатек".

Лабораторная работа 2.1, вариант 1: простое окно с кнопками.
Три кнопки - "Открыть файл", "Сохранить", "Выход" - при нажатии
выводят сообщение в консоль.
"""

import sys

# QApplication - главный объект приложения, управляет событийным циклом.
# QMainWindow - окно верхнего уровня (с потенциальной панелью инструментов,
# строкой состояния и т.п.) - именно от него наследуется наше окно.
# QPushButton - кнопка.
# QVBoxLayout - менеджер компоновки, расставляющий виджеты друг под другом.
# QWidget - базовый "пустой" виджет, используется как центральный контейнер.
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    """Главное окно приложения "Медиатек"."""

    def __init__(self):
        super().__init__()

        # Заголовок окна - ровно тот, что требует вариант 1.
        self.setWindowTitle('Медиатек')
        # setGeometry(x, y, width, height): x,y - положение окна на экране
        # при запуске, width/height - размер окна в пикселях.
        self.setGeometry(100, 100, 400, 250)

        self.init_ui()

    def init_ui(self):
        """Создаёт виджеты, раскладку и подключает сигналы к слотам."""
        # QMainWindow не позволяет класть виджеты прямо на себя -
        # нужен "центральный виджет"-контейнер, на который уже
        # устанавливается layout.
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Вертикальный layout - кнопки будут расположены одна под другой.
        layout = QVBoxLayout()

        # Создаём три кнопки, как того требует вариант.
        self.open_button = QPushButton('Открыть файл')
        self.save_button = QPushButton('Сохранить')
        self.exit_button = QPushButton('Выход')

        # Подключаем сигнал clicked каждой кнопки к своему слоту-обработчику.
        # .clicked - сигнал, который Qt сам генерирует при нажатии.
        # .connect(функция) - связывает сигнал с функцией-обработчиком.
        self.open_button.clicked.connect(self.on_open_click)
        self.save_button.clicked.connect(self.on_save_click)
        self.exit_button.clicked.connect(self.on_exit_click)

        # Добавляем кнопки в layout в нужном порядке.
        layout.addWidget(self.open_button)
        layout.addWidget(self.save_button)
        layout.addWidget(self.exit_button)

        # Применяем layout к центральному виджету - только после этого
        # кнопки реально появятся в окне.
        central_widget.setLayout(layout)

    def on_open_click(self):
        """Слот: обрабатывает нажатие кнопки "Открыть файл"."""
        print('Нажата кнопка "Открыть файл"')

    def on_save_click(self):
        """Слот: обрабатывает нажатие кнопки "Сохранить"."""
        print('Нажата кнопка "Сохранить"')

    def on_exit_click(self):
        """Слот: обрабатывает нажатие кнопки "Выход" - закрывает окно."""
        print('Нажата кнопка "Выход"')
        # self.close() корректно закрывает окно (генерирует событие
        # closeEvent), после чего app.exec() в main() завершается сам.
        self.close()


def main():
    # QApplication должен быть создан один раз, до любых виджетов.
    # sys.argv передаётся, чтобы Qt мог обработать свои служебные
    # аргументы командной строки (например, -style), если они есть.
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    # app.exec() запускает событийный цикл и блокирует выполнение,
    # пока пользователь не закроет окно. sys.exit(...) передаёт код
    # возврата Qt операционной системе.
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
