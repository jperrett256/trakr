# trakr

## Usage

```
trakr command [options]
```

## Examples

Show tasks
Add or remove tasks (force remove if task has sessions associated with it)
Rename tasks

```
trakr task
trakr task "name"
trakr task -d "name"
trakr task -D "name"
trakr task -m "new name"
trakr task -m "old name" "new name" (?)
```

Set current task
Will pause ongoing session if active

```
trakr switch "task name"
trakr switch -n "new task name"
```

Show previous sessions on current task

```
trakr log
```

Show ongoing session(s)
	- only one session may be active at a time (other sessions, if ongoing, are paused)
Start a new session
Pause or stop the ongoing session

```
trakr session
trakr session --all
trakr session start
trakr session pause
trakr session stop

```

TODO commands for directly:
	- moving sessions to another task
	- editing existing sessions
	- creating new sessions
	- splitting existing sessions (?)
and generally fixing mistakes

```
trakr edit TODO
```

TODO commands for analysing session data

```
trakr analyse
```

Set preferences:
- for editor (default vim)
- data file location
- TODO
