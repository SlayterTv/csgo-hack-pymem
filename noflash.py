import pymem, pymem.process, keyboard
m_flFlashMaxAlpha = (0x1046C)
dwLocalPlayer = (0xDA747C)
#init()
def main():
	print("Iniciando busqueda CsGo")
	pm = pymem.Pymem("csgo.exe")
	print("csgo encontrado y enlazado con pymem ")
	client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
	print("cConectando con client.dll")
	try:
		print("hack iniciado")
		while True:
			player = pm.read_int(client + dwLocalPlayer)
			if player:
				flash_value = player + m_flFlashMaxAlpha
				if flash_value:
					pm.write_float(flash_value, float(0))
			if keyboard.is_pressed("*"):
				print("cerrando hack")
				exit(0)			
	except Exception as e:
		Print(e)
if __name__ == '__main__':
	main()



