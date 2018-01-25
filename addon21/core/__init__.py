try:
    # import the main window object (mw) from aqt
    from aqt import mw
    # import the "show info" tool from utils.py
    from aqt.utils import showInfo
    # import all of the Qt GUI library
    from aqt.qt import *
except ImportError:
    print('Failed to import Anki modules')

from .gui import *

user_files = os.path.join(os.path.dirname(__file__), '..', 'user_files')

if mw:
    my_menu = None
    my_menu_name = 'My menu'
    my_action_name = 'Example addon'
    
    for action in mw.form.menuTools.actions():
        menu = action.menu()
        if menu is not None and action.text() == my_menu_name:
            my = menu
    if my_menu is None:
        my_menu = QMenu(my_menu_name)
        mw.form.menuTools.addSeparator()
        mw.form.menuTools.addMenu(my_menu)

    action = QAction(my_action_name, mw)
    action.triggered.connect(MainMenu)
    my.addAction(action)
