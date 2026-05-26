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

**ARGUS** é uma ferramenta OSINT de linha de comando desenvolvida para **Kali Linux**, com interface interactiva em menu. Centraliza num **único ficheiro Python** mais de **90 técnicas e recursos OSINT** organizados por categoria, desde reconhecimento de domínios e infraestrutura até pesquisa de pessoas, equipamentos IoT, geolocalização e fugas de dados.

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
- `[?]` **Estado das ferramentas** — lista todas as CLI com indicação instaladas/em falta

---

## 📋 Módulos

| Tecla | Módulo | Ferramentas / Recursos |
|-------|--------|------------------------|
| `T` | 🎯 Definir Alvo | Domínio, IP, Username, Email, Telefone, Nome, NIF |
| `A` | 🌐 Domínios / Empresas / DNS | WHOIS, dig, subfinder, amass, theHarvester, DNSDumpster, crt.sh, AXFR |
| `B` | 👤 Pessoas / Usernames | Sherlock, Maigret, Holehe, H8mail, Radaris, OSINT Industries, Datagma |
| `C` | 🖥️ IPs / Infraestrutura | Nmap, WHOIS IP, Shodan CLI+web, Censys, GreyNoise, AbuseIPDB, VirusTotal, BGP.tools, Hurricane Electric |
| `D` | 📱 Redes Sociais | Sherlock, Maigret, Twitter, Instagram, Facebook, LinkedIn, TikTok, Reddit, GitHub |
| `E` | 📡 Equipamentos / IoT | Shodan queries+dashboard, câmeras, routers, ICS/SCADA, WiGLE, GPSJam, FOFA, BinaryEdge, Onyphe |
| `F` | 📞 Telefone | Truecaller, Sync.me, SpyDialer, PhoneInfoga, NumVerify |
| `G` | 🗺️ Geolocalização | Google Earth, WiGLE, GPSJam, SunCalc, ExifTool GPS, What3Words |
| `H` | 🇵🇹 Portugal | NIF lookup, CC, Ubikron, Registo Comercial, RACIUS, Transparência.pt |
| `I` | 🔍 Google Dorks | Exploit-DB GHDB, DorkGPT, DorkSearch, dorks automáticos por categoria |
| `J` | 🗂️ Metadados / Arquivos | ExifTool, Wayback Machine, Arquivo.pt, ODCrawler, Waybackurls |
| `K` | 🔐 Breaches | HaveIBeenPwned, H8mail, Holehe, IntelX, DeHashed, LeakIX |
| `L` | 📚 Recursos / Ferramentas | OSINT Framework, Bellingcat, **Maltego**, Spiderfoot, Recon-ng, Hunter.io, BuiltWith, Wappalyzer, Pipl, PublicWWW |
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
- **Maltego** — https://www.maltego.com/downloads/
- **Spiderfoot** — https://www.spiderfoot.net/
- **Recon-ng** — https://github.com/lanmaster53/recon-ng

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
   → Nmap completo (-sC -sV), Shodan CLI+web, Censys, BGP.tools

5. Equipamentos expostos [E]
   → Shodan dashboard, câmeras, routers, BinaryEdge, Onyphe

6. Pesquisa de pessoas [B]
   → Sherlock, Maigret, Holehe, OSINT Industries

7. Google Dorks [I]
   → Ficheiros expostos, painéis de login, configurações

8. Verifica breaches [K]
   → HaveIBeenPwned, DeHashed, IntelX

9. Ferramentas avançadas [L]
   → Maltego, Spiderfoot, Recon-ng, Hunter.io

10. Guarda sessão [S]
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
  [C]  IPs / Infraestrutura          Nmap, Shodan CLI+web, BGP.tools, VirusTotal
  [D]  Redes Sociais                 Twitter, Instagram, Facebook, LinkedIn...
  [E]  Equipamentos / IoT / Shodan   Shodan, câmeras, routers, BinaryEdge, Onyphe
  [F]  Telefone / Identificação      Truecaller, Sync.me, SpyDialer, PhoneInfoga
  [G]  Geolocalização / Mapas        Google Earth, WiGLE, GPSJam, SunCalc
  [H]  Portugal Específico           NIF, CC, Ubikron, RACIUS, Transparência.pt
  [I]  Google Dorks                  GHDB, DorkGPT, dorks automáticos
  [J]  Metadados / Arquivos          ExifTool, Wayback Machine, Arquivo.pt
  [K]  Breaches / Fugas de Dados     HIBP, H8mail, Holehe, IntelX, DeHashed
  [L]  Recursos / Ferramentas        Maltego, Spiderfoot, Recon-ng, Hunter.io...
  ──────────────────────────────────────────────────────────────
  [M]  Configurações / API Keys      Shodan, Censys, HIBP, ZoomEye
  [?]  Estado das Ferramentas CLI    Verifica quais ferramentas estão instaladas
  [S]  Guardar Sessão                Exporta o log completo da sessão para JSON
  [0]  Sair

