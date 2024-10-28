def config():
    #main_dir: local para colocar dados decriptados
    #clean: limpar dados decriptados ao sair
    #data: data da ultima utilização

    try:
        file = open('config.cf', 'r')
        mode = 1
        main_dir = file.readline()
        clean = file.readline()
        file.close()

        print('Configurações Carregadas!')

        return [mode, main_dir[5:len(main_dir) - 2], int(clean[7:len(clean) - 1])]

    except:
        return [0]
