# Python Mini Projects Collection

[🇧🇷 Versão em Português](README-pt.md)

A simple collection of three interactive Python web applications built with Streamlit, demonstrating API integration, data visualization, and real-world problem solving. These projects were proposed by teacher **Juliano Faccioni** during the APIs for beginners course at **Asimov Academy**

## 🎯 Projects Overview
This repository contains three distinct mini-projects that demonstrate various Python capabilities:

1. **🌤️ Weather Web App** - Real-time weather information using OpenWeatherMap API
2. **🎵 Spotify Web App** - Artist search and top tracks discovery using Spotify Web API
3. **📊 Names by Decade App** - Brazilian name frequency analysis using IBGE data

### Required Environment Variables:
The API keys for all miniprojects should be stored in a .env file and imported individualy using python-dotenv.

```bash
OPEN_WEATHER_API="YOUR KEY"
SPOTIFY_CLIENT_ID="YOUR CID"
SPOTIFY_CLIENT_SECRET="YOUR CS"
```

## 🌤️ Weather Web App

### **Features:**
- **Global Weather Data:** Real-time weather for any city worldwide
- **Comprehensive Metrics:** Temperature, feels-like, humidity, and cloud coverage
- **Localized Content:** Weather descriptions in Portuguese
- **Responsive Interface:** Clean, mobile-friendly design

### **Technologies:**
- **OpenWeatherMap API:** Weather data provider
- **Streamlit:** Web interface framework
- **Requests:** HTTP client library

### **Usage:**
```bash
cd weather_app
streamlit run weather_app.py
```

## 🎵 Spotify Web App
### Features:
- Artist Search: Find artists by name using Spotify's database
- Top Tracks Display: Show most popular songs with popularity scores
- Direct Links: Clickable links to Spotify tracks
- Real-time Data: Live information from Spotify Web API

### Technologies:
- Spotify Web API: Music data and authentication
- OAuth 2.0: Client credentials flow for API access
- Streamlit: Interactive web interface

### **Usage**
```bash
cd spotify_app
streamlit run spotify_app.py
```

## 📊 Names by Decade App
### Features:
- Historical Data: Name frequency trends across decades in Brazil
- Data Visualization: Interactive charts showing name evolution
- Government Data: Official statistics from IBGE
- Dual Display: Both tabular and graphical data representation

### Technologies:
- IBGE API: Brazilian government statistical data
- Pandas: Data manipulation and analysis
- Streamlit Charts: Built-in visualization components

### **Usage**
```bash
cd names_app
streamlit run names_app.py
```
## 🚀 Getting Started
1. Python 3.8 or higher
   ```bash
   python -3.11 -m venv venv
   ```
3. Clone the repo:
   ```bash
   git clone https://github.com/your-username/python-mini-projects.git
   cd python-mini-projects
   ```
4. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

## 🔑 API Setup Guide
### OpenWeatherMap API (Weather App)
- Visit [openweathermap.org]
- Create a free account
- Verify your email
- Generate your API key --> may have to wait a few hours to activate
- Add to .env file as CHAVE_API_OPENWEATHER

## Spotify Web API (Spotify App)
- Go to [developer.spotify.com]
- Create a new app in your dashboard
- Copy Client ID and Client Secret
- Add to .env file as SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments
- **OpenWeatherMap** for providing comprehensive weather data
- **Spotify** for their excellent Web API and developer resources
- **IBGE** for open access to Brazilian demographic data
- **Streamlit** team for the amazing web app framework
- **Python** community for excellent libraries and tools

# 🛠️ Tecnologies Used
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-2CA5E0?style=for-the-badge&logo=python&logoColor=white)

---
🚀 "Building tomorrow's solutions with today's code."
