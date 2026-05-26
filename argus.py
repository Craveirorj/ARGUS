#!/usr/bin/env python3
# ============================================================
#   ARGUS - Advanced Reconnaissance & OSINT Intelligence Suite
#   Uso exclusivamente ético e em contexto autorizado
# ============================================================

import os
import sys
import json
import subprocess
import webbrowser
import datetime
import shutil
from pathlib import Path

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.text import Text
    from rich.prompt import Prompt, Confirm
    from rich.rule import Rule
    from rich import box
    from rich.align import Align
    from rich.theme import Theme
except ImportError:
    print("[!] Instala o rich: pip3 install rich --break-system-packages")
    sys.exit(1)

# ── TEMA VERDE / PRETO ─────────────────────────────────────
argus_theme = Theme({
    "primary":   "bold green",
    "secondary": "green",
    "dim_green": "dim green",
    "accent":    "bright_green",
    "warning":   "yellow",
    "error":     "red",
    "ok":        "bold green",
    "key":       "bold bright_green",
    "desc":      "green",
    "subdesc":   "dim green",
    "separator": "dim green",
    "target":    "bold yellow",
    "web":       "green",
    "prompt":    "bold green",
})

console = Console(theme=argus_theme)

# ──────────────────────────────────────────────────────────
#  CONFIG / SESSÃO
# ──────────────────────────────────────────────────────────
CONFIG_FILE = Path.home() / ".argus_config.json"
SESSION_DIR = Path.home() / "argus_sessions"
SESSION_DIR.mkdir(exist_ok=True)

def load_config():
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE) as f:
            return json.load(f)
    return {}

def save_config(cfg):
    with open(CONFIG_FILE, "w") as f:
        json.dump(cfg, f, indent=2)

config = load_config()
session_log = []
current_target = {"domain": None, "ip": None, "username": None, "email": None,
                  "phone": None, "name": None, "nif": None}

# ──────────────────────────────────────────────────────────
#  UTILITÁRIOS
# ──────────────────────────────────────────────────────────
def clear():
    os.system("clear")

def log(action, data):
    entry = {"timestamp": datetime.datetime.now().isoformat(), "action": action, "data": data}
    session_log.append(entry)

def run_cmd(cmd, description="A executar..."):
    console.print(f"\n[primary]▶ {description}[/primary]")
    console.print(f"[dim_green]$ {cmd}[/dim_green]\n")
    log(description, cmd)
    os.system(cmd)

def open_url(url, label=""):
    console.print(f"\n[ok]🌐 A abrir:[/ok] [accent]{label or url}[/accent]")
    webbrowser.open(url)
    log("browser_open", url)

def tool_exists(tool):
    return shutil.which(tool) is not None

def require_target(field):
    val = current_target.get(field)
    if not val:
        val = Prompt.ask(f"[warning]⚠ Sem {field} definido. Introduz agora[/warning]")
        current_target[field] = val
    return val

def section_header(title, subtitle=""):
    clear()
    console.print()
    body = f"[primary]{title}[/primary]\n[dim_green]{subtitle}[/dim_green]" if subtitle else f"[primary]{title}[/primary]"
    console.print(Panel(Align.center(body), border_style="green", padding=(1, 4)))
    console.print()

def pause():
    console.print()
    Prompt.ask("[dim_green]↵ Enter para continuar[/dim_green]")

def get_api_key(service):
    key = config.get(f"api_{service}")
    if not key:
        console.print(f"[warning]⚠ Sem API key para {service}.[/warning]")
        key = Prompt.ask(f"  Introduz a tua API key de {service} (ou deixa vazio para saltar)")
        if key:
            config[f"api_{service}"] = key
            save_config(config)
    return key

