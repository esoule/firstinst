#!/bin/bash
source /usr/lib/firstinst/firstinst-functions

cat <<"__GITCONFIG__" >/etc/gitconfig
[core]
	editor = vim
[color]
	branch = auto
	diff = auto
	grep = auto
	interactive = auto
	showbranch = auto
	status = auto
	ui = auto
[alias]
	lol = log --graph --decorate --pretty=oneline --abbrev-commit
	lola = log --graph --decorate --pretty=oneline --abbrev-commit --all
	logf = log --name-status --format=fuller --decorate
	co = checkout
	br = branch
	st = status
[log]
	date = iso
__GITCONFIG__

chmod 0644 /etc/gitconfig
/sbin/restorecon /etc/gitconfig
