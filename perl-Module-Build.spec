#
# Conditional build:
%bcond_without	tests	# do not perform "./Build test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Module
%define		pnam	Build
Summary:	Module::Build - build and install Perl modules
Summary(pl.UTF-8):	Module::Build - budowanie i instalowanie modułów Perla
Name:		perl-Module-Build
Version:	0.3800
Release:	2
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DA/DAGOLDEN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b9e3085a2f314c2dea2274bd5ab16236
Patch0:		%{name}-startperl.patch
URL:		http://search.cpan.org/dist/Module-Build/
BuildRequires:	perl(File::Spec) >= 0.82
%if %{with tests}
BuildRequires:	perl-CPAN-Meta
BuildRequires:	perl-ExtUtils-CBuilder >= 0.27
BuildRequires:	perl-ExtUtils-ParseXS >= 1.02
BuildRequires:	perl-Parse-CPAN-Meta >= 1.4401
BuildRequires:	perl-YAML > 0.49_01
%endif
BuildRequires:	perl-CPAN-Meta-YAML
BuildRequires:	perl-Module-Metadata >= 1.000002
BuildRequires:	perl-Perl-OSType >= 1.00
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-version >= 1:0.87
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Module::Build is a Perl module to build and install Perl modules. It
is meant to be a replacement for ExtUtils::MakeMaker.

%description -l pl.UTF-8
Module::Build to moduł Perla do budowania i instalowania modułów
Perla. Ma być zamiennikiem ExtUtils::MakeMaker.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

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
%attr(755,root,root) %{_bindir}/config_data
%{perl_vendorlib}/Module/Build.pm
%dir %{perl_vendorlib}/Module/Build
%{perl_vendorlib}/Module/Build/*.pm
%dir %{perl_vendorlib}/Module/Build/Platform
%{perl_vendorlib}/Module/Build/Platform/Unix.pm
%{_mandir}/man1/config_data.1*
%{_mandir}/man3/Module::Build.*
%{_mandir}/man3/Module::Build::PP*
%{_mandir}/man3/Module::Build::[!P]*
%{_mandir}/man3/Module::Build::Platform::Unix*
