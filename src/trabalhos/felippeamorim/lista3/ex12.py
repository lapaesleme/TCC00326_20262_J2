

sistema = {
    'arquivos': ['foto.jpg', 'texto.txt'],

    'subpastas': {
        'documentos': {
            'arquivos': ['trabalho.pdf'],

            'subpastas': {
                'faculdade': {
                    'arquivos': ['prova.py'],
                    'subpastas': {}
                }
            }
        },

        'downloads': {
            'arquivos': ['programa.exe'],
            'subpastas': {}
        }
    }
}


def buscar_arquivo(pasta, arquivo):

    if arquivo in pasta['arquivos']:
        return True

    for subpasta in pasta['subpastas'].values():

        if buscar_arquivo(subpasta, arquivo):
            return True

    return False


print(buscar_arquivo(sistema, 'prova.py'))
print(buscar_arquivo(sistema, 'musica.mp3'))