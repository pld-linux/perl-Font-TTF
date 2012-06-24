#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Font
%define	pnam	TTF
Summary:	Font::TTF Perl module
Summary(cs):	Modul Font::TTF pro Perl
Summary(da):	Perlmodul Font::TTF
Summary(de):	Font::TTF Perl Modul
Summary(es):	M�dulo de Perl Font::TTF
Summary(fr):	Module Perl Font::TTF
Summary(it):	Modulo di Perl Font::TTF
Summary(ja):	Font::TTF Perl �⥸�塼��
Summary(ko):	Font::TTF �� ����
Summary(no):	Perlmodul Font::TTF
Summary(pl):	Modu� Perla Font::TTF
Summary(pt):	M�dulo de Perl Font::TTF
Summary(pt_BR):	M�dulo Perl Font::TTF
Summary(ru):	������ ��� Perl Font::TTF
Summary(sv):	Font::TTF Perlmodul
Summary(uk):	������ ��� Perl Font::TTF
Summary(zh_CN):	Font::TTF Perl ģ��
Name:		perl-Font-TTF
Version:	0.32
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-XML-Parser
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Font::TTF - Perl module for TrueType font hacking. In short, you can do
almost anything with a standard TrueType font with this module.

%description -l pl
Font::TTF - modu� perla do operacji na fontach TrueType. W skr�cie,
u�ywaj�c tego modu�u mo�esz robi� niemal wszystko ze standardowym
fontem TrueType.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.TXT lib/Font/TTF/Changes
%attr(755,root,root) %{_bindir}/*.plx
%dir %{perl_vendorlib}/Font/TTF
%dir %{perl_vendorlib}/Font/TTF/Kern
%dir %{perl_vendorlib}/Font/TTF/Mort
%{perl_vendorlib}/Font/TTF/Manual.pod
%{perl_vendorlib}/Font/TTF/*.pm
%{perl_vendorlib}/ttfmod.pl
%{perl_vendorlib}/Font/TTF/Kern/*.pm
%{perl_vendorlib}/Font/TTF/Mort/*.pm
%{_mandir}/man[13]/*
