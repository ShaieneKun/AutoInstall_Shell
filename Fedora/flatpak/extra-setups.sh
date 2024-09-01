flatpak --user override --filesystem=/home/$USER/.icons/:ro
flatpak override --filesystem=/usr/share/icons/:ro

flatpak override --user --env=MANGOHUD=1 com.valvesoftware.Steam
flatpak override --user --filesystem=xdg-config/MangoHud:ro com.valvesoftware.Steam

# todo add ozone env var