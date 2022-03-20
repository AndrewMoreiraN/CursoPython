import pywinauto

titulo_completo = 'The Seven Deadly Sins: Grand Cross'
titulo = 'Grand Cross'

window2 = pywinauto.findwindows.find_elements(class_name=None,
                                              class_name_re=None,
                                              parent=None,
                                              process=6360,
                                              title=None,
                                              title_re=titulo.casefold(),
                                              top_level_only=True,
                                              visible_only=True,
                                              enabled_only=False,
                                              best_match=None,
                                              handle=None,
                                              ctrl_index=None,
                                              found_index=None,
                                              predicate_func=None,
                                              active_only=False,
                                              control_id=None,
                                              control_type=None,
                                              auto_id=None,
                                              framework_id=None,
                                              backend='win32',
                                              depth=None)
print(type(window2))
print(window2)
"""
while (True):
    if input(': ') != '':
        break
    mouse.click(button='left', coords=(1670, 484))
    sleep(1)

    mouse.click(button='left', coords=(794, 845))

    sleep(0)
    mouse.click(button='left', coords=(1123, 677))

    sleep(0)
    mouse.click(button='left', coords=(921, 853))
    sleep(3)

    mouse.click(button='left', coords=(953, 880))
    sleep(1)

    mouse.click(button='left', coords=(1164, 180))
"""
