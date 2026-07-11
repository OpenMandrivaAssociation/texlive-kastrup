%global tl_name kastrup
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Convert numbers into binary, octal and hexadecimal
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/kastrup
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kastrup.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kastrup.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kastrup.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides expandable macros for both fixed-width and minimum-width
numbers to bases 2, 4, 8 and 16.