def save_session():
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    target_str = "_".join(v for v in current_target.values() if v) or "sem_alvo"
    filename = SESSION_DIR / f"argus_{target_str}_{ts}.json"
    data = {"target": current_target, "log": session_log}
    with open(filename, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    console.print(f"\n[ok]✔ Sessão guardada em:[/ok] [accent]{filename}[/accent]")

def print_option(key, name, desc, req=""):
    """Imprime uma opção com nome, descrição e estado da ferramenta."""
    if key == "─":
        console.print(f"  [separator]{'─' * 60}[/separator]")
        return
    if req == "web":
        status = "[web]🌐 browser[/web]"
    elif req:
        status = "[ok]✔ instalado[/ok]" if tool_exists(req) else "[error]✗ não instalado[/error]"
    else:
        status = ""
    console.print(f"  [key][{key}][/key]  [desc]{name}[/desc]")
    console.print(f"       [subdesc]{desc}[/subdesc]  {status}")

# ──────────────────────────────────────────────────────────
#  BANNER
# ──────────────────────────────────────────────────────────
BANNER = """
[bold green]
 █████╗ ██████╗  ██████╗ ██╗   ██╗███████╗
██╔══██╗██╔══██╗██╔════╝ ██║   ██║██╔════╝
███████║██████╔╝██║  ███╗██║   ██║███████╗
██╔══██║██╔══██╗██║   ██║██║   ██║╚════██║
██║  ██║██║  ██║╚██████╔╝╚██████╔╝███████║
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝[/bold green]
[dim green]     Advanced Reconnaissance & OSINT Intelligence Suite[/dim green]
[dim green]     "O gigante de 100 olhos que tudo vê"  |  Kali Linux  |  v1.0[/dim green]
"""

def show_banner():
    clear()
    console.print(BANNER)
    console.print(Rule(style="green dim"))

# ──────────────────────────────────────────────────────────
#  DEFINIR ALVO
# ──────────────────────────────────────────────────────────
def menu_alvo():
    section_header("🎯  DEFINIR ALVO", "Define os dados do alvo desta sessão")
    fields = [
        ("domain",   "Domínio / Empresa    (ex: empresa.pt)"),
        ("ip",       "IP / Host            (ex: 192.168.1.1)"),
        ("username", "Username             (ex: joao_silva)"),
        ("email",    "Email                (ex: joao@empresa.pt)"),
        ("phone",    "Telemóvel/Telefone   (ex: +351910000000)"),
        ("name",     "Nome Completo        (ex: João Silva)"),
        ("nif",      "NIF Português        (ex: 123456789)"),
    ]
    for key, label in fields:
        val = current_target.get(key) or ""
        current_target[key] = Prompt.ask(f"  [secondary]{label}[/secondary]", default=val) or None

    console.print()
    console.print("[ok]✔ Alvo definido:[/ok]")
    for k, v in current_target.items():
        if v:
            console.print(f"  [dim_green]{k:10}[/dim_green] → [target]{v}[/target]")
    pause()

# ──────────────────────────────────────────────────────────
#  A. DOMÍNIOS / EMPRESAS / DNS
# ──────────────────────────────────────────────────────────
def menu_dominios():
    while True:
        section_header("A.  DOMÍNIOS / EMPRESAS / DNS")
        t = current_target["domain"] or "[dim]não definido[/dim]"
        console.print(f"  Alvo: [target]{t}[/target]\n")

        print_option("1", "WHOIS",              "Registo do domínio: proprietário, datas, contactos, registar", "whois")
        print_option("2", "DNS completo (dig)", "Todos os registos DNS: A, MX, NS, TXT, CNAME, SOA", "dig")
        print_option("3", "Subfinder",          "Enumeração passiva de subdomínios via OSINT", "subfinder")
        print_option("4", "Amass",              "Mapeamento avançado da superfície de ataque e subdomínios", "amass")
        print_option("5", "theHarvester",       "Recolhe emails, IPs e subdomínios de múltiplas fontes públicas", "theharvester")
        print_option("6", "DNSDumpster",        "Visualização gráfica de registos DNS e infraestrutura", "web")
        print_option("7", "DNSInspect",         "Diagnóstico completo de DNS: erros, TTL, propagação", "web")
        print_option("8", "Wayback Machine",    "Histórico de versões do site ao longo do tempo", "web")
        print_option("9", "MX / SPF / DMARC",  "Registos de email: servidor de correio e políticas anti-spam", "dig")
        print_option("A", "crt.sh – SSL certs", "Certificados SSL emitidos para o domínio (revela subdomínios)", "web")
        print_option("B", "AXFR – Zone Transfer","Tenta transferência de zona DNS para obter todos os registos", "dig")
        print_option("C", "theHarvester avançado","theHarvester com fontes e limites personalizados", "theharvester")
        print_option("0", "← Voltar",           "", "")
        console.print()

        choice = Prompt.ask("[prompt]Opção[/prompt]").strip().upper()
        d = require_target("domain") if choice != "0" else None

        if choice == "1":
            run_cmd(f"whois {d}", f"WHOIS → {d}")
        elif choice == "2":
            run_cmd(f"dig ANY {d} +noall +answer", f"DNS ANY → {d}")
        elif choice == "3":
            if tool_exists("subfinder"):
                run_cmd(f"subfinder -d {d} -silent", f"Subfinder → {d}")
            else:
                console.print("[error]subfinder não instalado: go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest[/error]")
        elif choice == "4":
            if tool_exists("amass"):
                run_cmd(f"amass enum -passive -d {d}", f"Amass → {d}")
            else:
                console.print("[error]amass não instalado: sudo apt install amass[/error]")
        elif choice == "5":
            if tool_exists("theHarvester") or tool_exists("theharvester"):
                run_cmd(f"theHarvester -d {d} -b all", f"theHarvester → {d}")
            else:
                console.print("[error]theHarvester não instalado: sudo apt install theharvester[/error]")
        elif choice == "6":
            open_url("https://dnsdumpster.com/", "DNSDumpster")
        elif choice == "7":
            open_url(f"https://www.dnsinspect.com/{d}", "DNSInspect")
        elif choice == "8":
            open_url(f"https://web.archive.org/web/*/{d}", "Wayback Machine")
        elif choice == "9":
            run_cmd(f"dig MX {d} +short && dig TXT {d} +short", f"MX/SPF/DMARC → {d}")
        elif choice == "A":
            open_url(f"https://crt.sh/?q=%25.{d}", "crt.sh SSL certs")
        elif choice == "B":
            ns = subprocess.getoutput(f"dig NS {d} +short | head -1").strip()
            if ns:
                run_cmd(f"dig AXFR {d} @{ns}", f"AXFR → {d} @ {ns}")
            else:
                console.print("[error]Não foi possível obter nameserver.[/error]")
        elif choice == "C":
            if tool_exists("theHarvester") or tool_exists("theharvester"):
                sources = Prompt.ask("Fontes (ex: google,bing,crtsh)", default="google,bing,crtsh")
                run_cmd(f"theHarvester -d {d} -b {sources} -l 500", f"theHarvester avançado → {d}")
            else:
                console.print("[error]theHarvester não instalado.[/error]")
        elif choice == "0":
            break
        else:
            console.print("[error]Opção inválida.[/error]")
        if choice != "0":
            pause()

# ──────────────────────────────────────────────────────────
#  B. PESSOAS / USERNAMES / IDENTIDADE
# ──────────────────────────────────────────────────────────
def menu_pessoas():
    while True:
        section_header("B.  PESSOAS / USERNAMES / IDENTIDADE")
        u = current_target["username"] or "[dim]não definido[/dim]"
        e = current_target["email"] or "[dim]não definido[/dim]"
        n = current_target["name"] or "[dim]não definido[/dim]"
        console.print(f"  Username: [target]{u}[/target]  |  Email: [target]{e}[/target]  |  Nome: [target]{n}[/target]\n")

        print_option("1", "Sherlock",          "Pesquisa username em mais de 300 redes sociais e sites", "sherlock")
        print_option("2", "Maigret",           "Constrói perfil completo a partir de username: foto, bio, links", "maigret")
        print_option("3", "WhatsMyName",       "Verifica presença de username em centenas de plataformas online", "web")
        print_option("4", "Holehe",            "Verifica se um email está registado em mais de 100 serviços", "holehe")
        print_option("5", "HaveIBeenPwned",    "Verifica se o email aparece em fugas de dados conhecidas", "web")
        print_option("6", "H8mail",            "Pesquisa local de emails em bases de dados de breaches", "h8mail")
        print_option("7", "Radaris",           "Background check: histórico de endereços, familiares, processos", "web")
        print_option("8", "FastPeopleSearch",  "Pesquisa de pessoas por nome, morada ou número de telefone", "web")
        print_option("9", "People Search",     "Agregador de informação pública sobre pessoas", "web")
        print_option("A", "Social Analyzer",   "Análise de perfis em redes sociais com scoring de confiança", "social-analyzer")
        print_option("B", "OSINTgram",         "Extrai seguidores, posts e metadados de perfis Instagram", "web")
        print_option("C", "Datagma",           "Enriquecimento de dados: empresa, cargo, perfis a partir de email", "web")
        print_option("D", "OSINT Industries",  "Plataforma all-in-one: email, username, telefone, IP numa só pesquisa", "web")
        print_option("E", "BehindTheName",     "Gerador de identidades fictícias para criação de personas OSINT", "web")
        print_option("0", "← Voltar",          "", "")
        console.print()

        choice = Prompt.ask("[prompt]Opção[/prompt]").strip().upper()

        if choice == "1":
            u2 = require_target("username")
            if tool_exists("sherlock"):
                run_cmd(f"sherlock {u2} --output ~/argus_sessions/sherlock_{u2}.txt", f"Sherlock → {u2}")
            else:
                console.print("[error]sherlock não instalado: pip3 install sherlock-project --break-system-packages[/error]")
        elif choice == "2":
            u2 = require_target("username")
            if tool_exists("maigret"):
                run_cmd(f"maigret {u2} --html --folderoutput ~/argus_sessions/", f"Maigret → {u2}")
            else:
                console.print("[error]maigret não instalado: pip3 install maigret --break-system-packages[/error]")
        elif choice == "3":
            open_url("https://whatsmyname.app/", "WhatsMyName")
        elif choice == "4":
            e2 = require_target("email")
            if tool_exists("holehe"):
                run_cmd(f"holehe {e2}", f"Holehe → {e2}")
            else:
                console.print("[error]holehe não instalado: pip3 install holehe --break-system-packages[/error]")
        elif choice == "5":
            e2 = require_target("email")
            open_url(f"https://haveibeenpwned.com/account/{e2}", "HaveIBeenPwned")
        elif choice == "6":
            e2 = require_target("email")
            if tool_exists("h8mail"):
                run_cmd(f"h8mail -t {e2}", f"H8mail → {e2}")
            else:
                console.print("[error]h8mail não instalado: pip3 install h8mail --break-system-packages[/error]")
        elif choice == "7":
            n2 = require_target("name")
            open_url(f"https://radaris.com/p/{n2.replace(' ', '-')}", "Radaris")
        elif choice == "8":
            n2 = require_target("name")
            open_url(f"https://fastpeoplesearch.ai/name/{n2.replace(' ', '-')}", "FastPeopleSearch")
        elif choice == "9":
            open_url("https://people-search.net/", "People Search")
        elif choice == "A":
            u2 = require_target("username")
            if tool_exists("social-analyzer"):
                run_cmd(f"social-analyzer --username {u2} --mode fast", f"Social Analyzer → {u2}")
            else:
                console.print("[error]social-analyzer não instalado: pip3 install social-analyzer --break-system-packages[/error]")
        elif choice == "B":
            open_url("https://github.com/Datalux/Osintgram", "OSINTgram GitHub")
        elif choice == "C":
            open_url("https://app.datagma.com/", "Datagma")
        elif choice == "D":
            open_url("https://app.osint.industries/", "OSINT Industries")
        elif choice == "E":
            open_url("https://www.behindthename.com/random/", "BehindTheName")
        elif choice == "0":
            break
        else:
            console.print("[error]Opção inválida.[/error]")
        if choice != "0":
            pause()

# ──────────────────────────────────────────────────────────
#  C. IPs / INFRAESTRUTURA
# ──────────────────────────────────────────────────────────
def menu_ips():
    while True:
        section_header("C.  IPs / INFRAESTRUTURA")
        ip = current_target["ip"] or "[dim]não definido[/dim]"
        console.print(f"  Alvo: [target]{ip}[/target]\n")

        print_option("1", "WHOIS de IP",          "Proprietário do bloco IP, ASN, organização e país de origem", "whois")
        print_option("2", "Nmap – scan básico",   "Scan rápido dos portos mais comuns com detecção de estado", "nmap")
        print_option("3", "Nmap – completo",      "Scan com detecção de serviços (-sC -sV): versões e scripts NSE", "nmap")
        print_option("4", "Nmap – agressivo (-A)","Scan completo com OS detection, traceroute e scripts", "nmap")
        print_option("5", "Traceroute",           "Mapa da rota de rede entre o teu host e o alvo", "traceroute")
        print_option("6", "Shodan CLI",           "Consulta informação pública do IP: portos, banners, CVEs", "shodan")
        print_option("7", "Shodan (browser)",     "Dashboard web do Shodan com histórico e detalhes do host", "web")
        print_option("8", "Censys (browser)",     "Alternativa ao Shodan: certificados, serviços e metadados", "web")
        print_option("9", "ZoomEye (browser)",    "Motor de busca de dispositivos em rede, foco em IoT/China", "web")
        print_option("A", "IPinfo.io",            "Geolocalização, ASN, operador e hostname do IP", "web")
        print_option("B", "GreyNoise",            "Verifica se o IP é scanner malicioso ou tráfego legítimo", "web")
        print_option("C", "AbuseIPDB",            "Reputação do IP: reportes de abuso, spam e ataques", "web")
        print_option("D", "VirusTotal",           "Análise do IP: malware, phishing, reputação em múltiplos engines", "web")
        print_option("0", "← Voltar",             "", "")
        console.print()

        choice = Prompt.ask("[prompt]Opção[/prompt]").strip().upper()
        ip2 = require_target("ip") if choice != "0" else None

        if choice == "1":
            run_cmd(f"whois {ip2}", f"WHOIS IP → {ip2}")
        elif choice == "2":
            run_cmd(f"nmap -T4 {ip2}", f"Nmap básico → {ip2}")
        elif choice == "3":
            run_cmd(f"nmap -sC -sV -T4 {ip2}", f"Nmap completo → {ip2}")
        elif choice == "4":
            run_cmd(f"nmap -A -T4 {ip2}", f"Nmap agressivo → {ip2}")
        elif choice == "5":
            run_cmd(f"traceroute {ip2}", f"Traceroute → {ip2}")
        elif choice == "6":
            key = get_api_key("shodan")
            if key and tool_exists("shodan"):
                run_cmd(f"shodan init {key} && shodan host {ip2}", f"Shodan CLI → {ip2}")
            elif not tool_exists("shodan"):
                console.print("[error]shodan CLI não instalado: pip3 install shodan --break-system-packages[/error]")
        elif choice == "7":
            open_url(f"https://www.shodan.io/host/{ip2}", "Shodan web")
        elif choice == "8":
            open_url(f"https://search.censys.io/hosts/{ip2}", "Censys")
        elif choice == "9":
            open_url(f"https://www.zoomeye.org/searchResult?q={ip2}", "ZoomEye")
        elif choice == "A":
            open_url(f"https://ipinfo.io/{ip2}", "IPinfo")
        elif choice == "B":
            open_url(f"https://www.greynoise.io/viz/ip/{ip2}", "GreyNoise")
        elif choice == "C":
            open_url(f"https://www.abuseipdb.com/check/{ip2}", "AbuseIPDB")
        elif choice == "D":
            open_url(f"https://www.virustotal.com/gui/ip-address/{ip2}", "VirusTotal")
        elif choice == "0":
            break
        else:
            console.print("[error]Opção inválida.[/error]")
        if choice != "0":
            pause()

# ──────────────────────────────────────────────────────────
#  D. REDES SOCIAIS
# ──────────────────────────────────────────────────────────
def menu_social():
    while True:
        section_header("D.  REDES SOCIAIS")
        u = current_target["username"] or "[dim]não definido[/dim]"
        console.print(f"  Username: [target]{u}[/target]\n")

        print_option("1", "Sherlock",         "Pesquisa username em mais de 300 plataformas sociais", "sherlock")
        print_option("2", "Maigret",          "Perfil completo: foto, bio, links cruzados entre plataformas", "maigret")
        print_option("3", "WhatsMyName",      "Interface web para verificar presença em redes sociais", "web")
        print_option("4", "Twitter / X",      "Pesquisa avançada de tweets e perfil público do utilizador", "web")
        print_option("5", "Instagram",        "Acesso directo ao perfil público do utilizador", "web")
        print_option("6", "Facebook",         "Pesquisa de nome, posts públicos e perfis associados", "web")
        print_option("7", "LinkedIn",         "Pesquisa profissional: cargo, empresa, conexões", "web")
        print_option("8", "TikTok",           "Perfil público com vídeos e informação do utilizador", "web")
        print_option("9", "Twint",            "Scraping de tweets sem API: histórico, menções, localização", "twint")
        print_option("A", "OSINTgram",        "Extrai dados de perfis Instagram: seguidores, geotags, hashtags", "web")
        print_option("B", "Reddit",           "Histórico de posts e comentários do utilizador no Reddit", "web")
        print_option("C", "GitHub",           "Perfil, repositórios públicos e actividade de desenvolvimento", "web")
        print_option("0", "← Voltar",         "", "")
        console.print()

        choice = Prompt.ask("[prompt]Opção[/prompt]").strip().upper()

        if choice == "1":
            u2 = require_target("username")
            if tool_exists("sherlock"):
                run_cmd(f"sherlock {u2} --output ~/argus_sessions/sherlock_{u2}.txt", f"Sherlock → {u2}")
            else:
                console.print("[error]sherlock não instalado: pip3 install sherlock-project --break-system-packages[/error]")
        elif choice == "2":
            u2 = require_target("username")
            if tool_exists("maigret"):
                run_cmd(f"maigret {u2} --html --folderoutput ~/argus_sessions/", f"Maigret → {u2}")
            else:
                console.print("[error]maigret não instalado: pip3 install maigret --break-system-packages[/error]")
        elif choice == "3":
            open_url("https://whatsmyname.app/", "WhatsMyName")
        elif choice == "4":
            u2 = require_target("username")
            open_url(f"https://twitter.com/search?q=from%3A{u2}&src=typed_query", "Twitter/X")
        elif choice == "5":
            u2 = require_target("username")
            open_url(f"https://www.instagram.com/{u2}/", "Instagram")
        elif choice == "6":
            u2 = require_target("username")
            open_url(f"https://www.facebook.com/search/top?q={u2}", "Facebook")
        elif choice == "7":
            u2 = require_target("username")
            open_url(f"https://www.linkedin.com/search/results/all/?keywords={u2}", "LinkedIn")
        elif choice == "8":
            u2 = require_target("username")
            open_url(f"https://www.tiktok.com/@{u2}", "TikTok")
        elif choice == "9":
            u2 = require_target("username")
            if tool_exists("twint"):
                run_cmd(f"twint -u {u2} -o ~/argus_sessions/twint_{u2}.json --json", f"Twint → {u2}")
            else:
                console.print("[error]twint não instalado: pip3 install twint --break-system-packages[/error]")
        elif choice == "A":
            open_url("https://github.com/Datalux/Osintgram", "OSINTgram GitHub")
        elif choice == "B":
            u2 = require_target("username")
            open_url(f"https://www.reddit.com/user/{u2}/", "Reddit")
        elif choice == "C":
            u2 = require_target("username")
            open_url(f"https://github.com/{u2}", "GitHub")
        elif choice == "0":
            break
        else:
            console.print("[error]Opção inválida.[/error]")
        if choice != "0":
            pause()

# ──────────────────────────────────────────────────────────
#  E. EQUIPAMENTOS / IoT / SHODAN
# ──────────────────────────────────────────────────────────
def menu_equipamentos():
    while True:
        section_header("E.  EQUIPAMENTOS / IoT / SHODAN")
        console.print("  [dim_green]Pesquisa de dispositivos expostos na internet: câmeras, routers, ICS/SCADA[/dim_green]\n")

        print_option("1", "Shodan – query personalizada", "Pesquisa livre no Shodan via CLI com qualquer filtro", "shodan")
        print_option("2", "Shodan – câmeras IP (PT)",     "Lista câmeras IP expostas em Portugal sem autenticação", "web")
        print_option("3", "Shodan – routers (PT)",        "Routers e gateways com portos abertos em Portugal", "web")
        print_option("4", "Shodan – ICS/SCADA",           "Sistemas industriais e infra-estruturas críticas expostas", "web")
        print_option("5", "Shodan – Portugal completo",   "Todos os dispositivos indexados pelo Shodan em Portugal", "web")
        print_option("6", "Censys – serviços e certs",    "Pesquisa de certificados SSL, serviços e metadados de hosts", "web")
        print_option("7", "ZoomEye – IoT",                "Motor de busca focado em IoT e dispositivos embedded", "web")
        print_option("8", "WiGLE – redes Wi-Fi",          "Mapa global de redes Wi-Fi detectadas por war driving", "web")
        print_option("9", "GPSJam",                       "Interferência GPS em tempo real: zonas afectadas no mapa", "web")
        print_option("A", "Shodan – CVEs de um IP",       "Lista vulnerabilidades CVE conhecidas associadas ao IP", "shodan")
        print_option("B", "Shodan – por organização",     "Todos os activos expostos de uma empresa ou ASN específico", "web")
        print_option("C", "FOFA",                         "Alternativa ao Shodan: motor de busca de activos de rede", "web")
        print_option("0", "← Voltar",                     "", "")
        console.print()

        choice = Prompt.ask("[prompt]Opção[/prompt]").strip().upper()

        if choice == "1":
            key = get_api_key("shodan")
            if key and tool_exists("shodan"):
                query = Prompt.ask("  Query Shodan (ex: port:22 country:PT)")
                run_cmd(f"shodan init {key} && shodan search \"{query}\"", f"Shodan search → {query}")
            elif not tool_exists("shodan"):
                console.print("[error]shodan CLI não instalado: pip3 install shodan --break-system-packages[/error]")
        elif choice == "2":
            open_url("https://www.shodan.io/search?query=webcam+country%3APT", "Shodan câmeras PT")
        elif choice == "3":
            open_url("https://www.shodan.io/search?query=router+country%3APT", "Shodan routers PT")
        elif choice == "4":
            open_url("https://www.shodan.io/search?query=tag%3Aics+country%3APT", "Shodan ICS/SCADA")
        elif choice == "5":
            open_url("https://www.shodan.io/search?query=country%3APT", "Shodan Portugal")
        elif choice == "6":
            open_url("https://search.censys.io/", "Censys")
        elif choice == "7":
            open_url("https://www.zoomeye.org/", "ZoomEye")
        elif choice == "8":
            open_url("https://wigle.net/", "WiGLE")
        elif choice == "9":
            open_url("https://gpsjam.org/", "GPSJam")
        elif choice == "A":
            ip2 = require_target("ip")
            key = get_api_key("shodan")
            if key and tool_exists("shodan"):
                run_cmd(f"shodan init {key} && shodan host {ip2} --history", f"Shodan CVEs → {ip2}")
        elif choice == "B":
            org = Prompt.ask("  Nome da organização ou ASN")
            open_url(f"https://www.shodan.io/search?query=org%3A%22{org.replace(' ', '+')}%22", f"Shodan org → {org}")
        elif choice == "C":
            open_url("https://fofa.info/", "FOFA")
        elif choice == "0":
            break
        else:
            console.print("[error]Opção inválida.[/error]")
        if choice != "0":
            pause()

# ──────────────────────────────────────────────────────────
#  F. TELEFONE / IDENTIFICAÇÃO
# ──────────────────────────────────────────────────────────
def menu_telefone():
    while True:
        section_header("F.  TELEFONE / IDENTIFICAÇÃO")
        ph = current_target["phone"] or "[dim]não definido[/dim]"
        console.print(f"  Número: [target]{ph}[/target]\n")

        print_option("1", "Truecaller",     "Identificação de número: nome do proprietário e operadora", "web")
        print_option("2", "Sync.me",        "Lookup reverso: identifica quem está por trás de um número", "web")
        print_option("3", "SpyDialer",      "Informação pública associada a número de telefone (EUA/Int'l)", "web")
        print_option("4", "PhoneInfoga",    "OSINT completo de número: operadora, localização, redes sociais", "phoneinfoga")
        print_option("5", "NumVerify",      "Validação e informação técnica do número: formato, país, tipo", "web")
        print_option("0", "← Voltar",       "", "")
        console.print()

        choice = Prompt.ask("[prompt]Opção[/prompt]").strip().upper()

        if choice == "1":
            ph2 = require_target("phone")
            open_url(f"https://www.truecaller.com/search/pt/{ph2.replace('+', '')}", "Truecaller")
        elif choice == "2":
            open_url("https://sync.me/", "Sync.me")
        elif choice == "3":
            open_url("https://www.spydialer.com/", "SpyDialer")
        elif choice == "4":
            ph2 = require_target("phone")
            if tool_exists("phoneinfoga"):
                run_cmd(f"phoneinfoga scan -n \"{ph2}\"", f"PhoneInfoga → {ph2}")
            else:
                console.print("[error]phoneinfoga não instalado. Ver: https://github.com/sundowndev/phoneinfoga[/error]")
                open_url("https://github.com/sundowndev/phoneinfoga", "PhoneInfoga GitHub")
        elif choice == "5":
            open_url("https://numverify.com/", "NumVerify")
        elif choice == "0":
            break
        else:
            console.print("[error]Opção inválida.[/error]")
        if choice != "0":
            pause()

# ──────────────────────────────────────────────────────────
#  G. GEOLOCALIZAÇÃO / MAPAS
# ──────────────────────────────────────────────────────────
def menu_geo():
    while True:
        section_header("G.  GEOLOCALIZAÇÃO / MAPAS")

        print_option("1",  "Google Earth",   "Vista de satélite 3D de qualquer ponto do globo", "web")
        print_option("2",  "Google Maps",    "Mapas, Street View e coordenadas GPS detalhadas", "web")
        print_option("3",  "Apple Maps",     "Alternativa da Apple com dados de trânsito em tempo real", "web")
        print_option("4",  "Bing Maps",      "Mapas aéreos e de satélite da Microsoft", "web")
        print_option("5",  "WiGLE",          "Mapa de redes Wi-Fi e Bluetooth detectadas globalmente", "web")
        print_option("6",  "GPSJam",         "Zonas com interferência e spoofing de GPS em tempo real", "web")
        print_option("7",  "SunCalc",        "Calcula ângulo e posição do sol para geolocalização por sombras", "web")
        print_option("8",  "OpenStreetMap",  "Mapa open-source colaborativo com dados de infraestrutura", "web")
        print_option("9",  "Geohints",       "Ferramenta para identificar localização através de imagens", "web")
        print_option("A",  "What3Words",     "Sistema de localização precisa em quadrados de 3x3 metros", "web")
        print_option("B",  "ExifTool – GPS", "Extrai coordenadas GPS e metadados de localização de imagens", "exiftool")
        print_option("0",  "← Voltar",       "", "")
        console.print()

        choice = Prompt.ask("[prompt]Opção[/prompt]").strip().upper()

        if choice == "1":
            open_url("https://earth.google.com/web/", "Google Earth")
        elif choice == "2":
            open_url("https://maps.google.com/", "Google Maps")
        elif choice == "3":
            open_url("https://maps.apple.com/", "Apple Maps")
        elif choice == "4":
            open_url("https://www.bing.com/maps/", "Bing Maps")
        elif choice == "5":
            open_url("https://wigle.net/", "WiGLE")
        elif choice == "6":
            open_url("https://gpsjam.org/", "GPSJam")
        elif choice == "7":
            open_url("https://www.suncalc.org/", "SunCalc")
        elif choice == "8":
            open_url("https://www.openstreetmap.org/", "OpenStreetMap")
        elif choice == "9":
            open_url("https://geohints.com/", "Geohints")
        elif choice == "A":
            open_url("https://what3words.com/", "What3Words")
        elif choice == "B":
            filepath = Prompt.ask("  Caminho para a imagem (ex: /home/kali/foto.jpg)")
            if tool_exists("exiftool"):
                run_cmd(f"exiftool '{filepath}' | grep -i gps", f"ExifTool GPS → {filepath}")
            else:
                console.print("[error]exiftool não instalado: sudo apt install libimage-exiftool-perl[/error]")
        elif choice == "0":
            break
        else:
            console.print("[error]Opção inválida.[/error]")
        if choice != "0":
            pause()

# ──────────────────────────────────────────────────────────
#  H. PORTUGAL ESPECÍFICO
# ──────────────────────────────────────────────────────────
def menu_portugal():
    while True:
        section_header("H.  🇵🇹  PORTUGAL ESPECÍFICO")
        nif = current_target["nif"] or "[dim]não definido[/dim]"
        console.print(f"  NIF: [target]{nif}[/target]\n")

        print_option("1", "Lookup NIF",          "Consulta dados públicos associados a um NIF português", "web")
        print_option("2", "Validar CC",          "Valida número de Cartão de Cidadão português", "web")
        print_option("3", "Ubikron",             "Pesquisa de pessoas em Portugal: nome, morada, telefone", "web")
        print_option("4", "Registo Comercial",   "Publicações oficiais do Ministério da Justiça: empresas e actos", "web")
        print_option("5", "RACIUS",              "Base de dados de empresas portuguesas: sede, CAE, capital", "web")
        print_option("6", "Transparência.pt",    "Financiamentos públicos, subsídios e contratos do Estado PT", "web")
        print_option("0", "← Voltar",            "", "")
        console.print()

        choice = Prompt.ask("[prompt]Opção[/prompt]").strip().upper()

        if choice == "1":
            nif2 = require_target("nif")
            open_url(f"https://nif.marcosantos.me/?i={nif2}", "NIF lookup PT")
        elif choice == "2":
            open_url("https://cc.marcosantos.me/", "CC Validação")
        elif choice == "3":
            n2 = require_target("name")
            open_url(f"https://www.ubikron.com/search?q={n2.replace(' ', '+')}", "Ubikron")
        elif choice == "4":
            open_url("https://publicacoes.mj.pt/", "Registo Comercial")
        elif choice == "5":
            d2 = require_target("domain")
            open_url(f"https://www.racius.com/pesquisa/?pesquisa={d2}", "RACIUS")
        elif choice == "6":
            open_url("https://www.transparencia.pt/", "Transparência.pt")
        elif choice == "0":
            break
        else:
            console.print("[error]Opção inválida.[/error]")
        if choice != "0":
            pause()

# ──────────────────────────────────────────────────────────
#  I. GOOGLE DORKS
# ──────────────────────────────────────────────────────────
def menu_dorks():
    while True:
        section_header("I.  GOOGLE DORKS / HACKING DATABASE")
        d = current_target["domain"] or ""

        print_option("1",  "Exploit-DB GHDB",       "Base de dados oficial de Google Dorks categorizados por tipo", "web")
        print_option("2",  "DorkGPT",               "Gera dorks personalizados com inteligência artificial", "web")
        print_option("3",  "DorkSearch Pro",         "Motor de pesquisa dedicado a dorks: filtra por categoria", "web")
        print_option("4",  "Ficheiros expostos",     "Encontra PDFs, DOCs e XLS públicos no domínio alvo", "web")
        print_option("5",  "Painéis de login",       "Descobre páginas de login, admin e painéis de controlo", "web")
        print_option("6",  "Directórios expostos",   "Encontra directórios sem index com listagem de ficheiros", "web")
        print_option("7",  "Ficheiros de config",    "Localiza ficheiros .env, .config e credenciais expostas", "web")
        print_option("8",  "Câmeras/webcams",        "Dorks específicos para encontrar câmeras de vigilância abertas", "web")
        print_option("9",  "Erros SQL",              "Páginas com erros de base de dados que revelam estrutura", "web")
        print_option("A",  "Emails no domínio",      "Lista endereços de email indexados de um domínio específico", "web")
        print_option("B",  "Subdomínios via Google", "Descobre subdomínios através de pesquisa no Google", "web")
        print_option("C",  "Dork personalizado",     "Introduz e executa o teu próprio Google Dork", "web")
        print_option("0",  "← Voltar",               "", "")
        console.print()

        choice = Prompt.ask("[prompt]Opção[/prompt]").strip().upper()
        base = "https://www.google.com/search?q="

        if choice == "1":
            open_url("https://www.exploit-db.com/google-hacking-database", "Google Hacking Database")
        elif choice == "2":
            open_url("https://www.dorkgpt.com/", "DorkGPT")
        elif choice == "3":
            open_url("https://dorksearch.pro/", "DorkSearch Pro")
        elif choice == "4":
            site = f"site:{d} " if d else ""
            open_url(base + f"{site}filetype:pdf OR filetype:doc OR filetype:xls OR filetype:xlsx", "Dork ficheiros")
        elif choice == "5":
            site = f"site:{d} " if d else ""
            open_url(base + f"{site}inurl:login OR inurl:admin OR inurl:painel", "Dork login")
        elif choice == "6":
            site = f"site:{d} " if d else ""
            open_url(base + f"{site}intitle:index.of", "Dork directórios")
        elif choice == "7":
            site = f"site:{d} " if d else ""
            open_url(base + f"{site}filetype:env OR filetype:config OR inurl:.env", "Dork config")
        elif choice == "8":
            open_url(base + "inurl:/view/index.shtml OR inurl:ViewerFrame?Mode=", "Dork câmeras")
        elif choice == "9":
            site = f"site:{d} " if d else ""
            open_url(base + f"{site}intext:\"sql syntax\" OR intext:\"mysql_fetch\"", "Dork SQL errors")
        elif choice == "A":
            d2 = require_target("domain")
            open_url(base + f"site:{d2} intext:\"@{d2}\"", f"Dork emails {d2}")
        elif choice == "B":
            d2 = require_target("domain")
            open_url(base + f"site:*.{d2}", f"Dork subdomínios {d2}")
        elif choice == "C":
            custom = Prompt.ask("  Introduz o teu dork")
            open_url(base + custom.replace(" ", "+"), "Dork personalizado")
        elif choice == "0":
            break
        else:
            console.print("[error]Opção inválida.[/error]")
        if choice != "0":
            pause()

# ──────────────────────────────────────────────────────────
#  J. METADADOS / ARQUIVOS / HISTÓRICO
# ──────────────────────────────────────────────────────────
def menu_metadados():
    while True:
        section_header("J.  METADADOS / ARQUIVOS / HISTÓRICO")

        print_option("1", "ExifTool",          "Extrai metadados de qualquer ficheiro: GPS, autor, software, datas", "exiftool")
        print_option("2", "Wayback Machine",   "Acede a versões arquivadas de qualquer URL ao longo do tempo", "web")
        print_option("3", "Arquivo.pt",        "Arquivo histórico da web portuguesa mantido pela FCCN", "web")
        print_option("4", "Newspaper Archive", "Pesquisa em jornais históricos digitalizados de todo o mundo", "web")
        print_option("5", "Google Cache",      "Versão em cache do Google de uma página web específica", "web")
        print_option("6", "ODCrawler",         "Crawler de domínios .onion na Dark Web para OSINT", "web")
        print_option("7", "Waybackurls",       "Extrai todos os URLs históricos de um domínio do Wayback Machine", "waybackurls")
        print_option("0", "← Voltar",          "", "")
        console.print()

        choice = Prompt.ask("[prompt]Opção[/prompt]").strip().upper()

        if choice == "1":
            filepath = Prompt.ask("  Caminho para o ficheiro")
            if tool_exists("exiftool"):
                run_cmd(f"exiftool '{filepath}'", f"ExifTool → {filepath}")
            else:
                console.print("[error]exiftool não instalado: sudo apt install libimage-exiftool-perl[/error]")
        elif choice == "2":
            url = Prompt.ask("  URL", default=f"https://{current_target['domain']}" if current_target['domain'] else "")
            open_url(f"https://web.archive.org/web/*/{url}", "Wayback Machine")
        elif choice == "3":
            open_url("https://arquivo.pt/", "Arquivo.pt")
        elif choice == "4":
            open_url("https://newspaperarchive.com/search/", "Newspaper Archive")
        elif choice == "5":
            url = Prompt.ask("  URL")
            open_url(f"https://webcache.googleusercontent.com/search?q=cache:{url}", "Google Cache")
        elif choice == "6":
            open_url("https://odcrawler.xyz/", "ODCrawler .onion")
        elif choice == "7":
            d2 = require_target("domain")
            if tool_exists("waybackurls"):
                run_cmd(f"waybackurls {d2} | tee ~/argus_sessions/waybackurls_{d2}.txt", f"Waybackurls → {d2}")
            else:
                console.print("[error]waybackurls não instalado: go install github.com/tomnomnom/waybackurls@latest[/error]")
        elif choice == "0":
            break
        else:
            console.print("[error]Opção inválida.[/error]")
        if choice != "0":
            pause()

# ──────────────────────────────────────────────────────────
#  K. BREACHES / SEGURANÇA
# ──────────────────────────────────────────────────────────
def menu_breaches():
    while True:
        section_header("K.  BREACHES / FUGAS DE DADOS")
        e = current_target["email"] or "[dim]não definido[/dim]"
        console.print(f"  Email: [target]{e}[/target]\n")

        print_option("1", "HaveIBeenPwned – email",   "Verifica se o email aparece em fugas de dados conhecidas", "web")
        print_option("2", "HaveIBeenPwned – domínio", "Lista todos os emails comprometidos de um domínio", "web")
        print_option("3", "H8mail",                   "Pesquisa email em múltiplas bases de dados de breaches locais", "h8mail")
        print_option("4", "Holehe",                   "Confirma em que serviços online o email está registado", "holehe")
        print_option("5", "IntelX",                   "Motor de busca de dados vazados: emails, IPs, domínios, hashes", "web")
        print_option("6", "DeHashed",                 "Base de dados de credenciais comprometidas com pesquisa avançada", "web")
        print_option("7", "LeakIX",                   "Indexa serviços vulneráveis e fugas de dados em tempo real", "web")
        print_option("0", "← Voltar",                 "", "")
        console.print()

        choice = Prompt.ask("[prompt]Opção[/prompt]").strip().upper()

        if choice == "1":
            e2 = require_target("email")
            open_url(f"https://haveibeenpwned.com/account/{e2}", "HIBP email")
        elif choice == "2":
            open_url("https://haveibeenpwned.com/DomainSearch", "HIBP domínio")
        elif choice == "3":
            e2 = require_target("email")
            if tool_exists("h8mail"):
                run_cmd(f"h8mail -t {e2}", f"H8mail → {e2}")
            else:
                console.print("[error]h8mail não instalado: pip3 install h8mail --break-system-packages[/error]")
        elif choice == "4":
            e2 = require_target("email")
            if tool_exists("holehe"):
                run_cmd(f"holehe {e2}", f"Holehe → {e2}")
            else:
                console.print("[error]holehe não instalado: pip3 install holehe --break-system-packages[/error]")
        elif choice == "5":
            open_url("https://intelx.io/", "IntelX")
        elif choice == "6":
            open_url("https://dehashed.com/", "DeHashed")
        elif choice == "7":
            open_url("https://leakix.net/", "LeakIX")
        elif choice == "0":
            break
        else:
            console.print("[error]Opção inválida.[/error]")
        if choice != "0":
            pause()

# ──────────────────────────────────────────────────────────
#  L. RECURSOS / REFERÊNCIAS
# ──────────────────────────────────────────────────────────
def menu_recursos():
    while True:
        section_header("L.  RECURSOS / REFERÊNCIAS OSINT")

        print_option("1", "OSINT Framework",       "Mapa visual interactivo de centenas de ferramentas OSINT", "web")
        print_option("2", "Bellingcat Toolkit",     "Toolkit investigativo usado por jornalistas e analistas OSINT", "web")
        print_option("3", "OSINT Combine",          "Colecção curada de ferramentas e técnicas OSINT combinadas", "web")
        print_option("4", "My OSINT Training",      "Plataforma de aprendizagem prática com exercícios reais", "web")
        print_option("5", "District4Labs",          "Plataforma profissional de inteligência e análise OSINT", "web")
        print_option("6", "Kagi",                   "Motor de busca privado sem rastreio: útil para OSINT neutro", "web")
        print_option("7", "FlightAware",            "Rastreio de voos em tempo real: rota, altitude, operador", "web")
        print_option("8", "MarineTraffic",          "Rastreio de embarcações em tempo real: posição AIS global", "web")
        print_option("9", "OpenCorporates",         "Base de dados global de empresas: registo, directores, filiais", "web")
        print_option("A", "EDGAR – SEC",            "Registos obrigatórios de empresas cotadas nos EUA", "web")
        print_option("B", "WeLiveSecurity – Dorks", "Artigo sobre Google Hacking: como usar dorks eficazmente", "web")
        print_option("0", "← Voltar",               "", "")
        console.print()

        choice = Prompt.ask("[prompt]Opção[/prompt]").strip().upper()

        urls = {
            "1": ("https://osintframework.com/", "OSINT Framework"),
            "2": ("https://bellingcat.gitbook.io/toolkit", "Bellingcat Toolkit"),
            "3": ("https://www.osintcombine.com/", "OSINT Combine"),
            "4": ("https://smart.myosint.training/", "My OSINT Training"),
            "5": ("https://www.district4labs.com/", "District4Labs"),
            "6": ("https://kagi.com/", "Kagi"),
            "7": ("https://flightaware.com/", "FlightAware"),
            "8": ("https://www.marinetraffic.com/", "MarineTraffic"),
            "9": ("https://opencorporates.com/", "OpenCorporates"),
            "A": ("https://www.sec.gov/edgar/search/", "EDGAR"),
            "B": ("https://www.welivesecurity.com/br/2021/07/30/google-hacking-verifique-quais-informacoes-sobre-voce-ou-sua-empresa-aparecem-nos-resultados/", "WeLiveSecurity Dorks"),
        }
        if choice in urls:
            open_url(*urls[choice])
            pause()
        elif choice == "0":
            break
        else:
            console.print("[error]Opção inválida.[/error]")

# ──────────────────────────────────────────────────────────
#  M. CONFIGURAÇÕES / API KEYS
# ──────────────────────────────────────────────────────────
def menu_config():
    section_header("M.  CONFIGURAÇÕES / API KEYS")
    console.print("  [dim_green]As API keys ficam guardadas em ~/.argus_config.json[/dim_green]\n")

    services = [
        ("shodan",         "Shodan",         "Necessária para shodan CLI e queries avançadas"),
        ("censys_id",      "Censys UID",     "ID de acesso à API Censys"),
        ("censys_secret",  "Censys Secret",  "Secret da API Censys"),
        ("hibp",           "HaveIBeenPwned", "Necessária para queries programáticas HIBP"),
        ("zoomeye",        "ZoomEye",        "Acesso à API do ZoomEye"),
    ]
    for key_id, label, hint in services:
        current = config.get(f"api_{key_id}", "")
        masked = ("*" * (len(current) - 4) + current[-4:]) if len(current) > 4 else ("*" * len(current))
        display = masked if current else "[dim]não definida[/dim]"
        console.print(f"  [secondary]{label:20}[/secondary]  {display}  [dim_green]# {hint}[/dim_green]")

    console.print()
    if Confirm.ask("  Queres actualizar alguma API key?"):
        for key_id, label, _ in services:
            val = Prompt.ask(f"  {label} (Enter para manter)", default=config.get(f"api_{key_id}", ""))
            if val:
                config[f"api_{key_id}"] = val
        save_config(config)
        console.print("[ok]✔ Configurações guardadas.[/ok]")
    pause()

# ──────────────────────────────────────────────────────────
#  MENU PRINCIPAL
# ──────────────────────────────────────────────────────────
def menu_principal():
    while True:
        show_banner()

        # Alvo activo
        alvos_activos = {k: v for k, v in current_target.items() if v}
        if alvos_activos:
            t = Table(box=box.SIMPLE, show_header=False, padding=(0, 2))
            for k, v in alvos_activos.items():
                t.add_row(f"[dim_green]{k}[/dim_green]", f"[target]{v}[/target]")
            console.print(Panel(t, title="[bold green]🎯 Alvo Activo[/bold green]", border_style="green dim", padding=(0, 2)))
        else:
            console.print(Panel("[dim_green]Sem alvo definido. Usa [T] para definir.[/dim_green]",
                                border_style="green dim", padding=(0, 2)))

        console.print()

        menus = [
            ("T", "Definir Alvo",                    "Configura domínio, IP, username, email, telefone, nome e NIF"),
            ("─", "", ""),
            ("A", "Domínios / Empresas / DNS",        "WHOIS, dig, subfinder, amass, theHarvester, crt.sh"),
            ("B", "Pessoas / Usernames / Identidade", "Sherlock, Maigret, Holehe, H8mail, Radaris, OSINT Industries"),
            ("C", "IPs / Infraestrutura",             "Nmap, WHOIS IP, Shodan, Censys, AbuseIPDB, VirusTotal"),
            ("D", "Redes Sociais",                    "Twitter, Instagram, Facebook, LinkedIn, TikTok, Reddit"),
            ("E", "Equipamentos / IoT / Shodan",      "Shodan queries, câmeras, routers, ICS/SCADA, WiGLE, GPSJam"),
            ("F", "Telefone / Identificação",         "Truecaller, Sync.me, SpyDialer, PhoneInfoga"),
            ("G", "Geolocalização / Mapas",           "Google Earth, WiGLE, GPSJam, SunCalc, ExifTool GPS"),
            ("H", "🇵🇹 Portugal Específico",           "NIF lookup, CC, Ubikron, RACIUS, Transparência.pt"),
            ("I", "Google Dorks",                     "GHDB, DorkGPT, dorks automáticos por categoria"),
            ("J", "Metadados / Arquivos / Histórico", "ExifTool, Wayback Machine, Arquivo.pt, ODCrawler"),
            ("K", "Breaches / Fugas de Dados",        "HIBP, H8mail, Holehe, IntelX, DeHashed, LeakIX"),
            ("L", "Recursos / Referências",           "OSINT Framework, Bellingcat, FlightAware, MarineTraffic"),
            ("─", "", ""),
            ("M", "Configurações / API Keys",         "Shodan, Censys, HIBP, ZoomEye"),
            ("S", "Guardar Sessão",                   "Exporta o log completo da sessão para JSON"),
            ("0", "Sair",                             ""),
        ]

        for key, label, hint in menus:
            if key == "─":
                console.print(f"  [separator]{'─' * 58}[/separator]")
            elif key == "0":
                console.print(f"  [key][{key}][/key]  [desc]{label}[/desc]")
            else:
                console.print(f"  [key][{key}][/key]  [desc]{label}[/desc]  [subdesc]{hint}[/subdesc]")

        console.print()
        choice = Prompt.ask("[bold green]ARGUS ▶[/bold green]").strip().upper()

        dispatch = {
            "T": menu_alvo,
            "A": menu_dominios,
            "B": menu_pessoas,
            "C": menu_ips,
            "D": menu_social,
            "E": menu_equipamentos,
            "F": menu_telefone,
            "G": menu_geo,
            "H": menu_portugal,
            "I": menu_dorks,
            "J": menu_metadados,
            "K": menu_breaches,
            "L": menu_recursos,
            "M": menu_config,
        }

        if choice in dispatch:
            dispatch[choice]()
        elif choice == "S":
            save_session()
            pause()
        elif choice == "0":
            if Confirm.ask("\n  Guardar sessão antes de sair?"):
                save_session()
            console.print("\n[bold green]ARGUS[/bold green] [dim_green]encerrado. Stay ethical.[/dim_green]\n")
            sys.exit(0)
        else:
            console.print("[error]Opção inválida.[/error]")

# ──────────────────────────────────────────────────────────
#  ENTRY POINT
# ──────────────────────────────────────────────────────────
if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        console.print("\n\n[bold green]ARGUS[/bold green] [dim_green]interrompido.[/dim_green]\n")
        sys.exit(0)
