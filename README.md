an overlay made to work on wayland, needs the user to have the "input" permission

also the names of the devices are absolute, change them in server.py,
you can also change the layout in overlay.html

## setup

figure out the device names through evtest, change them in server.py, then i would recommend creating a background process

after that click "add source" in obs, "browser" and choose overlay.html(local file option)

<img width="170" height="167" alt="image" src="https://github.com/user-attachments/assets/974c310f-f6e2-4dda-83a2-901cc8962378" />
