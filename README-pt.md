# Coleção de Mini Projetos Python

[🇺🇸 English Version](README.md)

Uma coleção simples de três aplicações web interativas em Python construídas com Streamlit, demonstrando integração de APIs, visualização de dados e resolução de problemas do mundo real. Estes projetos foram propostos pelo professor **Juliano Faccioni** durante o curso de APIs para iniciantes na **Asimov Academy**

## 🎯 Visão Geral dos Projetos
Este repositório contém três mini-projetos distintos que demonstram várias capacidades do Python:

1. **🌤️ Aplicativo Web do Tempo** - Informações meteorológicas em tempo real usando a API OpenWeatherMap
2. **🎵 Aplicativo Web Spotify** - Busca de artistas e descoberta de top tracks usando a API Web do Spotify
3. **📊 Aplicativo Nomes por Década** - Análise de frequência de nomes brasileiros usando dados do IBGE

### Variáveis de Ambiente Necessárias:
As chaves de API para todos os miniprojetos devem ser armazenadas em um arquivo .env e importadas individualmente usando python-dotenv.

```bash
OPEN_WEATHER_API="SUA CHAVE"
SPOTIFY_CLIENT_ID="SEU CID"
SPOTIFY_CLIENT_SECRET="SEU CS"
```
## 🌤️ Aplicativo Web do Tempo
### Funcionalidades:
- Dados Meteorológicos Globais: Tempo em tempo real para qualquer cidade do mundo
- Métricas Abrangentes: Temperatura, sensação térmica, umidade e cobertura de nuvens
- Conteúdo Localizado: Descrições do tempo em português
- Interface Responsiva: Design limpo e amigável para dispositivos móveis

### Tecnologias:
- API OpenWeatherMap: Provedor de dados meteorológicos
- Streamlit: Framework de interface web
- Requests: Biblioteca cliente HTTP

### Uso:
```bash
cd weather_app
streamlit run weather_app.py
```

## 🎵 Aplicativo Web Spotify
### Funcionalidades:
- Busca de Artistas: Encontre artistas por nome usando o banco de dados do Spotify
- Exibição de Top Tracks: Mostre as músicas mais populares com pontuações de popularidade
- Links Diretos: Links clicáveis para faixas do Spotify
- Dados em Tempo Real: Informações ao vivo da API Web do Spotify

### Tecnologias:
- API Web Spotify: Dados musicais e autenticação
- OAuth 2.0: Fluxo de credenciais do cliente para acesso à API
- Streamlit: Interface web interativa

### Uso
```bash
cd spotify_app
streamlit run spotify_app.py
```

## 📊 Aplicativo Nomes por Década
### Funcionalidades:
- Dados Históricos: Tendências de frequência de nomes ao longo das décadas no Brasil
- Visualização de Dados: Gráficos interativos mostrando a evolução dos nomes
- Dados Governamentais: Estatísticas oficiais do IBGE
- Exibição Dupla: Representação de dados tanto tabular quanto gráfica

### Tecnologias:
- API IBGE: Dados estatísticos do governo brasileiro
- Pandas: Manipulação e análise de dados
- Gráficos Streamlit: Componentes de visualização integrados

### Uso
```bash
cd names_app
streamlit run names_app.py
```

## 🚀 Como Começar

1. Python 3.8 ou superior
    ```bash
    python -3.11 -m venv venv
    ```
2. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/python-mini-projects.git
    cd python-mini-projects
    ```
3. Instale as dependências
    ```bash
    pip install -r requirements.txt
    ```

## 🔑 Guia de Configuração de API
### API OpenWeatherMap (Aplicativo do Tempo)
- Visite [openweathermap.org]
- Crie uma conta gratuita
- Verifique seu email
- Gere sua chave de API --> pode ter que esperar algumas horas para ativar
- Adicione ao arquivo .env como CHAVE_API_OPENWEATHER

### API Web Spotify (Aplicativo Spotify)
- Vá para [developer.spotify.com]
- Crie um novo app no seu dashboard
- Copie o Client ID e Client Secret
- Adicione ao arquivo .env como SPOTIFY_CLIENT_ID e SPOTIFY_CLIENT_SECRET

##📄 Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.

##🙏 Agradecimentos
- **OpenWeatherMap** por fornecer dados meteorológicos abrangentes
- **Spotify** por sua excelente API Web e recursos para desenvolvedores
- **IBGE** pelo acesso aberto aos dados demográficos brasileiros
- Equipe **Streamlit** pelo incrível framework de aplicações web
- Comunidade **Python** pelas excelentes bibliotecas e ferramentas

## 🛠️ Tecnologias Utilizadas
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-2CA5E0?style=for-the-badge&logo=python&logoColor=white)
