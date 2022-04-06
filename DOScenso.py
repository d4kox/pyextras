import pyautogui as pg, time as tm
numeros = "0123456789"
clave = ""
tm.sleep(5)
for a in range(0,6):
    for c1 in numeros:
        for c2 in numeros:
            for c3 in numeros:
                for c4 in numeros:
                    for c5 in numeros:
                        intento = c1+c2+c3+c4+c5
                        if intento != clave:
                            pg.write(intento)
                            #captcha
                            #pg.moveTo(355,620)
                            #pg.click(button='left')
                            #alert_remove
                            pg.moveTo(695,590)
                            pg.click(button='left')
                            #next_code
                            pg.moveTo(650,710)
                            pg.click(button='left')
                            #code_input
                            pg.moveTo(330,540)
                            pg.click(button='left')
                            for a in range(0,5):
                                pg.press('del')
                            pg.press('f5')