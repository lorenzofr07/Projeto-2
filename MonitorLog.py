import random
import datetime

#NOMES: LORENZO FERREIRA RODRIGUES
        #GUILHERME SALES
        #WANDERSON LIMA

# =========================
# MENU
# =========================

def menu():
    nome_arquivo = "log.txt"

    while True:
        print("\n===== MENU =====")
        print("1 - Gerar logs")
        print("2 - Analisar logs")
        print("3 - Gerar e analisar logs")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                quantidade = int(input("Quantidade de logs: "))
                gerar_arquivo_logs(nome_arquivo, quantidade)
            except:
                print("Entrada inválida.")

        elif opcao == "2":
            analisar_arquivo_logs(nome_arquivo)

        elif opcao == "3":
            try:
                quantidade = int(input("Quantidade de logs: "))
                gerar_arquivo_logs(nome_arquivo, quantidade)
                analisar_arquivo_logs(nome_arquivo)
            except:
                print("Entrada inválida.")

        elif opcao == "4":
            print("Encerrando o sistema.")
            break

        else:
            print("Opção inválida.")


# =========================
# GERAÇÃO DOS LOGS
# =========================

def gerar_arquivo_logs(nome_arquivo, quantidade):
    with open(nome_arquivo, "w", encoding="utf-8") as arq:
        for i in range(quantidade):
            linha = montar_log(i)
            arq.write(linha + "\n")

    print("Arquivo gerado com sucesso.")


def montar_log(indice):
    data_hora = gerar_data_hora(indice)
    ip = gerar_ip(indice)
    recurso = gerar_recurso(indice)
    metodo = gerar_metodo(recurso)
    status = gerar_status(indice, recurso)
    tempo = gerar_tempo_resposta(indice, status)
    tamanho = gerar_tamanho(status, recurso)
    protocolo = gerar_protocolo(indice)
    user_agent = gerar_user_agent(indice)
    referer = gerar_referer(recurso)

    linha = "[" + data_hora + "] " + ip + " - " + metodo + " - " + str(status)
    linha = linha + " - " + recurso + " - " + str(tempo) + "ms"
    linha = linha + " - " + str(tamanho) + "B - " + protocolo
    linha = linha + " - " + user_agent + " - " + referer

    return linha


def gerar_data_hora(indice):
    base = datetime.datetime.now()
    delta = datetime.timedelta(seconds=indice * random.randint(3, 10))
    return (base + delta).strftime("%d/%m/%Y %H:%M:%S")


def gerar_ip(indice):
    # força bruta
    if indice >= 20 and indice <= 24:
        return "203.120.45.7"

    # sequência do mesmo ip para simular bot
    elif indice >= 70 and indice <= 75:
        return "177.88.10.9"

    n = random.randint(1, 6)

    if n == 1:
        return "192.168.0.12"
    elif n == 2:
        return "192.168.0.15"
    elif n == 3:
        return "10.0.0.8"
    elif n == 4:
        return "172.16.5.4"
    elif n == 5:
        return "201.10.1.20"
    else:
        return "189.44.3.9"


def gerar_recurso(indice):
    if indice >= 20 and indice <= 24:
        return "/login"
    elif indice >= 40 and indice <= 43:
        return "/admin"
    elif indice >= 50 and indice <= 53:
        return "/pagina-inexistente"
    elif indice >= 60 and indice <= 62:
        return "/api"
    elif indice >= 70 and indice <= 71:
        return "/backup"
    elif indice >= 72 and indice <= 73:
        return "/config"
    elif indice >= 74 and indice <= 75:
        return "/private"

    n = random.randint(1, 6)

    if n == 1:
        return "/home"
    elif n == 2:
        return "/produtos"
    elif n == 3:
        return "/contato"
    elif n == 4:
        return "/sobre"
    elif n == 5:
        return "/login"
    else:
        return "/carrinho"


def gerar_metodo(recurso):
    if recurso == "/login":
        return "POST"
    elif recurso == "/api":
        return "POST"
    elif recurso == "/admin":
        return "GET"
    else:
        n = random.randint(1, 2)
        if n == 1:
            return "GET"
        else:
            return "POST"