ARGUS ▶
```

---

## 🔗 Links por Módulo

Todos os recursos web integrados no ARGUS, organizados por categoria.

### 🌐 Domínios / Empresas / DNS
- [DNSDumpster](https://dnsdumpster.com/) — visualização gráfica de registos DNS
- [DNSInspect](https://www.dnsinspect.com/) — diagnóstico completo de DNS
- [Wayback Machine](https://web.archive.org/) — histórico de versões de sites
- [crt.sh](https://crt.sh/) — certificados SSL emitidos (revela subdomínios)
- [theHarvester – docs](https://www.kali.org/tools/theharvester/) — documentação oficial

### 👤 Pessoas / Usernames / Identidade
- [WhatsMyName](https://whatsmyname.app/) — username em centenas de plataformas
- [Radaris](https://radaris.com/) — background check de pessoas
- [FastPeopleSearch](https://fastpeoplesearch.ai/) — pesquisa de pessoas por nome
- [People Search](https://people-search.net/) — agregador de informação pública
- [Datagma](https://app.datagma.com/) — enriquecimento de dados por email
- [OSINT Industries](https://app.osint.industries/) — plataforma all-in-one
- [BehindTheName](https://www.behindthename.com/random/) — gerador de identidades fictícias
- [HaveIBeenPwned](https://haveibeenpwned.com/) — email em fugas de dados

### 🖥️ IPs / Infraestrutura
- [Shodan](https://www.shodan.io/dashboard) — dashboard principal
- [Shodan host lookup](https://www.shodan.io/host/) — detalhes de um host específico
- [Censys](https://search.censys.io/) — certificados, serviços e metadados
- [ZoomEye](https://www.zoomeye.org/) — motor de busca IoT
- [IPinfo.io](https://ipinfo.io/) — geolocalização e ASN de IPs
- [GreyNoise](https://www.greynoise.io/) — reputação e classificação de IPs
- [AbuseIPDB](https://www.abuseipdb.com/) — reportes de abuso e spam
- [VirusTotal](https://www.virustotal.com/) — análise de IPs, domínios e ficheiros
- [BGP.tools](https://bgp.tools/) — informação BGP e ASN em tempo real
- [Hurricane Electric BGP](https://bgp.he.net/) — BGP Toolkit completo

### 📱 Redes Sociais
- [WhatsMyName](https://whatsmyname.app/) — presença em redes sociais
- [Twitter / X](https://twitter.com/) — pesquisa avançada de tweets
- [Instagram](https://www.instagram.com/) — perfis públicos
- [Facebook](https://www.facebook.com/) — pesquisa de pessoas e posts
- [LinkedIn](https://www.linkedin.com/) — perfis profissionais
- [TikTok](https://www.tiktok.com/) — perfis públicos
- [Reddit](https://www.reddit.com/) — histórico de posts e comentários
- [GitHub](https://github.com/) — perfis e repositórios públicos
- [OSINTgram](https://github.com/Datalux/Osintgram) — Instagram OSINT

### 📡 Equipamentos / IoT / Shodan
- [Shodan – dashboard](https://www.shodan.io/dashboard) — pesquisa e exploração
- [Shodan – câmeras PT](https://www.shodan.io/search?query=webcam+country%3APT) — câmeras expostas em Portugal
- [Shodan – routers PT](https://www.shodan.io/search?query=router+country%3APT) — routers em Portugal
- [Shodan – ICS/SCADA](https://www.shodan.io/search?query=tag%3Aics) — sistemas industriais expostos
- [Shodan – Portugal](https://www.shodan.io/search?query=country%3APT) — todos os dispositivos PT
- [Censys](https://search.censys.io/) — certificados e serviços
- [ZoomEye](https://www.zoomeye.org/) — IoT e dispositivos embedded
- [WiGLE](https://wigle.net/) — mapeamento global de redes Wi-Fi
- [GPSJam](https://gpsjam.org/) — interferência GPS em tempo real
- [FOFA](https://fofa.info/) — motor de busca de activos de rede
- [BinaryEdge](https://www.binaryedge.io/) — threat intelligence e scan de internet
- [Onyphe](https://www.onyphe.io/) — cyber threat intelligence passivo
- [Natlas](https://github.com/natlas/natlas) — framework open-source de scanning

### 📞 Telefone / Identificação
- [Truecaller](https://www.truecaller.com/) — identificação de números
- [Sync.me](https://sync.me/) — lookup reverso de números
- [SpyDialer](https://www.spydialer.com/) — informação pública de números
- [NumVerify](https://numverify.com/) — validação técnica de números
- [PhoneInfoga](https://github.com/sundowndev/phoneinfoga) — OSINT completo de números

### 🗺️ Geolocalização / Mapas
- [Google Earth](https://earth.google.com/web/) — vista de satélite 3D
- [Google Maps](https://maps.google.com/) — mapas e Street View
- [Apple Maps](https://maps.apple.com/) — mapas da Apple
- [Bing Maps](https://www.bing.com/maps/) — mapas aéreos Microsoft
- [WiGLE](https://wigle.net/) — redes Wi-Fi geolocalizadas
- [GPSJam](https://gpsjam.org/) — interferência GPS em tempo real
- [SunCalc](https://www.suncalc.org/) — ângulo do sol para geolocalização
- [OpenStreetMap](https://www.openstreetmap.org/) — mapa open-source
- [Geohints](https://geohints.com/) — geolocalização por imagem
- [What3Words](https://what3words.com/) — localização precisa em 3x3 metros

### 🇵🇹 Portugal Específico
- [NIF Lookup](https://nif.marcosantos.me/) — dados públicos de NIF português
- [CC Validação](https://cc.marcosantos.me/) — validação de Cartão de Cidadão
- [Ubikron](https://www.ubikron.com/) — pesquisa de pessoas em Portugal
- [Registo Comercial](https://publicacoes.mj.pt/) — publicações do Ministério da Justiça
- [RACIUS](https://www.racius.com/) — base de dados de empresas portuguesas
- [Transparência.pt](https://www.transparencia.pt/) — financiamentos e contratos do Estado

### 🔍 Google Dorks
- [Exploit-DB GHDB](https://www.exploit-db.com/google-hacking-database) — base de dados de dorks
- [DorkGPT](https://www.dorkgpt.com/) — geração de dorks com IA
- [DorkSearch Pro](https://dorksearch.pro/) — motor de pesquisa de dorks
- [WeLiveSecurity – Dorks](https://www.welivesecurity.com/br/2021/07/30/google-hacking-verifique-quais-informacoes-sobre-voce-ou-sua-empresa-aparecem-nos-resultados/) — artigo sobre Google Hacking

### 🗂️ Metadados / Arquivos / Histórico
- [Wayback Machine](https://web.archive.org/) — histórico de URLs arquivados
- [Arquivo.pt](https://arquivo.pt/) — arquivo histórico da web portuguesa
- [Newspaper Archive](https://newspaperarchive.com/search/) — jornais históricos digitalizados
- [ODCrawler](https://odcrawler.xyz/) — crawler de domínios .onion

### 🔐 Breaches / Fugas de Dados
- [HaveIBeenPwned](https://haveibeenpwned.com/) — email em fugas de dados conhecidas
- [IntelX](https://intelx.io/) — motor de busca de dados vazados
- [DeHashed](https://dehashed.com/) — base de dados de credenciais comprometidas
- [LeakIX](https://leakix.net/) — serviços vulneráveis e fugas em tempo real

### 📚 Recursos / Ferramentas OSINT
- [OSINT Framework](https://osintframework.com/) — mapa visual de ferramentas OSINT
- [Bellingcat Toolkit](https://bellingcat.gitbook.io/toolkit) — toolkit investigativo
- [OSINT Combine](https://www.osintcombine.com/) — colecção de ferramentas combinadas
- [My OSINT Training](https://smart.myosint.training/) — plataforma de aprendizagem
- [District4Labs](https://www.district4labs.com/) — plataforma profissional OSINT
- [Maltego](https://www.maltego.com/) — mapeamento visual de relações e entidades
- [Spiderfoot](https://www.spiderfoot.net/) — recon automatizado completo
- [Recon-ng](https://github.com/lanmaster53/recon-ng) — framework modular OSINT
- [Hunter.io](https://hunter.io/) — emails profissionais por domínio
- [Pipl](https://pipl.com/) — pesquisa avançada de pessoas
- [PublicWWW](https://publicwww.com/) — pesquisa em código-fonte de sites
- [BuiltWith](https://builtwith.com/) — tecnologias usadas por um site
- [Wappalyzer](https://www.wappalyzer.com/) — fingerprinting de tecnologias web
- [Kagi](https://kagi.com/) — motor de busca privado sem rastreio
- [FlightAware](https://flightaware.com/) — rastreio de voos em tempo real
- [MarineTraffic](https://www.marinetraffic.com/) — rastreio de embarcações AIS
- [OpenCorporates](https://opencorporates.com/) — base de dados global de empresas
- [EDGAR – SEC](https://www.sec.gov/edgar/search/) — registos de empresas cotadas EUA

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
