import asyncio
import websockets
import evdev
from evdev import ecodes

async def listen_to_device(device_path, websocket):
    while True:
        try:
            device = evdev.InputDevice(device_path)
            print(f"SUCCESS: Connected to {device.name} at {device_path}")
            
            async for event in device.async_read_loop():
                if event.type == ecodes.EV_KEY:
                    
                    state = "DOWN" if event.value == 1 else "UP" if event.value == 0 else "HOLD"
                    
                    if state != "HOLD": 
                        keycode_str = ""
                        
                        if event.code == 272:
                            keycode_str = "BTN_LEFT"
                        elif event.code == 273:
                            keycode_str = "BTN_RIGHT"
                        else:
                            key_event = evdev.categorize(event)
                            raw_code = key_event.keycode
                            keycode_str = raw_code[0] if isinstance(raw_code, list) else raw_code
                        
                        try:
                            await websocket.send(f"{keycode_str}|{state}")
                        except websockets.exceptions.ConnectionClosed:
                            pass
                            
        except FileNotFoundError:
            await asyncio.sleep(2)
        except OSError:
            print(f"Connection lost to {device_path}. Waiting for it to wake up...")
            await asyncio.sleep(2)
        except Exception as e:
            print(f"ERROR on {device_path}: {e}")
            await asyncio.sleep(2)

async def handle_client(websocket):
    keyboard_path = '/dev/input/by-id/usb-Keychron_Keychron_V1_Max-event-kbd'
    mouse_path = '/dev/input/by-id/usb-Logitech_USB_Receiver-if02-event-mouse'
    
    await asyncio.gather(
        listen_to_device(keyboard_path, websocket),
        listen_to_device(mouse_path, websocket)
    )

async def main():
    print("Server running... Waiting for OBS on ws://localhost:8765")
    async with websockets.serve(handle_client, "localhost", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
