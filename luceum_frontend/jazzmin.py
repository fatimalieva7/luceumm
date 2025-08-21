# settings.py

JAZZMIN_SETTINGS = {
    "site_title": "Админпанель Лицея",
    "site_header": "Лицей – управление сайтом",
    "site_brand": "Админка Лицея",

    # Логотип (положи картинку в static/logo/)
    "site_logo": "logo/lyceum_logo.png",
    "login_logo": "logo/lyceum_logo.png",
    "site_icon": "logo/lyceum_logo.png",

    "site_logo_classes": "img-circle",
    "welcome_sign": "Добро пожаловать в админку Лицея",
    "copyright": "Лицей © 2025",

    # Поиск
    "search_model": ["users.Student", "users.Teacher"],

    # Главное меню сверху
    "topmenu_links": [
        {"name": "Главная", "url": "admin:index", "icon": "fas fa-home"},
        {"name": "Сайт Лицея", "url": "https://lyceum-site.kg", "icon": "fas fa-globe"},
    ],

    # Меню пользователя справа
    "usermenu_links": [
        {"name": "Помощь", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],

    # Боковое меню
    "show_sidebar": True,
    "navigation_expanded": True,

    # Иконки приложений и моделей
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.group": "fas fa-users",

        "users.Student": "fas fa-user-graduate",
        "users.Teacher": "fas fa-chalkboard-teacher",
        "education.Class": "fas fa-school",
        "education.Subject": "fas fa-book",
        "education.Schedule": "fas fa-calendar-alt",
        "news.News": "fas fa-newspaper",
    },

    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    # Формат отображения форм
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs"
    }
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": True,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": True,

    # Цвета лицея
    "brand_colour": "navbar-primary",
    "accent": "accent-info",
    "navbar": "navbar-white navbar-light",
    "sidebar": "sidebar-dark-primary",

    "navbar_fixed": True,
    "sidebar_fixed": True,
    "layout_boxed": False,

    "sidebar_nav_small_text": True,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_flat_style": True,

    "theme": "lux",   # Можешь попробовать "cyborg" или "darkly" для тёмной темы
    "dark_mode_theme": "cyborg",

    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    }
}
