#
# Conditional build:
%bcond_without	tests	# do not perform "./Build test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Module
%define	pnam	Build
Summary:	Module::Build - build and install Perl modules
Summary(pl):	Module::Build - budowanie i instalowanie modu��w Perla
Name:		perl-Module-Build
Version:	0.25
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fbcf9fcbd1de321eb781ee8271bffd73
BuildRequires:	perl-devel
BuildRequires:	rpm-perlprov >= 4.0.2-104
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
%{perl_sitelib}/Module/Build.pm
%dir %{perl_sitelib}/Module/Build
%{perl_sitelib}/Module/Build/*.pm
%dir %{perl_sitelib}/Module/Build/Platform
%{perl_sitelib}/Module/Build/Platform/Unix.pm
%{_mandir}/man3/*
# We don't need them, i guess
%exclude %{_mandir}/man3/Module::Build::Platform::*
