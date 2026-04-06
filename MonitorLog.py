import random
import datetime

def menu():
    nome_arq = 'log.txt'
    while True:
        print('\nMENU\n')
        print('1 Gerar logs')
        print('2 Analisar logs')
        print('3 Gerar e analisar logs')
        print('4 Sair')

        try:
            opc = int(input('Escolha uma opção: '))
        except:
            print("Digite um número válido")
            continue

        if opc == 1:
            try:
                qtd = int(input('Quantidade de logs: '))
                gerarArquivo(nome_arq, qtd)
            except Exception as e:
                print('Erro:', e)

        elif opc == 2:
            analisarLogs(nome_arq)

        elif opc == 3:
            try:
                qtd = int(input('Quantidade de logs: '))
                gerarArquivo(nome_arq, qtd)
                analisarLogs(nome_arq)
            except Exception as e:
                print('Erro:', e)

        elif opc == 4:
            print('Até mais')
            break

        else:
            print('Opção inválida')

def gerarArquivo(nome_arq, qtd):
    with open(nome_arq, 'w', encoding='UTF-8') as arq:
        for i in range(qtd):
            arq.write(montarLog(i) + '\n')
    print('Log gerado com sucesso!')


def montarLog(i):
    data = gerarData(i)
    ip = gerarIp(i)
    recurso = gerarRecurso(i)
    metodo = gerarMetodo(i)
    status = gerarStatus(i)
    tempo = gerarTempo(i)
    agente = gerarAgente(i)
    protocolo = gerarProtocolo(i)
    tamanho = gerarTamanho(i)

    return f'{ip} [{data}] {i} - {metodo} - {status} - {recurso} - {tempo}ms - {tamanho} - {protocolo} - {agente}'

def gerarData(i):
    base = datetime.datetime.now()
    delta = datetime.timedelta(seconds=i * random.randint(5, 20))
    return (base + delta).strftime('%d/%m/%Y %H:%M:%S')


def gerarIp(i):
    r = random.randint(1, 6)

    if 20 <= i <= 50:
        return '203.120.45.7'

    if r == 1:
        return '192.168.12.1'
    elif r == 2:
        return '192.168.12.3'
    elif r == 3:
        return '192.100.12.3'
    elif r == 4:
        return '192.162.12.3'
    elif r == 5:
        return '192.168.23.3'
    else:
        return '192.168.0.3'


def gerarRecurso(i):
    r = random.randint(1, 4)
    if r == 1:
        return '/home'
    elif r == 2:
        return '/login'
    elif r == 3:
        return '/admin'
    else:
        return '/produtos'


def gerarMetodo(i):
    r = random.randint(1, 3)
    if r == 1:
        return 'GET'
    elif r == 2:
        return 'POST'
    else:
        return 'PUT'


def gerarStatus(i):
    r = random.randint(1, 10)
    if r <= 6:
        return 200
    elif r == 7:
        return 403
    elif r == 8:
        return 404
    else:
        return 500


def gerarTempo(i):
    return random.randint(50, 800)


def gerarAgente(i):
    r = random.randint(1, 4)
    if r == 1:
        return 'Mozilla'
    elif r == 2:
        return 'Chrome'
    elif r == 3:
        return 'Bot'
    else:
        return 'Crawler'


def gerarProtocolo(i):
    return 'HTTP/1.1'


def gerarTamanho(i):
    return random.randint(100, 5000)

def extrairCampos(linha):
    i = 0

    # ===== IP =====
    ip = ""
    while linha[i] != ' ':
        ip += linha[i]
        i += 1

    # ===== pular até STATUS =====
    cont_tracos = 0
    while cont_tracos < 2:
        if linha[i] == '-':
            cont_tracos += 1
        i += 1

    # pular espaço
    while linha[i] == ' ':
        i += 1

    # ===== STATUS =====
    status = ""
    while linha[i] != ' ':
        status += linha[i]
        i += 1
    status = int(status)

    # ===== pular " - " =====
    while linha[i] != '-':
        i += 1
    i += 1
    while linha[i] == ' ':
        i += 1

    # ===== RECURSO =====
    recurso = ""
    while linha[i] != ' ':
        recurso += linha[i]
        i += 1

    # ===== pular " - " =====
    while linha[i] != '-':
        i += 1
    i += 1
    while linha[i] == ' ':
        i += 1

    # ===== TEMPO =====
    tempo = ""
    while linha[i] != 'm':
        tempo += linha[i]
        i += 1

    tempo = int(tempo)

    return ip, status, recurso, tempo

