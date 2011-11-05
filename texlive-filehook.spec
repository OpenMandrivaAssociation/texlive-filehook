# revision 24280
# category Package
# catalog-ctan /macros/latex/contrib/filehook
# catalog-date 2011-10-13 10:45:00 +0200
# catalog-license lppl1.3
# catalog-version 0.5d
Name:		texlive-filehook
Version:	0.5d
Release:	1
Summary:	Hooks for input files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/filehook
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/filehook.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/filehook.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/filehook.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides several file hooks (AtBegin, AtEnd, ...)
for files read by \input, \include and \InputIfFileExists.
General hooks for all such files (e.g. all \include'd ones) and
file specific hooks only used for named files are provided; two
hooks are provided for the end of \included files -- one
before, and one after the final \clearpage.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/filehook/filehook-fink.sty
%{_texmfdistdir}/tex/latex/filehook/filehook-listings.sty
%{_texmfdistdir}/tex/latex/filehook/filehook-memoir.sty
%{_texmfdistdir}/tex/latex/filehook/filehook-scrlfile.sty
%{_texmfdistdir}/tex/latex/filehook/filehook.sty
%{_texmfdistdir}/tex/latex/filehook/pgf-filehook.sty
%doc %{_texmfdistdir}/doc/latex/filehook/README
%doc %{_texmfdistdir}/doc/latex/filehook/filehook.pdf
#- source
%doc %{_texmfdistdir}/source/latex/filehook/filehook.dtx
%doc %{_texmfdistdir}/source/latex/filehook/filehook.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
