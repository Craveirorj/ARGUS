# 👁️ ARGUS
### Advanced Reconnaissance & OSINT Intelligence Suite

> *"O gigante de 100 olhos que tudo vê"*

![Python](https://img.shields.io/badge/Python-3.8%2B-brightgreen?style=flat-square&logo=python)
![Platform](https://img.shields.io/badge/Platform-Kali%20Linux-brightgreen?style=flat-square&logo=linux)
![License](https://img.shields.io/badge/License-MIT-brightgreen?style=flat-square)
![OSINT](https://img.shields.io/badge/Category-OSINT-brightgreen?style=flat-square)
![AI](https://img.shields.io/badge/AI-Ollama%20%7C%20Groq%20%7C%20Claude-brightgreen?style=flat-square)

---

## 📌 Descrição

**ARGUS** é uma ferramenta OSINT de linha de comando desenvolvida para **Kali Linux**, com interface interactiva em menu. Centraliza num único ponto de acesso mais de **80 técnicas e recursos OSINT** organizados por categoria — desde reconhecimento de domínios e infraestrutura até pesquisa de pessoas, equipamentos IoT, geolocalização e fugas de dados.

A versão actual inclui o módulo **ARGUS INTELLIGENCE** — um motor de IA integrado que analisa automaticamente os resultados dos scans, sugere vectores de investigação e responde a perguntas OSINT em linguagem natural, adaptado ao nível do utilizador (Iniciante / Intermédio / Avançado).

Desenvolvida para uso exclusivamente **ético e em contexto autorizado** — testes de segurança, investigação académica, CTF e certificações de cibersegurança.

---

## ✨ Funcionalidades

### 🔍 Reconhecimento OSINT
| Módulo | Ferramentas / Recursos |
|--------|----------------------|
| **Domínios / Empresas / DNS** | WHOIS, dig, subfinder, amass, theHarvester, dnsx, httpx, gowitness, metagoofil, DNSDumpster, crt.sh, AXFR |
| **Pessoas / Usernames** | Maigret, OSINT Industries, Datagma, OSINTgram, Radaris, FastPeopleSearch, Spokeo, BeenVerified, Pipl |
| **IPs / Infraestrutura** | Nmap, Masscan, RustScan, Shodan CLI, Censys, ZoomEye, IPinfo, GreyNoise, AbuseIPDB, VirusTotal, BGP.tools |
| **Redes Sociais** | Twitter/X, Instagram, Facebook, LinkedIn, TikTok, Reddit, GitHub (perfis, posts, geotags) |
| **Equipamentos / IoT** | Shodan queries, câmeras abertas, routers, ICS/SCADA, BinaryEdge, FOFA, Onyphe, WiGLE |
| **Telefone** | Truecaller, Sync.me, SpyDialer, PhoneInfoga, NumVerify |
| **Geolocalização** | Google Earth, WiGLE, GPSJam, SunCalc, ExifTool GPS, What3Words, Geohints |
| **🇵🇹 Portugal** | NIF lookup, Cartão de Cidadão, Ubikron, Registo Comercial, RACIUS, Transparência.pt |

### 🛠️ Técnicas
| Módulo | Descrição |
|--------|-----------|
| **Google Dorks** | Exploit-DB GHDB, DorkGPT, DorkSearch, dorks automáticos por categoria (ficheiros, login, config, câmeras, SQL) |
| **Metadados / Arquivos** | ExifTool, Wayback Machine, Arquivo.pt, Waybackurls, ODCrawler, Google Cache |
| **Breaches / Fugas** | HaveIBeenPwned, H8mail, Holehe, IntelX, DeHashed, LeakIX |

### 🤖 ARGUS INTELLIGENCE (IA)
| Função | Descrição |
|--------|-----------|
| **Analisar último scan** | Analisa automaticamente o output do último scan capturado |
| **Analisar output manual** | Cola qualquer output de ferramenta para análise de IA |
| **Chat OSINT livre** | Faz perguntas sobre o alvo activo em linguagem natural |
| **Gerar Dorks por IA** | Dorks personalizados e explicados para o alvo definido |
| **Analisar breach/leak** | Interpreta resultados de breaches e sugere acções |
| **Relatório de sessão** | Gera relatório executivo inteligente de toda a sessão |

### ⚙️ Sistema
- **Auto-instalação do `rich`** — se não estiver presente, instala automaticamente e reinicia
- **Gestão de ferramentas CLI** — verifica estado e instala ferramentas com `[?]`
- **Gestão de alvos** — guarda e carrega automaticamente o último alvo (domínio, IP, username, email, telefone, nome, NIF)
- **Log de sessão** — regista todas as acções com timestamp e exporta para JSON
- **API Keys** — gestão centralizada de Shodan, Censys, HIBP, ZoomEye, Groq, Claude
- **OPSEC** — ferramentas para verificar exposição, fugas de IP/DNS, anonimato e fingerprinting

---

## 🚀 Instalação

### Pré-requisitos
- Kali Linux (recomendado) ou qualquer distro Debian/Ubuntu
- Python 3.8 ou superior
- Git

### Passo 1 — Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/argus.git
cd argus
```

### Passo 2 — Executar

```bash
python3 argus.py
```

> O ARGUS instala automaticamente a biblioteca `rich` se não estiver presente. Não é necessário mais nenhum passo de instalação obrigatório.

### Passo 3 (opcional) — Tornar executável globalmente

```bash
chmod +x argus.py
sudo cp argus.py /usr/local/bin/argus
argus
```

---

## 🤖 Configurar a IA (ARGUS INTELLIGENCE)

O módulo de IA é **opcional** mas altamente recomendado. Suporta três providers — escolhe o que se adequa à tua situação:

---

### Opção 1 — Ollama (Local, 100% Gratuito) ✅ Recomendado

O Ollama corre um modelo de IA directamente na tua máquina. Não precisa de internet, não precisa de conta, sem limites de uso.

**Instalar o Ollama:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Descarregar um modelo** (escolhe um):
```bash
ollama pull llama3        # Recomendado — bom equilíbrio velocidade/qualidade
ollama pull mistral       # Alternativa mais leve
ollama pull llama3:70b    # Máxima qualidade (requer ~40GB RAM)
```

**Iniciar o servidor Ollama** (precisa de estar activo para o ARGUS usar):
```bash
ollama serve
```

> Dica: adiciona `ollama serve &` ao teu `.bashrc` para iniciar automaticamente.

**Configurar no ARGUS:**
1. No menu principal → `[O]` → `[C] Configurar IA`
2. Escolhe `[1] Ollama (local, gratuito)`
3. Introduz o nome do modelo (ex: `llama3`)
4. Escolhe o teu nível (Iniciante / Intermédio / Avançado)

---

### Opção 2 — Groq API (Cloud, Gratuito com conta)

A Groq oferece uma API gratuita com limites generosos para modelos como Llama3 e Mixtral. Requer internet mas é muito rápida.

**Criar conta gratuita:**
1. Acede a [https://console.groq.com/](https://console.groq.com/)
2. Regista-te (gratuito)
3. Em **API Keys** → **Create API Key**
4. Copia a chave gerada

**Configurar no ARGUS:**
1. No menu principal → `[O]` → `[C] Configurar IA`
2. Escolhe `[2] Groq API (cloud, gratuito)`
3. Cola a tua API key
4. Modelo recomendado: `llama3-70b-8192`
5. Escolhe o teu nível

---

### Opção 3 — Claude API (Anthropic, Pago)

Para quem tem acesso à API da Anthropic. Máxima qualidade de análise.

**Obter API key:**
1. Acede a [https://console.anthropic.com/](https://console.anthropic.com/)
2. Em **API Keys** → **Create Key**
3. Copia a chave

**Configurar no ARGUS:**
1. No menu principal → `[O]` → `[C] Configurar IA`
2. Escolhe `[3] Claude API (Anthropic, pago)`
3. Cola a tua API key
4. Modelo recomendado: `claude-opus-4-6`
5. Escolhe o teu nível

---

### Níveis de utilizador da IA

| Nível | Comportamento |
|-------|--------------|
| **Iniciante** | Explica tudo em detalhe, dá comandos completos com cada flag explicada |
| **Intermédio** | Sugere vectores, dá comandos, deixa explorar sem explicações excessivas |
| **Avançado** | Lista vulnerabilidades e vectores directamente, sem explicações |

---

## 📖 Como usar

### Iniciar o ARGUS

```bash
python3 argus.py          # Modo normal
python3 argus.py --status # Ver estado de todas as ferramentas CLI
python3 argus.py --help   # Ajuda rápida
```

### Fluxo básico de trabalho

```
1. [T] Definir Alvo       → Introduz domínio, IP, username, email, etc.
2. [A-N] Módulos OSINT    → Escolhe o módulo adequado ao teu alvo
3. Executa ferramentas    → Output capturado automaticamente
4. [O] ARGUS INTELLIGENCE → Analisa resultados com IA, faz perguntas, gera relatório
5. [S] Guardar Sessão     → Exporta log completo para JSON
```

### Navegação

- **Letras maiúsculas** `[A]` a `[O]` — acesso aos módulos
- **`[T]`** — definir/editar alvo
- **`[O]`** — ARGUS INTELLIGENCE (módulo de IA)
- **`[M]`** — configurações e API keys
- **`[?]`** — estado das ferramentas CLI
- **`[S]`** — guardar sessão
- **`[0]`** — voltar / sair

---

## 🔧 Ferramentas CLI recomendadas

O ARGUS instala ferramentas automaticamente quando necessário, mas podes instalar tudo de uma vez:

```bash
# Ferramentas apt
sudo apt update && sudo apt install -y \
  nmap masscan theharvester amass sherlock h8mail \
  exiftool traceroute whois metagoofil

# Ferramentas pip/pipx
pipx install maigret holehe
pip3 install shodan rustscan instaloader spiderfoot recon-ng --break-system-packages

# Ferramentas Go
go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install github.com/projectdiscovery/dnsx/cmd/dnsx@latest
go install github.com/projectdiscovery/httpx/cmd/httpx@latest
go install github.com/sensepost/gowitness@latest
go install github.com/tomnomnom/waybackurls@latest
```

---

## 📁 Estrutura de ficheiros

```
argus/
├── argus.py          # Ficheiro principal — tudo num único script
└── README.md         # Este ficheiro

# Criados automaticamente em execução:
~/.argus_config.json  # Configurações e API keys (criado automaticamente)
~/argus_sessions/     # Logs de sessão e relatórios de IA exportados
```

---

## ⚠️ Aviso Legal

Este software é disponibilizado **exclusivamente para fins educativos e de investigação em segurança**. A utilização do ARGUS em sistemas sem autorização explícita é ilegal e antiética.

O autor não se responsabiliza por qualquer uso indevido desta ferramenta. Usa sempre em ambientes controlados, laboratórios, CTFs ou com autorização escrita do proprietário do sistema alvo.

---

## 👤 Autor

Desenvolvido por **Craveiro**
Projecto criado no âmbito de formação em cibersegurança ofensiva — Kali Linux

---

## 📄 Licença

MIT License — livre para usar, modificar e distribuir com atribuição ao autor.
