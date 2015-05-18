#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Font
%define		pnam	TTF
Summary:	Font::TTF - Perl module for TrueType font hacking
Summary(pl.UTF-8):	Font::TTF - moduł Perla do operacji na fontach TrueType
Name:		perl-Font-TTF
Version:	1.05
Release:	1
License:	Artistic v2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Font/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a9d0acf4cb9ebaee875d71732b83dfe5
URL:		http://search.cpan.org/dist/Font-TTF/
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Font::TTF is a Perl module for TrueType font hacking. In short, you
can do almost anything with a standard TrueType font with this module.

%description -l pl.UTF-8
Font::TTF - moduł Perla do operacji na fontach TrueType. W skrócie,
używając tego modułu można zrobić niemal wszystko ze standardowym
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

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Font/TTF/{Changes_old.txt,Manual.pod}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CONTRIBUTORS Changes README.TXT TODO
%dir %{perl_vendorlib}/Font/TTF
%dir %{perl_vendorlib}/Font/TTF/Kern
%dir %{perl_vendorlib}/Font/TTF/Mort
%dir %{perl_vendorlib}/Font/TTF/Woff
%dir %{perl_vendorlib}/Font/TTF/Features
%{perl_vendorlib}/Font/TTF.pm
%{perl_vendorlib}/Font/TTF/*.pm
%{perl_vendorlib}/Font/TTF/Kern/*.pm
%{perl_vendorlib}/Font/TTF/Mort/*.pm
%{perl_vendorlib}/Font/TTF/Woff/*.pm
%{perl_vendorlib}/Font/TTF/Features/*.pm
%{perl_vendorlib}/ttfmod.pl
%{_mandir}/man3/Font::TTF*.3pm*
%{_mandir}/man3/ttfmod.3pm*
