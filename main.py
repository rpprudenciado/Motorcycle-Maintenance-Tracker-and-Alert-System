"""
MotoPulse - Application Entry Point
"""
import sys
from MotoPulse_UI import MotoPulseCLI

if __name__ == "__main__":
    cli = MotoPulseCLI()
    cli.display_welcome()
    try:
        cli.main_menu()
    except KeyboardInterrupt:
        print("\n🏍️  EXITING MOTOPULSE... RIDE SAFE!")
        cli.app_state.save_data()
        sys.exit(0)