def analisarLogs(nome_arq):
    try:
        arq = open(nome_arq, 'r', encoding='UTF-8')
    except:
        print('Erro ao abrir arquivo')
        return

    total = sucessos = erros = erros_500 = 0
    soma_tempo = 0
    maior = -1
    menor = 999999

    rapidos = normais = lentos = 0
    s200 = s403 = s404 = s500 = 0

    home = login = admin = produtos = 0

    ultimo_ip = ""
    cont_ip = maior_cont_ip = 0
    ip_mais_ativo = ""

    cont_500 = eventos_fc = 0

    sensiveis = falhas_sensiveis = 0

    for linha in arq:
        total += 1

        ip, status, recurso, tempo = extrairCampos(linha)

        # status
        if status == 200:
            sucessos += 1
            s200 += 1
        else:
            erros += 1

        if status == 403:
            s403 += 1
        elif status == 404:
            s404 += 1
        elif status == 500:
            s500 += 1
            erros_500 += 1

        # tempo
        soma_tempo += tempo

        if tempo > maior:
            maior = tempo
        if tempo < menor:
            menor = tempo

        if tempo < 200:
            rapidos += 1
        elif tempo < 500:
            normais += 1
        else:
            lentos += 1

        # recurso
        if recurso == "/home":
            home += 1
        elif recurso == "/login":
            login += 1
        elif recurso == "/admin":
            admin += 1
        elif recurso == "/produtos":
            produtos += 1

        # ip mais ativo
        if ip == ultimo_ip:
            cont_ip += 1
        else:
            if cont_ip > maior_cont_ip:
                maior_cont_ip = cont_ip
                ip_mais_ativo = ultimo_ip
            cont_ip = 1
            ultimo_ip = ip

        # falha crítica
        if status == 500:
            cont_500 += 1
        else:
            cont_500 = 0

        if cont_500 == 3:
            eventos_fc += 1

        # rotas sensíveis
        if recurso == "/admin" or recurso == "/backup" or recurso == "/config" or recurso == "/private":
            sensiveis += 1
            if status != 200:
                falhas_sensiveis += 1

    arq.close()

    media = soma_tempo / total
    taxa = (erros / total) * 100
    disponibilidade = (sucessos / total) * 100

    mais = "/home"
    if login > home and login > admin and login > produtos:
        mais = "/login"
    elif admin > home and admin > login and admin > produtos:
        mais = "/admin"
    elif produtos > home and produtos > login and produtos > admin:
        mais = "/produtos"

    if eventos_fc >= 1 or disponibilidade < 70:
        estado = "CRÍTICO"
    elif disponibilidade < 85:
        estado = "INSTÁVEL"
    elif disponibilidade < 95:
        estado = "ATENÇÃO"
    else:
        estado = "SAUDÁVEL"

    print("\n===== RELATÓRIO =====")
    print("Total:", total)
    print("Sucessos:", sucessos)
    print("Erros:", erros)
    print("Erros 500:", erros_500)
    print("Disponibilidade:", disponibilidade)
    print("Taxa erro:", taxa)
    print("Tempo médio:", media)
    print("Maior tempo:", maior)
    print("Menor tempo:", menor)
    print("Rápidos:", rapidos)
    print("Normais:", normais)
    print("Lentos:", lentos)
    print("200:", s200)
    print("403:", s403)
    print("404:", s404)
    print("500:", s500)
    print("Mais acessado:", mais)
    print("IP mais ativo:", ip_mais_ativo)
    print("Falhas críticas:", eventos_fc)
    print("Rotas sensíveis:", sensiveis)
    print("Falhas sensíveis:", falhas_sensiveis)
    print("Estado:", estado)

menu()
