%global tl_name mpostinl
%global tl_revision 77187

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5.3
Release:	%{tl_revision}.1
Summary:	Embed MetaPost figures within LaTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mpostinl
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mpostinl.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mpostinl.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mpostinl.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX2e package enables the embedding of MetaPost figures within
LaTeX documents. The package automatically collects the embedded
definitions and figures in a .mp file, adds an appropriate LaTeX
document structure, and compiles it to .mps files. It also allows for
various configuration options to manage the generation of files and
compilation.

