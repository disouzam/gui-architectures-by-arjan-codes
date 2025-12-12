"""
    Entry point module for MVC application
"""

from controller import Controller
from model import Model

def main() -> None:
    """
    Entry point for MVC application
    """
    model = Model()
    # view = TodoList(model)
    controller = Controller(model)
    controller.run()

if __name__ == "__main__":
    main()