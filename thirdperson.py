import pymem, keyboard, time
m_iObserverMode = (0x3388)
dwLocalPlayer = (0xDA747C)
def main():
	print("Iniciando busqueda CsGo")
	pm = pymem.Pymem("csgo.exe")
	print("csgo encontrado y enlazado con pymem ")
	client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
	print("cConectando con client.dll")
	try:
		print("hack iniciado")
		switch = 0
		while True:
			localplayer = pm.read_int(client + dwLocalPlayer)
			if keyboard.is_pressed("*") and switch == 0:
				pm.write_int(localplayer + m_iObserverMode, 1)
				switch = 1
				time.sleep(0.5)
			if keyboard.is_pressed("*") and switch == 1:
				pm.write_int(localplayer + m_iObserverMode, 0)
				switch = 0
				time.sleep(0.5)
			if keyboard.is_pressed("-") and switch == 0:
				exit(0)
				print("cerrando hack")

	except Exception as e:
		Print(e)
if __name__ == '__main__':
	main()



