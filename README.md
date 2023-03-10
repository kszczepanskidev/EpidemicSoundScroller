# EpidemicSoundScroller

Simple script that open Firefox with Epidemic Sound page and looks for song and artist names, then saves it into file so it can be displayed while livestreaming.

## Usage
_(Optional)_ Edit `.env` file entering your Epidemic Sound credentials. You can also adjust how many seconds it will wait before fetching music info again.

After singing into Epidemic Sound account you can play any music and the script will save information about artist name and song title into `music_info.txt` file.

## Windows binary
To create your own `.exe` for Windows ensure you have PyInstaller installed and use following command:
```bash
pyinstaller ./app.py --onefile -c --add-binary "./driver/geckodriver.exe;./driver"
```
