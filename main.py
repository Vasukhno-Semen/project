from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy_garden.mapview import MapView, MapMarker
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.core.window import Window
import sqlite3
from kivy.properties import NumericProperty



def create_database():
    connection = sqlite3.connect('registrations.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS registrations (
            id INTEGER,
            nickname TEXT UNIQUE,
            fullname TEXT NOT NULL,
            phone TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            institution TEXT,
            email TEXT UNIQUE,
            PRIMARY KEY(id)
        )
    ''')
    connection.commit()
    connection.close()

create_database()

class MainMenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MainMenuScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        register_button = Button(text='Регистрация', size_hint_y=None, height=50)
        register_button.bind(on_press=self.go_to_registration)
        layout.add_widget(register_button)

        login_button = Button(text='Вход', size_hint_y=None, height=50)
        login_button.bind(on_press=self.go_to_login)
        layout.add_widget(login_button)

        self.add_widget(layout)

    def go_to_registration(self, instance):
        self.manager.current = 'register_form'

    def go_to_login(self, instance):
        self.manager.current = 'login_form'

    def update_font_size(self, size):
        for widget in self.walk():
            if isinstance(widget, Label) or isinstance(widget, Button):
                widget.font_size = size


class RegisterFormScreen1(Screen):
    def __init__(self, **kwargs):
        super(RegisterFormScreen1, self).__init__(**kwargs)
        layout = GridLayout(cols=2, padding=10, spacing=10)

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

        submit_button = Button(text='Зарегистрироваться', size_hint_y=None, height=50)
        submit_button.bind(on_press=self.submit_registration)
        layout.add_widget(submit_button)

        back_button = Button(text='Назад', size_hint_y=None, height=50)
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def submit_registration(self, instance):
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
        self.manager.current = 'main_menu'

    def update_font_size(self, size):
        for widget in self.walk():
            if isinstance(widget, Label) or isinstance(widget, Button):
                widget.font_size = size

    def on_enter(self, *args):
        font_size = self.manager.get_screen('settings').font_size
        self.update_font_size(font_size)

class LoginFormScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginFormScreen, self).__init__(**kwargs)
        layout = GridLayout(cols=2, padding=10, spacing=10)

        layout.add_widget(Label(text='Телефон/Никнейм/Почта'))
        self.username_input = TextInput(multiline=False)
        layout.add_widget(self.username_input)

        layout.add_widget(Label(text='Пароль'))
        self.password_input = TextInput(multiline=False, password=True)
        layout.add_widget(self.password_input)

        login_button = Button(text='Войти', size_hint_y=None, height=50)
        login_button.bind(on_press=self.submit_login)
        layout.add_widget(login_button)

        back_button = Button(text='Назад', size_hint_y=None, height=50)
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def submit_login(self, instance):
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
            profile_screen.update_profile(user_id, nickname, fullname, phone, institution, email)

            self.manager.current = 'profile'
        else:
            print("Неверные учетные данные.")

    def check_credentials(self, username, password):
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
        self.manager.current = 'main_menu'


    def on_enter(self, *args):
        settings_screen = self.manager.get_screen('settings')
        if hasattr(settings_screen, 'font_size'):
            font_size = settings_screen.font_size
            self.update_font_size(font_size)

    def update_font_size(self, size):
        for widget in self.walk():
            if isinstance(widget, Label) or isinstance(widget, Button):
                widget.font_size = size


class MainScreen(Screen):
    menu_width = NumericProperty(200)

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        self.main_layout = FloatLayout()

        self.content_layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint=(1, 1))
        self.stage = 'stage1'
        self.stage_label = Label(text='Главный Экран', font_size='24sp')
        self.content_layout.add_widget(self.stage_label)

        self.paper_block = BoxLayout(orientation='horizontal', spacing=10)
        self.paper_status_label = Label(text='Вы сдали 0 кг из 3 кг', font_size='18sp')

        self.paper_button = Button(text='Сдать бумагу', on_press=self.submit_paper, size_hint=(None, None), size=(300, 150))
        self.paper_block.add_widget(self.paper_status_label)
        self.paper_block.add_widget(self.paper_button)
        self.content_layout.add_widget(self.paper_block)

        self.masterclass_block = BoxLayout(orientation='horizontal', spacing=10)
        self.masterclass_label = Label(text='Ближайшие мастер-классы', font_size='18sp')
        self.masterclass_button = Button(text='Пойти на мастер-класс', on_press=self.show_masterclasses, size_hint=(None, None), size=(300, 150))
        self.masterclass_block.add_widget(self.masterclass_label)
        self.masterclass_block.add_widget(self.masterclass_button)
        self.content_layout.add_widget(self.masterclass_block)

        self.main_layout.add_widget(self.content_layout)

        # Удаляем старое меню
        # self.menu_layout = BoxLayout(...)

        # Добавляем кнопки настроек и личного кабинета
        self.settings_button = Button(text='Н', size_hint=(None, None), size=(50, 50))
        self.settings_button.pos_hint = {'right': 1, 'bottom': 0}
        self.settings_button.bind(on_press=self.show_settings)

        self.profile_button = Button(text='ЛК', size_hint=(None, None), size=(50, 50))
        self.profile_button.pos_hint = {'left': 1, 'bottom': 0}
        self.profile_button.bind(on_press=self.show_profile)

        self.main_layout.add_widget(self.settings_button)
        self.main_layout.add_widget(self.profile_button)

        self.add_widget(self.main_layout)

    def update_paper_status(self):
        connection = sqlite3.connect('registrations.db')
        cursor = connection.cursor()
        profile_screen = self.manager.get_screen('profile')
        user_id_text = profile_screen.uid_label.text.split(': ')[1]  # Получаем ID пользователя
        print(f'User ID: {user_id_text}')  # Проверка ID пользователя
        cursor.execute('SELECT weight FROM registrations WHERE id = ?', (user_id_text,))
        result = cursor.fetchone()
        connection.close()

        if result and result[0] is not None and result[0] != "":
            weight = result[0]
            self.paper_status_label.text = f'Вы сдали {weight} кг из 3 кг'
        else:
            self.paper_status_label.text = 'Ошибка получения данных'

    def on_enter(self, *args):
        self.update_paper_status()
        settings_screen = self.manager.get_screen('settings')
        if hasattr(settings_screen, 'font_size'):
            font_size = settings_screen.font_size
            self.update_font_size(font_size)

    def update_font_size(self, size):
        for widget in self.walk():
            if isinstance(widget, Label) or isinstance(widget, Button):
                widget.font_size = size

    def _update_rectangle(self, instance, value):
        self.blur_rect.pos = instance.pos
        self.blur_rect.size = instance.size

    def show_profile(self, instance):
        self.manager.current = 'profile'

    def show_settings(self, instance):
        self.manager.current = 'settings'

    def submit_paper(self, instance):
        self.manager.current = 'map'

    def show_masterclasses(self, instance):
        self.manager.current = 'masterclasses'

    def update_stage(self, stage):
        self.stage = stage
        if stage == 'stage1':
            self.stage_label.text = 'Прогрев аудитории'
        elif stage == 'stage2':
            self.stage_label.text = 'Сбор макулатуры'
        elif stage == 'stage3':
            self.stage_label.text = 'Мастерклассы'


class ProfileScreen(Screen):
    def __init__(self, **kwargs):
        super(ProfileScreen, self).__init__(**kwargs)

        # Основной макет для профиля
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Элементы профиля
        self.image = Image(source='path/to/profile_picture.png', size_hint=(None, None), size=(100, 100))
        self.nickname_label = Label(text='Никнейм: ')
        self.uid_label = Label(text='UID: ')
        self.registration_date_label = Label(text='Дата регистрации: ')
        self.email_binding_label = Label(text='Привязка к почте: ')
        self.logout_button = Button(text='Выйти из аккаунта', size_hint_y=None, height=50)
        self.logout_button.bind(on_press=self.logout)

        # Основной макет для кнопок внизу
        bottom_layout = FloatLayout(size_hint=(1, None), height=50)

        # Кнопка "Главный Экран" в нижнем центре
        self.main_screen_button = Button(text='ГЭ', size_hint=(None, None), size=(50, 50),
                                         pos_hint={"center_x": 0.5, "bottom": 0})
        self.main_screen_button.bind(on_press=self.go_back)
        bottom_layout.add_widget(self.main_screen_button)

        # Кнопка настроек в нижнем правом углу
        self.settings_button = Button(text='Н', size_hint=(None, None), size=(50, 50),
                                      pos_hint={"right": 1, "bottom": 0})
        self.settings_button.bind(on_press=self.show_settings)
        bottom_layout.add_widget(self.settings_button)

        # Добавление виджетов в основной макет
        layout.add_widget(self.image)
        layout.add_widget(self.nickname_label)
        layout.add_widget(self.uid_label)
        layout.add_widget(self.registration_date_label)
        layout.add_widget(self.email_binding_label)
        layout.add_widget(self.logout_button)
        layout.add_widget(bottom_layout)

        self.add_widget(layout)

    def update_profile(self, user_id, nickname, fullname, phone, institution, email):
        self.uid_label.text = f'UID: {user_id}'
        self.nickname_label.text = f'Никнейм: {nickname}'
        self.registration_date_label.text = 'Дата регистрации: [Placeholder]'
        self.email_binding_label.text = f'Почта: {email}'

    def go_back(self, instance):
        self.manager.current = 'main'

    def show_settings(self, instance):
        self.manager.current = "settings"

    def logout(self, instance):
        self.manager.current = 'main_menu'

    def on_enter(self, *args):
        settings_screen = self.manager.get_screen('settings')
        if hasattr(settings_screen, 'font_size'):
            font_size = settings_screen.font_size
            self.update_font_size(font_size)

    def update_font_size(self, size):
        for widget in self.walk():
            if isinstance(widget, Label) or isinstance(widget, Button):
                widget.font_size = size



class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        layout = FloatLayout()  # Используем FloatLayout для точного позиционирования

        self.font_size = '18sp'
        button_size = (150, 50)  # Устанавливаем размер кнопок

        self.theme_label = Label(text='Тема:', font_size=self.font_size,
                                 size_hint=(None, None), size=(100, 40))
        self.theme_label.pos_hint = {'x': 0.05, 'top': 0.9}
        layout.add_widget(self.theme_label)

        self.theme_dropdown = BoxLayout(orientation='horizontal', spacing=10,
                                        size_hint=(None, None), size=(400, 50))
        self.theme_dropdown.pos_hint = {'x': 0.05, 'top': 0.85}
        self.light_theme = Button(text='Светлая', size_hint=(None, None), size=(250,50))
        self.dark_theme = Button(text='Темная', size_hint=(None, None), size=(250,50))
        self.system_theme = Button(text='Системная', size_hint=(None, None), size=(250,50))
        self.theme_dropdown.add_widget(self.light_theme)
        self.theme_dropdown.add_widget(self.dark_theme)
        self.theme_dropdown.add_widget(self.system_theme)
        layout.add_widget(self.theme_dropdown)

        self.font_size_label = Label(text='Размер шрифта:', font_size=self.font_size,
                                     size_hint=(None, None), size=(200, 40))
        self.font_size_label.pos_hint = {'x': 0.05, 'top': 0.75}
        layout.add_widget(self.font_size_label)

        self.font_size_dropdown = BoxLayout(orientation='horizontal', spacing=10,
                                            size_hint=(None, None), size=(400, 50))
        self.font_size_dropdown.pos_hint = {'x': 0.05, 'top': 0.7}
        self.large_font = Button(text='Большой', size_hint=(None, None), size=(250,50))
        self.medium_font = Button(text='Средний', size_hint=(None, None), size=(250,50))
        self.small_font = Button(text='Маленький', size_hint=(None, None), size=(250,50))
        self.font_size_dropdown.add_widget(self.large_font)
        self.font_size_dropdown.add_widget(self.medium_font)
        self.font_size_dropdown.add_widget(self.small_font)
        layout.add_widget(self.font_size_dropdown)

        self.notifications_label = Label(text='Уведомления:', font_size=self.font_size,
                                         size_hint=(None, None), size=(200, 40))
        self.notifications_label.pos_hint = {'x': 0.05, 'top': 0.6}
        layout.add_widget(self.notifications_label)

        self.notifications_dropdown = BoxLayout(orientation='horizontal', spacing=10,
                                                size_hint=(None, None), size=(400, 50))
        self.notifications_dropdown.pos_hint = {'x': 0.05, 'top': 0.55}
        self.notifications_off = Button(text='Отключить', size_hint=(None, None), size=(175,50))
        self.notifications_on = Button(text='Включить', size_hint=(None, None), size=(175,50))
        self.push_notifications = Button(text='Пуш', size_hint=(None, None), size=(175,50))
        self.email_notifications = Button(text='На почту', size_hint=(None, None), size=(175,50))
        self.notifications_dropdown.add_widget(self.notifications_off)
        self.notifications_dropdown.add_widget(self.notifications_on)
        self.notifications_dropdown.add_widget(self.push_notifications)
        self.notifications_dropdown.add_widget(self.email_notifications)
        layout.add_widget(self.notifications_dropdown)

        # Кнопка "Главный Экран" в нижнем левом углу
        self.main_screen_button = Button(text='ГЭ', size_hint=(None, None), size=(100, 50),
                                         pos_hint={"x": 0, "y": 0})
        self.main_screen_button.bind(on_press=self.go_back)
        layout.add_widget(self.main_screen_button)

        # Кнопка профиля в нижнем правом углу
        self.profile_button = Button(text='ЛК', size_hint=(None, None), size=(100, 50),
                                     pos_hint={"right": 1, "y": 0})
        self.profile_button.bind(on_press=self.show_profile)
        layout.add_widget(self.profile_button)

        self.light_theme.bind(on_press=self.set_light_theme)
        self.dark_theme.bind(on_press=self.set_dark_theme)
        self.system_theme.bind(on_press=self.set_system_theme)
        self.small_font.bind(on_press=self.set_small_font)
        self.medium_font.bind(on_press=self.set_medium_font)
        self.large_font.bind(on_press=self.set_large_font)

        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'main'

    def show_profile(self, instance):
        self.manager.current = 'profile'  # Переход на экран профиля, имя экрана может быть другим

    def set_light_theme(self, instance):
        Window.clearcolor = (1, 1, 1, 1)  # Изменение фона окна

    def set_dark_theme(self, instance):
        Window.clearcolor = (0, 0, 0, 1)  # Изменение фона окна

    def set_system_theme(self, instance):
        # Реализация системной темы, если это необходимо
        pass

    def set_small_font(self, instance):
        self.update_font_size('14sp')  # Установка маленького размера шрифта

    def set_medium_font(self, instance):
        self.update_font_size('18sp')  # Установка среднего размера шрифта

    def set_large_font(self, instance):
        self.update_font_size('24sp')  # Установка большого размера шрифта

    def update_font_size(self, size):
        self.font_size = size
        # Обновление размера шрифта для всех меток и кнопок в SettingsScreen
        for widget in self.walk():
            if isinstance(widget, Label) or isinstance(widget, Button):
                widget.font_size = size

class MapScreen(Screen):
    def __init__(self, **kwargs):
        super(MapScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')


        map_view = MapView(zoom=10, lat=40.7128, lon=-74.0060)  # Example location
        layout.add_widget(map_view)


        marker = MapMarker(lat=40.7128, lon=-74.0060)
        map_view.add_marker(marker)


        info_layout = BoxLayout(orientation='vertical', padding=10)
        info_label = Label(text='Адрес: 1234 Example St\nТелефон: (123) 456-7890\nВремя работы: 9:00 - 18:00',
                           size_hint_y=None, height=100)
        info_button = Button(text='Построить маршрут от моего местоположения', size_hint_y=None, height=50)
        info_layout.add_widget(info_label)
        info_layout.add_widget(info_button)

        layout.add_widget(info_layout)


        back_button = Button(text='Назад', size_hint_y=None, height=50)
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def go_back(self, instance):

        self.manager.current = 'main'

    def on_enter(self, *args):
        settings_screen = self.manager.get_screen('settings')
        if hasattr(settings_screen, 'font_size'):
            font_size = settings_screen.font_size
            self.update_font_size(font_size)

    def update_font_size(self, size):
        for widget in self.walk():
            if isinstance(widget, Label) or isinstance(widget, Button):
                widget.font_size = size


class MasterclassScreen(Screen):
    def __init__(self, **kwargs):
        super(MasterclassScreen, self).__init__(**kwargs)

        main_layout = FloatLayout()

        content_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.masterclasses = [
            {'name': 'Мастер-класс 1', 'time': '10:00', 'location': 'Место 1'},
            {'name': 'Мастер-класс 2', 'time': '14:00', 'location': 'Место 2'}
        ]

        # Проверка наличия записей в таблице
        if self.check_records_exist('masterclass'):
            self.add_masterclass_3_button(content_layout)

        for index, mc in enumerate(self.masterclasses):
            btn = Button(text=f"{mc['name']}\n{mc['time']} - {mc['location']}", size_hint_y=None, height=60)
            btn.bind(on_press=lambda instance, idx=index: self.show_masterclass_info(idx))
            content_layout.add_widget(btn)

        main_layout.add_widget(content_layout)

        back_button = Button(text='Назад', size_hint=(None, None), size=(100, 50), pos_hint={'right': 1, 'top': 1})
        back_button.bind(on_press=self.go_back)
        main_layout.add_widget(back_button)

        self.add_widget(main_layout)

    def check_records_exist(self, table_name):
        try:
            connection = sqlite3.connect('registrations.db')  # Укажите путь к вашей базе данных
            cursor = connection.cursor()
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            count = cursor.fetchone()[0]
            connection.close()
            return count > 0  # Вернет True, если записи существуют
        except Exception as e:
            print(f"Ошибка при проверке записей: {e}")
            return False

    def add_masterclass_3_button(self, layout):
        mc3_button = Button(text='Мастер-класс 3', size_hint_y=None, height=60)
        mc3_button.bind(on_press=lambda instance: self.show_masterclass_info(len(self.masterclasses)))  # Индекс для мастер-класса 3
        layout.add_widget(mc3_button)

    def show_masterclass_info(self, index):
        if index < len(self.masterclasses):
            selected_masterclass = self.masterclasses[index]
        else:
            selected_masterclass = {'name': 'Мастер-класс 3', 'time': '16:00', 'location': 'Место 3'}  # Информация для мастер-класса 3
        info_screen = self.manager.get_screen('masterclass_info')
        info_screen.set_masterclass_info(selected_masterclass)
        self.manager.current = 'masterclass_info'

    def go_back(self, instance):
        self.manager.current = 'main'

    def on_enter(self, *args):
        settings_screen = self.manager.get_screen('settings')
        if hasattr(settings_screen, 'font_size'):
            font_size = settings_screen.font_size
            self.update_font_size(font_size)

    def update_font_size(self, size):
        for widget in self.walk():
            if isinstance(widget, Label) or isinstance(widget, Button):
                widget.font_size = size

class MasterclassInfoScreen(Screen):
    def __init__(self, **kwargs):
        super(MasterclassInfoScreen, self).__init__(**kwargs)
        self.info_label = Label(font_size='18sp')
        self.map_view = MapView(zoom=10, lat=40.7128, lon=-74.0060)
        register_button = Button(text='Я приду', size_hint_y=None, height=50)
        register_button.bind(on_press=self.register_for_masterclass)

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.info_label)
        layout.add_widget(self.map_view)
        layout.add_widget(register_button)
        self.add_widget(layout)

    def set_masterclass_info(self, masterclass_info):
        info_text = f"Название: {masterclass_info['name']}\nВремя: {masterclass_info['time']}\nМесто: {masterclass_info['location']}"
        self.info_label.text = info_text
        self.map_view.lat = 40.7128
        self.map_view.lon = -74.0060

    def register_for_masterclass(self, instance):
        self.manager.current = 'register_form_of_masterclass'

    def on_enter(self, *args):
        settings_screen = self.manager.get_screen('settings')
        if hasattr(settings_screen, 'font_size'):
            font_size = settings_screen.font_size
            self.update_font_size(font_size)

    def update_font_size(self, size):
        for widget in self.walk():
            if isinstance(widget, Label) or isinstance(widget, Button):
                widget.font_size = size

class RegisterFormScreen(Screen):
    def __init__(self, **kwargs):
        super(RegisterFormScreen, self).__init__(**kwargs)
        layout = GridLayout(cols=2, padding=10, spacing=10)

        # Registration form fields
        layout.add_widget(Label(text='ФИО'))
        self.name_input = TextInput(multiline=False)
        layout.add_widget(self.name_input)

        layout.add_widget(Label(text='Номер телефона'))
        self.phone_input = TextInput(multiline=False)
        layout.add_widget(self.phone_input)

        submit_button = Button(text='Записаться', size_hint_y=None, height=50)
        submit_button.bind(on_press=self.submit_registration)
        layout.add_widget(submit_button)

        # Back button
        back_button = Button(text='Назад', size_hint_y=None, height=50)
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def submit_registration(self, instance):
        name = self.name_input.text
        phone = self.phone_input.text

        if not name or not phone:
            print("ФИО и номер телефона обязательны для заполнения.")
            return

        self.save_to_database(name, phone)
        print(f"Registered {name} with phone {phone}")
        # Switch to masterclass screen
        self.manager.current = 'masterclasses'

    def save_to_database(self, name, phone):
        connection = sqlite3.connect('registrations.db')
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO registrations1 (name, phone)
            VALUES (?, ?)
        ''', (name, phone))
        connection.commit()
        connection.close()

    def go_back(self, instance):
        self.manager.current = 'masterclasses'

    def on_enter(self, *args):
        settings_screen = self.manager.get_screen('settings')
        if hasattr(settings_screen, 'font_size'):
            font_size = settings_screen.font_size
            self.update_font_size(font_size)

    def update_font_size(self, size):
        for widget in self.walk():
            if isinstance(widget, Label) or isinstance(widget, Button):
                widget.font_size = size

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenuScreen(name='main_menu'))
        sm.add_widget(RegisterFormScreen1(name='register_form'))
        sm.add_widget(RegisterFormScreen(name='register_form_of_masterclass'))
        sm.add_widget(LoginFormScreen(name='login_form'))
        sm.add_widget(ProfileScreen(name='profile'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(MapScreen(name='map'))
        sm.add_widget(MasterclassScreen(name='masterclasses'))
        sm.add_widget(MasterclassInfoScreen(name='masterclass_info'))
        return sm

if __name__ == '__main__':
    MyApp().run()
