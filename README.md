### Overview

Fishtest is a distributed task queue for testing chess engines.  The main instance
for Stockfish is http://tests.stockfishchess.org

It is currently being used for testing changes on Stockfish, using tens of thousands
of games, both on Linux and Windows.  The following setup describes a step-by-step
installation for a machine that will run test matches (a worker).

#### Setup Python on Windows

On Windows you will need to install Python 2.7.x for x86 (not 3.x series and not
64 bit) from http://www.python.org/ftp/python/2.7.4/python-2.7.4.msi

In case something is not clear please read windows-step-by-step-installation.txt

#### Setup fishtest

You can download fishtest directly from Github:

https://github.com/glinscott/fishtest/archive/master.zip

or, in case you have a git installation, you can clone it.

```
git clone https://github.com/glinscott/fishtest.git
```

#### Get username/password

Please e-mail me at gmail.com, username "glinscott", and we will give you your username and password.

### Launching the worker

To launch the worker open a console window in *fishtest/worker* directory and run
the following command (after changing *concurrency* to the correct value for
your system, see below), providing username and password you've been given.

```
python worker.py --concurrency 3 username password
```
or, after the first access, a simple
```
python worker.py
```

Option *concurrency* refers to the number of available cores in your system (not
including Hyperthreaded cores!), leaving one core for the OS.  For example,
on my 4 core machine, I use `--concurrency 3`.

On Linux, you can use the `nohup` command to run the worker as a background task.

```
nohup python worker.py &
```

#### Override default make command

Once launched, fishtest will automatically connect to host, download the book,
the cutechess-cli game manager and the engine sources that will be compiled
according to the type of worker platform. If default make command is not suitable
for you, for instance if you need to use some other compiler than gcc/mingw,
then you can create a `custom_make.txt` file in *fishtest/worker* directory,
containing a single line command that fishtest will run to compile the sources.

### Running the website

This is only if you wish to run your own testing environment (ie. you are testing
changes on another engine). As a pre-requisite, the website needs a mongodb instance.
By default it assumes there is one running on localhost.  You can set FISHTEST_HOST
environment variable to connect to a different host. To launch a development version
of the site, open a console window in *fishtest/fishtest* directory and do:

```
sudo python setup.py develop
./start.sh
```


In German

C:\fishtest-master\fishtest-master\worker>C:\Python27\python.exe worker.py --concurrency 5 username password
Dann einfach Enter drücken und fertig.
Am besten ihr speichert euch diesen Satz bei Word mit eurem richtigen username und password, dann könnt ihr den Satz ganz einfach und vor allem sehr schnell mit copy und paste in das schwarze Fenster einfügen.

Ein kleiner Trick:
https://github.com/glinscott/fishtest/blob/master/README.md download http://www.python.org/ftp/python/2.7.4/python-2.7.4.msi und https://github.com/glinscott/fishtest/archive/master.zip installiert beide unter C. Danach:
Man geht auf Lokaler Datenträger C Doppelklick, fishtest-master Doppelklick, fishtest-master Doppelklick, worker Doppelklick und jetzt einfach nichts auswählen, sondern auf der leeren weißen Fläche linke Umschalttaste + rechte Maustaste klicken.
Dann öffnet sich ein kleines Fenster, dort Eingabeaufforderung hier öffnen anklicken.
Jetzt hat sich das schwarze Fenster geöffnet in dem steht jetzt C:\fishtest-master\fishtest-master\worker>
Ihr müsst jetzt nur noch dahinter C:\Python27\python.exe worker.py --concurrency 5 username password eingeben.

--concurrency bedeutet Anzahl der Kerne die euer PC hat.
Mein PC hat 6 Kerne deshalb habe ich --concurrency 5 eingegeben, da 1 Kern fürs Betriebssystem und für die unsichtbaren PC/Windows Programme nötig ist.
Habt ihr 1 Kern gebt ihr --concurrency 1 ein
Habt ihr 2 Kerne gebt ihr --concurrency 1 ein
Habt ihr 4 Kerne gebt ihr --concurrency 3 ein
Habt ihr 6 Kerne gebt ihr --concurrency 5 ein
Habt ihr 8 Kerne gebt ihr --concurrency 7 ein
Habt ihr 12 Kerne gebt ihr --concurrency 11 ein
Habt ihr 16 Kerne gebt ihr --concurrency 15 ein
Habt ihr 32 Kerne gebt ihr --concurrency 31 ein
Habt ihr 64 Kerne gebt ihr --concurrency 63 ein
