import pymem, keyboard, time
dwGlowObjectManager = (0x5309C78)
m_iGlowIndex = (0x10470)
dwLocalPlayer = (0xDA747C)
dwEntityList = (0x4DC179C)
m_iTeamNum = (0xF4)
def main():
	print("Iniciando busqueda CsGo")
	pm = pymem.Pymem("csgo.exe")
	print("csgo encontrado y enlazado con pymem ")
	client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
	print("cConectando con client.dll y engine.dll")
	try:
		print("hack iniciado")
		while True:
			if keyboard.is_pressed("*"):
				print("cerrando hack")
				exit(0)			
			glow_manager = pm.read_int(client + dwGlowObjectManager)
			for i in range(1, 32):
				entity = pm.read_int(client + dwEntityList + i * 0x10)
				if entity:
					entity_team_id = pm.read_int(entity + m_iTeamNum)
					entity_glow = pm.read_int(entity + m_iGlowIndex)
					if entity_team_id == 2:
						pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(1))
						pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))
						pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(0))
						pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1))
						pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)
					elif entity_team_id == 3:
						pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))
						pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))
						pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1))
						pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1))
						pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)						
				else:
					pass
	except Exception as e:
		Print(e)
if __name__ == '__main__':
	main()