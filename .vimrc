" Uncomment for plugins you want to use
"
" call plug#begin()
"
" Plug 'neoclide/coc.nvim',{'branch': 'release'}
" Plug 'mattn/vim-lsp-settings'
" Plug 'junegunn/fzf'
" Plug 'junegunn/fzf.vim'
" Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
" Plug 'preservim/nerdtree'
" Plug 'Xuyuanp/nerdtree-git-plugin'
" Plug 'tiagofumo/vim-nerdtree-syntax-highlight'
" Plug 'ryanoasis/vim-devicons'
" Plug 'airblade/vim-gitgutter'
" Plug 'github/copilot.vim'
" Plug 'jreybert/vimagit'
"
" call plug#end()
"
" nnoremap <leader>n :NERDTreeToggle<CR>

let mapleader = ' '

" turn of vi compatability
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

" Save when running make
set autowrite
" set tildeop
" filetype plugin indent on

" set spell

" set re=0 " for preventing timeout during tsx syntax highlighting
colorscheme torte
" colorscheme pablo

map <leader>t :term<CR>
map <leader>m :make<CR>
map <leader>c :make %<CR>
map <leader>h :noh<CR>
map <leader>w :set list<CR>
map <leader>t :%s/ \+$//gc<CR>
