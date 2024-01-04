import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Database GUI Example")
        self.setGeometry(500, 500, 500, 500)

        self.init_ui()

    def init_ui(self):
        
        self.createDB()
        self.name_label = QLabel("Name:")
        self.name_edit = QLineEdit()
        self.number_class_label = QLabel("Number of Classes:")
        self.number_class_edit = QLineEdit()
        self.time_class_label = QLabel("Time of Classes:")
        self.time_class_edit = QLineEdit()
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.insert_data)

        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_edit)
        layout.addWidget(self.number_class_label)
        layout.addWidget(self.number_class_edit)
        layout.addWidget(self.time_class_label)
        layout.addWidget(self.time_class_edit)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def createDB(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('mojtama.db')

        if not db.open():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error in Database Creation")
            retval = msg.exec_()
            return False

        query = QSqlQuery()
        query.exec_("""
            CREATE TABLE IF NOT EXISTS teacher (
                id INTEGER PRIMARY KEY,
                Name TEXT NOT NULL,
                Number_class INTEGER,
                Time_class INTEGER
            )
        """)

        query.exec_("""
            CREATE TABLE IF NOT EXISTS honar_amoz (
                id INTEGER PRIMARY KEY,
                Title TEXT NOT NULL,
                Description TEXT
            )
        """)

        query.exec_("""
            CREATE TABLE IF NOT EXISTS class (
                id INTEGER PRIMARY KEY,
                ClassName TEXT NOT NULL,
                ClassDescription TEXT
            )
        """)

        query.exec_("""
            CREATE TABLE IF NOT EXISTS time_class (
                id INTEGER PRIMARY KEY,
                ClassTime TEXT NOT NULL,
                Day TEXT NOT NULL
            )
        """)
    def insert_data(self):
        name = self.name_edit.text()
        number_class = int(self.number_class_edit.text())
        time_class = int(self.time_class_edit.text())
        query = QSqlQuery()
        query.prepare("INSERT INTO teacher (Name, Number_class, Time_class) VALUES (?, ?, ?)")
        query.addBindValue(name)
        query.addBindValue(number_class)
        query.addBindValue(time_class)

        if query.exec_():
            print("اطلاعات با موفقیت اعمال شدند")
        else:
            print("خطا در وارد کردن اطلاعات")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())