VS Code workspaceStorage Cleaner
================================

Problem
-------

It is a well-known problem with VS Code that the `workspaceStorage`
cache folder can grow really big (easily 10+ GB).

How to keep its size acceptable?

Solution
--------

This folder is located at `~/.config/Code/User/workspaceStorage` (under Linux).
It's a good idea to move it somewhere else (e.g. on an external hard drive) and
put a symbolic link on it. This way it's out of your HOME directory.

But, the problem is still there: this folder can grow really big if you use
VS Code extensively. In this case, you can use this script. It checks
the date of the last modification of each cache folder and if they
are too old, then they are deleted.

(These are cache folders, so even if you delete one by accident, VS Code
can re-create it.)

Usage
-----

* Put this script in the folder `~/.config/Code/User/workspaceStorage` (under Linux).
* Modify `LIMIT` as you wish.
* Leave `DRY_RUN = True` and execute it.
* If the output is OK and you want to get rid of the old folders,
  set `DRY_RUN = False` and re-execute the script. This time the old
  folders will be deleted.
