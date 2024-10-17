Name:		texlive-mpostinl
Version:	49559
Release:	2
Summary:	Embed MetaPost figures within LaTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mpostinl
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mpostinl.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mpostinl.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mpostinl.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX2e package enables the embedding of MetaPost figures
within LaTeX documents. The package automatically collects the
embedded definitions and figures in a .mp file, adds an
appropriate LaTeX document structure, and compiles it to .mps
files. It also allows for various configuration options to
manage the generation of files and compilation.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/mpostinl
%{_texmfdistdir}/tex/latex/mpostinl
%doc %{_texmfdistdir}/doc/latex/mpostinl

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
