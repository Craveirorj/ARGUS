# 👁️ ARGUS
### Advanced Reconnaissance & OSINT Intelligence Suite

> *"O gigante de 100 olhos que tudo vê"*

![Python](https://img.shields.io/badge/Python-3.8%2B-brightgreen?style=flat-square&logo=python)
![Platform](https://img.shields.io/badge/Platform-Kali%20Linux-brightgreen?style=flat-square&logo=linux)
![License](https://img.shields.io/badge/License-MIT-brightgreen?style=flat-square)
![OSINT](https://img.shields.io/badge/Category-OSINT-brightgreen?style=flat-square)
![Files](https://img.shields.io/badge/Ficheiros-1-brightgreen?style=flat-square)

---

## 📌 Descrição

**ARGUS** é uma ferramenta OSINT de linha de comando desenvolvida para **Kali Linux**, com interface interactiva em menu. Centraliza num **único ficheiro Python** mais de **80 técnicas e recursos OSINT** organizados por categoria, desde reconhecimento de domínios e infraestrutura até pesquisa de pessoas, equipamentos IoT, geolocalização e fugas de dados.

A ferramenta **instala automaticamente** a sua única dependência (`rich`) na primeira execução — não é necessária nenhuma configuração prévia.

Desenvolvida para uso exclusivamente **ético e em contexto autorizado** — testes de segurança, investigação académica, CTF e certificações de cibersegurança.

---

## ✨ Funcionalidades

- 📄 **Ficheiro único** — apenas `argus.py`, sem dependências externas a instalar manualmente
- 🔧 **Auto-instalação** — instala o `rich` automaticamente na primeira execução
- 🎯 **Alvo persistente** — define uma vez, usado automaticamente em todos os módulos
- 🌐 **13 módulos OSINT** com navegação por letras e números
- 🖥️ **Ferramentas CLI integradas** — execução directa no terminal com detecção automática
- 🌍 **Recursos web** — abre no browser com o alvo pré-preenchido no URL
- 💾 **Sessões JSON** — registo completo de todas as acções guardado automaticamente
- ⚙️ **Gestão de API keys** — Shodan, Censys, HIBP, ZoomEye guardadas em config local
- 🎨 **Interface verde/preto** com descrição de cada ferramenta e estado de instalação
- 🇵🇹 **Módulo Portugal** — NIF, CC, Ubikron, RACIUS, Transparência.pt
- `[?]` **Estado das ferramentas** — lista todas as CLI com indicação de instaladas ou em falta

---

## 📋 Módulos

| Tecla | Módulo | Ferramentas / Recursos |
|-------|--------|------------------------|
| `T` | 🎯 Definir Alvo | Domínio, IP, Username, Email, Telefone, Nome, NIF |
| `A` | 🌐 Domínios / Empresas / DNS | WHOIS, dig, subfinder, amass, theHarvester, DNSDumpster, crt.sh, AXFR |
| `B` | 👤 Pessoas / Usernames | Sherlock, Maigret, Holehe, H8mail, Radaris, OSINT Industries, Datagma |
| `C` | 🖥️ IPs / Infraestrutura | Nmap, WHOIS IP, Shodan CLI, Censys, GreyNoise, AbuseIPDB, VirusTotal |
| `D` | 📱 Redes Sociais | Sherlock, Maigret, Twitter, Instagram, Facebook, LinkedIn, TikTok, Reddit |
| `E` | 📡 Equipamentos / IoT | Shodan queries, câmeras, routers, ICS/SCADA, WiGLE, GPSJam, FOFA |
| `F` | 📞 Telefone | Truecaller, Sync.me, SpyDialer, PhoneInfoga, NumVerify |
| `G` | 🗺️ Geolocalização | Google Earth, WiGLE, GPSJam, SunCalc, ExifTool GPS, What3Words |
| `H` | 🇵🇹 Portugal | NIF lookup, CC, Ubikron, Registo Comercial, RACIUS, Transparência.pt |
| `I` | 🔍 Google Dorks | Exploit-DB GHDB, DorkGPT, DorkSearch, dorks automáticos por categoria |
| `J` | 🗂️ Metadados / Arquivos | ExifTool, Wayback Machine, Arquivo.pt, ODCrawler, Waybackurls |
| `K` | 🔐 Breaches | HaveIBeenPwned, H8mail, Holehe, IntelX, DeHashed, LeakIX |
| `L` | 📚 Recursos | OSINT Framework, Bellingcat Toolkit, FlightAware, MarineTraffic, EDGAR |
| `M` | ⚙️ Configurações | API keys: Shodan, Censys, HIBP, ZoomEye |
| `?` | 🔧 Estado das Ferramentas | Lista todas as CLI com estado instalado/em falta e comandos de instalação |
| `S` | 💾 Guardar Sessão | Exporta log JSON completo para `~/argus_sessions/` |

---

## ⚙️ Requisitos

### Sistema operativo
- **Kali Linux** (recomendado) — todas as ferramentas CLI disponíveis via `apt`
- Ubuntu / Debian — compatível, algumas ferramentas requerem instalação manual

### Python
```
Python 3.8 ou superior
```

### Dependências
> **Nenhuma instalação manual necessária.**
> O ARGUS detecta e instala automaticamente a biblioteca `rich` na primeira execução.

---

## 🚀 Instalação e Execução

O ARGUS é um **ficheiro único**. Basta clonar e executar:

```bash
# 1. Clonar o repositório
git clone https://github.com/teu-username/argus.git
cd argus

# 2. Dar permissões de execução
chmod +x argus.py

# 3. Executar
python3 argus.py
```

Na primeira execução, se a biblioteca `rich` não estiver instalada, o ARGUS instala-a automaticamente e reinicia.

---

## 📄 Ficheiros do Repositório

```
argus/
├── argus.py     ← ferramenta completa (ficheiro único)
└── README.md    ← documentação
```

Ficheiros criados automaticamente pelo ARGUS (fora do repositório):
```
~/.argus_config.json    ← API keys guardadas localmente
~/argus_sessions/       ← sessões OSINT exportadas em JSON
```

---

## 🛠️ Ferramentas CLI — Instalação Opcional

O ARGUS detecta automaticamente quais ferramentas estão instaladas — mostra `✔` nas disponíveis e `✗` nas em falta. Usa **`[?]` no menu** para ver o estado completo com os comandos de instalação.

Instala apenas as que precisas:

### Via apt (Kali / Debian)
```bash
sudo apt install nmap theharvester amass libimage-exiftool-perl whois traceroute
```

### Via pip3
```bash
pip3 install sherlock-project maigret holehe h8mail shodan social-analyzer twint --break-system-packages
```

### Via Go
```bash
# Subfinder — enumeração passiva de subdomínios
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

# Waybackurls — URLs históricos do Wayback Machine
go install github.com/tomnomnom/waybackurls@latest
```

### Instalação manual
- **PhoneInfoga** — https://github.com/sundowndev/phoneinfoga
- **OSINTgram** — https://github.com/Datalux/Osintgram

---

## 🔑 API Keys

Algumas ferramentas requerem API keys. Configura-as dentro do ARGUS em **`[M] Configurações`** — ficam guardadas em `~/.argus_config.json`.

| Serviço | Onde obter | Plano gratuito |
|---------|-----------|----------------|
| **Shodan** | https://account.shodan.io/ | Limitado |
| **Censys** | https://censys.io/register | Sim |
| **HaveIBeenPwned** | https://haveibeenpwned.com/API/Key | Pago |
| **ZoomEye** | https://www.zoomeye.org/profile | Sim |

---

## 🖥️ Argumentos de Linha de Comando

```bash
python3 argus.py             # lança normalmente
python3 argus.py --status    # mostra estado de todas as ferramentas CLI
python3 argus.py --help      # mostra ajuda rápida
```

---

## 📖 Fluxo Típico de Investigação

```
1. Inicia o ARGUS
   python3 argus.py

2. Define o alvo [T]
   → Domínio: empresa.pt
   → IP: 192.168.1.100
   → Username: joao_silva
   → Email: joao@empresa.pt

3. Reconhecimento de domínio [A]
   → WHOIS, DNS completo, subfinder, theHarvester, crt.sh

4. Infraestrutura [C]
   → Nmap completo (-sC -sV), Shodan, Censys, AbuseIPDB

5. Pesquisa de pessoas [B]
   → Sherlock, Maigret, Holehe, OSINT Industries

6. Google Dorks [I]
   → Ficheiros expostos, painéis de login, configurações

7. Verifica breaches [K]
   → HaveIBeenPwned, DeHashed, IntelX

8. Guarda sessão [S]
   → JSON completo em ~/argus_sessions/
```

### Navegação
- Introduz a **letra ou número** da opção e prime `Enter`
- O alvo definido em **`[T]`** é usado automaticamente em todos os módulos
- **`[?]`** mostra quais ferramentas CLI estão instaladas e os comandos para instalar as que faltam
- Os recursos web abrem no browser com o alvo pré-preenchido no URL sempre que possível

---

## 📸 Preview

```
 █████╗ ██████╗  ██████╗ ██╗   ██╗███████╗
██╔══██╗██╔══██╗██╔════╝ ██║   ██║██╔════╝
███████║██████╔╝██║  ███╗██║   ██║███████╗
██╔══██║██╔══██╗██║   ██║██║   ██║╚════██║
██║  ██║██║  ██║╚██████╔╝╚██████╔╝███████║
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝

     Advanced Reconnaissance & OSINT Intelligence Suite
     "O gigante de 100 olhos que tudo vê"  |  Kali Linux  |  v1.0

──────────────────────────────────────────────────────────────

  [T]  Definir Alvo                  Configura domínio, IP, username, email...
  ──────────────────────────────────────────────────────────────
  [A]  Domínios / Empresas / DNS     WHOIS, dig, subfinder, amass, theHarvester
  [B]  Pessoas / Usernames           Sherlock, Maigret, Holehe, H8mail, Radaris
  [C]  IPs / Infraestrutura          Nmap, Shodan, Censys, AbuseIPDB, VirusTotal
  [D]  Redes Sociais                 Twitter, Instagram, Facebook, LinkedIn...
  [E]  Equipamentos / IoT / Shodan   Shodan queries, câmeras, routers, ICS/SCADA
  [F]  Telefone / Identificação      Truecaller, Sync.me, SpyDialer, PhoneInfoga
  [G]  Geolocalização / Mapas        Google Earth, WiGLE, GPSJam, SunCalc
  [H]  Portugal Específico           NIF, CC, Ubikron, RACIUS, Transparência.pt
  [I]  Google Dorks                  GHDB, DorkGPT, dorks automáticos
  [J]  Metadados / Arquivos          ExifTool, Wayback Machine, Arquivo.pt
  [K]  Breaches / Fugas de Dados     HIBP, H8mail, Holehe, IntelX, DeHashed
  [L]  Recursos / Referências        OSINT Framework, Bellingcat, FlightAware
  ──────────────────────────────────────────────────────────────
  [M]  Configurações / API Keys      Shodan, Censys, HIBP, ZoomEye
  [?]  Estado das Ferramentas CLI    Verifica quais ferramentas estão instaladas
  [S]  Guardar Sessão                Exporta o log completo da sessão para JSON
  [0]  Sair

ARGUS ▶
```

---

## ⚠️ Aviso Legal

Esta ferramenta é disponibilizada **exclusivamente para fins educativos, académicos e de investigação de segurança autorizada**.

- ✅ Testes em sistemas **próprios** ou com **autorização expressa**
- ✅ Contexto académico e certificações (CEH, OSCP, eJPT, etc.)
- ✅ CTF — Capture The Flag
- ❌ Uso não autorizado em sistemas de terceiros
- ❌ Actividades ilegais de qualquer natureza

O autor não se responsabiliza por qualquer uso indevido desta ferramenta. **O utilizador é o único responsável pelas suas acções.**

---

## 👤 Autor

Desenvolvido como ferramenta de apoio ao estudo de **cibersegurança e OSINT**.

---

## 📄 Licença

MIT License — livre para usar, modificar e distribuir com atribuição.
