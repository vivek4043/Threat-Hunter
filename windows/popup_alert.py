import ctypes

def popup_alert(message, title="⚠️ Suspicious Login Alert"):
    ctypes.windll.user32.MessageBoxW(0, message, title, 0x40 | 0x1)
