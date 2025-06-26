# DUW Queue Monitor 🎫

A Python application that monitors queue status at Lower Silesian Voivodeship Office (Dolnośląski Urząd Wojewódzki) and alerts you when your appointment time is approaching.

## 📋 Overview

This tool helps you track your position in the queue for temporary residence applications and other services at DUW offices. Instead of constantly checking the website or waiting at the office, you'll get an audio notification when it's almost your turn.

## 🏢 Supported Cities

- **Wrocław**
- **Legnica**
- **Wałbrzych**
- **Jelenia Góra**

## ✨ Features

- 🔍 Real-time queue monitoring
- 🔔 Audio alert notifications
- ⚙️ Customizable reminder threshold
- 🏙️ Multi-city support
- 🛡️ Network error handling with auto-retry
- 📱 Simple command-line interface

## 🚀 Installation

### Prerequisites

- Python 3.6 or higher
- Internet connection

#### 1. Install Pipenv

```bash
pip install pipenv
```

#### 2. Clone this repository

```bash
git clone https://github.com/Suleymanmalikov/duw-queue-monitor
cd duw-queue-monitor
```

#### 3. Install dependencies and create a virtual environment

```bash
pipenv install
```

### 4. Install Dependencies

```bash
pip install requests pygame urllib3
```

#### 5. Run the application

```bash
pipenv run python main.py
```

#### or activate the shell

```bash
pipenv shell
python main.py
```

### Audio File Setup

Place an audio file named `alert.wav` in the same directory as the script. This will be played when your turn approaches.

## 📖 Usage

1. **Run the application:**

   ```bash
   python main.py
   ```

2. **Select your city:**

   ```
   Choose City:
   1. Wrocław       2. Legnica      3. Wałbrzych        4. Jelenia Góra
   ```

3. **Enter your ticket number:**

   ```
   What is your Ticket Value(ex: C085): C085
   ```

4. **Set reminder threshold:**

   ```
   How many line before do you want to be reminded(ex: 5): 5
   ```

5. **Wait for notification:**
   The application will continuously monitor the queue and alert you when ticket `C080` is called (5 positions before your `C085` ticket).

## 🛠️ How It Works

1. **API Polling**: Fetches queue status from `https://rezerwacje.duw.pl/status_kolejek/`
2. **Ticket Parsing**: Extracts letter prefix and number from your ticket
3. **Position Tracking**: Monitors current ticket being served
4. **Smart Alerting**: Calculates when to notify based on your reminder preference
5. **Audio Notification**: Plays sound alert when your time approaches

## 📁 Project Structure

```
queue-monitor/
├── main.py            # Main application
├── alert.wav          # Audio notification file
└── README.md          # This file
```

## ⚡ Example

```bash
$ python main.py
Choose City:
1. Wrocław       2. Legnica      3. Wałbrzych        4. Jelenia Góra
1
What is your Ticket Value(ex: C085): C085
How many line before do you want to be reminded(ex: 5): 3

C078
C079
C080
C081
C082
Get ready your time has come
[Audio alert plays]
```

## 🔧 Configuration

### Monitoring Interval

The application checks the queue every 5 seconds. You can modify this in the code:

```python
time.sleep(5)  # Change this value to adjust check frequency
```

### Audio File

Replace `alert.wav` with your preferred notification sound. Supported formats include WAV, OGG, and MP3.

## 🚨 Error Handling

- **Network Issues**: Automatic retry with 3-second delay
- **Invalid Input**: Input validation with error messages
- **API Errors**: Graceful handling of malformed responses
- **Missing Audio**: Application continues without sound if audio file is missing

## 📋 Requirements

```txt
requests>=2.32.4
pygame>=2.6.1
urllib3>=2.5.0
```

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## ⚠️ Disclaimer

This tool is for personal use only. Please be respectful of the DUW servers and avoid excessive API requests. The application is not affiliated with Dolnośląski Urząd Wojewódzki.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙋‍♂️ Support

If you encounter any issues or have questions:

1. Check that your internet connection is stable
2. Verify the audio file exists and is accessible
3. Ensure your ticket format matches the expected pattern (Letter + Numbers)
4. Make sure the DUW website is accessible

---

**Happy queuing! 🎯**
