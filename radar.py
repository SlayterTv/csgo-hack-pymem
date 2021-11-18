import pymem, keyboard, time
m_bSpotted = (0x93D)
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
			if keyboard.is_pressed("*"):
				print("cerrando hack")
				exit(0)			
			for i in range(1, 32):
				entity = pm.read_int(client + dwEntityList + i * 0x10)
				if entity:
					pm.write_uchar(entity + m_bSpotted, 1)
	except Exception as e:
		Print(e)
if __name__ == '__main__':
	main()



