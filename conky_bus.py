from fetch_station import compile_menu

for line in compile_menu("Helmholtzstraße"):
	if "Striesen" in line:
		print(line)
		break