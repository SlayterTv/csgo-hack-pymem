import pymem, keyboard, time
m_iDefaultFOV = (0x333C)
dwEntityList = (0x4DC179C)
def main():
	print("Iniciando busqueda CsGo")
	pm = pymem.Pymem("csgo.exe")
	print("csgo encontrado y enlazado con pymem ")
	client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
	print("cConectando con client.dll")
	try:
		print("hack iniciado")
		while True:
			player = pm.read_int(client + dwEntityList)
			iFOV = pm.read_int(player + m_iDefaultFOV)
			if keyboard.is_pressed("/"):
				print("cerrando hack")
				pm.write_int(player + m_iDefaultFOV, 100)
				exit(0)			
			if keyboard.is_pressed("*"):
				pm.write_int(player + m_iDefaultFOV, 140)
			if keyboard.is_pressed("-"):
				pm.write_int(player + m_iDefaultFOV, 100)
	except Exception as e:
		Print(e)
if __name__ == '__main__':
	main()



