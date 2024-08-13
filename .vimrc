call plug#begin()

Plug 'neoclide/coc.nvim',{'branch': 'release'}
Plug 'mattn/vim-lsp-settings'
Plug 'junegunn/fzf'
Plug 'junegunn/fzf.vim'
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'preservim/nerdtree'
Plug 'Xuyuanp/nerdtree-git-plugin'
Plug 'tiagofumo/vim-nerdtree-syntax-highlight'
Plug 'ryanoasis/vim-devicons'
Plug 'airblade/vim-gitgutter'
Plug 'github/copilot.vim'

call plug#end()

nnoremap <leader>n :NERDTreeToggle<CR>

" might not be needed if .vimrc exists?
set nocompatible
syntax on

set path+=**

set number
set relativenumber
set ruler
set visualbell

set wrap

set tabstop=4
set shiftwidth=4
set softtabstop=4
set expandtab

set hlsearch
set ignorecase
set showmatch

set autoindent
"set tildeop
filetype plugin indent on

set spell

set re=0 " for preventing timeout during tsx syntax highlighting
colorscheme torte
