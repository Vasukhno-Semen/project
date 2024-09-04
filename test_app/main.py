import calendar  # Импортируем модуль для работы с календарем
from babel.dates import format_date  # Импортируем функцию для форматирования дат
from datetime import date  # Импортируем класс date для работы с датами
from kivy.app import App  # Импортируем базовый класс приложения Kivy
from PIL import Image  # Импортируем модуль для работы с изображениями
from kivy.uix.boxlayout import BoxLayout  # Импортируем BoxLayout для размещения виджетов
from kivy.uix.label import Label  # Импортируем Label для отображения текста
from kivy.uix.togglebutton import ToggleButton  # Импортируем ToggleButton для переключаемых кнопок
from kivy.uix.relativelayout import RelativeLayout  # Импортируем RelativeLayout для относительного размещения
from kivy.graphics import Color, Rectangle  # Импортируем Color и Rectangle для рисования
from kivy.uix.button import Button  # Импортируем Button для кнопок
from kivy.uix.textinput import TextInput  # Импортируем TextInput для ввода текста
from kivy.uix.gridlayout import GridLayout  # Импортируем GridLayout для размещения виджетов в сетке
from kivy.uix.screenmanager import ScreenManager, Screen  # Импортируем ScreenManager и Screen для управления экранами
from kivy_garden.mapview import MapView, MapMarker  # Импортируем MapView и MapMarker для работы с картами
from kivy.uix.floatlayout import FloatLayout  # Импортируем FloatLayout для плавающего размещения
from kivy.uix.image import Image  # Импортируем Image для отображения изображений
from kivy.core.window import Window  # Импортируем Window для работы с окном приложения
import sqlite3  # Импортируем sqlite3 для работы с базой данных
from kivycalendar3 import CalendarWidget  # Импортируем виджет календаря
from kivy.uix.popup import Popup  # Импортируем Popup для всплывающих окон
import webbrowser  # Импортируем webbrowser для открытия ссылок в браузере
import os  # Импортируем os для работы с операционной системой
from kivy.metrics import dp  # Импортируем dp для работы с плотностью пикселей
from kivy.logger import Logger  # Импортируем Logger для ведения логов
from kivy.uix.anchorlayout import AnchorLayout  # Импортируем AnchorLayout для размещения виджетов с якорями

# Получаем путь к текущей папке
current_directory = os.path.dirname(os.path.abspath(__file__))

# Имена файлов изображений
image_filename = 'Settings.png'
image_filename1 = 'Settings (1).png'
image_filename2 = 'User.png'
image_filename3 = 'User (2).png'
image_filename4 = 'Open Parcel.png'
image_filename5 = 'Open Parcel (2).png'
image_filename6 = 'Rectangle 48.png'
image_filename7 = 'Rectangle 70.png'
image_filename8 = 'Rectangle 64.png'
image_filename9 = 'Ellipse 10.png'
image_filename10 = 'Ellipse 6.png'
image_filename11 = 'Ellipse 7.png'
image_filename12 = 'Ellipse 7 (1).png'
image_filename13 = 'Bookmark.png'
image_filename14 = 'Bookmark (1).png'

# Полные пути к изображениям
settingslight_path = os.path.join(current_directory, image_filename)
settingsdark_path = os.path.join(current_directory, image_filename1)
userdark_path = os.path.join(current_directory, image_filename2)
userlight_path = os.path.join(current_directory, image_filename3)
catalogdark_path = os.path.join(current_directory, image_filename4)
cataloglight_path = os.path.join(current_directory, image_filename5)
rec48_path = os.path.join(current_directory, image_filename6)
rec70_path = os.path.join(current_directory, image_filename7)
rec64_path = os.path.join(current_directory, image_filename8)
el1light_path = os.path.join(current_directory, image_filename9)
el1dark_path = os.path.join(current_directory, image_filename10)
el2dark_path = os.path.join(current_directory, image_filename11)
el2light_path = os.path.join(current_directory, image_filename12)
maindark_path = os.path.join(current_directory, image_filename13)
mainlight_path = os.path.join(current_directory, image_filename14)


def create_database():
    # Создаем подключение к базе данных
    connection = sqlite3.connect('registrations.db')
    cursor = connection.cursor()

    # Создаем таблицы, если они не существуют
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS registrations (
            id INTEGER,
            nickname TEXT UNIQUE,
            fullname TEXT NOT NULL,
            phone TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            institution TEXT,
            email TEXT UNIQUE,
            weight NUMERIC,
            PRIMARY KEY(id)
        );
    ''')
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS calendar (
            "id"	INTEGER,
            "year"	TEXT,
            "month"	TEXT,
            PRIMARY KEY("id")
            );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
            "id"	INTEGER,
            "school"	TEXT,
            "time"	TEXT,
            "event_date"	TEXT,
            PRIMARY KEY("id")
            );
    """)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "our_progress" (
            "id"	INTEGER,
            "stage"	INTEGER,
            PRIMARY KEY("id")
            );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recycling_stations (
            "id"	INTEGER,
            "lat"	REAL,
            "lon"	REAL,
            PRIMARY KEY("id")
            );
    ''')

    # Проверяем и добавляем записи, если они отсутствуют
    record_id = "1"
    cursor.execute('''SELECT * FROM calendar WHERE id = ?''', (record_id,))
    result = cursor.fetchone()
    if result is None:
        cursor.execute('''INSERT INTO calendar (year, month) VALUES ("2024","9")''')
        connection.commit()

    record_id2 = "1"
    cursor.execute('''SELECT * FROM events WHERE id = ?''', (record_id2,))
    result2 = cursor.fetchone()
    if result2 is None:
        cursor.execute(
            '''INSERT INTO events (school, time, event_date) VALUES ("Пример школы №1","12:00", "2024-09-09")''')
        connection.commit()

    record_id = "2"
    cursor.execute('''SELECT * FROM events WHERE id = ?''', (record_id,))
    result3 = cursor.fetchone()
    if result3 is None:
        cursor.execute(
            '''INSERT INTO events (school, time, event_date) VALUES ("Пример школы №2","08:50", "2024-09-22")''')
        connection.commit()

    record_id = "1"
    cursor.execute('''SELECT * FROM our_progress WHERE id = ?''', (record_id,))
    result4 = cursor.fetchone()
    if result4 is None:
        cursor.execute('''INSERT INTO our_progress (stage) VALUES (2)''')
        connection.commit()

    record_id = "1"
    cursor.execute('''SELECT * FROM recycling_stations WHERE id = ?''', (record_id,))
    result5 = cursor.fetchone()
    if result5 is None:
        cursor.execute('''INSERT INTO recycling_stations (lat, lon) VALUES (-23.987, 18.78)''')
        connection.commit()

    record_id1 = "2"
    cursor.execute('''SELECT * FROM recycling_stations WHERE id = ?''', (record_id1,))
    result6 = cursor.fetchone()
    if result6 is None:
        cursor.execute('''INSERT INTO recycling_stations (lat, lon) VALUES (-32.987, 81.78)''')
        connection.commit()

    connection.commit()  # Сохраняем изменения
    connection.close()  # Закрываем подключение


create_database()  # Создаем базу данных


class BaseScreen(Screen):
    def __init__(self, **kwargs):
        super(BaseScreen, self).__init__(**kwargs)
        self.font_size = 18  # Устанавливаем размер шрифта

    def update_text_color(self, color):
        # Обновляем цвет текста для всех виджетов Label и Button
        for widget in self.walk():
            if isinstance(widget, Label) or isinstance(widget, Button):
                widget.color = color

    def update_images(self, light):
        # Обновляем изображения в зависимости от темы
        if light:
            self.settings_image.source = 'https://github.com/Vasukhno-Semen/project/blob/main/Settings.png'
            self.main_screen_image.source = "https://github.com/Vasukhno-Semen/project/blob/main/Bookmark%20(1).png"
            self.personal_image.source = 'https://github.com/Vasukhno-Semen/project/blob/main/User%20(2).png'
            self.catalog_image.source = 'https://github.com/Vasukhno-Semen/project/blob/main/Open%20Parcel%20(2).png'
        else:
            self.settings_image.source = 'C:\\Users\\admin\\PycharmProjects\\pythonProject\\Settings (1).png'
            self.main_screen_image.source = 'C:\\Users\\admin\\PycharmProjects\\pythonProject\\Bookmark.png'
            self.personal_image.source = 'C:\\Users\\admin\\PycharmProjects\\pythonProject\\User.png'
            self.catalog_image.source = 'C:\\Users\\admin\\PycharmProjects\\pythonProject\\Open Parcel.png'

        # Перезагружаем изображения, чтобы изменения вступили в силу
        self.settings_image.reload()
        self.main_screen_image.reload()
        self.personal_image.reload()
        self.catalog_image.reload()


