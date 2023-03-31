Name:		texlive-kastrup
Version:	15878
Release:	2
Summary:	TeXLive kastrup package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kastrup.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kastrup.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kastrup.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive kastrup package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
