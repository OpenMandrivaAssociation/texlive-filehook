%global tl_name filehook
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.8b
Release:	%{tl_revision}.1
Summary:	Hooks for input files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/filehook
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/filehook.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/filehook.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/filehook.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides several file hooks (AtBegin, AtEnd, ...) for files
read by \input, \include and \InputIfFileExists. General hooks for all
such files (e.g. all \included ones) and file specific hooks only used
for named files are provided; two hooks are provided for the end of
\included files -- one before, and one after the final \clearpage.

