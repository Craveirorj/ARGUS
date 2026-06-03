# 👁️ ARGUS
### Advanced Reconnaissance & OSINT Intelligence Suite

> *"O gigante de 100 olhos que tudo vê"*

![Python](https://img.shields.io/badge/Python-3.8%2B-brightgreen?style=flat-square&logo=python)
![Platform](https://img.shields.io/badge/Platform-Kali%20Linux-brightgreen?style=flat-square&logo=linux)
![License](https://img.shields.io/badge/License-MIT-brightgreen?style=flat-square)
![OSINT](https://img.shields.io/badge/Category-OSINT-brightgreen?style=flat-square)
![Files](https://img.shields.io/badge/Ficheiros-1-brightgreen?style=flat-square)
![Tools](https://img.shields.io/badge/Ferramentas-100%2B-brightgreen?style=flat-square)

---

## 📌 Descrição

**ARGUS** é uma ferramenta OSINT de linha de comando desenvolvida para **Kali Linux**, com interface interactiva em menu. Centraliza num **único ficheiro Python** mais de **100 técnicas e recursos OSINT** organizados por categoria, desde reconhecimento de domínios e infraestrutura até pesquisa de pessoas, equipamentos IoT, geolocalização, fugas de dados e OPSEC.

A ferramenta **instala automaticamente** qualquer dependência em falta — sem sair do menu, sem reboot, sem configuração prévia.

Desenvolvida para uso exclusivamente **ético e em contexto autorizado** — testes de segurança, investigação académica, CTF e certificações de cibersegurança.

---

## ✨ Funcionalidades

- 📄 **Ficheiro único** — apenas `argus.py`, sem dependências a instalar manualmente
- 🔧 **Auto-instalação inteligente** — instala qualquer ferramenta em falta sem sair do ARGUS, corrige o PATH automaticamente e continua sem reboot
- 🎯 **Alvo persistente** — define uma vez por campo (domínio, IP, username, email, telefone, nome, NIF), guardado automaticamente entre sessões
- 🔄 **Carregamento automático** — o último alvo é carregado ao arrancar o ARGUS
- 🌐 **14 módulos OSINT** com navegação por letras e números
- 🖥️ **Ferramentas CLI integradas** — execução directa no terminal com detecção automática
- 🌍 **Recursos web** — abre no browser com o alvo pré-preenchido no URL
- 💾 **Sessões JSON** — registo completo de todas as acções guardado em `~/argus_sessions/`
- ⚙️ **Gestão de API keys** — Shodan, Censys, HIBP, ZoomEye guardadas em `~/.argus_config.json`
- 🎨 **Interface verde/preto** com descrição de cada ferramenta e estado de instalação
- 🇵🇹 **Módulo Portugal** — NIF, CC, Ubikron, RACIUS, Transparência.pt
- 🛡️ **Módulo OPSEC** — DeviceInfo.me, BrowserLeaks, IPLeak, DNSLeakTest, Tor Check, emails temporários
- `[?]` **Estado das ferramentas** — lista todas as CLI com indicação instaladas/em falta

---

## 📋 Módulos

| Tecla | Módulo | Ferramentas / Recursos |
|-------|--------|------------------------|
| `T` | 🎯 Definir Alvo | Domínio, IP, Username, Email, Telefone, Nome, NIF — guardado automaticamente |
| `A` | 🌐 Domínios / Empresas / DNS | WHOIS, dig, subfinder, amass, theHarvester, **dnsx**, **httpx**, **gowitness**, **metagoofil**, crt.sh, AXFR |
| `B` | 👤 Pessoas / Usernames | Maigret, OSINT Industries, Datagma, **Spokeo**, **BeenVerified**, **TruthFinder**, **Intelius**, **Social Catfish**, **CocoFinder**, Radaris, Pipl |
| `C` | 🖥️ IPs / Infraestrutura | Nmap, **Masscan**, **RustScan**, Shodan CLI+web, Censys, BGP.tools, GreyNoise, AbuseIPDB, VirusTotal |
| `D` | 📱 Redes Sociais | Sherlock, WhatsMyName, Social Analyzer, **Instaloader**, Twitter, Instagram, Facebook, LinkedIn, TikTok, Reddit |
| `E` | 📡 Equipamentos / IoT | Shodan queries+dashboard, câmeras, routers, ICS/SCADA, WiGLE, GPSJam, FOFA, **BinaryEdge**, **Onyphe** |
| `F` | 📞 Telefone | Truecaller, Sync.me, SpyDialer, PhoneInfoga, NumVerify |
| `G` | 🗺️ Geolocalização | Google Earth, WiGLE, GPSJam, SunCalc, ExifTool GPS, What3Words, OpenStreetMap |
| `H` | 🇵🇹 Portugal | NIF lookup, CC, Ubikron, Registo Comercial, RACIUS, Transparência.pt |
| `I` | 🔍 Google Dorks | Exploit-DB GHDB, DorkGPT, DorkSearch, dorks automáticos por categoria |
| `J` | 🗂️ Metadados / Arquivos | ExifTool, Wayback Machine, Arquivo.pt, ODCrawler, Waybackurls |
| `K` | 🔐 Breaches | HaveIBeenPwned, H8mail, Holehe, IntelX, DeHashed, LeakIX |
| `L` | 📚 Recursos / Ferramentas | Maltego, **Spiderfoot CLI**, **Recon-ng CLI**, OSINT Framework, Bellingcat, Hunter.io, BuiltWith, Wappalyzer, **Awesome OSINT Arsenal** |
| `M` | ⚙️ Configurações | API keys: Shodan, Censys, HIBP, ZoomEye |
| `N` | 🛡️ OPSEC / Anonimato | **DeviceInfo.me**, BrowserLeaks, CoverYourTracks (EFF), AmIUnique, IPLeak, DNSLeakTest, Mullvad Check, Tor Check, Temp Mail |
| `?` | 🔧 Estado das Ferramentas | Lista todas as CLI com estado instalado/em falta e comando de instalação automática |
| `S` | 💾 Guardar Sessão | Exporta log JSON completo para `~/argus_sessions/` |

---

## ⚙️ Requisitos

### Sistema operativo
- **Kali Linux** (recomendado) — todas as ferramentas CLI disponíveis via `apt`
- Ubuntu / Debian — compatível

### Python
```
Python 3.8 ou superior
```

### Dependências
> **Nenhuma instalação manual necessária.**
> O ARGUS detecta e instala automaticamente qualquer ferramenta em falta quando a seleccionas no menu.

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
~/.argus_config.json    ← API keys e último alvo guardados localmente
~/argus_sessions/       ← sessões OSINT exportadas em JSON
```

---

## 🔧 Auto-Instalação de Ferramentas

Quando seleccionas uma opção cuja ferramenta CLI não está instalada, o ARGUS trata de tudo automaticamente:

```
⚠ subfinder não está instalado.
  Comando: go install github.com/projectdiscovery/subfinder/...
  Instalar agora? [s/n]: s

▶ A instalar subfinder...
  [instalação corre aqui sem sair do ARGUS]

A verificar instalação...
✔ subfinder instalado e disponível! A continuar...
```

O ARGUS procura a ferramenta em múltiplos locais (`~/.local/bin`, `~/go/bin`, `/usr/bin`, etc.) e corrige o PATH automaticamente para a sessão actual — **sem reboot, sem reiniciar o ARGUS**.

| Método | Ferramentas |
|--------|-------------|
| `sudo apt install` | sherlock, h8mail, amass, nmap, theharvester, metagoofil, masscan, exiftool, traceroute, whois |
| `pipx install` | maigret, holehe, social-analyzer |
| `pip3 install` | shodan, rustscan, instaloader, spiderfoot, recon-ng |
| `go install` | subfinder, dnsx, httpx, gowitness, waybackurls |
| Manual (abre browser) | phoneinfoga, maltego |

---

## 🎯 Alvo Persistente

O ARGUS guarda o alvo automaticamente — não precisas de reintroduzir os dados a cada sessão.

```
🎯 DEFINIR ALVO

  💾 Último alvo guardado: domain=empresa.pt, ip=192.168.1.1

  [1]  Domínio / Empresa    empresa.pt       (ex: empresa.pt)
  [2]  IP / Host            192.168.1.1      (ex: 192.168.1.1)
  [3]  Username             não definido     (ex: joao_silva)
  ...

  [A]  Preencher todos os campos
  [R]  Carregar último alvo guardado
  [L]  Limpar todos os campos
  [0]  ← Voltar (guarda automaticamente)
```

- Edita **só o campo que precisas** sem tocar nos outros
- **Guardado automaticamente** ao voltar ao menu principal
- **Carregado automaticamente** ao arrancar o ARGUS

---

## 🔑 API Keys

Configura as API keys dentro do ARGUS em **`[M] Configurações`** — ficam guardadas em `~/.argus_config.json`.

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
   → Último alvo carregado automaticamente

2. Define o alvo [T]
   → Edita só os campos necessários
   → Guardado automaticamente ao sair

3. Reconhecimento de domínio [A]
   → WHOIS, DNS completo, subfinder, theHarvester
   → dnsx (valida subdomínios), httpx (verifica activos)
   → gowitness (screenshots), metagoofil (metadados docs)

4. Infraestrutura [C]
   → Nmap, Masscan (scan rápido), RustScan
   → Shodan CLI+web, Censys, BGP.tools

5. Equipamentos expostos [E]
   → Shodan queries, câmeras, routers, ICS/SCADA
   → BinaryEdge, Onyphe, FOFA

6. Pesquisa de pessoas [B]
   → Maigret, OSINT Industries
   → Background check: Spokeo, BeenVerified, TruthFinder

7. Redes sociais [D]
   → Sherlock, Social Analyzer
   → Instaloader (Instagram completo)

8. Google Dorks [I]
   → Ficheiros expostos, painéis de login, configurações

9. Verifica breaches [K]
   → HaveIBeenPwned, DeHashed, IntelX

10. Ferramentas avançadas [L]
    → Spiderfoot CLI, Recon-ng CLI, Maltego

11. Verifica a tua exposição [N]
    → DeviceInfo.me, IPLeak, BrowserLeaks

12. Guarda sessão [S]
    → JSON completo em ~/argus_sessions/
```

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

─────────────────────────────────────────────────────
                    🎯  ALVO
─────────────────────────────────────────────────────

  [T]  Definir Alvo
       Domínio, IP, Username, Email, Telefone, Nome, NIF

─────────────────────────────────────────────────────
                 🔍  RECONHECIMENTO
─────────────────────────────────────────────────────

  [A]  Domínios / Empresas / DNS
       WHOIS, dig, subfinder, amass, theHarvester, dnsx, httpx, gowitness

  [B]  Pessoas / Usernames / Identidade
       Maigret, OSINT Industries, Spokeo, BeenVerified, TruthFinder...

  [C]  IPs / Infraestrutura
       Nmap, Masscan, RustScan, Shodan CLI+web, Censys, BGP.tools

  [D]  Redes Sociais
       Sherlock, Social Analyzer, Instaloader, Twitter, Instagram...

  [E]  Equipamentos / IoT / Shodan
       Shodan queries+dashboard, câmeras, routers, BinaryEdge, Onyphe

  ...

─────────────────────────────────────────────────────
                 🛡️  OPSEC / ANONIMATO
─────────────────────────────────────────────────────

  [N]  OPSEC / Anonimato / Exposição
       DeviceInfo.me, BrowserLeaks, IPLeak, Tor Check, Temp Mail...

─────────────────────────────────────────────────────
                    ⚙️  SISTEMA
─────────────────────────────────────────────────────

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
- ✅ Contexto académico e certificações (CEH, OSCP, eJPT, PNPT, etc.)
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
