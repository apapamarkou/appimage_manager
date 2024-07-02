# AppImage Menu Manager Script

A simple and convenient way to manage appimages. Just put the `appimage_manager.py` in your startup applications, make a directory in your home folder, name it "Applications" and add or remove your appimages there. 
This script automatically adds or removes AppImages to/from your desktop application menus when they are added to or removed from the `~/Application` folder. It helps to keep your application menus updated with your AppImages seamlessly.

## Features

- Automatically add AppImages to application menus.
- Automatically remove AppImages from application menus when deleted from `~/Application`.
- Easy setup and configuration.

## Dependencies

- `inotify-tools` (for monitoring changes in the `~/Application` folder)
- `python3` (for executing the script)

## Installation

1. **Install dependencies**
   - **Arch Linux, Manjaro, Garuda**
    ```sh
    sudo pacman -Syu inotify-tools python
    ```

    - **Solus**
    ```sh
    sudo eopkg install inotify-tools python3
    ```

    - **Debian, Ubuntu, Mint**
    ```sh
    sudo apt update
    sudo apt install inotify-tools python3
    ```

    - **Red Hat, Fedora**
    ```sh
    sudo dnf install inotify-tools python3
    ```

    - **OpenSUSE**
    ```sh
    sudo zypper install inotify-tools python3
    ```

    - **Slackware**
    Install `inotify-tools` and `python3` from the SlackBuilds repository or your preferred method.


2. **Install the script**:
    ```bash
    mkdir -p ~/Applications/appimage_manager
    wget https://github.com/apapamarkou/appimage_manager/raw/main/appimage_manager.py -O ~/Applications/appimage_manager/appimage_manager.py
    chmod +x ~/Applications/appimage_manager/appimage_manager.py
    ```


3. **Add to startup:**

    - **KDE Plasma:** Go to `System Settings` -> `Startup and Shutdown` -> `Autostart` -> `Add Login Script` and point to `~/Applications/appimage_manager/appimage_manager.py`.

    - **GNOME:** Open `Startup Applications`, click `Add`, and point to `~/Applications/appimage_manager/appimage_manager.py`.

    - **XFCE:** Go to `Session and Startup` -> `Application Autostart`, click `Add`, and enter the command `~/Applications/appimage_manager/appimage_manager.py`.

    - **i3/Sway:** Add the script to your `~/.config/i3/config` or `~/.config/sway/config` file using `exec --no-startup-id ~/Applications/appimage_manager/appimage_manager.py`.


## Usage

1. Place your AppImages in the `~/Application` folder.
2. The script will automatically detect and update your application menu.

## Troubleshooting

- Ensure the `inotify-tools` and `python3` packages are installed and up to date.
- Verify that the script has executable permissions.
- Check your desktop environment's logs if the script does not run as expected.

## License

This script is licensed under the GNU License. See the [LICENSE](LICENSE) file for details.


