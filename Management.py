import sys
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def createDB():
   db = QSqlDatabase.addDatabase('QSQLITE')
   db.setDatabaseName('class.db')

   if not db.open():
      msg = QMessageBox()
      msg.setIcon(QMessageBox.Critical)
      msg.setText("Error in Database Creation")
      retval = msg.exec_()
      return False
query = QSqlQuery()


query.exec_("""
CREATE TABLE IF NOT EXSIST teacher(
            id INTEGER PRYMARY KEY,
            Name TEXT NOT NULL,
            Number_class INTEGER,
            Time_class INTEGER
)
""")