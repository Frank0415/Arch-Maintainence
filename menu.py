from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
import os
import readchar

console = Console()

choices = [
    "Toggle Monitor Scaling",
    "Toggle Wacom Tablet",
    "Reboot Polybar",
    "Upgrade ALL using AUR",
    "Sudo Original Maintenance",
    "Exit program"
]

def run_command(cmd, sudo=False, background=False):
    if sudo:
        cmd = f"sudo {cmd}"
    if background:
        os.system(f"{cmd} &")
    else:
        os.system(cmd)

def main():
    highlight = 0
    try:
        while True:
            console.clear()
            table = Table(show_header=False, box=None, expand=False)
            for idx, item in enumerate(choices):
                if idx == highlight:
                    table.add_row(f"[reverse]{idx+1}. {item}[/reverse]")
                else:
                    table.add_row(f"{idx+1}. {item}")
            panel = Panel(Align.center(table), title="System Maintenance Menu", expand=False)
            console.print(panel)
            # console.print("Use Up/Down arrows or 1-6 to select, Enter to confirm", style="bold")
            key = readchar.readkey()
            if key in (readchar.key.UP, 'k'):
                highlight = (highlight - 1) % len(choices)
            elif key in (readchar.key.DOWN, 'j'):
                highlight = (highlight + 1) % len(choices)
            elif key in map(str, range(1, len(choices)+1)):
                highlight = int(key) - 1
            elif key in (readchar.key.ENTER, '\r', '\n'):
                choice = highlight
                if choice == 0:
                    run_command("./Utilities/8-Monitor-Toggle")
                elif choice == 1:
                    run_command("./Utilities/9-Wacom")
                elif choice == 2:
                    run_command("$HOME/.config/polybar/launch.sh", background=True)
                elif choice == 3:
                    run_command("./Utilities/4-AURupgrade")
                elif choice == 4:
                    run_command("./ArchLinux-Maintenance-orig", sudo=True)
                elif choice == 5:
                    break
                input("Press Enter to return to menu...")
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
