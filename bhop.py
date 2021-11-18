import pymem, keyboard, time
dwForceJump = (0x526B5B0)
m_fFlags = (0x104)
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
			if keyboard.is_pressed("space"):
				force_jump = client + dwForceJump
				player = pm.read_int(client + dwLocalPlayer)
				if player:
					on_ground = pm.read_int(player + m_fFlags)
					if on_ground and on_ground == 257:
						pm.write_int(force_jump, 5)
						time.sleep(0.08)
						pm.write_int(force_jump, 4)
			if keyboard.is_pressed("*"):
				print("cerrando hack")
				exit(0)			
	except Exception as e:
		Print(e)
if __name__ == '__main__':
	main()