def gerar_status(indice, recurso):
    if indice >= 20 and indice <= 24 and recurso == "/login":
        return 403
    elif indice >= 40 and indice <= 43 and recurso == "/admin":
        return 403
    elif indice >= 50 and indice <= 53:
        return 404
    elif indice >= 60 and indice <= 62:
        return 500
    elif indice >= 70 and indice <= 75:
        if indice % 2 == 0:
            return 403
        else:
            return 200

    n = random.randint(1, 10)

    if n <= 7:
        return 200
    elif n == 8:
        return 403
    elif n == 9:
        return 404
    else:
        return 500


def gerar_tempo_resposta(indice, status):
    # trecho para degradação de desempenho
    if indice == 30:
        return 120
    elif indice == 31:
        return 240
    elif indice == 32:
        return 390
    elif indice == 33:
        return 700

    if status == 500:
        return random.randint(900, 1800)
    elif status == 404:
        return random.randint(150, 500)
    elif status == 403:
        return random.randint(100, 450)
    else:
        return random.randint(80, 850)


def gerar_tamanho(status, recurso):
    if status == 404:
        return random.randint(200, 700)
    elif status == 500:
        return random.randint(300, 900)
    elif recurso == "/home":
        return random.randint(1500, 3500)
    elif recurso == "/produtos":
        return random.randint(2500, 6000)
    elif recurso == "/login":
        return random.randint(500, 1200)
    elif recurso == "/admin":
        return random.randint(600, 1400)
    else:
        return random.randint(700, 2500)


def gerar_protocolo(indice):
    n = random.randint(1, 3)

    if n == 1:
        return "HTTP/1.0"
    elif n == 2:
        return "HTTP/1.1"
    else:
        return "HTTP/2"


def gerar_user_agent(indice):
    if indice >= 70 and indice <= 72:
        return "GoogleBot"
    elif indice >= 73 and indice <= 75:
        return "CrawlerX"

    n = random.randint(1, 5)

    if n == 1:
        return "Chrome"
    elif n == 2:
        return "Firefox"
    elif n == 3:
        return "Edge"
    elif n == 4:
        return "Safari"
    else:
        return "Opera"


def gerar_referer(recurso):
    if recurso == "/home":
        return "/"
    elif recurso == "/produtos":
        return "/home"
    elif recurso == "/login":
        return "/home"
    elif recurso == "/carrinho":
        return "/produtos"
    elif recurso == "/contato":
        return "/home"
    else:
        return "/home"


# =========================
# EXTRAÇÃO MANUAL
# =========================

def ler_ate(texto, inicio, marcador):
    parte = ""
    i = inicio

    while i < len(texto):
        if texto[i:i + len(marcador)] == marcador:
            return parte, i + len(marcador)
        parte = parte + texto[i]
        i = i + 1

    return parte, i


def extrair_campos_linha(linha):
    linha = linha.strip()

    if len(linha) == 0:
        return None

    if linha[0] != "[":
        return None

    pos_fecha = linha.find("]")
    if pos_fecha == -1:
        return None

    data_hora = linha[1:pos_fecha]
    resto = linha[pos_fecha + 2:]

    ip, pos = ler_ate(resto, 0, " - ")
    metodo, pos = ler_ate(resto, pos, " - ")
    status, pos = ler_ate(resto, pos, " - ")
    recurso, pos = ler_ate(resto, pos, " - ")
    tempo, pos = ler_ate(resto, pos, "ms - ")
    tamanho, pos = ler_ate(resto, pos, "B - ")
    protocolo, pos = ler_ate(resto, pos, " - ")
    user_agent, pos = ler_ate(resto, pos, " - ")
    referer = resto[pos:]

    return data_hora, ip, metodo, int(status), recurso, int(tempo), int(tamanho), protocolo, user_agent, referer


# =========================
# CLASSIFICAÇÕES
# =========================

def classificar_tempo(tempo):
    if tempo < 200:
        return "rapido"
    elif tempo < 800:
        return "normal"
    else:
        return "lento"


def classificar_estado_final(disponibilidade, falhas_criticas, acessos_lentos, suspeitas_bot):
    if falhas_criticas >= 1 or disponibilidade < 70:
        return "CRÍTICO"
    elif disponibilidade < 85 or acessos_lentos >= 10:
        return "INSTÁVEL"
    elif disponibilidade < 95 or suspeitas_bot > 0:
        return "ATENÇÃO"
    else:
        return "SAUDÁVEL"


