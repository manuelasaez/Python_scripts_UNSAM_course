#listar_imgs.py
import os
def main(param):
	if len(param) != 2:
		raise SystemExit(f'Uso adecuado: {param[0]} ' 'path')
	path = param[1]
	if 'home' not in path:
		print('debe pasar el path desde el home ej: /home......')
	lista_imgs(path)


def lista_imgs(path):
	'''Dado un directorio con su path dado desde el home (vale para linux), 
		imprime en pantalla los nombres de todos los archivos .png 
		que se encuentren en algún subdirectorio del él.'''
	os.chdir(path)
	print(f'Lista de archivos png encontrados en la carpeta {path}:')
	for root, dirs, files in os.walk("."):
		for name in files:
			if(name.endswith(".png")): 
				print(os.path.join(root, name))
		for name in dirs:
			if(name.endswith(".png")): 
				print(os.path.join(root, name))




if __name__ == '__main__':
    import sys
    main(sys.argv)

