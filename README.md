# AdeRawl
HTML5 Viewer for YouTube videos to bypass ads and that pesky popup that shows up nowadays if you use an adblocker. Don't really feel like web hosting, since I'm not really willing to pay for it and dealing with it. So I'm making this open to everyone.

# Requirements
1. [Python](https://www.python.org/downloads/) (install the latest version)
2. `Flask` (Install via `pip install flask` in your Terminal)
3. `pytube` (Install via `pip install pytube` in your Terminal)
4. (*Optional*) `pytz` (Install via `pip install pytz`)

# Instructions
1. `git clone` this repository in your Terminal
2. `cd` to this repository in Terminal
3. (*Optional*) Change timezone in `get_login_time()` function at the bottom of `main.py`. Also optionally, you can remove that function and line altogether, as it's there just for my own sake.
4. `python3 main.py` in Terminal
5. The terminal should have generated a IP address at which your `localhost` is live. Enter that IP address in your browser search bar.
6. `Ctrl+C` in Terminal when finished with your downloading. Alternatively, just leave your Terminal session open for theoretical 24/7 access to the site.
