%include	/usr/lib/rpm/macros.perl
Summary:	Font-TTF perl module
Summary(pl):	Modu� perla Font-TTF
Name:		perl-Font-TTF
Version:	0.20
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Font/Font-TTF-%{version}.tar.gz
Patch0:		%{name}-man.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Font-TTF - Perl module for TrueType font hacking. In short, you can do
almost anything with a standard TrueType font with this module.

%description -l pl
Font-TTF - modu� perla do operacji na fontach TrueType. W skr�cie,
u�ywaj�c tego modu�u mo�esz robi� niemal wszystko ze standardowym
fontem TrueType.

%prep
%setup -q -n Font-TTF-%{version}
%patch -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README.TXT lib/Font/TTF/Changes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz lib/Font/TTF/*.gz
%attr(755,root,root) %{_bindir}/*.plx
%{perl_sitelib}/Ttfmod.pl
%dir %{perl_sitelib}/Font/TTF
%{perl_sitelib}/Font/TTF/*.pm
%{_mandir}/man3/*
