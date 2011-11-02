Name:		texlive-kastrup
Version:	20111102
Release:	1
Summary:	TeXLive kastrup package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kastrup.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kastrup.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kastrup.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
TeXLive kastrup package.

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
%{_texmfdistdir}/tex/generic/kastrup/binhex.tex
%doc %{_texmfdistdir}/doc/generic/kastrup/binhex.pdf
#- source
%doc %{_texmfdistdir}/source/generic/kastrup/binhex.drv
%doc %{_texmfdistdir}/source/generic/kastrup/binhex.dtx
%doc %{_texmfdistdir}/source/generic/kastrup/binhex.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
