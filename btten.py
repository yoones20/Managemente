import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QTableView, QSizePolicy
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery

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

        self.table_view = QTableView()
        self.table_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.load_data()

        self.btn_teacher = QPushButton("Show Teacher Table")
        self.btn_teacher.clicked.connect(self.show_teacher_table)
        self.btn_honar_amoz = QPushButton("Show Honar Amoz Table")
        self.btn_honar_amoz.clicked.connect(self.show_honar_amoz_table)
        self.btn_class = QPushButton("Show Class Table")
        self.btn_class.clicked.connect(self.show_class_table)
        self.update_button = QPushButton("Update")
        self.update_button.clicked.connect(self.update_data)
        self.edit_button = QPushButton("Edit")
        self.edit_button.clicked.connect(self.edit_data)
        self.delete_button = QPushButton("Delete")
        self.delete_button.clicked.connect(self.delete_data)

        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_edit)
        layout.addWidget(self.number_class_label)
        layout.addWidget(self.number_class_edit)
        layout.addWidget(self.time_class_label)
        layout.addWidget(self.time_class_edit)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.table_view)
        layout.addWidget(self.btn_teacher)
        layout.addWidget(self.btn_honar_amoz)
        layout.addWidget(self.btn_class)
        layout.addWidget(self.update_button)
        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)

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
            print("Data inserted successfully")
            self.load_data()
        else:
            print("Error inserting data")

    def load_data(self):
        model = QSqlQueryModel()
        model.setQuery("SELECT * FROM teacher")
        self.table_view.setModel(model)

    def show_teacher_table(self):
        model = QSqlQueryModel()
        model.setQuery("SELECT * FROM teacher")
        self.table_view.setModel(model)

    def show_honar_amoz_table(self):
        model = QSqlQueryModel()
        model.setQuery("SELECT * FROM honar_amoz")
        self.table_view.setModel(model)

    def show_class_table(self):
        model = QSqlQueryModel()
        model.setQuery("SELECT * FROM class")
        self.table_view.setModel(model)

    def update_data(self):
     selected_row = self.table_view.selectionModel().currentIndex().row()
     if selected_row >= 0:
        name = self.name_edit.text()
        number_class = int(self.number_class_edit.text())
        time_class = int(self.time_class_edit.text())

        query = QSqlQuery()
        query.prepare("UPDATE teacher SET Name=?, Number_class=?, Time_class=? WHERE id=?")
        query.addBindValue(name)
        query.addBindValue(number_class)
        query.addBindValue(time_class)
        query.addBindValue(selected_row + 1) 

        if query.exec_():
            print("Data updated successfully")
            self.load_data()
        else:
            print("Error updating data")
    def edit_data(self):
        selected_row = self.table_view.selectionModel().currentIndex().row()
        if selected_row >= 0:
            model = self.table_view.model()
            index_name = model.index(selected_row, 1)
            index_number_class = model.index(selected_row, 2) 
            index_time_class = model.index(selected_row, 3)

            name = model.data(index_name)
            number_class = model.data(index_number_class)
            time_class = model.data(index_time_class)
            self.name_edit.setText(str(name))
            self.number_class_edit.setText(str(number_class))
            self.time_class_edit.setText(str(time_class))

    def delete_data(self):
     selected_row = self.table_view.selectionModel().currentIndex().row()
     if selected_row >= 0:
        query = QSqlQuery()
        query.prepare("DELETE FROM teacher WHERE id=?")
        query.addBindValue(selected_row + 1)  

        if query.exec_():
            print("Data deleted successfully")
            self.load_data()
        else:
            print("Error deleting data")
    def apply_changes(self):
     selected_row = self.table_view.selectionModel().currentIndex().row()
     if selected_row >= 0:
        name = self.name_edit.text()
        number_class = int(self.number_class_edit.text())
        time_class = int(self.time_class_edit.text())

        query = QSqlQuery()
        query.prepare("UPDATE teacher SET Name=?, Number_class=?, Time_class=? WHERE id=?")
        query.addBindValue(name)
        query.addBindValue(number_class)
        query.addBindValue(time_class)
        query.addBindValue(selected_row + 1) 

        if query.exec_():
            print("Changes applied successfully")
            self.load_data()
        else:
            print("Error applying changes")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())