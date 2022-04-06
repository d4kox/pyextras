import pyautogui as pg, time as tm, os 
msg_counter = input("Cantidad de mensajes >> ")
msg_counter = int(msg_counter)
msg_text = input("Texto del mensaje >> ")
print('\n [!] Clickea el campo en WhatsApp Web que dice "Escribe un mensaje aquí"')
print(" [*] Los mensajes se enviaran en 5 segundos...")
tm.sleep(5)
for a in range(0,msg_counter):
    pg.write(msg_text)
    pg.press('enter')
print("[+] Mensajes enviados correctamente...")
