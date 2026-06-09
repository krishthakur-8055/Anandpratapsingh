import win32com.client
import time
speak = win32com.client.Dispatch ("SAPI.SpVoice")
#text = '''krish what are you doing,
#how pari is looking'''
#speak.Speak(text)
time.sleep(2)
text = 'krish you are nothing'
speak.Speak(text) 