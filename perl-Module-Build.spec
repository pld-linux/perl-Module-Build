#
# Conditional build:
# _without_tests - do not perform "./Build test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Module
%define	pnam	Build
Summary:	Module::Build - build and install Perl modules
Summary(pl):	Module::Build - budowanie i instalowanie modu³ów Perla
Name:		perl-Module-Build
Version:	0.18
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	18f35dc7e5751f8e56554f564293d0bc
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Module::Build is a Perl module to build and install Perl modules. It
is meant to be a replacement for ExtUtils::MakeMaker.

%description -l pl
Module::Build to modu³ Perla do budowania i instalowania modu³ów
Perla. Ma byæ zamiennikiem ExtUtils::MakeMaker.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	config="sitelib=%{perl_vendorlib} sitearch=%{perl_vendorarch}"

./Build

for f in `find lib -name '*.pm'`; do
	pod2man $f `basename $f .pm`.3pm
done

%{!?_without_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install \
	destdir=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man3

install Build.3pm $RPM_BUILD_ROOT%{_mandir}/man3/Module::Build.3pm
install Base.3pm $RPM_BUILD_ROOT%{_mandir}/man3/Module::Build::Base.3pm
install Compat.3pm $RPM_BUILD_ROOT%{_mandir}/man3/Module::Build::Compat.3pm
install Unix.3pm $RPM_BUILD_ROOT%{_mandir}/man3/Module::Build::Platform::Unix.3pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Module/Build.pm
%dir %{perl_vendorlib}/Module/Build
%{perl_vendorlib}/Module/Build/*.pm
%dir %{perl_vendorlib}/Module/Build/Platform
%{perl_vendorlib}/Module/Build/Platform/Unix.pm
%{_mandir}/man3/*