class MainMenuScreen(BaseScreen):
    def __init__(self, **kwargs):
        super(MainMenuScreen, self).__init__(**kwargs)
        Window.clearcolor = (0.121, 0.121, 0.121, 1)  # Устанавливаем цвет фона

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Кнопка регистрации
        register_button = Button(text='Регистрация', size_hint_y=None, height=50)
        register_button.bind(on_press=self.go_to_registration)
        layout.add_widget(register_button)

        # Кнопка входа
        login_button = Button(text='Вход', size_hint_y=None, height=50)
        login_button.bind(on_press=self.go_to_login)
        layout.add_widget(login_button)

        self.add_widget(layout)

    def update_bg_rect(self, *args):
        # Обновляем позицию и размер фона
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size

    def go_to_registration(self, instance):
        # Переход на экран регистрации
        self.manager.current = 'register_form'

    def go_to_login(self, instance):
        # Переход на экран входа
        self.manager.current = 'login_form'

    def update_font_size(self, size):
        # Обновляем размер шрифта для всех виджетов Label и Button
        for widget in self.walk():
            if isinstance(widget, Label) or isinstance(widget, Button):
                widget.font_size = size


class RegisterFormScreen1(BaseScreen):
    def __init__(self, **kwargs):
        super(RegisterFormScreen1, self).__init__(**kwargs)
        with self.canvas.before:
            Color(0.121, 0.121, 0.121, 1)  # Устанавливаем цвет фона
            self.bg_rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(pos=self.update_bg_rect, size=self.update_bg_rect)

        layout = GridLayout(cols=2, padding=10, spacing=10)

        # Поля ввода для регистрации
        layout.add_widget(Label(text='Никнейм'))
        self.nickname_input = TextInput(multiline=False)
        layout.add_widget(self.nickname_input)

        layout.add_widget(Label(text='ФИО'))
        self.name_input = TextInput(multiline=False)
        layout.add_widget(self.name_input)

        layout.add_widget(Label(text='Телефон'))
        self.phone_input = TextInput(multiline=False)
        layout.add_widget(self.phone_input)

        layout.add_widget(Label(text='Пароль'))
        self.password_input = TextInput(multiline=False, password=True)
        layout.add_widget(self.password_input)

        layout.add_widget(Label(text='Повторите пароль'))
        self.password_confirm_input = TextInput(multiline=False, password=True)
        layout.add_widget(self.password_confirm_input)

        layout.add_widget(Label(text='Учебное заведение (необязательно)'))
        self.institution_input = TextInput(multiline=False)
        layout.add_widget(self.institution_input)

        layout.add_widget(Label(text='Почта'))
        self.email_input = TextInput(multiline=False)
        layout.add_widget(self.email_input)

        # Кнопка отправки регистрации
        submit_button = Button(text='Зарегистрироваться', size_hint_y=None, height=50)
        submit_button.bind(on_press=self.submit_registration)
        layout.add_widget(submit_button)

        # Кнопка назад
        back_button = Button(text='Назад', size_hint_y=None, height=50)
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def update_bg_rect(self, *args):
        # Обновляем позицию и размер фона
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size

    def submit_registration(self, instance):
        # Обработка регистрации
        nickname = self.nickname_input.text
        fullname = self.name_input.text
        phone = self.phone_input.text
        password = self.password_input.text
        password_confirm = self.password_confirm_input.text
        institution = self.institution_input.text
        email = self.email_input.text

        if not nickname or not fullname or not phone or not password or not password_confirm:
            print("Все обязательные поля должны быть заполнены.")
            return

        if password != password_confirm:
            print("Пароли не совпадают.")
            return

        user_id = self.save_to_database(nickname, fullname, phone, password, institution, email)

        profile_screen = self.manager.get_screen('profile')
        profile_screen.update_profile(user_id, nickname, fullname, phone, institution, email)

        self.manager.current = 'profile'

    def save_to_database(self, nickname, fullname, phone, password, institution, email):
        # Сохраняем данные в базу данных
        connection = sqlite3.connect('registrations.db')
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO registrations (nickname, fullname, phone, password, institution, email, weight)
            VALUES (?, ?, ?, ?, ?, ?, 0)
        ''', (nickname, fullname, phone, password, institution, email))
        connection.commit()
        user_id = cursor.lastrowid
        connection.close()
        return user_id

    def go_back(self, instance):
        # Переход на главный экран
        self.manager.current = 'main_menu'

    def update_font_size(self, size):
        # Обновляем размер шрифта для всех виджетов Label и Button
        for widget in self.walk():
            if isinstance(widget, Label) or isinstance(widget, Button):
                widget.font_size = size

    def on_enter(self, *args):
        # Обновляем размер шрифта при входе на экран
        font_size = self.manager.get_screen('settings').font_size
        self.update_font_size(font_size)


class LoginFormScreen(BaseScreen):
    def __init__(self, **kwargs):
        super(LoginFormScreen, self).__init__(**kwargs)

        layout = GridLayout(cols=2, padding=10, spacing=10)

        # Поля ввода для входа
        layout.add_widget(Label(text='Телефон/Никнейм/Почта'))
        self.username_input = TextInput(multiline=False)
        layout.add_widget(self.username_input)

        layout.add_widget(Label(text='Пароль'))
        self.password_input = TextInput(multiline=False, password=True)
        layout.add_widget(self.password_input)

        # Кнопка входа
        login_button = Button(text='Войти', size_hint_y=None, height=50)
        login_button.bind(on_press=self.submit_login)
        layout.add_widget(login_button)

        # Кнопка назад
        back_button = Button(text='Назад', size_hint_y=None, height=50)
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def submit_login(self, instance):
        # Обработка входа
        username = self.username_input.text
        password = self.password_input.text

        if not username or not password:
            print("Пожалуйста, заполните все поля.")
            return

        user_data = self.check_credentials(username, password)
        if user_data:
            user_id, nickname, fullname, phone, institution, email, weight = user_data
            print("Вход успешен!")

            profile_screen = self.manager.get_screen('profile')
            main_screen = self.manager.get_screen('main')
            profile_screen.update_profile(user_id, nickname, password, phone, institution, email)
            main_screen.get_user_id(user_id)

            self.manager.current = 'profile'
        else:
            print("Неверные учетные данные.")

    def check_credentials(self, username, password):
        # Проверяем учетные данные
        connection = sqlite3.connect('registrations.db')
        cursor = connection.cursor()
        cursor.execute('''
            SELECT id, nickname, fullname, phone, institution, email, weight 
            FROM registrations
            WHERE (phone = ? OR nickname = ? OR email = ?) AND password = ?
        ''', (username, username, username, password))
        result = cursor.fetchone()
        connection.close()
        return result

    def go_back(self, instance):
        # Переход на главный экран
        self.manager.current = 'main_menu'

    def on_enter(self, *args):
        # Обновляем размер шрифта при входе на экран
        settings_screen = self.manager.get_screen('settings')
        if hasattr(settings_screen, 'font_size'):
            font_size = settings_screen.font_size
            self.update_font_size(font_size)

    def update_font_size(self, size):
        # Обновляем размер шрифта для всех виджетов Label и Button
        for widget in self.walk():
            if isinstance(widget, Label) or isinstance(widget, Button):
                widget.font_size = size


class CalendarWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.year, self.month = self.load_calendar_date()  # Загружаем текущий год и месяц из базы данных
        self.dates_with_events = self.load_event_dates()  # Загружаем даты с событиями
        self.weekday_labels = []  # Список для хранения меток дней недели
        self.create_calendar()  # Создаем календарь

    def update_text_color(self, color):
        # Обновляем цвет текста для всех меток дней недели
        for label in self.weekday_labels:
            label.color = color

        # Изменяем цвет текста для всех кнопок
        for button, date_str in self.buttons:
            if date_str not in self.dates_with_events:
                button.color = color

    def load_calendar_date(self):
        # Загружаем текущий год и месяц из базы данных
        connection = sqlite3.connect('registrations.db')
        cursor = connection.cursor()
        cursor.execute('SELECT year, month FROM calendar LIMIT 1')
        year, month = cursor.fetchone()
        connection.close()
        return int(year), int(month)

    def load_event_dates(self):
        # Загружаем даты с событиями из базы данных
        connection = sqlite3.connect('registrations.db')
        cursor = connection.cursor()
        cursor.execute('SELECT event_date FROM events')
        dates = [row[0] for row in cursor.fetchall()]
        connection.close()
        return dates

    def create_calendar(self):
        # Создаем календарь
        year = self.year
        month = self.month

        # Форматируем название месяца
        month_name = format_date(date(year, month, 1), "LLLL", locale='ru')
        header = Label(text=f'{month_name.capitalize()} {year}', size_hint_y=None, height=50,
                       color=(0.37, 0.64, 0.93, 1))
        self.add_widget(header)

        # Создаем макет календаря
        calendar_layout = GridLayout(cols=7, size_hint_y=None, height=350, padding=[0, 0, 0, 0], spacing=0)
        calendar_layout.bind(minimum_height=calendar_layout.setter('height'))

        # Добавляем метки дней недели
        days_of_week = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
        for day in days_of_week:
            label = Label(text=day, size_hint_y=None, height=40, color=(0.37, 0.64, 0.93, 1))
            calendar_layout.add_widget(label)
            self.weekday_labels.append(label)

        # Получаем первый день и количество дней в месяце
        first_day, num_days = calendar.monthrange(year, month)

        # Добавляем пустые метки для выравнивания
        for _ in range(first_day):
            calendar_layout.add_widget(Label(text='', size_hint_y=None, height=40))

        self.buttons = []  # Сохраняем кнопки для последующего изменения цвета

        # Добавляем кнопки для каждого дня
        for day in range(1, num_days + 1):
            date_str = f'{year}-{month:02d}-{day:02d}'
            button = Button(
                text=str(day),
                background_normal='',
                background_color=(0, 0, 0, 0),  # Полностью прозрачный фон
                color=(0.37, 0.64, 0.93, 1),  # Цвет текста для всех кнопок
                size_hint=(1, None),
                height=50
            )

            # Если дата в базе данных, используем другой цвет
            if date_str in self.dates_with_events:
                button.color = (1, 0, 0, 1)  # Ярко-красный текст для дат с событиями

            button.bind(on_press=self.on_day_press)
            calendar_layout.add_widget(button)
            self.buttons.append((button, date_str))  # Сохраняем кнопку и дату

        with calendar_layout.canvas.before:
            Color(1, 1, 1, 1)  # Белый цвет фона
            self.bg_rect = Rectangle(source=str(rec70_path), pos=self.pos, size=self.size)

        calendar_layout.bind(pos=self.update_bg_rect, size=self.update_bg_rect)

        self.add_widget(calendar_layout)

        # Горизонтальные линии
        with self.canvas:
            Color(1, 0.5, 0, 1)  # Оранжевый цвет
            self.weekday_divider = Rectangle(size=(self.width, 2))

        self.line_images = []
        for _ in range(5):
            with self.canvas:
                Color(1, 0.5, 0, 1)  # Оранжевый цвет
                line_image = Rectangle(size=(self.width, 2))
                self.line_images.append(line_image)

        # Вертикальные линии
        self.vertical_lines = []
        for _ in range(6):  # 6 линий для 7 столбцов
            with self.canvas:
                Color(1, 0.5, 0, 1)  # Оранжевый цвет
                vertical_line = Rectangle(size=(2, calendar_layout.height))
                self.vertical_lines.append(vertical_line)

        calendar_layout.bind(pos=self.update_lines, size=self.update_lines)

    def check_theme(self):
        # Проверяем текущую тему и обновляем цвет текста
        current_color = self.get_background_color()
        Logger.info(f"MainScreen: Current background color: {current_color}")

        if current_color == [1, 1, 1, 1]:
            Logger.info("MainScreen: Applying light theme")
            self.update_text_color((0.21, 0.37, 0.19, 1))
        elif current_color == [0.121, 0.121, 0.121, 1]:
            Logger.info("MainScreen: Applying dark theme")
            self.update_text_color((0.71, 0.87, 0.19, 1))

    def on_day_press(self, instance):
        # Обработка нажатия на день
        day = instance.text
        selected_date = f'{self.year}-{self.month:02d}-{int(day):02d}'

        # Обновление цвета текста для выбранной даты
        for button, date_str in self.buttons:
            if date_str == selected_date:
                button.color = (1, 0, 0, 1)  # Красный цвет текста для выбранной даты
            else:
                # Возвращаем цвет в зависимости от состояния
                if date_str in self.dates_with_events:
                    button.color = (1, 0, 0, 1)
                else:
                    button.color = (0.37, 0.64, 0.93, 1)

        if self.parent and self.parent.parent:
            self.parent.parent.on_day_select(selected_date)

    def update_bg_rect(self, instance, value):
        # Обновляем позицию и размер фона
        self.bg_rect.pos = instance.pos
        self.bg_rect.size = instance.size

    def update_lines(self, instance, value):
        # Обновляем линии сетки календаря
        label_height = 40  # Высота меток
        button_height = 50  # Высота кнопок
        column_width = instance.width / 7  # Ширина каждого столбца

        # Обновляем горизонтальные линии
        self.weekday_divider.pos = (instance.x, instance.top - label_height)
        self.weekday_divider.size = (instance.width, 2)

        for i, line_image in enumerate(self.line_images):
            y = instance.top - label_height - (i + 1) * button_height
            line_image.pos = (instance.x, y)
            line_image.size = (instance.width, 2)

        # Обновляем вертикальные линии
        for i, vertical_line in enumerate(self.vertical_lines):
            x = instance.x + (i + 1) * column_width
            vertical_line.pos = (x, instance.y)
            vertical_line.size = (2, instance.height)


class MainScreen(Screen):
    def __init__(self, **kwargs):
        # Инициализация главного экрана, вызывая родительский конструктор
        super(MainScreen, self).__init__(**kwargs)

        # Логируем информацию о инициализации экрана
        Logger.info('MainScreen: Initializing MainScreen')

        # Создаем основной макет экрана
        self.main_layout = FloatLayout()

        # Создаем нижний макет с кнопками на экране
        self.create_bottom_layout()

        # Получаем текущее состояние (stage) из базы данных
        self.stage = self.get_stage_from_db()
        Logger.info(f'MainScreen: Stage from DB: {self.stage}')

        # Отображаем содержимое, соответствующее текущему состоянию
        self.show_stage_content()

        # Добавляем основной макет на экран
        self.add_widget(self.main_layout)

    def update_text_color(self, color):
        # Обновление цвета текста для всех кнопок на экране
        for widget in self.main_layout.children:
            if isinstance(widget, Button):
                widget.color = color

    def on_enter(self):
        # Логируем событие входа на экран
        Logger.info('MainScreen: Entering screen')
        self.check_theme()

    def create_bottom_layout(self):
        # Создает нижний макет, который будет содержать кнопки и изображения
        bottom_layout = FloatLayout(size_hint=(1, None), height=dp(48))

        # Создаем фоновое изображение для нижнего макета
        bottom_background = Image(
            source=str(rec48_path),
            size_hint=(1, 1),
            allow_stretch=True,
            keep_ratio=False,
            pos_hint={'center_x': 0.5, 'y': 0}
        )
        # Добавляем фоновое изображение в нижний макет
        bottom_layout.add_widget(bottom_background)

        # Создаем кнопку для перехода в каталог
        self.catalog_button = Button(
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            pos_hint={'right': 0.4, 'y': 0.05},
            background_normal='',
            background_down='',
            background_color=(1, 1, 1, 0),
            on_press=self.show_catalog
        )

        # Создаем кнопку для настроек
        self.settings_button = Button(
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            pos_hint={'right': 0.95, 'y': 0.05},
            background_normal='',
            background_down='',
            background_color=(1, 1, 1, 0),
            on_press=self.show_settings
        )

        # Создаем изображение для кнопки настроек
        self.settings_image = Image(
            source=str(settingsdark_path),
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            pos_hint={'right': 0.95, 'y': 0.05}
        )

        # Создаем кнопку профиля
        self.profile_button = Button(
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            pos_hint={'center_x': 0.2, 'y': 0.05},
            background_normal='',
            background_down='',
            background_color=(1, 1, 1, 0),
            on_press=self.show_profile
        )

        # Создаем изображения для других кнопок (главный экран, личный профиль и т.д.)
        self.main_screen_image = Image(
            source=str(maindark_path),
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            pos_hint={'right': 0.75, 'y': 0.05}
        )

        self.eclipse_image = Image(
            source=str(el1dark_path),
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            pos_hint={'right': 0.75, 'y': 0.05}
        )

        self.personal_image = Image(
            source=str(rec48_path),
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            pos_hint={'right': 0.2, 'y': 0.05}
        )

        self.catalog_image = Image(
            source=str(catalogdark_path),
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            pos_hint={'right': 0.4, 'y': 0.05}
        )

        # Добавляем все кнопки и изображения в нижний макет
        bottom_layout.add_widget(self.profile_button)
        bottom_layout.add_widget(self.settings_button)
        bottom_layout.add_widget(self.catalog_button)
        bottom_layout.add_widget(self.settings_image)
        bottom_layout.add_widget(self.eclipse_image)
        bottom_layout.add_widget(self.main_screen_image)
        bottom_layout.add_widget(self.personal_image)
        bottom_layout.add_widget(self.catalog_image)

        # Добавляем нижний макет в основной макет
        self.main_layout.add_widget(bottom_layout)

    def clear_layout(self):
        # Очищает основной макет и заново создает нижний макет
        self.main_layout.clear_widgets()
        self.create_bottom_layout()

    def get_stage_from_db(self):
        # Получает текущее состояние из базы данных
        try:
            connection = sqlite3.connect('registrations.db')
            cursor = connection.cursor()
            cursor.execute('SELECT stage FROM our_progress')
            result = cursor.fetchone()
            connection.close()
            return result[0] if result else 1  # Возвращает 1, если нет результатов
        except sqlite3.Error as e:
            Logger.error(f"Database error: {e}")
            return 1  # Возвращает 1 при ошибке

    def get_background_color(self):
        # Получает цвет фона окна
        return Window.clearcolor

    def check_theme(self):
        # Проверяет текущую тему и применяет изменения
        current_color = self.get_background_color()
        Logger.info(f"MainScreen: Current background color: {current_color}")

        if current_color == [1, 1, 1, 1]:  # Если светлая тема
            Logger.info("MainScreen: Applying light theme")
            self.update_text_color((0.21, 0.37, 0.19, 1))
            # Загружаем светлые изображения на кнопки
            self.settings_image.source = str(settingslight_path)
            self.main_screen_image.source = str(mainlight_path)
            self.personal_image.source = str(userlight_path)
            self.catalog_image.source = str(cataloglight_path)
            self.eclipse_image.source = str(el1light_path)

        elif current_color == [0.121, 0.121, 0.121, 1]:  # Если темная тема
            Logger.info("MainScreen: Applying dark theme")
            self.update_text_color((0.71, 0.87, 0.19, 1))
            # Загружаем темные изображения на кнопки
            self.settings_image.source = str(settingsdark_path)
            self.main_screen_image.source = str(maindark_path)
            self.personal_image.source = str(userdark_path)
            self.catalog_image.source = str(catalogdark_path)
            self.eclipse_image.source = str(el1dark_path)

        # Обновляем изображения для применения изменений
        self.settings_image.reload()
        self.main_screen_image.reload()
        self.personal_image.reload()
        self.catalog_image.reload()
        self.eclipse_image.reload()

    def show_stage_content(self):
        # Отображает содержимое экрана в зависимости от текущего состояния
        self.check_theme()
        self.clear_layout()
        if self.stage == 1:
            Logger.info('MainScreen: Showing stage1')
            self.show_stage1()
        elif self.stage == 2:
            Logger.info('MainScreen: Showing stage2')
            self.show_stage2()
        elif self.stage == 3:
            Logger.info('MainScreen: Showing stage3')
            self.show_stage3()

    def show_stage1(self):
        # Отображает содержимое первого этапа
        calendar = CalendarWidget(size_hint=(0.8, 0.6), pos_hint={'center_x': 0.5, 'center_y': 0.6})
        self.main_layout.add_widget(calendar)

        # Кнопка для перехода на главную страницу Google
        google_link_button = Button(text='Перейти на главную страницу Google', size_hint=(0.6, 0.1),
                                    pos_hint={'center_x': 0.5, 'y': 0.1}, background_normal=str(rec48_path))
        google_link_button.bind(on_press=self.open_google)
        self.main_layout.add_widget(google_link_button)

    def on_day_select(self, selected_date):
        # Обрабатывает выбор даты на календаре
        try:
            Logger.info(f"Selected date: {selected_date}")
            connection = sqlite3.connect('registrations.db')
            cursor = connection.cursor()
            cursor.execute('SELECT school, time FROM events WHERE event_date = ?', (selected_date,))
            result = cursor.fetchone()
            connection.close()

            if result:
                school, time = result
                Logger.info(f"Event found: School: {school}, Time: {time}")
                content = BoxLayout(orientation='vertical')
                content.add_widget(Label(text=f'Школа: {school}\nВремя: {time}'))
                close_button = Button(text='Закрыть')
                content.add_widget(close_button)

                popup = Popup(title='Информация о лекции', content=content, size_hint=(0.7, 0.7))
                close_button.bind(on_press=popup.dismiss)
                popup.open()
            else:
                Logger.info(f"No event found for date: {selected_date}")
        except sqlite3.Error as e:
            Logger.error(f"Database error: {e}")

    def open_google(self, instance):
        # Открывает главную страницу Google в браузере
        webbrowser.open('https://www.google.com')

    def show_stage2(self):
        # Отображает содержимое второго этапа
        layout = FloatLayout()

        # Создаем и добавляем изображение
        image = Image(
            source=str(rec64_path),
            allow_stretch=True, keep_ratio=False,
            size_hint=(0.9, 0.7),
            pos_hint={'center_x': 0.5, 'center_y': 0.6}
        )
        layout.add_widget(image)

        # Создаем вид карты с заданными координатами
        map_view = MapView(
            zoom=10, lat=40.7128, lon=-74.0060,
            size_hint=(0.8, 0.6),
            pos_hint={'center_x': 0.5, 'center_y': 0.6}
        )
        layout.add_widget(map_view)

        # Добавляем макет карты в основной макет
        self.main_layout.add_widget(layout)

        # Получаем данные с координатами станций переработки из базы данных
        try:
            connection = sqlite3.connect('registrations.db')
            cursor = connection.cursor()
            cursor.execute('SELECT lat, lon FROM recycling_stations')
            for lat, lon in cursor.fetchall():
                marker = MapMarker(lat=lat, lon=lon)
                map_view.add_marker(marker)
            connection.close()
        except sqlite3.Error as e:
            Logger.error(f"Database error: {e}")

        # Кнопка для получения своего ID
        id_button = Button(
            text='Узнать свой ID',
            size_hint=(0.6, 0.1),
            pos_hint={'center_x': 0.5, 'y': 0.1},
            background_normal=str(rec48_path),
            background_down=str(rec48_path),
            color=(0.71, 0.87, 0.19, 1)
        )
        id_button.bind(on_press=self.show_user_id)
        self.main_layout.add_widget(id_button)

    def get_user_id(self, user_id):
        # Хранит ID пользователя для дальнейшего использования
        global user_id1
        user_id1 = user_id

    def show_user_id(self, instance):
        # Показывает ID пользователя в всплывающем окне
        global user_id1
        try:
            connection = sqlite3.connect('registrations.db')
            cursor = connection.cursor()
            cursor.execute('SELECT id FROM registrations')
            result = cursor.fetchone()
            connection.close()

            content = BoxLayout(orientation='vertical')
            content.add_widget(Label(text=f'Ваш ID: {user_id1}'))
            close_button = Button(text='Закрыть')
            content.add_widget(close_button)

            popup = Popup(title='Ваш ID', content=content, size_hint=(0.7, 0.7))
            close_button.bind(on_press=popup.dismiss)
            popup.open()
        except sqlite3.Error as e:
            Logger.error(f"Database error: {e}")

    def show_stage3(self):
        # Отображает содержимое третьего этапа
        calendar = CalendarWidget(size_hint=(0.8, 0.6), pos_hint={'center_x': 0.5, 'center_y': 0.6})
        self.main_layout.add_widget(calendar)

        # Кнопка для перехода на главную страницу Google
        google_link_button = Button(text='Перейти на главную страницу Google', size_hint=(0.6, 0.1),
                                    pos_hint={'center_x': 0.5, 'y': 0.1},
                                    background_normal=str(rec48_path))
        google_link_button.bind(on_press=self.open_google)
        self.main_layout.add_widget(google_link_button)

    def go_to_masterclass(self, instance):
        # Переход на экран мастер-классов
        self.manager.current = 'masterclasses'

    def show_profile(self, instance):
        # Переход на экран профиля
        self.manager.current = 'profile'

    def show_settings(self, instance):
        # Переход на экран настроек
        self.manager.current = 'settings'

    def show_catalog(self, instance):
        # Переход на экран каталога
        self.manager.current = 'catalog'


class ProfileScreen(Screen):
    def __init__(self, **kwargs):
        # Инициализация экрана профиля
        super(ProfileScreen, self).__init__(**kwargs)

        # Создание основного макета для профиля
        self.layout = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))

        # Создаем макет для изображения профиля
        image_layout = AnchorLayout(size_hint_y=None, height=dp(120))
        self.image = Image(source=str(el2dark_path),
                           size_hint=(None, None), size=(dp(100), dp(100)))
        image_layout.add_widget(self.image)

        # Создаем метки для отображения информации о пользователе
        self.nickname_label = self.create_label('Имя пользователя', width=dp(250))
        self.phone_label = self.create_label('Телефон', width=dp(250))
        self.email_label = self.create_label('Почта', width=dp(250))
        self.password_label = self.create_label('Пароль', width=dp(250))
        self.institution_label = self.create_label('Учебное заведение', width=dp(250))
        self.ecoins_label = self.create_label('Экокоины', width=dp(250))

        # Создаем макет для кнопки выхода
        logout_layout = AnchorLayout(size_hint_y=None, height=dp(54))
        self.logout_button = Button(
            text='Выйти из аккаунта',
            size_hint=(None, None),
            size=(dp(170), dp(44)),
            background_normal=str(rec48_path),
            background_down=str(rec48_path),
            color=(0.705, 0.875, 0.188, 1)
        )
        self.logout_button.bind(on_press=self.logout)
        logout_layout.add_widget(self.logout_button)

        # Создаем нижний макет для кнопок
        bottom_layout = FloatLayout(size_hint=(1, None), height=dp(48))

        # Добавляем фоновое изображение в нижний макет
        bottom_background = Image(
            source=str(rec48_path),
            size_hint=(1, 1),
            allow_stretch=True,
            keep_ratio=False,
            pos_hint={'center_x': 0.5, 'y': 0}
        )
        bottom_layout.add_widget(bottom_background)

        # Создаем кнопки для перехода на экран настроек и в каталог
        self.settings_button = Button(
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            pos_hint={'right': 0.95, 'y': 0.05},
            background_normal='',
            background_down='',
            background_color=(1, 1, 1, 0),
            on_press=self.go_to_settings
        )
        self.catalog_button = Button(
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            pos_hint={'right': 0.4, 'y': 0.05},
            background_normal='',
            background_down='',
            background_color=(1, 1, 1, 0),
            on_press=self.show_catalog
        )
        # Изображения для кнопок
        self.settings_image = Image(
            source=str(settingsdark_path),
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            pos_hint={'right': 0.95, 'y': 0.05}
        )

        self.main_screen_button = Button(
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            pos_hint={'center_x': 0.75, 'y': 0.05},
            background_normal='',
            background_down='',
            background_color=(1, 1, 1, 0)
        )

        self.main_screen_image = Image(
            source=str(maindark_path),
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            pos_hint={'right': 0.75, 'y': 0.05}
        )

        self.eclipse_image = Image(
            source=str(el1dark_path),
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            pos_hint={'right': 0.2, 'y': 0.05}
        )

        self.personal_image = Image(
            source=str(userdark_path),
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            pos_hint={'right': 0.2, 'y': 0.05}
        )

        self.catalog_image = Image(
            source=str(catalogdark_path),
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            pos_hint={'right': 0.4, 'y': 0.05}
        )

        # Привязываем действие нажатия на кнопку
        self.main_screen_button.bind(on_press=self.go_to_main)

        # Добавляем все кнопки и изображения в нижний макет
        bottom_layout.add_widget(self.main_screen_button)
        bottom_layout.add_widget(self.settings_button)
        bottom_layout.add_widget(self.catalog_button)
        bottom_layout.add_widget(self.settings_image)
        bottom_layout.add_widget(self.main_screen_image)
        bottom_layout.add_widget(self.eclipse_image)
        bottom_layout.add_widget(self.personal_image)
        bottom_layout.add_widget(self.catalog_image)

        # Добавляем все элементы в общий макет
        self.layout.add_widget(image_layout)
        self.layout.add_widget(self.create_anchor_layout(self.nickname_label))
        self.layout.add_widget(self.create_anchor_layout(self.phone_label))
        self.layout.add_widget(self.create_anchor_layout(self.email_label))
        self.layout.add_widget(self.create_anchor_layout(self.password_label))
        self.layout.add_widget(self.create_anchor_layout(self.institution_label))
        self.layout.add_widget(self.create_anchor_layout(self.ecoins_label))
        self.layout.add_widget(logout_layout)
        self.layout.add_widget(bottom_layout)

        # Добавляем общий макет на экран
        self.add_widget(self.layout)

    def get_background_color(self):
        # Получает цвет фона окна
        return Window.clearcolor

    def update_text_color(self, color):
        # Обновление текста всех кнопок на экране профиля
        for widget in self.layout.children:
            if isinstance(widget, Button):
                widget.color = color

    def on_enter(self):
        # Логируем событие входа на экран профиля
        Logger.info('MainScreen: Entering screen')
        self.check_theme()

    def check_theme(self):
        # Проверяет текущую тему и применяет изменения
        current_color = self.get_background_color()
        Logger.info(f"MainScreen: Current background color: {current_color}")

        if current_color == [1, 1, 1, 1]:  # Светлая тема
            Logger.info("MainScreen: Applying light theme")
            self.update_text_color((0.21, 0.37, 0.19, 1))
            # Загружаем светлые изображения на кнопки
            self.settings_image.source = str(settingslight_path)
            self.main_screen_image.source = str(mainlight_path)
            self.personal_image.source = str(userlight_path)
            self.catalog_image.source = str(cataloglight_path)
            self.eclipse_image.source = str(el1light_path)
            # дополнительное изображение
            self.image.source = str(el2light_path)

        elif current_color == [0.121, 0.121, 0.121, 1]:  # Темная тема
            Logger.info("MainScreen: Applying dark theme")
            self.update_text_color((0.71, 0.87, 0.19, 1))
            # Загружаем темные изображения на кнопки
            self.settings_image.source = str(settingsdark_path)
            self.main_screen_image.source = str(maindark_path)
            self.personal_image.source = str(userdark_path)
            self.catalog_image.source = str(catalogdark_path)
            self.eclipse_image.source = str(el1dark_path)
            self.image.source = str(el2dark_path)

        # Обновляем изображения для применения изменений
        self.settings_image.reload()
        self.main_screen_image.reload()
        self.personal_image.reload()
        self.catalog_image.reload()
        self.eclipse_image.reload()
        self.image.reload()

    def create_label(self, text, width):
        # Создает метку с заданным текстом и шириной
        label = Label(text=text, size_hint=(None, None), size=(width, dp(44)),
                      color=(0.705, 0.875, 0.188, 1))
        with label.canvas.before:
            # Создание фона для метки
            label.bg_rect = Rectangle(
                source='C:\\Users\\admin\\PycharmProjects\\pythonProject\\Rectangle 48.png',
                pos=label.pos,
                size=label.size
            )

        # Привязка размерами метки к прямоугольнику фона
        label.bind(pos=self.update_bg_rect, size=self.update_bg_rect)
        return label

    def create_anchor_layout(self, widget):
        # Создает макет для виджета с заданной высотой
        anchor_layout = AnchorLayout(size_hint_y=None, height=dp(54))
        anchor_layout.add_widget(widget)
        return anchor_layout

    def update_bg_rect(self, instance, *args):
        # Обновляет размеры и позицию фона метки
        instance.bg_rect.pos = instance.pos
        instance.bg_rect.size = instance.size

    def update_profile(self, user_id, nickname, password, phone, institution, email):
        # Обновляет информацию о пользователе в метках
        self.nickname_label.text = f'Никнейм: {nickname}'
        self.phone_label.text = f'Телефон: {phone}'
        self.email_label.text = f'Почта: {email}'
        self.institution_label.text = f'Учебное заведение: {institution}'
        self.password_label.text = f'Пароль: {password}'

    def go_to_main(self, instance):
        # Переход на главный экран
        self.manager.current = 'main'

    def go_to_settings(self, instance):
        # Переход на экран настроек
        self.manager.current = 'settings'

    def show_catalog(self, instance):
        # Переход на экран каталога
        self.manager.current = "catalog"

    def logout(self, instance):
        # Выход из аккаунта и переход на экран главного меню
        self.manager.current = 'main_menu'

    def on_enter1(self, *args):
        # Обновление при входе на экран профиля
        settings_screen = self.manager.get_screen('settings')
        if hasattr(settings_screen, 'font_size'):
            font_size = settings_screen.font_size
            self.update_font_size(font_size)

    def update_font_size(self, size):
        # Обновление размера шрифта для всех виджетов
        for widget in self.walk():
            if isinstance(widget, Label) or isinstance(widget, Button):
                widget.font_size = size

class CatalogScreen(Screen):
    def __init__(self, **kwargs):
        # Инициализация экранирования CatalogScreen
        super(CatalogScreen, self).__init__(**kwargs)

        # Создание макета с плавающей компоновкой
        self.layout = FloatLayout()

        # Поле ввода для поиска товаров в верхней части экрана
        self.search_input = TextInput(
            hint_text='Поиск',  # Подсказка для пользователя
            size_hint=(0.8, None),  # Занимает 80% ширины экрана
            height=dp(40),  # Высота поля ввода
            pos_hint={'top': 1, 'center_x': 0.5},  # Позиционирование в верхней части экрана по центру
            background_normal=str(rec48_path),  # Фоновое изображение для поля ввода
            background_active=str(rec48_path),  # Изображение при активном состоянии
            padding=[dp(10), dp(10), dp(10), dp(10)],  # Отступы внутри поля ввода
            foreground_color=(0.37, 0.64, 0.93, 1)  # Цвет текста в поле ввода
        )
        self.search_input.bind(text=self.on_search_text)  # Привязка метода к событию изменения текста
        self.layout.add_widget(self.search_input)  # Добавление поля ввода на макет

        # Метка для сообщений о том, что товары отсутствуют
        self.no_items_label = Label(
            text='Товары пока отсутствуют',  # Текст метки
            size_hint=(None, None),  # Размеры не зависят от размера экрана
            size=(dp(200), dp(40)),  # Фиксированные размеры метки
            pos_hint={'center_x': 0.5, 'center_y': 0.5},  # Позиционирование по центру
            color=(0.37, 0.64, 0.93, 1)  # Цвет текста метки
        )
        self.layout.add_widget(self.no_items_label)  # Добавление метки на макет

        # Создание нижнего макета для кнопок навигации
        bottom_layout = FloatLayout(size_hint=(1, None), height=dp(48), pos_hint={'y': 0})

        # Фоновое изображение для нижнего макета
        bottom_background = Image(
            source=str(rec48_path),  # Путь к изображению
            size_hint=(1, 1),  # Занимает всю ширину и высоту своего контейнера
            allow_stretch=True,  # Позволяет изображению растягиваться
            keep_ratio=False,  # Не сохраняет пропорции изображения при растяжении
            pos_hint={'center_x': 0.5, 'y': 0}  # Позиционирование по центру в нижней части
        )
        bottom_layout.add_widget(bottom_background)  # Добавление фонового изображения на нижний макет

        # Кнопка профиля
        self.profile_button = Button(
            size_hint=(None, None),  # Фиксированный размер кнопки
            size=(dp(40), dp(40)),  # Размер кнопки
            pos_hint={'center_x': 0.2, 'y': 0.05},  # Позиционирование кнопки
            background_normal='',  # Нет фонового изображения
            background_down='',  # Нет изображения для нажатой кнопки
            background_color=(1, 1, 1, 0),  # Прозрачный фон кнопки
            on_press=self.show_profile  # Метод, вызываемый при нажатии
        )

        # Кнопка настроек
        self.settings_button = Button(
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            pos_hint={'right': 0.95, 'y': 0.05},
            background_normal='',
            background_down='',
            background_color=(1, 1, 1, 0),
            on_press=self.go_to_settings  # Переход к экрану настроек
        )

        # Изображение настроек
        self.settings_image = Image(
            source=str(settingsdark_path),  # Путь к изображению
            size_hint=(None, None),  # Фиксированный размер изображения
            size=(dp(40), dp(40)),  # Размер изображения
            pos_hint={'right': 0.95, 'y': 0.05}  # Позиционирование изображения
        )

        # Кнопка для перехода на главный экран
        self.main_screen_button = Button(
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            pos_hint={'center_x': 0.75, 'y': 0.05},
            background_normal='',
            background_down='',
            background_color=(1, 1, 1, 0),
            on_press=self.go_to_main  # Переход на главный экран
        )

        # Изображение главного экрана
        self.main_screen_image = Image(
            source=str(maindark_path),  # Путь к изображению
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            pos_hint={'right': 0.75, 'y': 0.05}  # Позиционирование изображения
        )

        # Другие изображения и кнопки
        self.eclipse_image = Image(
            source=str(el1dark_path),
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            pos_hint={'right': 0.4, 'y': 0.05}
        )

        self.personal_image = Image(
            source=str(userdark_path),
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            pos_hint={'right': 0.2, 'y': 0.05}
        )

        self.catalog_image = Image(
            source=str(catalogdark_path),
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            pos_hint={'right': 0.4, 'y': 0.05}
        )

        # Добавление кнопок и изображений в нижний макет
        bottom_layout.add_widget(self.main_screen_button)
        bottom_layout.add_widget(self.settings_button)
        bottom_layout.add_widget(self.profile_button)
        bottom_layout.add_widget(self.settings_image)
        bottom_layout.add_widget(self.main_screen_image)
        bottom_layout.add_widget(self.eclipse_image)
        bottom_layout.add_widget(self.personal_image)
        bottom_layout.add_widget(self.catalog_image)

        # Добавление нижнего макета на основной макет
        self.layout.add_widget(bottom_layout)
        self.add_widget(self.layout)  # Добавление основного макета на экран

    def on_search_text(self, instance, value):
        # Логика для поиска товаров
        print(f"Searching for: {value}")

    def go_to_settings(self, instance):
        # Переход к экрану настроек
        self.manager.current = 'settings'

    def go_to_main(self, instance):
        # Переход на главный экран
        self.manager.current = 'main'

    def show_profile(self, instance):
        # Переход к экрану профиля
        self.manager.current = "profile"

    def get_background_color(self):
        # Получение текущего цвета фона
        return Window.clearcolor

    def update_text_color(self, color):
        # Обновление цвета текста для всех кнопок на экране
        for widget in self.layout.children:
            if isinstance(widget, Button):
                widget.color = color

    def on_enter(self):
        # Метод, вызываемый при входе на экран
        Logger.info('CatalogScreen: Entering screen')
        self.check_theme()

    def check_theme(self):
        # Проверка текущей темы (светлая или темная)
        current_color = self.get_background_color()
        Logger.info(f"CatalogScreen: Current background color: {current_color}")

        if current_color == [1, 1, 1, 1]:  # Светлая тема
            Logger.info("MainScreen: Applying light theme")
            self.update_text_color((0.21, 0.37, 0.19, 1))  # Установка цвета текста
            self.settings_image.source = str(settingslight_path)
            self.main_screen_image.source = str(mainlight_path)
            self.personal_image.source = str(userlight_path)
            self.catalog_image.source = str(cataloglight_path)
            self.eclipse_image.source = str(el1light_path)

        elif current_color == [0.121, 0.121, 0.121, 1]:  # Темная тема
            Logger.info("MainScreen: Applying dark theme")
            self.update_text_color((0.71, 0.87, 0.19, 1))  # Установка цвета текста
            self.settings_image.source = str(settingsdark_path)
            self.main_screen_image.source = str(maindark_path)
            self.personal_image.source = str(userdark_path)
            self.catalog_image.source = str(catalogdark_path)
            self.eclipse_image.source = str(el1dark_path)

        # Обновление изображений
        self.settings_image.reload()
        self.main_screen_image.reload()
        self.personal_image.reload()
        self.catalog_image.reload()
        self.eclipse_image.reload()

# Определение экрана настроек
class SettingsScreen(BaseScreen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        layout = FloatLayout()

        # Метка для выбора темы
        self.theme_label = Label(text='Тема:', font_size=self.font_size,
                                 size_hint=(None, None), size=(100, 40))
        self.theme_label.pos_hint = {'x': 0.05, 'top': 0.9}
        layout.add_widget(self.theme_label)

        # Дропдаун для выбора темы
        self.theme_dropdown = BoxLayout(orientation='horizontal', spacing=10,
                                        size_hint_x=0.9, size_hint_y=None, height=50)
        self.theme_dropdown.pos_hint = {'x': 0.05, 'top': 0.85}

        # Кнопки для выбора тем
        self.light_theme = Button(text='Светлая', size_hint=(1, None), height=50,
                                  background_normal=str(rec48_path),
                                  background_down=str(rec48_path))
        self.dark_theme = Button(text='Темная', size_hint=(1, None), height=50,
                                 background_normal=str(rec48_path),
                                 background_down=str(rec48_path))
        self.system_theme = Button(text='Системная', size_hint=(1, None), height=50,
                                   background_normal=str(rec48_path),
                                   background_down=str(rec48_path))

        # Добавление кнопок выбора темы в дропдаун
        self.theme_dropdown.add_widget(self.light_theme)
        self.theme_dropdown.add_widget(self.dark_theme)
        self.theme_dropdown.add_widget(self.system_theme)
        layout.add_widget(self.theme_dropdown)

        # Метка для выбора размера шрифта
        self.font_size_label = Label(text='Размер шрифта:', font_size=self.font_size,
                                     size_hint=(None, None), size=(200, 40))
        self.font_size_label.pos_hint = {'x': 0.05, 'top': 0.75}
        layout.add_widget(self.font_size_label)

        # Дропдаун для выбора размера шрифта
        self.font_size_dropdown = BoxLayout(orientation='horizontal', spacing=10,
                                            size_hint_x=0.9, size_hint_y=None, height=50)
        self.font_size_dropdown.pos_hint = {'x': 0.05, 'top': 0.7}

        # Кнопки для выбора размера шрифта
        self.large_font = Button(text='Большой', size_hint=(1, None), height=50,
                                 background_normal=str(rec48_path),
                                 background_down=str(rec48_path))
        self.medium_font = Button(text='Средний', size_hint=(1, None), height=50,
                                  background_normal=str(rec48_path),
                                  background_down=str(rec48_path))
        self.small_font = Button(text='Маленький', size_hint=(1, None), height=50,
                                 background_normal=str(rec48_path),
                                 background_down=str(rec48_path))

        # Добавление кнопок выбора размера шрифта в дропдаун
        self.font_size_dropdown.add_widget(self.large_font)
        self.font_size_dropdown.add_widget(self.medium_font)
        self.font_size_dropdown.add_widget(self.small_font)
        layout.add_widget(self.font_size_dropdown)

        # Метка для уведомлений
        self.notifications_label = Label(text='Уведомления:', font_size=self.font_size,
                                         size_hint=(None, None), size=(200, 40))
        self.notifications_label.pos_hint = {'x': 0.05, 'top': 0.6}
        layout.add_widget(self.notifications_label)

        # Создание виджета для уведомлений
        self.create_notification_widget(layout, 'ВЫКЛЮЧИТЬ',
                                        str(rec48_path))

        # Кнопка для получения уведомлений по PUSH
        self.push_button = Button(text='ПУШ', size_hint=(None, None), size=(100, 50), opacity=0,
                                  background_normal=str(rec48_path),
                                  background_down=str(rec48_path),
                                  color=(0.71, 0.87, 0.19, 1)
                                  )
        self.push_button.pos_hint = {'x': 0.05, 'top': 0.45}
        layout.add_widget(self.push_button)

        # Кнопка для получения уведомлений на почту
        self.email_button = Button(text='НА ПОЧТУ', size_hint=(None, None), size=(100, 50), opacity=0,
                                   background_normal=str(rec48_path),
                                   background_down=str(rec48_path),
                                   color=(0.71, 0.87, 0.19, 1))
        self.email_button.pos_hint = {'right': 0.95, 'top': 0.45}
        layout.add_widget(self.email_button)

        self.add_widget(layout)  # Добавление макета на экран

        # Создание нижнего макета для кнопок навигации
        self.create_bottom_layout(layout)

        # Привязка методов к кнопкам
        self.light_theme.bind(on_press=self.set_light_theme)
        self.dark_theme.bind(on_press=self.set_dark_theme)
        self.system_theme.bind(on_press=self.set_system_theme)
        self.small_font.bind(on_press=self.set_small_font)
        self.medium_font.bind(on_press=self.set_medium_font)
        self.large_font.bind(on_press=self.set_large_font)

    def update_font_size(self, size):
        # Обновление размера шрифта для всех виджетов
        for widget in self.walk():
            if isinstance(widget, Label) or isinstance(widget, Button):
                widget.font_size = size

    def create_notification_widget(self, layout, label_text, background_image_path):
        # Создание виджета для уведомлений
        notification_layout = RelativeLayout(size_hint=(0.9, None), height=50)
        notification_layout.pos_hint = {'x': 0.05, 'top': 0.55}

        # Фоновое изображение для уведомления
        background = Image(source=background_image_path, allow_stretch=True, keep_ratio=False)
        notification_layout.add_widget(background)

        # Метка для текста уведомления
        self.label = Label(text=label_text, font_size='14sp', color=(0.6, 1, 0.2, 1),
                           size_hint=(None, None), size=(100, 30),
                           pos_hint={'x': 0.05, 'center_y': 0.5})
        notification_layout.add_widget(self.label)

        # Переключатель для включения и выключения уведомлений
        toggle_button = ToggleButton(size_hint=(None, None), size=(40, 30),
                                     pos_hint={'right': 0.95, 'center_y': 0.5},
                                     background_normal='', background_color=(1, 1, 0, 1))
        toggle_button.bind(on_press=self.toggle_label)  # Привязка к методу изменения состояния
        notification_layout.add_widget(toggle_button)

        layout.add_widget(notification_layout)  # Добавление виджета уведомлений на макет

    def toggle_label(self, instance):
        # Изменение текста уведомления на переключателе
        if instance.state == 'down':
            self.label.text = 'ВЫКЛЮЧИТЬ'
            self.push_button.opacity = 1  # Включение кнопки PUSH
            self.email_button.opacity = 1  # Включение кнопки для почты
        else:
            self.label.text = 'ВКЛЮЧИТЬ'
            self.push_button.opacity = 0  # Выключение кнопки PUSH
            self.email_button.opacity = 0  # Выключение кнопки для почты

    def create_bottom_layout(self, layout):
        # Создание нижнего макета для кнопок навигации
        bottom_layout = FloatLayout(size_hint=(1, None), height=dp(48))

        # Фоновое изображение для нижнего макета
        bottom_background = Image(
            source=str(rec48_path),
            size_hint=(1, 1),
            allow_stretch=True,
            keep_ratio=False,
            pos_hint={'center_x': 0.5, 'y': 0}
        )
        bottom_layout.add_widget(bottom_background)

        # Кнопка для перехода на экран каталога
        self.catalog_button = Button(
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            pos_hint={'right': 0.4, 'y': 0.05},
            background_normal='',
            background_down='',
            background_color=(1, 1, 1, 0),
            on_press=self.show_catalog  # Методу, вызываемому нажатии
        )

        # Кнопка для возврата на главный экран
        self.main_screen_button = Button(
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            pos_hint={'right': 0.75, 'y': 0.05},
            background_normal='',
            background_down='',
            background_color=(1, 1, 1, 0),
            on_press=self.go_back  # Переход на главный экран
        )

        # Изображение для экрана настроек
        self.settings_image = Image(
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            pos_hint={'right': 0.95, 'y': 0.05},
            source=str(settingsdark_path),
        )

        # Кнопка для просмотра профиля
        self.profile_button = Button(
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            pos_hint={'center_x': 0.2, 'y': 0.05},
            background_normal='',
            background_down='',
            background_color=(1, 1, 1, 0),
            on_press=self.show_profile  # Переход к экрану профиля
        )

        # Остальные изображения для навигации
        self.eclipse_image = Image(
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            pos_hint={'right': 0.95, 'y': 0.05},
            source=str(el1dark_path),
        )

        self.main_screen_image = Image(
            source=str(maindark_path),
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            pos_hint={'right': 0.75, 'y': 0.05}
        )

        self.personal_image = Image(
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            pos_hint={'right': 0.2, 'y': 0.05},
            source=str(userdark_path),
        )

        self.catalog_image = Image(
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            pos_hint={'right': 0.4, 'y': 0.05},
            source=str(catalogdark_path),
        )

        # Добавление всех кнопок и изображений в нижний макет
        bottom_layout.add_widget(self.profile_button)
        bottom_layout.add_widget(self.main_screen_button)
        bottom_layout.add_widget(self.eclipse_image)
        bottom_layout.add_widget(self.catalog_button)
        bottom_layout.add_widget(self.settings_image)
        bottom_layout.add_widget(self.main_screen_image)
        bottom_layout.add_widget(self.personal_image)
        bottom_layout.add_widget(self.catalog_image)

        layout.add_widget(bottom_layout)  # Добавление нижнего макета на основной

    def go_back(self, instance):
        # Возврат на предыдущий экран (главный)
        self.manager.current = 'main'

    def show_profile(self, instance):
        # Переход к экрану профиля
        self.manager.current = 'profile'

    def show_catalog(self, instance):
        # Переход на экран каталога
        self.manager.current = 'catalog'

    def set_screens(self, screens):
        # Установка экранов для менеджера экранов
        self._screens = screens

    def set_light_theme(self, instance):
        # Установка светлой темы
        Window.clearcolor = (1, 1, 1, 1)  # Цвет фона
        self.update_text_color((0.21, 0.37, 0.19, 1))  # Цвет текста для светлой темы
        self.update_images(light=True)

    def set_dark_theme(self, instance):
        # Установка темной темы
        Window.clearcolor = (0.121, 0.121, 0.121, 1)  # Цвет фона
        self.update_text_color((0.71, 0.87, 0.19, 1))  # Цвет текста для темной темы
        self.update_images(light=False)

    def set_system_theme(self, instance):
        # Метод для установки системной темы (пока не реализован)
        pass

    def set_small_font(self, instance):
        # Установка маленького размера шрифта
        self.update_font_size('14sp')

    def set_medium_font(self, instance):
        # Установка среднего размера шрифта
        self.update_font_size('18sp')

    def set_large_font(self, instance):
        # Установка большого размера шрифта
        self.update_font_size('24sp')

    def update_images(self, light):
        # Обновление изображений в зависимости от установленной темы
        if light:
            # Светлая тема
            self.settings_image.source = str(settingslight_path)
            self.main_screen_image.source = str(mainlight_path)
            self.personal_image.source = str(userlight_path)
            self.catalog_image.source = str(cataloglight_path)
            self.eclipse_image.source = str(el1light_path)
        else:
            # Темная тема
            self.settings_image.source = str(settingsdark_path)
            self.main_screen_image.source = str(maindark_path)
            self.personal_image.source = str(userdark_path)
            self.catalog_image.source = str(catalogdark_path)
            self.eclipse_image.source = str(el1dark_path)

        # Обновление изображений после изменения темы
        self.settings_image.reload()
        self.main_screen_image.reload()
        self.personal_image.reload()
        self.catalog_image.reload()
        self.eclipse_image.reload()

# Определение экрана карты
class MapScreen(Screen):
    def __init__(self, **kwargs):
        super(MapScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Создание карты с заданными координатами
        map_view = MapView(zoom=10, lat=40.7128, lon=-74.0060)  # Пример местоположения
        layout.add_widget(map_view)

        # Создание маркера на карте
        marker = MapMarker(lat=40.7128, lon=-74.0060)
        map_view.add_marker(marker)

        # Макет с информацией
        info_layout = BoxLayout(orientation='vertical', padding=10)
        # Метка с информацией о месте
        info_label = Label(text='Адрес: 1234 Example St\nТелефон: (123) 456-7890\nВремя работы: 9:00 - 18:00',
                           size_hint_y=None, height=100)  # Ограничение высоты метки
        info_button = Button(text='Построить маршрут от моего местоположения', size_hint_y=None, height=50)
        info_layout.add_widget(info_label)  # Добавление метки с информацией
        info_layout.add_widget(info_button)  # Кнопка для построения маршрута

        layout.add_widget(info_layout)  # Добавление информационного макета на основной макет

        # Кнопка для возврата на предыдущий экран
        back_button = Button(text='Назад', size_hint_y=None, height=50)
        back_button.bind(on_press=self.go_back)  # Привязка метода к кнопке
        layout.add_widget(back_button)  # Добавление кнопки на макет

        self.add_widget(layout)  # Добавление основного макета на экран

    def go_back(self, instance):
        # Метод для возврата на предыдущий экран (главный)
        self.manager.current = 'main'

    def on_enter(self, *args):
        # Метод, вызываемый при входе на экран
        settings_screen = self.manager.get_screen('settings')
        if hasattr(settings_screen, 'font_size'):
            font_size = settings_screen.font_size
            self.update_font_size(font_size)  # Обновление размера шрифта

    def update_font_size(self, size):
        # Обновление размера шрифта для всех виджетов на экране
        for widget in self.walk():
            if isinstance(widget, Label) or isinstance(widget, Button):
                widget.font_size = size

# Основной класс приложения
class MyApp(App):
    def build(self):
        sm = ScreenManager()  # Создание менеджера экранов
        # Добавление экранов в менеджер
        sm.add_widget(MainMenuScreen(name='main_menu'))
        sm.add_widget(RegisterFormScreen1(name='register_form'))
        sm.add_widget(LoginFormScreen(name='login_form'))
        sm.add_widget(ProfileScreen(name='profile'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(CatalogScreen(name='catalog'))
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(MapScreen(name='map'))
        return sm  # Возврат менеджера экранов

# Запуск приложения
if __name__ == '__main__':
    MyApp().run()