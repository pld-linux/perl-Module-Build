#
# Conditional build:
%bcond_without	tests	# do not perform "./Build test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Module
%define	pnam	Build
Summary:	Module::Build - build and install Perl modules
Summary(pl):	Module::Build - budowanie i instalowanie modu³ów Perla
Name:		perl-Module-Build
Version:	0.25
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fbcf9fcbd1de321eb781ee8271bffd73
BuildRequires:	perl-devel >= 1:5.8.0
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
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT
./Build
%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install 

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
