#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

if [[ -z $DISPLAY ]] && [[ $(tty) = /dev/tty1 ]]; then
    startx
fi

# unlimited history
export HISTFILESIZE=
export HISTSIZE=


function exitstatus()
{
    if [[ $? == 0 ]] then
        echo -en "\e[32m\xE2\x9C\x94\e[0m"
    else
        echo -en "\e[31m\xE2\x9C\x97\e[0m"
    fi
}

function gitbranch()
{
    BRANCH=$(git branch 2>/dev/null)
    if [[ $? == 0 ]] then
        echo -en "(\e[36m$BRANCH\e[0m)"
    fi
}

alias ls='ls --color=auto'
alias ll='ls -l'
alias la='ls -la'
alias grep='grep --color=auto'
alias rmr='rm -r'

PROMPT_COMMAND='ESTATUS=$(exitstatus)'
PS1='\[$(tput sc; tput cuf $((COLUMNS - 5)))\A$(tput rc)\][\u@\h $ESTATUS]$(gitbranch)\n$(pwd)$ '