# =========================
# CONTAGEM MANUAL DE RECURSOS
# =========================

def contar_recurso(recurso, home, produtos, contato, sobre, login, carrinho, admin, api, pagina, backup, config, private):
    if recurso == "/home":
        home = home + 1
    elif recurso == "/produtos":
        produtos = produtos + 1
    elif recurso == "/contato":
        contato = contato + 1
    elif recurso == "/sobre":
        sobre = sobre + 1
    elif recurso == "/login":
        login = login + 1
    elif recurso == "/carrinho":
        carrinho = carrinho + 1
    elif recurso == "/admin":
        admin = admin + 1
    elif recurso == "/api":
        api = api + 1
    elif recurso == "/pagina-inexistente":
        pagina = pagina + 1
    elif recurso == "/backup":
        backup = backup + 1
    elif recurso == "/config":
        config = config + 1
    elif recurso == "/private":
        private = private + 1

    return home, produtos, contato, sobre, login, carrinho, admin, api, pagina, backup, config, private


def descobrir_recurso_mais_acessado(home, produtos, contato, sobre, login, carrinho, admin, api, pagina, backup, config, private):
    nome = "/home"
    maior = home

    if produtos > maior:
        maior = produtos
        nome = "/produtos"
    if contato > maior:
        maior = contato
        nome = "/contato"
    if sobre > maior:
        maior = sobre
        nome = "/sobre"
    if login > maior:
        maior = login
        nome = "/login"
    if carrinho > maior:
        maior = carrinho
        nome = "/carrinho"
    if admin > maior:
        maior = admin
        nome = "/admin"
    if api > maior:
        maior = api
        nome = "/api"
    if pagina > maior:
        maior = pagina
        nome = "/pagina-inexistente"
    if backup > maior:
        maior = backup
        nome = "/backup"
    if config > maior:
        maior = config
        nome = "/config"
    if private > maior:
        maior = private
        nome = "/private"

    return nome


# =========================
# CONTAGEM MANUAL DE IPS
# =========================

def contar_ip(ip, ip1, c1, ip2, c2, ip3, c3, ip4, c4, ip5, c5, ip6, c6, ip7, c7, ip8, c8):
    if ip == ip1:
        c1 = c1 + 1
    elif ip == ip2:
        c2 = c2 + 1
    elif ip == ip3:
        c3 = c3 + 1
    elif ip == ip4:
        c4 = c4 + 1
    elif ip == ip5:
        c5 = c5 + 1
    elif ip == ip6:
        c6 = c6 + 1
    elif ip == ip7:
        c7 = c7 + 1
    elif ip == ip8:
        c8 = c8 + 1

    return c1, c2, c3, c4, c5, c6, c7, c8


def descobrir_ip_mais_ativo(ip1, c1, ip2, c2, ip3, c3, ip4, c4, ip5, c5, ip6, c6, ip7, c7, ip8, c8):
    nome = ip1
    maior = c1

    if c2 > maior:
        maior = c2
        nome = ip2
    if c3 > maior:
        maior = c3
        nome = ip3
    if c4 > maior:
        maior = c4
        nome = ip4
    if c5 > maior:
        maior = c5
        nome = ip5
    if c6 > maior:
        maior = c6
        nome = ip6
    if c7 > maior:
        maior = c7
        nome = ip7
    if c8 > maior:
        maior = c8
        nome = ip8

    return nome


# =========================
# ANÁLISE DOS LOGS
# =========================

