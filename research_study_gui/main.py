from controller.controller import Controller
from view.main_view import MainView
from model.registry_manager import RegistryManager
from controller.sql_functions import SQLSetup as su
import tkinter as tk

if __name__ == "__main__":

    sql_setup = su()

    # Create shared model
    shared_registry_manager = RegistryManager(sql_setup)
    shared_registry_manager.setup_objects()

    # Create view (and later pass controller to it)
    root = tk.Tk()
    view = MainView(root)

    # Create controller and inject shared model
    controller = Controller(view, shared_registry_manager)

    # Optionally connect controller back to view
    view.set_controller(controller)

    # Start GUI
    view.mainloop()
