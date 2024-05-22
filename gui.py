import sys
import keys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QComboBox, QWidget, QLabel, QLineEdit
import sms_function
from misc_funcs import TimezoneFunctions, WeatherFunctions

def run():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("My Reminders/Weather App")

    layout = QVBoxLayout()

    global timezone_selection_combobox
    timezone_selection_combobox = QComboBox()
    timezone_selection_combobox.addItems(TimezoneFunctions.zones)
    timezone_selection_combobox.setCurrentText(TimezoneFunctions.zones[0])  # Set the default value
    layout.addWidget(timezone_selection_combobox)

    # Create a button to get the selected item
    get_tz = QPushButton("Save Timezone")
    get_tz.clicked.connect(updateTime)
    layout.addWidget(get_tz)

    global weather_selection_textbox
    label2 = QLabel("Enter City (City State) :")
    label2.setGeometry(50, 100, 100, 30)

    weather_selection_textbox = QLineEdit()
    weather_selection_textbox.setGeometry(150, 100, 200, 30)
    layout.addWidget(weather_selection_textbox)

    get_city = QPushButton("Save City")
    get_city.clicked.connect(updateCity)
    layout.addWidget(get_city)

    # Set the layout to the main window
    central_widget = QWidget()
    central_widget.setLayout(layout)
    window.setCentralWidget(central_widget)

    window.show()
    sys.exit(app.exec())


def updateTime():
    selected_item = timezone_selection_combobox.currentText()
    time_dict = TimezoneFunctions.convertTimeZone(selected_item)
    sms_function.update_message(time_dict)


def updateCity():
    input_city = weather_selection_textbox.text()
    location_coords = WeatherFunctions.getCurrentLocation(input_city)
    lat = location_coords["lat"]
    lon = location_coords["long"]
    keys.coord_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={keys.openWeatherAPI}"
    print(keys.coord_url)


