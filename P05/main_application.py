import tkinter as tk
from transport_api_service import TransportApiService

"""
Main application with search interface. 
The interface asks the user's home location in Switzerland and the desired destination somewhere in the neighbouring countries.
The application then calculates the shortest route between the two locations.
"""


class MainApplication:
    def __init__(self):
        self.transport_api_service = TransportApiService()
        self.connections = []
        self.main()

    def main(self):
        self.window = tk.Tk()

        self.start_location_label = tk.Label(text="Von")
        self.start_location_label.pack()
        self.start_location_input = tk.Entry(self.window)
        self.start_location_input.pack()
        self.destination_label = tk.Label(text="Nach")
        self.destination_label.pack()
        self.destination_input = tk.Entry(self.window)
        self.destination_input.pack()
        self.button = tk.Button(
            text="Verbindung suchen",
            width=25,
            height=1,
            bg="red",
            fg="white",
        )
        self.button.bind("<Button-1>", self.handle_click)
        self.button.pack()
        self.window.mainloop()

    def handle_click(self, event):
        print("Button clicked")
        self.connections = self.transport_api_service.get_connections(
            self.start_location_input.get(), self.destination_input.get())
        print(self.connections)


def main():
    main_application = MainApplication()


if __name__ == '__main__':
    main()