def analisar_arquivo_logs(nome_arquivo):
    try:
        arq = open(nome_arquivo, "r", encoding="utf-8")
    except:
        print("Arquivo não encontrado.")
        return

    total_acessos = 0
    total_sucessos = 0
    total_erros = 0
    total_erros_criticos = 0

    soma_tempos = 0
    maior_tempo = -1
    menor_tempo = -1

    qtd_rapidos = 0
    qtd_normais = 0
    qtd_lentos = 0

    qtd_200 = 0
    qtd_403 = 0
    qtd_404 = 0
    qtd_500 = 0

    # contagem manual de recursos
    r_home = 0
    r_produtos = 0
    r_contato = 0
    r_sobre = 0
    r_login = 0
    r_carrinho = 0
    r_admin = 0
    r_api = 0
    r_pagina = 0
    r_backup = 0
    r_config = 0
    r_private = 0

    # ips conhecidos da geração
    ip1 = "192.168.0.12"
    ip2 = "192.168.0.15"
    ip3 = "10.0.0.8"
    ip4 = "172.16.5.4"
    ip5 = "201.10.1.20"
    ip6 = "189.44.3.9"
    ip7 = "203.120.45.7"
    ip8 = "177.88.10.9"

    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    c7 = 0
    c8 = 0

    e1 = 0
    e2 = 0
    e3 = 0
    e4 = 0
    e5 = 0
    e6 = 0
    e7 = 0
    e8 = 0

    eventos_forca_bruta = 0
    ultimo_ip_forca_bruta = "Nenhum"

    acessos_admin_indevidos = 0
    eventos_degradacao = 0
    eventos_falha_critica = 0

    suspeitas_bot = 0
    ultimo_ip_suspeito = "Nenhum"

    acessos_rotas_sensiveis = 0
    falhas_rotas_sensiveis = 0

    ip_login_403_anterior = ""
    seq_login_403 = 0

    t1 = -1
    t2 = -1
    t3 = -1
    t4 = -1

    seq_500 = 0

    ip_anterior = ""
    seq_mesmo_ip = 0

    for linha in arq:
        dados = extrair_campos_linha(linha)

        if dados is None:
            continue

        data_hora, ip, metodo, status, recurso, tempo, tamanho, protocolo, user_agent, referer = dados

        total_acessos = total_acessos + 1

        if status == 200:
            total_sucessos = total_sucessos + 1
        else:
            total_erros = total_erros + 1

        if status == 500:
            total_erros_criticos = total_erros_criticos + 1

        soma_tempos = soma_tempos + tempo

        if maior_tempo == -1 or tempo > maior_tempo:
            maior_tempo = tempo

        if menor_tempo == -1 or tempo < menor_tempo:
            menor_tempo = tempo

        classe = classificar_tempo(tempo)

        if classe == "rapido":
            qtd_rapidos = qtd_rapidos + 1
        elif classe == "normal":
            qtd_normais = qtd_normais + 1
        else:
            qtd_lentos = qtd_lentos + 1

        if status == 200:
            qtd_200 = qtd_200 + 1
        elif status == 403:
            qtd_403 = qtd_403 + 1
        elif status == 404:
            qtd_404 = qtd_404 + 1
        elif status == 500:
            qtd_500 = qtd_500 + 1

        r_home, r_produtos, r_contato, r_sobre, r_login, r_carrinho, r_admin, r_api, r_pagina, r_backup, r_config, r_private = contar_recurso(
            recurso, r_home, r_produtos, r_contato, r_sobre, r_login, r_carrinho, r_admin, r_api, r_pagina, r_backup, r_config, r_private
        )

        c1, c2, c3, c4, c5, c6, c7, c8 = contar_ip(ip, ip1, c1, ip2, c2, ip3, c3, ip4, c4, ip5, c5, ip6, c6, ip7, c7, ip8, c8)

        if status != 200:
            e1, e2, e3, e4, e5, e6, e7, e8 = contar_ip(ip, ip1, e1, ip2, e2, ip3, e3, ip4, e4, ip5, e5, ip6, e6, ip7, e7, ip8, e8)

        # força bruta
        if recurso == "/login" and status == 403:
            if ip == ip_login_403_anterior:
                seq_login_403 = seq_login_403 + 1
            else:
                ip_login_403_anterior = ip
                seq_login_403 = 1
        else:
            ip_login_403_anterior = ""
            seq_login_403 = 0

        if seq_login_403 == 3:
            eventos_forca_bruta = eventos_forca_bruta + 1
            ultimo_ip_forca_bruta = ip

        # acesso indevido ao admin
        if recurso == "/admin" and status != 200:
            acessos_admin_indevidos = acessos_admin_indevidos + 1

        # degradação de desempenho
        t1 = t2
        t2 = t3
        t3 = t4
        t4 = tempo

        if t1 != -1 and t2 != -1 and t3 != -1 and t4 != -1:
            if t1 < t2 and t2 < t3 and t3 < t4:
                eventos_degradacao = eventos_degradacao + 1

        # falha crítica
        if status == 500:
            seq_500 = seq_500 + 1
        else:
            seq_500 = 0

        if seq_500 == 3:
            eventos_falha_critica = eventos_falha_critica + 1

        # suspeita por user agent
        if "Bot" in user_agent or "Crawler" in user_agent or "Spider" in user_agent:
            suspeitas_bot = suspeitas_bot + 1
            ultimo_ip_suspeito = ip

        # suspeita por mesmo ip repetido
        if ip == ip_anterior:
            seq_mesmo_ip = seq_mesmo_ip + 1
        else:
            ip_anterior = ip
            seq_mesmo_ip = 1

        if seq_mesmo_ip == 5:
            suspeitas_bot = suspeitas_bot + 1
            ultimo_ip_suspeito = ip

        # rotas sensíveis
        if recurso == "/admin" or recurso == "/backup" or recurso == "/config" or recurso == "/private":
            acessos_rotas_sensiveis = acessos_rotas_sensiveis + 1
            if status != 200:
                falhas_rotas_sensiveis = falhas_rotas_sensiveis + 1

    arq.close()

    if total_acessos > 0:
        disponibilidade = (total_sucessos / total_acessos) * 100
        taxa_erro = (total_erros / total_acessos) * 100
        tempo_medio = soma_tempos / total_acessos
    else:
        disponibilidade = 0
        taxa_erro = 0
        tempo_medio = 0

    recurso_mais_acessado = descobrir_recurso_mais_acessado(
        r_home, r_produtos, r_contato, r_sobre, r_login, r_carrinho, r_admin, r_api, r_pagina, r_backup, r_config, r_private
    )

    ip_mais_ativo = descobrir_ip_mais_ativo(ip1, c1, ip2, c2, ip3, c3, ip4, c4, ip5, c5, ip6, c6, ip7, c7, ip8, c8)
    ip_com_mais_erros = descobrir_ip_mais_ativo(ip1, e1, ip2, e2, ip3, e3, ip4, e4, ip5, e5, ip6, e6, ip7, e7, ip8, e8)

    estado_final = classificar_estado_final(disponibilidade, eventos_falha_critica, qtd_lentos, suspeitas_bot)

    print("\n========== RELATÓRIO FINAL ==========")
    print("Total de acessos:", total_acessos)
    print("Total de sucessos:", total_sucessos)
    print("Total de erros:", total_erros)
    print("Total de erros críticos:", total_erros_criticos)
    print("Disponibilidade do sistema: {:.2f}%".format(disponibilidade))
    print("Taxa de erro: {:.2f}%".format(taxa_erro))
    print("Tempo médio de resposta: {:.2f} ms".format(tempo_medio))
    print("Maior tempo de resposta:", maior_tempo, "ms")
    print("Menor tempo de resposta:", menor_tempo, "ms")
    print("Quantidade de acessos rápidos:", qtd_rapidos)
    print("Quantidade de acessos normais:", qtd_normais)
    print("Quantidade de acessos lentos:", qtd_lentos)
    print("Quantidade de status 200:", qtd_200)
    print("Quantidade de status 403:", qtd_403)
    print("Quantidade de status 404:", qtd_404)
    print("Quantidade de status 500:", qtd_500)
    print("Recurso mais acessado:", recurso_mais_acessado)
    print("IP mais ativo:", ip_mais_ativo)
    print("IP com mais erros:", ip_com_mais_erros)
    print("Total de eventos de força bruta:", eventos_forca_bruta)
    print("Último IP com força bruta detectada:", ultimo_ip_forca_bruta)
    print("Total de acessos indevidos ao /admin:", acessos_admin_indevidos)
    print("Total de eventos de degradação de desempenho:", eventos_degradacao)
    print("Total de eventos de falha crítica:", eventos_falha_critica)
    print("Total de suspeitas de bot:", suspeitas_bot)
    print("Último IP suspeito de bot:", ultimo_ip_suspeito)
    print("Total de acessos a rotas sensíveis:", acessos_rotas_sensiveis)
    print("Total de falhas em rotas sensíveis:", falhas_rotas_sensiveis)
    print("Estado final do sistema:", estado_final)
    print("====================================")


menu()