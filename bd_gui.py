import sys
import sqlite3
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QTabWidget, QAbstractScrollArea,
                             QVBoxLayout, QHBoxLayout,
                             QTableWidget, QGroupBox,
                             QTableWidgetItem, QPushButton, QMessageBox)


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('Schedule')

        self._connect_to_db()

        self.vbox = QVBoxLayout(self)
        self.tabs = QTabWidget(self)

        self.vbox.addWidget(self.tabs)

        self._create_schedule_tab()
        self._create_subject_tab()
        self._create_teacher_tab()


    def _connect_to_db(self):
        self.conn = sqlite3.connect('base.db')
        self.cursor = self.conn.cursor()


    def _create_schedule_tab(self):
        self.schedule_tab = QWidget()
        self.tabs.addTab(self.schedule_tab, "Schedule")

        self.monday_gbox = QGroupBox("Monday")

        self.svbox = QVBoxLayout()
        self.shboxSchedule = QHBoxLayout()
        self.sh2boxSchedule = QHBoxLayout()
        self.shboxButton = QHBoxLayout()

        self.svbox.addLayout(self.shboxSchedule)  # only one added
        self.svbox.addLayout(self.sh2boxSchedule)
        self.svbox.addLayout(self.shboxButton)

        self.shboxSchedule.addWidget(self.monday_gbox)
        self._create_monday_table()

        self.update_schedule_button = QPushButton("Update")
        self.shboxButton.addWidget(self.update_schedule_button)

        self.update_schedule_button.clicked.connect(self._update_schedule)

        self.tuesday_gbox = QGroupBox("Tuesday")

        self.shboxSchedule.addWidget(self.tuesday_gbox)
        self._create_tuesday_table()

        self.wednesday_gbox = QGroupBox("Wednesday")

        self.shboxSchedule.addWidget(self.wednesday_gbox)
        self._create_wednesday_table()

        self.thursday_gbox = QGroupBox("Thursday")

        self.sh2boxSchedule.addWidget(self.thursday_gbox)
        self._create_thursday_table()

        self.friday_gbox = QGroupBox("Friday")

        self.sh2boxSchedule.addWidget(self.friday_gbox)
        self._create_friday_table()

        self.saturday_gbox = QGroupBox("Saturday")

        self.sh2boxSchedule.addWidget(self.saturday_gbox)
        self._create_saturday_table()

        self.schedule_tab.setLayout(self.svbox)


    def _create_subject_tab(self):
        self.subject_tab = QWidget()
        self.tabs.addTab(self.subject_tab, "Subject")

        self.subject_gbox = QGroupBox("Subject")

        self.svboxSubject = QVBoxLayout()
        self.shboxList = QHBoxLayout()
        self.shboxButton = QHBoxLayout()

        self.svboxSubject.addLayout(self.shboxList)
        self.svboxSubject.addLayout(self.shboxButton)

        self.shboxList.addWidget(self.subject_gbox)
        self._create_subject_table()

        self.update_subject_button = QPushButton("Update")
        self.shboxButton.addWidget(self.update_subject_button)

        self.update_subject_button.clicked.connect(self._update_subject_table)

        self.subject_tab.setLayout(self.svboxSubject)


    def _create_teacher_tab(self):
        self.teacher_tab = QWidget()
        self.tabs.addTab(self.teacher_tab, "Teacher")

        self.teacher_gbox = QGroupBox("Teacher")

        self.svboxTeacher = QVBoxLayout()
        self.shboxList = QHBoxLayout()
        self.shboxButton = QHBoxLayout()

        self.svboxTeacher.addLayout(self.shboxList)
        self.svboxTeacher.addLayout(self.shboxButton)

        self.shboxList.addWidget(self.teacher_gbox)
        self._create_teacher_table()

        self.update_teacher_button = QPushButton("Update")
        self.shboxButton.addWidget(self.update_teacher_button)

        self.update_teacher_button.clicked.connect(self._update_teacher_table)

        self.teacher_tab.setLayout(self.svboxTeacher)


    def _create_monday_table(self):
        self.monday_table = QTableWidget()
        self.monday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.monday_table.setColumnCount(5)
        #self.monday_table.setHorizontalHeaderLabels(['Subject', 'Room number', 'Time', 'Teacher'])
        self.monday_table.setHorizontalHeaderLabels(['Subject', 'Room number', 'Time'])

        self._update_monday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.monday_table)
        self.monday_gbox.setLayout(self.mvbox)


    def _create_tuesday_table(self):
        self.tuesday_table = QTableWidget()
        self.tuesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.tuesday_table.setColumnCount(5)
        self.tuesday_table.setHorizontalHeaderLabels(['Subject', 'Room number', 'Time'])

        self._update_tuesday_table()

        self.tvbox = QVBoxLayout()
        self.tvbox.addWidget(self.tuesday_table)
        self.tuesday_gbox.setLayout(self.tvbox)


    def _create_wednesday_table(self):
        self.wednesday_table = QTableWidget()
        self.wednesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.wednesday_table.setColumnCount(5)
        self.wednesday_table.setHorizontalHeaderLabels(['Subject', 'Room number', 'Time'])

        self._update_wednesday_table()

        self.tvbox = QVBoxLayout()
        self.tvbox.addWidget(self.wednesday_table)
        self.wednesday_gbox.setLayout(self.tvbox)


    def _create_thursday_table(self):
        self.thursday_table = QTableWidget()
        self.thursday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.thursday_table.setColumnCount(5)
        self.thursday_table.setHorizontalHeaderLabels(['Subject', 'Room number', 'Time'])

        self._update_thursday_table()

        self.tvbox = QVBoxLayout()
        self.tvbox.addWidget(self.thursday_table)
        self.thursday_gbox.setLayout(self.tvbox)


    def _create_friday_table(self):
        self.friday_table = QTableWidget()
        self.friday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.friday_table.setColumnCount(5)
        self.friday_table.setHorizontalHeaderLabels(['Subject', 'Room number', 'Time'])

        self._update_friday_table()

        self.tvbox = QVBoxLayout()
        self.tvbox.addWidget(self.friday_table)
        self.friday_gbox.setLayout(self.tvbox)


    def _create_saturday_table(self):
        self.saturday_table = QTableWidget()
        self.saturday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.saturday_table.setColumnCount(5)
        self.saturday_table.setHorizontalHeaderLabels(['Subject', 'Room number', 'Time'])

        self._update_saturday_table()

        self.tvbox = QVBoxLayout()
        self.tvbox.addWidget(self.saturday_table)
        self.saturday_gbox.setLayout(self.tvbox)


    def _create_subject_table(self):
        self.subject_table = QTableWidget()
        self.subject_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.subject_table.setColumnCount(3)
        self.subject_table.setHorizontalHeaderLabels(['Subject'])

        self._update_subject_table()

        self.tvbox = QVBoxLayout()
        self.tvbox.addWidget(self.subject_table)
        self.subject_gbox.setLayout(self.tvbox)


    def _create_teacher_table(self):
        self.teacher_table = QTableWidget()
        self.teacher_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.teacher_table.setColumnCount(4)
        self.teacher_table.setHorizontalHeaderLabels(['Full name', 'Subject'])

        self._update_teacher_table()

        self.tvbox = QVBoxLayout()
        self.tvbox.addWidget(self.teacher_table)
        self.teacher_gbox.setLayout(self.tvbox)


    def _update_monday_table(self):
        self.cursor.execute("select * from timetable where day='monday'")
        records = self.cursor.fetchall()

        self.monday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):

            self.monday_table.setItem(i, 0, QTableWidgetItem(str(r[2])))
            self.monday_table.setItem(i, 1, QTableWidgetItem(str(r[3])))
            self.monday_table.setItem(i, 2, QTableWidgetItem(str(r[4])))

            joinButton = QPushButton("Change")
            self.monday_table.setCellWidget(i, 3, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num, 'monday'))

            removeButton = QPushButton("Remove")
            self.monday_table.setCellWidget(i, 4, removeButton)

            removeButton.clicked.connect(lambda ch, num=i: self._remove_from_table(num, 'monday'))
        joinButton = QPushButton("Create")
        self.monday_table.setCellWidget(len(records), 4, joinButton)

        joinButton.clicked.connect(lambda ch, num=len(records): self._change_day_from_table(num, 'monday', True))

        self.monday_table.resizeRowsToContents()


    def _update_tuesday_table(self):
        self.cursor.execute("select * from timetable where day='tuesday'")
        records = self.cursor.fetchall()

        self.tuesday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):

            self.tuesday_table.setItem(i, 0, QTableWidgetItem(str(r[2])))
            self.tuesday_table.setItem(i, 1, QTableWidgetItem(str(r[3])))
            self.tuesday_table.setItem(i, 2, QTableWidgetItem(str(r[4])))

            joinButton = QPushButton("Change")
            self.tuesday_table.setCellWidget(i, 3, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num, 'tuesday'))

            removeButton = QPushButton("Remove")
            self.tuesday_table.setCellWidget(i, 4, removeButton)

            removeButton.clicked.connect(lambda ch, num=i: self._remove_from_table(num, 'tuesday'))
        joinButton = QPushButton("Create")
        self.tuesday_table.setCellWidget(len(records), 4, joinButton)

        joinButton.clicked.connect(lambda ch, num=len(records): self._change_day_from_table(num, 'tuesday', True))

        self.tuesday_table.resizeRowsToContents()


    def _update_wednesday_table(self):
        self.cursor.execute("select * from timetable where day='wednesday'")
        records = self.cursor.fetchall()

        self.wednesday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):

            self.wednesday_table.setItem(i, 0, QTableWidgetItem(str(r[2])))
            self.wednesday_table.setItem(i, 1, QTableWidgetItem(str(r[3])))
            self.wednesday_table.setItem(i, 2, QTableWidgetItem(str(r[4])))

            joinButton = QPushButton("Change")
            self.wednesday_table.setCellWidget(i, 3, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num, 'wednesday'))

            removeButton = QPushButton("Remove")
            self.wednesday_table.setCellWidget(i, 4, removeButton)

            removeButton.clicked.connect(lambda ch, num=i: self._remove_from_table(num, 'wednesday'))
        joinButton = QPushButton("Create")
        self.wednesday_table.setCellWidget(len(records), 4, joinButton)

        joinButton.clicked.connect(lambda ch, num=len(records): self._change_day_from_table(num, 'wednesday', True))

        self.wednesday_table.resizeRowsToContents()


    def _update_thursday_table(self):
        self.cursor.execute("select * from timetable where day='thursday'")
        records = self.cursor.fetchall()

        self.thursday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):

            self.thursday_table.setItem(i, 0, QTableWidgetItem(str(r[2])))
            self.thursday_table.setItem(i, 1, QTableWidgetItem(str(r[3])))
            self.thursday_table.setItem(i, 2, QTableWidgetItem(str(r[4])))

            joinButton = QPushButton("Change")
            self.thursday_table.setCellWidget(i, 3, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num, 'thursday'))

            removeButton = QPushButton("Remove")
            self.thursday_table.setCellWidget(i, 4, removeButton)

            removeButton.clicked.connect(lambda ch, num=i: self._remove_from_table(num, 'thursday'))
        joinButton = QPushButton("Create")
        self.thursday_table.setCellWidget(len(records), 4, joinButton)

        joinButton.clicked.connect(lambda ch, num=len(records): self._change_day_from_table(num, 'thursday', True))

        self.thursday_table.resizeRowsToContents()


    def _update_friday_table(self):
        self.cursor.execute("select * from timetable where day='friday'")
        records = self.cursor.fetchall()

        self.friday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):

            self.friday_table.setItem(i, 0, QTableWidgetItem(str(r[2])))
            self.friday_table.setItem(i, 1, QTableWidgetItem(str(r[3])))
            self.friday_table.setItem(i, 2, QTableWidgetItem(str(r[4])))

            joinButton = QPushButton("Change")
            self.friday_table.setCellWidget(i, 3, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num, 'friday'))

            removeButton = QPushButton("Remove")
            self.friday_table.setCellWidget(i, 4, removeButton)

            removeButton.clicked.connect(lambda ch, num=i: self._remove_from_table(num, 'friday'))
        joinButton = QPushButton("Create")
        self.friday_table.setCellWidget(len(records), 4, joinButton)

        joinButton.clicked.connect(lambda ch, num=len(records): self._change_day_from_table(num, 'friday', True))

        self.friday_table.resizeRowsToContents()


    def _update_saturday_table(self):
        self.cursor.execute("select * from timetable where day='saturday'")
        records = self.cursor.fetchall()

        self.saturday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):

            self.saturday_table.setItem(i, 0, QTableWidgetItem(str(r[2])))
            self.saturday_table.setItem(i, 1, QTableWidgetItem(str(r[3])))
            self.saturday_table.setItem(i, 2, QTableWidgetItem(str(r[4])))

            joinButton = QPushButton("Change")
            self.saturday_table.setCellWidget(i, 3, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num, 'saturday'))

            removeButton = QPushButton("Remove")
            self.saturday_table.setCellWidget(i, 4, removeButton)

            removeButton.clicked.connect(lambda ch, num=i: self._remove_from_table(num, 'saturday'))
        joinButton = QPushButton("Create")
        self.saturday_table.setCellWidget(len(records), 4, joinButton)

        joinButton.clicked.connect(lambda ch, num=len(records): self._change_day_from_table(num, 'saturday', True))

        self.saturday_table.resizeRowsToContents()


    def _update_subject_table(self):
        self.cursor.execute("select name from subject")
        records = self.cursor.fetchall()

        self.subject_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):

            self.subject_table.setItem(i, 0, QTableWidgetItem(str(r[0])))

            joinButton = QPushButton("Change")
            self.subject_table.setCellWidget(i, 1, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_subject_from_table(num))

            removeButton = QPushButton("Remove")
            self.subject_table.setCellWidget(i, 2, removeButton)

            removeButton.clicked.connect(lambda ch, num=i: self._remove_subject_from_table(num))
        joinButton = QPushButton("Create")
        self.subject_table.setCellWidget(len(records), 2, joinButton)

        joinButton.clicked.connect(lambda ch, num=len(records): self._change_subject_from_table(num, True))

        self.subject_table.resizeRowsToContents()


    def _update_teacher_table(self):
        self.cursor.execute("select * from teacher")
        records = self.cursor.fetchall()

        self.teacher_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):

            self.teacher_table.setItem(i, 0, QTableWidgetItem(str(r[1])))
            self.teacher_table.setItem(i, 1, QTableWidgetItem(str(r[2])))

            joinButton = QPushButton("Change")
            self.teacher_table.setCellWidget(i, 2, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_teacher_from_table(num))

            removeButton = QPushButton("Remove")
            self.teacher_table.setCellWidget(i, 3, removeButton)

            removeButton.clicked.connect(lambda ch, num=i: self._remove_teacher_from_table(num))
        joinButton = QPushButton("Create")
        self.teacher_table.setCellWidget(len(records), 3, joinButton)

        joinButton.clicked.connect(lambda ch, num=len(records): self._change_teacher_from_table(num, True))

        self.teacher_table.resizeRowsToContents()


    def _change_day_from_table(self, rowNumb, day, new=False):
        rows = list()
        if day == 'monday':
            for i in range(self.monday_table.columnCount()):
                try:
                    rows.append(self.monday_table.item(rowNumb, i).text())
                except:
                    rows.append(None)
        elif day == 'tuesday':
            for i in range(self.tuesday_table.columnCount()):
                try:
                    rows.append(self.tuesday_table.item(rowNumb, i).text())
                except:
                    rows.append(None)
        elif day == 'wednesday':
            for i in range(self.wednesday_table.columnCount()):
                try:
                    rows.append(self.wednesday_table.item(rowNumb, i).text())
                except:
                    rows.append(None)
        elif day == 'thursday':
            for i in range(self.thursday_table.columnCount()):
                try:
                    rows.append(self.thursday_table.item(rowNumb, i).text())
                except:
                    rows.append(None)
        elif day == 'friday':
            for i in range(self.friday_table.columnCount()):
                try:
                    rows.append(self.friday_table.item(rowNumb, i).text())
                except:
                    rows.append(None)
        elif day == 'saturday':
            for i in range(self.saturday_table.columnCount()):
                try:
                    rows.append(self.saturday_table.item(rowNumb, i).text())
                except:
                    rows.append(None)
        self.cursor.execute("select name from subject")
        subjects = self.cursor.fetchall()
        subjects = [x[0] for x in subjects]
        if rows[0] not in subjects:
            QMessageBox.about(self, "Error", f"Subject \"{rows[0]}\" not exists")
            self._update_schedule()
            return
        if new:
            try:
                self.cursor.execute('insert into timetable (id, day, subject, room_numb, start_time) values (?, ?, ?, ?, ?)', (rowNumb, day, rows[0], rows[1], rows[2],))
                self.conn.commit()
                self._update_schedule()
            except:
                QMessageBox.about(self, "Error", "Enter all fields")
        else:
            try:
                self.cursor.execute('update timetable set subject=?, room_numb=?, start_time=? where id=? and day=?', (rows[0], rows[1], rows[2], rowNumb, day,))
                self.conn.commit()
                self._update_schedule()
            except:
                QMessageBox.about(self, "Error", "Enter all fields")


    def _change_subject_from_table(self, rowNumb, new=False):
        rows = list()
        try:
            rows.append(self.subject_table.item(rowNumb, 0).text())
        except:
            rows.append(None)
        self.cursor.execute("select name from subject")
        subjects = self.cursor.fetchall()
        subjects = [x[0] for x in subjects]
        if rows[0] in subjects:
            QMessageBox.about(self, "Error", f"Subject \"{rows[0]}\" already exists")
            self._update_subject_table()
            return
        if new:
            try:
                self.cursor.execute('insert into subject (name) values (?)', (rows[0],))
                self.conn.commit()
                self._update_subject_table()
            except:
                QMessageBox.about(self, "Error", "Enter all fields")
        else:
            try:
                self.cursor.execute('update subject set name=? where id=?', (rows[0], rowNumb,))
                self.conn.commit()
                self._update_subject_table()
            except:
                QMessageBox.about(self, "Error", "Enter all fields")


    def _change_teacher_from_table(self, rowNumb, new=False):
        rows = list()
        for i in range(self.teacher_table.columnCount()):
            try:
                rows.append(self.teacher_table.item(rowNumb, i).text())
            except:
                rows.append(None)
        self.cursor.execute("select name from subject")
        subjects = self.cursor.fetchall()
        subjects = [x[0] for x in subjects]
        if rows[1] not in subjects:
            QMessageBox.about(self, "Error", f"Subject \"{rows[1]}\" not exists")
            self._update_teacher_table()
            return
        if new:
            try:
                self.cursor.execute('insert into teacher (full_name, subject) values (?, ?)', (rows[0], rows[1],))
                self.conn.commit()
                self._update_teacher_table()
            except:
                QMessageBox.about(self, "Error", "Enter all fields or be shure, that subject wrote is correct!")
        else:
            try:
                self.cursor.execute('update teacher set full_name=?, subject=? where id=?', (rows[0], rows[1], rowNumb,))
                self.conn.commit()
                self._update_teacher_table()
            except:
                QMessageBox.about(self, "Error", "Enter all fields or be shure, that subject wrote is correct!")


    def _remove_from_table(self, rowNumb, day):
        try:
            self.cursor.execute('update timetable set subject="", room_numb="", start_time="" where id=? and day=?', (rowNumb, day,))
            self.conn.commit()
            self._update_schedule()
        except:
            QMessageBox.about(self, "Error", "Can't delete")


    def _remove_subject_from_table(self, rowNumb):
        try:
            self.cursor.execute('update subject set name="" where id=?', (rowNumb,))
            self.conn.commit()
            self._update_subject_table()
        except:
            QMessageBox.about(self, "Error", "Can't delete")


    def _remove_teacher_from_table(self, rowNumb):
        try:
            self.cursor.execute('update teacher set full_name="", subject="" where id=?', (rowNumb,))
            self.conn.commit()
            self._update_teacher_table()
        except:
            QMessageBox.about(self, "Error", "Can't delete")


    def _update_schedule(self):
        self._update_monday_table()
        self._update_tuesday_table()
        self._update_wednesday_table()
        self._update_thursday_table()
        self._update_friday_table()
        self._update_saturday_table()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
