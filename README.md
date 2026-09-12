an overlay made to work on wayland, needs the user to have the "input" permission

also the names of the devices are absolute, change them in server.py,
you can also change the layout in overlay.html

## setup

figure out the device names through evtest, change them in server.py, then i would recommend creating a background process

after that click "add source" in obs, "browser" and choose overlay.html(local file option)

<img width="173" height="175" alt="image" src="https://github.com/user-attachments/assets/014f40cc-c2fd-421c-a31b-d12fdb083364" />

