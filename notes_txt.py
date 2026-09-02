#для начала скопируй сюда интерфейс "Умных заметок" и проверь его работу

#затем запрограммируй демо-версию функционала
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QTextEdit, QLineEdit, QInputDialog

notes = []

app = QApplication([])
main = QWidget()
main.resize(900, 600)
main.setWindowTitle('Умные заметки')

textedit = QTextEdit()
listNotes = QListWidget()
listTags = QListWidget()
lineTag = QLineEdit()
NotesLabel = QLabel('Список заметок')
TagsLabel = QLabel('Список тегов')
lineTag.setPlaceholderText('Введите тег ...')
createNotes = QPushButton('Создать заметку')
deleteNotes = QPushButton('Удалить заметку')
saveNotes = QPushButton('Сохранить заметку')
addNotes = QPushButton('Добавить к заметке')
clearNotes = QPushButton('Открепить от заметки')
searchNotes = QPushButton('Искать заметки по тегу')

h_line = QHBoxLayout()
v1_line = QVBoxLayout()
v1_line.addWidget(textedit)
v2_line = QVBoxLayout()
v2_line.addWidget(NotesLabel)
v2_line.addWidget(listNotes)
h1_line = QHBoxLayout()
h1_line.addWidget(createNotes)
h1_line.addWidget(deleteNotes)
v2_line.addLayout(h1_line)
v2_line.addWidget(saveNotes)
v2_line.addWidget(TagsLabel)
v2_line.addWidget(listTags)
v2_line.addWidget(lineTag)
h2_line = QHBoxLayout()
h2_line.addWidget(addNotes)
h2_line.addWidget(clearNotes)
v2_line.addLayout(h2_line)
v2_line.addWidget(searchNotes)
h_line.addLayout(v1_line)
h_line.addLayout(v2_line)

main.setLayout(h_line)

def add_note():
    k, note_name = QInputDialog.getText(main, 'Добавить заметку', 'Название заметки')
    if k and note_name != '':
        note = list()
        note = [note_name, '', []]
        notes.append(note)
        listNotes.addItem(note[0])
        listTags.addItems(note[2])
        print(notes)
        with open(str(len(notes)-1) + '.txt', 'w') as file:
            file.write(note[0] + '\n')

def save_notes():
    if listNotes.selectedItems():
        k = listNotes.selectedItems()[0].text()
        i = 0
        for note in notes:
            if note[0] == k:
                note[1] = textedit.toPlainText()
                filename = str(i) + '.txt'
                with open (filename, 'w') as file:
                    file.write(note[0] + '\n')
                    file.write(note[1] + '\n')
                    for tag in note[2]:
                        file.write(tag + '')
                    file.write('\n')
            i += 1

def show_note():
    k = listNotes.selectedItems()[0].text()
    for note in notes:
        if note[0] == k:
            textedit.setText(note[1])
            listTags.clear()
            listTags.addItems(note[2])

note = list()
name = 0
while True:
    filename = str(name) + '.txt'
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.replace('\n', '')
                line.append(note)
        tags = note[2].split(' ')
        note[2] = tags
        notes.append(note)
        note = []
        name += 1
    except IOError:
        break
print(notes)
for note in notes:
    listNotes.addItem(note[0])

createNotes.clicked.connect(add_note)
saveNotes.clicked.connect(save_notes)

main.show()
app.exec_()