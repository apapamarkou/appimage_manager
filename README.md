# AppImage Menu Manager Script

This script automatically adds or removes AppImages to/from the application menus when they are added to or removed from the `~/Application` folder. It helps to keep your application menus updated with your AppImages seamlessly.

## Features

- Automatically add AppImages to application menus.
- Remove AppImages from application menus when deleted from `~/Application`.
- Easy setup and configuration.

## Dependencies

- `inotify-tools` (for monitoring changes in the `~/Application` folder)
- `python3` (for executing the script)

## Installation

### Arch Linux, Manjaro, Garuda

1. **Install dependencies**:
    ```sh
    sudo pacman -Syu inotify-tools python
    ```

2. **Install the script**:
    - Download or clone the script to a directory of your choice.
    - Make the script executable:
      ```sh
      chmod +x /path/to/your/script.sh
      ```

### Solus

1. **Install dependencies**:
    ```sh
    sudo eopkg install inotify-tools python3
    ```

2. **Install the script**:
    - Download or clone the script to a directory of your choice.
    - Make the script executable:
      ```sh
      chmod +x /path/to/your/script.sh
      ```

### Debian, Ubuntu, Mint

1. **Install dependencies**:
    ```sh
    sudo apt update
    sudo apt install inotify-tools python3
    ```

2. **Install the script**:
    - Download or clone the script to a directory of your choice.
    - Make the script executable:
      ```sh
      chmod +x /path/to/your/script.sh
      ```

### Red Hat, Fedora

1. **Install dependencies**:
    ```sh
    sudo dnf install inotify-tools python3
    ```

2. **Install the script**:
    - Download or clone the script to a directory of your choice.
    - Make the script executable:
      ```sh
      chmod +x /path/to/your/script.sh
      ```

### OpenSUSE

1. **Install dependencies**:
    ```sh
    sudo zypper install inotify-tools python3
    ```

2. **Install the script**:
    - Download or clone the script to a directory of your choice.
    - Make the script executable:
      ```sh
      chmod +x /path/to/your/script.sh
      ```

### Slackware

1. **Install dependencies**:
    - Install `inotify-tools` and `python3` from the SlackBuilds repository or your preferred method.

2. **Install the script**:
    - Download or clone the script to a directory of your choice.
    - Make the script executable:
      ```sh
      chmod +x /path/to/your/script.sh
      ```

## Autostart Configuration

To ensure the script runs automatically at startup, you need to configure it in your desktop environment.

### KDE

1. Open System Settings.
2. Go to **Startup and Shutdown**.
3. Click on **Autostart**.
4. Click **Add Login Script...**.
5. Browse to your script and add it.

### GNOME

1. Open **Startup Applications** from the Activities overview.
2. Click **Add**.
3. Enter a name (e.g., "AppImage Menu Manager"), and in the command field, enter the path to your script.
4. Click **Add** to save.

### XFCE

1. Open **Session and Startup** from the settings manager.
2. Go to the **Application Autostart** tab.
3. Click **Add**.
4. Enter a name (e.g., "AppImage Menu Manager") and in the command field, enter the path to your script.
5. Click **OK** to add it.

## Usage

1. Place your AppImages in the `~/Application` folder.
2. The script will automatically detect and update your application menu.

## Troubleshooting

- Ensure the `inotify-tools` and `python3` packages are installed and up to date.
- Verify that the script has executable permissions.
- Check your desktop environment's logs if the script does not run as expected.

## License

This script is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to contribute by submitting issues, pull requests, or suggestions.

## Contact

For any questions or support, please open an issue on the repository or contact the script author.

