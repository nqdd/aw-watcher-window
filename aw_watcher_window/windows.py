import logging
from aw_core.log import setup_logging

from typing import Optional

import wmi
import win32gui
import win32process

c = wmi.WMI()

logger = logging.getLogger(__name__)

"""
Much of this derived from: http://stackoverflow.com/a/14973422/965332
"""

def get_app_path(hwnd) -> Optional[str]:
    """Get application path given hwnd."""
    path = None
    try:
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        query = 'SELECT ExecutablePath FROM Win32_Process WHERE ProcessId = %s' % str(pid)
        for p in c.query(query):
            path = p.ExecutablePath
            break
    except:
        logger.error(f"getting name error query is: {query}")
    return path

def get_app_name(hwnd) -> Optional[str]:
    """Get application filename given hwnd."""
    name = None
    try:
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        query = 'SELECT Name FROM Win32_Process WHERE ProcessId = %s' % str(pid)
        for p in c.query(query):
            name = p.Name
            break
    except:
        logger.error(f"getting name error query is: {query}")
    return name

def get_window_title(hwnd):
    return win32gui.GetWindowText(hwnd)

def get_active_window_handle():
    hwnd = win32gui.GetForegroundWindow()
    return hwnd


if __name__ == "__main__":
    hwnd = get_active_window_handle()
    print("Title:", get_window_title(hwnd))
    print("App:", get_app_name(hwnd))