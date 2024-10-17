Name:		texlive-filehook
Version:	64822
Release:	2
Summary:	Hooks for input files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/filehook
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/filehook.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/filehook.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/filehook.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides several file hooks (AtBegin, AtEnd, ...)
for files read by \input, \include and \InputIfFileExists.
General hooks for all such files (e.g. all \include'd ones) and
file specific hooks only used for named files are provided; two
hooks are provided for the end of \included files -- one
before, and one after the final \clearpage.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/filehook
%doc %{_texmfdistdir}/doc/latex/filehook
#- source
%doc %{_texmfdistdir}/source/latex/filehook

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
