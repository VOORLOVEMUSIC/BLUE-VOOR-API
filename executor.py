import sys
import requests
from PyQt5 import QtWidgets

# Define the API URL
API_URL = "http://127.0.0.1:5000"

class ExecutorApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("VOOR/BLUE EXECUTOR")
        self.setGeometry(100, 100, 600, 400)  # Width and height

        # Layout
        self.layout = QtWidgets.QVBoxLayout()

        # Text Box for Script Input
        self.text_box = QtWidgets.QTextEdit(self)
        self.text_box.setPlaceholderText("Enter your script here...")
        self.layout.addWidget(self.text_box)

        # Execute Button
        self.execute_button = QtWidgets.QPushButton("Execute Script", self)
        self.execute_button.clicked.connect(self.execute_script)
        self.layout.addWidget(self.execute_button)

        self.setLayout(self.layout)
        self.setStyleSheet("background-color: black; color: white; font-size: 16px;")  # Dark theme

    def execute_script(self):
        script = self.text_box.toPlainText()
        try:
            # First attach to the process
            attach_response = requests.post(f"{API_URL}/attach")
            print("Attach response:", attach_response.json())

            # Then execute the script
            execute_response = requests.post(f"{API_URL}/execute", json={"script": script})
            print("Execute response:", execute_response.json())
        except Exception as e:
            print(f"Error during execution: {e}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    executor = ExecutorApp()
    executor.show()
    sys.exit(app.exec_())
