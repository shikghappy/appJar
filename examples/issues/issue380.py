import sys
sys.path.append("../../")

from appJar import gui

def press():
    pass

tabs = ['a', 'b', 'c', 'd', 'e', 'f']

with gui() as app:
    app.toolbar(['save', 'web'], press, findIcon=True)
    app.label('hello world')
    app.addIconButton('save', None, 'save')
    with app.tabbedFrame('tf'):
        for tab in tabs:
            with app.tab(tab):
                app.label(tab)
    app.setTabIcon('tf', 'a', 'open')
    app.setTabIcon('tf', 'b', 'save')
    app.setTabIcon('tf', 'c', 'web')