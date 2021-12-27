from ui.main import Ui_MainWindow
from PySide6 import QtCore, QtGui, QtWidgets, QtCharts
import subprocess
import pathlib

from config.manager import ConfigManager
from vehicle.formulas import calc_oss_from_mph, calc_engine_rpm_from_oss, Tire, to_ordinal_number


from vehicle import vehiclebuilder

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.gear_chart = QtCharts.QChart()
        #self.gear_chart.legend().hide()
        self.gear_chart.createDefaultAxes()
        self.gear_chart.setTitle("OSS vs Engine RPM")

        self.chart_view = QtCharts.QChartView(self.gear_chart)
        self.chart_view.setRenderHint(QtGui.QPainter.Antialiasing)
        self.chart_view.chart().setTheme(QtCharts.QChart.ChartThemeQt.ChartThemeDark)

        layout = QtWidgets.QGridLayout(self)
        layout.addWidget(self.chart_view)
        self.ui.widgetGearsChart.setLayout(layout)

        for fname, values in self.get_configs().items():
            self.ui.comboBoxProfile.addItem(f"{values['name']}")        

    def get_configs(self):
        """
        Returns a dictionary of config files. Key is the fname, value is the name specified in the file
        """
        config_manager = ConfigManager()
        configs = {}
        for config in config_manager.list():
            values = config_manager.load(config.name)
            configs[config.name] = values
            #self.ui.comboBoxProfile.addItem(values['name'])
        return configs

    def get_current_profile(self):
        profile_name = self.ui.comboBoxProfile.currentText()
        for fname, values in self.get_configs().items():
            if profile_name == values['name']:
                return fname, values
    
    def get_vehicle(self):
        fname, values = self.get_current_profile()
        return vehiclebuilder.create_from_config(fname)

    def create_profile_model(self):
        def append_children(parent, values):
            for k, v in values.items():
                items = []
                items.append(QtGui.QStandardItem(str(k)))
                if isinstance(v, dict):
                    append_children(items[0], v)
                else:
                    items.append(QtGui.QStandardItem(str(v)))
                parent.appendRow(items)

        model = QtGui.QStandardItemModel()
        self.ui.treeViewProfile.setModel(model)
        fname, values = self.get_current_profile()
        
        model.setHorizontalHeaderLabels(("Name", "Value"))
        parent = QtGui.QStandardItem(str(fname))
        append_children(parent, values)
        model.appendRow([parent, QtGui.QStandardItem()])
        self.ui.treeViewProfile.expandAll()
        for i in range(model.columnCount()):
            self.ui.treeViewProfile.resizeColumnToContents(i)
    
    def create_gears_model(self):
        vehicle = self.get_vehicle()

        self.ui.tableWidgetGears.setRowCount(len(vehicle.transmission.gears))

        MAX_OSS = 6000
        gears = vehicle.transmission.gears
        gear_labels = ['MPH', ]
        gear_labels.extend(([to_ordinal_number(gear+1) for gear in range(len(gears))]))
        # setup the QTableWidget
        self.ui.tableWidgetGears.setColumnCount(len(gear_labels))
        self.ui.tableWidgetGears.setHorizontalHeaderLabels(gear_labels)
        self.ui.tableWidgetGears.setRowCount(MAX_OSS)

        for oss in range(1, MAX_OSS):
            oss_items = []
            mph = vehicle.get_mph_from_oss(oss)
            self.ui.tableWidgetGears.setItem(oss-1, 0, QtWidgets.QTableWidgetItem(f'{mph:.1f}MPH'))
            for i, ratio in enumerate(gears):
                rpm = vehicle.get_rpm(oss, i+1)
                #rpm = calc_engine_rpm_from_oss(oss, ratio)
                self.ui.tableWidgetGears.setItem(oss-1, i+1, QtWidgets.QTableWidgetItem(f'{rpm:.1f}RPM'))
        self.ui.tableWidgetGears.resizeColumnsToContents()
    
        self.gear_chart.hide()

        """
            def get_oss(self, mph):
        return calc_oss_from_mph(mph, self.tire, self.drivetrain.axle_ratio)
    
    def get_rpm(self, oss, gear):
        return calc_engine_rpm_from_oss(oss, self.transmission.gears[gear-1])
    
    def get_rpm_from_mph(self, mph, gear):
        oss = self.get_oss(mph)
        return self.get_rpm(oss, gear)
        """
        """
        fname, values = self.get_current_profile()
        gears = values['transmission']['gears']
        horizontal_labels = ['MPH', 'OSS'] + (list(gears.keys()))
        max_mph = 100
        tire = Tire(values['drivetrain']['tire_diameter'])
        gear_ratios = gears.values()
        axle_ratio = values['drivetrain']['axle_ratio']
        max_rpm = values['engine']['max_rpm']
        self.ui.tableWidgetGears.setRowCount(max_mph*10)
        self.ui.tableWidgetGears.setColumnCount(len(horizontal_labels))
        self.ui.tableWidgetGears.setHorizontalHeaderLabels(horizontal_labels)
        for i, mph in enumerate(range(max_mph*10)):
            items = []
            mph = mph / 10.0
            oss = calc_oss_from_mph(mph, tire, axle_ratio)
            items.append(QtWidgets.QTableWidgetItem(f'{mph:.1f}'))
            items.append(QtWidgets.QTableWidgetItem(f'{oss:.1f}'))
            self.gear_series = QtCharts.QLineSeries()
            for gear, ratio in enumerate(gear_ratios):
                rpm = calc_engine_rpm_from_oss(oss, ratio)
                #if gear == 1 and mph % 1 == 0:
                #    self.gear_series.append(int(mph), int(rpm))
                #    print(mph, rpm)
                items.append(QtWidgets.QTableWidgetItem(f'{rpm:.1f}'))
            for x, item in enumerate(items):
                self.ui.tableWidgetGears.setItem(i, x, item)
        self.ui.tableWidgetGears.resizeColumnsToContents()


        self.gear_chart.removeAllSeries()
        all_series = []
        # Generate all the series for each gear
        for gear, ratio in enumerate(gear_ratios):
            series = QtCharts.QLineSeries()
            series.setName(list(gears.keys())[gear])
            all_series.append(series)
            for oss in range(10000):
                rpm = calc_engine_rpm_from_oss(oss, ratio)
                if rpm > max_rpm:
                    break
                series.append(QtCore.QPointF(rpm, oss))
        for series in all_series:
            self.gear_chart.addSeries(series)
        self.gear_chart.createDefaultAxes()
        """

    @QtCore.Slot()
    def on_toolButtonProfileExplore_clicked(self):
        config_manager = ConfigManager()
        fname, values = self.get_current_profile()
        path = pathlib.Path(config_manager.path).joinpath(fname)
        subprocess.run(f'explorer /select,"{str(path)}"')

    @QtCore.Slot(str)
    def on_comboBoxProfile_currentTextChanged(self, value):
        self.create_profile_model()
        self.create_gears_model()
        print(value)
    


class CustomTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data=None):
        QtCore.QAbstractTableModel.__init__(self)
        self.load_data(data)

    def load_data(self, data):
        self.input_dates = data[0].values
        self.input_magnitudes = data[1].values

        self.column_count = 2
        self.row_count = len(self.input_magnitudes)

    def rowCount(self, parent=QtCore.QModelIndex()):
        return self.row_count

    def columnCount(self, parent=QtCore.QModelIndex()):
        return self.column_count

    def headerData(self, section, orientation, role):
        if role != QtCore.Qt.DisplayRole:
            return None
        if orientation == QtCore.Qt.Horizontal:
            return ("Date", "Magnitude")[section]
        else:
            return "{}".format(section)

    def data(self, index, role = QtCore.Qt.DisplayRole):
        column = index.column()
        row = index.row()

        if role == QtCore.Qt.DisplayRole:
            if column == 0:
                raw_date = self.input_dates[row]
                date = "{}".format(raw_date.toPython())
                return date[:-3]
            elif column == 1:
                return "{:.2f}".format(self.input_magnitudes[row])
        elif role == QtCore.Qt.BackgroundRole:
            return QtCore.QColor(QtCore.Qt.white)
        elif role == QtCore.Qt.TextAlignmentRole:
            return QtCore.Qt.AlignRight

        return None