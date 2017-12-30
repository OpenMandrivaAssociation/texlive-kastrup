# revision 15878
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-kastrup
Version:	20170414
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111103-2
+ Revision: 752979
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111103-1
+ Revision: 718768
- texlive-kastrup
- texlive-kastrup
- texlive-kastrup
- texlive-kastrup

