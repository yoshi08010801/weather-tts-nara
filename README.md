# 天気読み上げツール / Weather TTS Notifier (Python)

日本語と英語の両方で記載しています。  
This README is written in both Japanese and English.

---

## 📌 概要 / Overview

このツールは、OpenWeatherMap の天気情報を取得し、gTTS で日本語音声に変換して再生する Python スクリプトです。  
This Python script fetches weather information from OpenWeatherMap and reads it aloud in Japanese using gTTS.

例: 「奈良の今日の天気は晴れ、気温は25度です」  
Example: "Today's weather in Nara is sunny, and the temperature is 25°C."

---

## 🛠️ 使用ライブラリ / Requirements

- requests  
- gTTS  
- OpenWeatherMap API

---

## 📝 使い方 / How to Use

### 🔸 必要な設定 / Setup

1. `config.py` をこのフォルダに作成し、以下のように書いてください：  
   Create a file named `config.py` and add the following:

```python
API_KEY = "あなたのOpenWeatherMap APIキー"
# Replace with your actual OpenWeatherMap API key
```

2. スクリプトを実行します：  
   Run the script:

```bash
python weather_tts.py
```

3. `weather.mp3` が生成され、自動的に再生されます。  
   An audio file `weather.mp3` will be created and played automatically.

---

## 🔒 注意 / Notes

- `config.py` は `.gitignore` により GitHub には含まれていません。  
  The `config.py` file is excluded via `.gitignore` to keep your API key safe.
- OpenWeatherMap API キーは無料で取得できます。  
  You can get a free API key from [OpenWeatherMap](https://openweathermap.org/).

---

## 🎓 学習目的 / For Learning

このツールは、Python 初心者の学習プロジェクトとして、**趣味で作成したものです。**  
This tool was created as a **hobby project** and part of a personal learning journey in Python.

Feel free to use or modify it for your own practice!

---

## 📺 YouTube 作業ログ / YouTube Work Logs

このツールを作成・テストしている様子を YouTube ライブ配信で記録しています。  
Live recordings of coding and testing this tool are available on YouTube.

▶ https://youtube.com/live/TxcfXSHNHGg?feature=share  
▶ https://youtube.com/live/6Bt9btue24g?feature=share  
▶ https://youtube.com/live/08X4HF0dQNU?feature=share

※ 雑談や手直しなども含まれた学習ログです。  
※ These are relaxed, real-time learning sessions including casual work and trial & error.
