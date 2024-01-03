import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QTableWidget, QTableWidgetItem, QInputDialog
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Database GUI Example")
        self.setGeometry(100, 100, 600, 400)

        self.init_ui()
        self.show_data()

    def init_ui(self):
        self.createDB()
        self.teache_label = QLabel("Teache Data:")
        self.teache_table = QTableWidget(self)
        self.init_table(self.teache_table, ["ID", "Name", "Number of Classes", "Time of Classes"])
        self.teache_search_edit = QLineEdit()
        self.teache_search_button = QPushButton("Search")
        self.teache_search_button.clicked.connect(lambda: self.show_table_data("teache", self.teache_table, self.teache_search_edit.text()))
        self.teache_edit_button = QPushButton("Edit")
        self.teache_edit_button.clicked.connect(self.edit_teache)
        self.teache_delete_button = QPushButton("Delete")
        self.teache_delete_button.clicked.connect(self.delete_teache)

        layout = QVBoxLayout()
        teache_layout = QVBoxLayout()
        teache_layout.addWidget(self.teache_label)
        teache_layout.addWidget(self.teache_search_edit)
        teache_layout.addWidget(self.teache_search_button)
        teache_layout.addWidget(self.teache_table)
        teache_layout.addWidget(self.teache_edit_button)
        teache_layout.addWidget(self.teache_delete_button)
        layout.addLayout(teache_layout)

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
            CREATE TABLE IF NOT EXISTS teache (
                id INTEGER PRIMARY KEY,
                Name TEXT NOT NULL,
                Number_class INTEGER,
                Time_class INTEGER
            )
        """)

    def insert_data(self, table_name, data):
        placeholders = ', '.join(['?'] * len(data))
        query = QSqlQuery()
        query.prepare(f"INSERT INTO {table_name} VALUES ({placeholders})")
        for i, value in enumerate(data, 1):
            query.bindValue(i, value)

        if query.exec_():
            print("Data inserted successfully.")
            self.show_data()
        else:
            print("Error inserting data.")

    def show_data(self):
        self.show_table_data("teache", self.teache_table)

    def show_table_data(self, table_name, table_widget, filter_text=""):
        query = QSqlQuery(f"SELECT * FROM {table_name} WHERE Name LIKE :filter_text")
        query.bindValue(":filter_text", f"%{filter_text}%")
        table_widget.setRowCount(0)

        row_position = 0
        while query.next():
            table_widget.insertRow(row_position)
            for column in range(query.record().count()):
                item = QTableWidgetItem(str(query.value(column)))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                table_widget.setItem(row_position, column, item)
            row_position += 1

    def init_table(self, table_widget, headers):
        table_widget.setColumnCount(len(headers))
        table_widget.setHorizontalHeaderLabels(headers)

    def edit_teache(self):
     selected_row = self.teache_table.currentRow()
     if selected_row >= 0:
        name = self.teache_table.item(selected_row, 1).text()
        number_class = self.teache_table.item(selected_row, 2).text()
        time_class = self.teache_table.item(selected_row, 3).text()
        new_name, ok_name = self.get_user_input("Edit Name", "Enter new name:", name)
        new_number_class, ok_number_class = self.get_user_input("Edit Number of Classes", "Enter new number of classes:", number_class)
        new_time_class, ok_time_class = self.get_user_input("Edit Time of Classes", "Enter new time of classes:", time_class)

        if ok_name and ok_number_class and ok_time_class:
            query = QSqlQuery()
            query.prepare("UPDATE teache SET Name = ?, Number_class = ?, Time_class = ? WHERE id = ?")
            query.addBindValue(new_name)
            query.addBindValue(new_number_class)
            query.addBindValue(new_time_class)
            query.addBindValue(self.teache_table.item(selected_row, 0).text())
            if query.exec_():
                print("Data updated successfully.")
                self.show_data()
            else:
                print("Error updating data.")

def delete_teache(self):
        selected_row = self.teache_table.currentRow()
        if selected_row >= 0:
            id_to_delete = self.teache_table.item(selected_row, 0).text()
            query = QSqlQuery()
            query.prepare("DELETE FROM teache WHERE id = ?")
            query.addBindValue(id_to_delete)

            if query.exec_():
                print("Data deleted successfully.")
                self.show_data()
            else:
                print("Error deleting data.")

def get_user_input(self, title, prompt, default_text=""):
        text, ok = QInputDialog.getText(self, title, prompt, QLineEdit.Normal, default_text)
        return text, ok

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())