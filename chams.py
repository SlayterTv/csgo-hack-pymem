import pymem, keyboard, time
m_clrRender = (0x70)
model_ambient_min = (0x58D044)
dwLocalPlayer = (0xDA747C)
dwEntityList = (0x4DC179C)
m_iTeamNum = (0xF4)
def main():
	print("Iniciando busqueda CsGo")
	pm = pymem.Pymem("csgo.exe")
	print("csgo encontrado y enlazado con pymem ")
	client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
	engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll
	print("cConectando con client.dll y engine.dll")
	rgbtT = [255, 51, 0]
	rgbtCT = [0, 51, 255]
	try:
		print("hack iniciado")
		while True:
			time.sleep(0.001)
			if keyboard.is_pressed("*"):
				print("cerrando hack")
				exit(0)			
			for i in range(1, 32):
				entity = pm.read_int(client + dwEntityList + i * 0x10)
				if entity:
					entity_team_id = pm.read_int(entity + m_iTeamNum)
					if entity_team_id == 2:
						pm.write_int(entity + m_clrRender, (rgbtT[0]))
						pm.write_int(entity + m_clrRender + 0x1, (rgbtT[1]))
						pm.write_int(entity + m_clrRender + 0x2, (rgbtT[2]))
					elif entity_team_id == 3:
						pm.write_int(entity + m_clrRender, (rgbtCT[0]))
						pm.write_int(entity + m_clrRender + 0x1, (rgbtCT[1]))
						pm.write_int(entity + m_clrRender + 0x2, (rgbtCT[2]))
				else:
					pass
	except Exception as e:
		Print(e)
if __name__ == '__main__':
	main()