# FantasyTimeTracker
Time Tracking tool for tabletop roleplaying games. Time counting is set up for
fifth edition Dungeons and Dragons, but chancing turn length should be enough
to fit for most other games.

The tracker and the calendar views are provided for game master to set current
time dependent conditions and track how events move the clock forward.

This tool also provides a web page that can be shown to players on secondary
monitor or projector to give a bit of atmosphere and keep them on track of the
time passing in game.

## Setup
* Make sure Python 3, pip and venv are installed
* Create Python 3 virtual environment for the program.
  ```
  python3 -m venv path/to/venv
  ```
* Activate the virtual enviroment
  ```
  . ./path/to/venv/Scripts/activate
  ```
  on Windows or
  ```
  . ./path/to/venv/bin/activate
  ```
  on Unix
* Install the dependency libraries with pip

```
pip install flask
pip install flask_wtf
pip install flask_pagedown
pip install markdown
pip install wtforms
pip install mdx_truly_sane_lists
```

* Deactivate the venv
  ```
  deactivate
  ```

Other than Python 3, pip and venv setup, this step can be completed on windows
with setup.ps1 or on unix with setup.sh. The scripts create a folder for venv
in the folder they are run from.

## Running the server

* Set either production or development environment in the config.py
* Set environment variables FLASK_ENV and FLASK_DEBUG to match production or
  development option as in config.py. FLASK_APP should be set to "run.py".
* Set secret keys in config.py to random strings only you know
* Activate the virtual environment
  ```
  . ./path/to/venv/bin/activate
  ```
  on unix and
  ```
  . ./path/to/venv/Scrips/activate
  ```
  on windows
* Run python flask
  ```
  python -m flask run
  ```
* Open browser of your choice on address displayed

Setting the virtual environment and starting the server can be also done with
start.sh or start.ps1 scripts.

## Other dependencies

This tool only requires actual internet connection for single mat4 type dependency.
Fetching this script should be only connection to anywhere other than the machine
running the server. It should also be quite easy to make local copy of that js file
and to change the templates to fetch it from local storage like rest of the scripts.

If this change is made, the tool can be used fully without internet connection,
and is thus suitable for use in places that lack proper connection.

## Security

The tracker is meant to be used locally by the game master, running the server
either on same machine that is used for interface browser or on another computer
on same local area network. There is currently no login system or any other
protections against anyone with internet connection to the machine running the
server from opening the time tracker interface and changing the values there. It
is also perfectly possible to send requests that are accepted to the system
without using the Time Tracker interface. Nothing that is received from these
requests is executed as a code.

As the program makes changes to local copies of its event log files, it might
be possible to send trough request malicious code to be stored on these files.
While the server doesn't execute anything form the files it reads as a code,
there is no filtering for content that the browser might interpret as a executable
script. So potentially the event log could be used to store and distribute client
side malicious code, that has same risks as any other code that could be run on
the browser. This server should not leak any information about the file system
on the server machine, though filling the storage media is possible.

Most likely, the worst you are going to face is angry player trying to set game
clock to a point before their snowflake character died totally of their own fault,
but you still should not left this running for unnecessarily when not in use.

And you should never execute the log files as programs, but generally you should
never run anything that is not meant to be run and known to be safe.

## Configuration

The calendar and timekeeping can be customised using configuration json files.
By default two calendars have been implemented, first is quite close to our
normal calendar, but lacks leap days. Second is a custom calendar used in my
homebrew setting. These are provided as examples of what can be done.

