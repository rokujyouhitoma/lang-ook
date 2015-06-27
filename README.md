# README

## Requirements

```
$ pip install -r requirements.txt
```
or

```
$ pip install rpython
```

## Translate

### pure python

```
$ python ook.py <input ook file>
```

### rpython

```
$ rpython ook.py
$ ./ook-c <input ook file>
```

### rpython with jit

```
$ rpython --opt=jit ook-jit.py
$ ./ook-jit-c <input ook file>
```

### rpython with jit, optimization

```
$ rpython --opt=jit ook-jit2.py
$ ./ook-jit2-c <input ook file>
```

### rpython with jit, debug=True

```
$ rpython --opt=jit ook-jit-debug.py
./ook-jit-debug-c <input ook file>
```

## Run with output log file

```
$ PYPYLOG=<log file> ./ook-jit-debug-c <input ook file>
```

```
$ python ${RPython}/rpython/tool/logparser.py draw-time <log file> <output.png file>
```
