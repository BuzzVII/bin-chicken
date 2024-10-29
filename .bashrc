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
    BRANCH=$( git branch 2>/dev/null | grep "*" - )
    if [[ $BRANCH ]] then
        echo -n "("
        if  [[ -n $(git status -s) ]]; then
            echo -en "\e[1;41m"
        else
            BRANCH=$(echo -en "$BRANCH" | sed -e's/^* //')
        fi
        echo -en "\e[1;36m$BRANCH\e[0m)"
    fi

}


function truncateword()
{
    WORD=$1
    LEN=$2
    DLEN=$(awk "BEGIN { d= 2*$LEN; print d}")
    WORDLEN=$(echo -en "$WORD" | wc -c)
    if [[ WORDLEN -ge DLEN ]]; then
        WORD=$(echo -en "$WORD" | head -c$LEN )"..."$(echo -en "$WORD" | tail -c$LEN)
    fi
    echo -en "$WORD"
}

alias ls='ls --color=auto'
alias ll='ls -l'
alias la='ls -la'
alias grep='grep --color=auto'
alias rmr='rm -r'

PROMPT_COMMAND='ESTATUS=$(exitstatus)'
# PS1='$(tput sc; tput cuf $((columns - 5)))\a$(tput rc)\]\[[\u@\h $ESTATUS]$(gitbranch)\n\[\e[1;37m\]$(truncateword $PWD 30 )\[\e[1;33m\]$\[\e[0m\] '
PS1='[\u@\h $ESTATUS]$(gitbranch)\[\n\e[1;37m\]$(truncateword $PWD 10 )\[\e[1;33m\]$\[\e[0m\] '

