%include	/usr/lib/rpm/macros.perl
%define	pdir	Font
%define	pnam	TTF
Summary:	Font::TTF perl module
Summary(pl):	Modu� perla Font::TTF
Name:		perl-Font-TTF
Version:	0.30
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-XML-Parser
BuildRequires:	rpm-perlprov >= 3.0.3-16
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
%setup -q -n %{pdir}-%{pnam}-0.3

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.TXT lib/Font/TTF/Changes
%attr(755,root,root) %{_bindir}/*.plx
%dir %{perl_sitelib}/Font/TTF
%dir %{perl_sitelib}/Font/TTF/Kern
%dir %{perl_sitelib}/Font/TTF/Mort
%{perl_sitelib}/Font/TTF/Manual.pod
%{perl_sitelib}/Font/TTF/*.pm
%{perl_sitelib}/ttfmod.pl
%{perl_sitelib}/Font/TTF/Kern/*.pm
%{perl_sitelib}/Font/TTF/Mort/*.pm
%{_mandir}/man[13]/*
