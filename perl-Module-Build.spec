#
# Conditional build:
# _without_tests - do not perform "./Build test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Module
%define	pnam	Build
Summary:	Module::Build - build and install Perl modules
Summary(pl):	Module::Build - budowanie i instalowanie modu��w Perla
Name:		perl-Module-Build
Version:	0.20
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0a9e596924b9ef35142d085a5ef80294
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Module::Build is a Perl module to build and install Perl modules. It
is meant to be a replacement for ExtUtils::MakeMaker.

%description -l pl
Module::Build to modu� Perla do budowania i instalowania modu��w
Perla. Ma by� zamiennikiem ExtUtils::MakeMaker.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	installdirs=vendor
./Build

%{!?_without_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install \
	destdir=$RPM_BUILD_ROOT

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
# We don't need them, i guess
%exclude %{_mandir}/man3/Module::Build::Platform::*