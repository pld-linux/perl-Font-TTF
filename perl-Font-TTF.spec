#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Font
%define	pnam	TTF
Summary:	Font::TTF - Perl module for TrueType font hacking
Summary(pl):	Font::TTF - modu� Perla do operacji na fontach TrueType
Name:		perl-Font-TTF
Version:	0.34
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3b0354a25650899cbec767f4b147f526
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-XML-Parser
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Font::TTF is a Perl module for TrueType font hacking. In short, you
can do almost anything with a standard TrueType font with this module.

%description -l pl
Font::TTF - modu� Perla do operacji na fontach TrueType. W skr�cie,
u�ywaj�c tego modu�u mo�na zrobi� niemal wszystko ze standardowym
fontem TrueType.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
