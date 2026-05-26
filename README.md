# 👁️ ARGUS
### Advanced Reconnaissance & OSINT Intelligence Suite

> *"O gigante de 100 olhos que tudo vê"*

![Python](https://img.shields.io/badge/Python-3.8%2B-brightgreen?style=flat-square&logo=python)
![Platform](https://img.shields.io/badge/Platform-Kali%20Linux-brightgreen?style=flat-square&logo=linux)
![License](https://img.shields.io/badge/License-MIT-brightgreen?style=flat-square)
![OSINT](https://img.shields.io/badge/Category-OSINT-brightgreen?style=flat-square)

---

## 📌 Descrição

**ARGUS** é uma ferramenta OSINT de linha de comando desenvolvida para **Kali Linux**, com interface interactiva em menu. Centraliza num único ponto de acesso mais de **80 técnicas e recursos OSINT** organizados por categoria, desde reconhecimento de domínios e infraestrutura até pesquisa de pessoas, equipamentos IoT, geolocalização e fugas de dados.

Desenvolvida para uso exclusivamente **ético e em contexto autorizado** — testes de segurança, investigação académica, CTF e certificações de cibersegurança.

---

## ✨ Funcionalidades

- 🎯 **Alvo persistente** — define uma vez, usa em todos os módulos
- 🌐 **13 módulos OSINT** com navegação por letras/números
- 🖥️ **Ferramentas CLI integradas** — execução directa no terminal
- 🌍 **Recursos web** — abre automaticamente no browser com o alvo pré-preenchido
- 💾 **Sessões JSON** — todo o histórico de acções guardado automaticamente
- ⚙️ **Gestão de API keys** — Shodan, Censys, HIBP, ZoomEye guardadas em config
- 🎨 **Interface verde/preto** com descrição de cada ferramenta
- 🇵🇹 **Módulo Portugal** — NIF, CC, Ubikron, RACIUS, Transparência.pt

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

### Dependências Python (obrigatórias)
```
rich
```

---

## 🚀 Instalação

### 1. Clonar o repositório
```bash
git clone https://github.com/teu-username/argus.git
cd argus
```

### 2. Instalar dependência Python
```bash
pip3 install rich --break-system-packages
```

### 3. Dar permissões de execução
```bash
chmod +x argus.py
```

### 4. Executar
```bash
python3 argus.py
```

---

## 🛠️ Ferramentas CLI — Instalação Opcional

O ARGUS detecta automaticamente quais ferramentas estão instaladas e mostra `✔` ou `✗` em cada opção. Instala apenas as que precisas:

### Via apt (Kali / Debian)
```bash
# Nmap — scanner de rede e portos
sudo apt install nmap

# theHarvester — emails, subdomínios, IPs via OSINT
sudo apt install theharvester

# Amass — enumeração de subdomínios e superfície de ataque
sudo apt install amass

# ExifTool — metadados de ficheiros (imagens, PDFs, etc.)
sudo apt install libimage-exiftool-perl

# Traceroute
sudo apt install traceroute

# WHOIS
sudo apt install whois
```

### Via pip3
```bash
# Sherlock — username em 300+ redes sociais
pip3 install sherlock-project --break-system-packages

# Maigret — perfil completo por username
pip3 install maigret --break-system-packages

# Holehe — email em 100+ serviços
pip3 install holehe --break-system-packages

# H8mail — pesquisa de email em breaches
pip3 install h8mail --break-system-packages

# Shodan CLI — interface de linha de comando para Shodan
pip3 install shodan --break-system-packages

# Social Analyzer — análise de redes sociais
pip3 install social-analyzer --break-system-packages

# Twint — scraping de Twitter sem API
pip3 install twint --break-system-packages
```

### Via Go
```bash
# Subfinder — enumeração passiva de subdomínios
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

# Waybackurls — URLs históricos do Wayback Machine
go install github.com/tomnomnom/waybackurls@latest
```

### Instalação manual
```bash
# PhoneInfoga — OSINT de números de telefone
# Ver: https://github.com/sundowndev/phoneinfoga

# OSINTgram — Instagram OSINT
# Ver: https://github.com/Datalux/Osintgram
```

---

## 🔑 API Keys

Algumas ferramentas requerem API keys para funcionar. Configura-as dentro do ARGUS em **[M] Configurações** ou edita directamente o ficheiro `~/.argus_config.json`.

| Serviço | Onde obter | Plano gratuito |
|---------|-----------|----------------|
| **Shodan** | https://account.shodan.io/ | Limitado |
| **Censys** | https://censys.io/register | Sim |
| **HaveIBeenPwned** | https://haveibeenpwned.com/API/Key | Pago |
| **ZoomEye** | https://www.zoomeye.org/profile | Sim |

As keys ficam guardadas em `~/.argus_config.json` (apenas acessível pelo teu utilizador).

---

## 📁 Estrutura de Ficheiros

```
argus/
├── argus.py              # Ferramenta principal
├── README.md             # Este ficheiro
└── ~/.argus_config.json  # API keys (criado automaticamente)
└── ~/argus_sessions/     # Sessões guardadas em JSON (criado automaticamente)
```

### Formato de sessão JSON
```json
{
  "target": {
    "domain": "exemplo.pt",
    "ip": "192.168.1.1",
    "username": "joao_silva",
    "email": "joao@exemplo.pt",
    "phone": null,
    "name": null,
    "nif": null
  },
  "log": [
    {
      "timestamp": "2025-01-15T14:32:01.123456",
      "action": "WHOIS → exemplo.pt",
      "data": "whois exemplo.pt"
    }
  ]
}
```

---

## 🖥️ Utilização

### Fluxo típico de investigação

```
1. Inicia o ARGUS
   python3 argus.py

2. Define o alvo [T]
   → Domínio: empresa.pt
   → IP: 192.168.1.100
   → Username: joao_silva

3. Reconhecimento de domínio [A]
   → WHOIS, DNS, subfinder, theHarvester

4. Infraestrutura [C]
   → Nmap completo, Shodan, Censys

5. Pesquisa de pessoas [B]
   → Sherlock, Maigret, Holehe

6. Google Dorks [I]
   → Ficheiros expostos, painéis de login

7. Verifica breaches [K]
   → HaveIBeenPwned, DeHashed

8. Guarda sessão [S]
   → JSON completo em ~/argus_sessions/
```

### Navegação
- Introduz a **letra ou número** da opção e prime `Enter`
- O alvo definido em **[T]** é usado automaticamente em todos os módulos
- Se uma ferramenta CLI não estiver instalada, o ARGUS mostra o comando de instalação
- Os recursos web abrem directamente no browser com o alvo pré-preenchido no URL quando possível

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

──────────────────────────────────────────────────────────

  [T]  Definir Alvo             Configura domínio, IP, username, email...
  ──────────────────────────────────────────────────────
  [A]  Domínios / Empresas / DNS    WHOIS, dig, subfinder, amass, theHarvester
  [B]  Pessoas / Usernames          Sherlock, Maigret, Holehe, H8mail, Radaris
  [C]  IPs / Infraestrutura         Nmap, Shodan, Censys, AbuseIPDB, VirusTotal
  ...

ARGUS ▶
```

---

## ⚠️ Aviso Legal

Esta ferramenta é disponibilizada **exclusivamente para fins educativos, académicos e de investigação de segurança autorizada**.

- ✅ Testes em sistemas **próprios** ou com **autorização expressa**
- ✅ Contexto académico e certificações (CEH, OSCP, etc.)
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
