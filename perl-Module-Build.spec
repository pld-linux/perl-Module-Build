#
# Conditional build:
%bcond_without	tests	# do not perform "./Build test"
#
%define		pdir	Module
%define		pnam	Build
Summary:	Module::Build - build and install Perl modules
Summary(pl.UTF-8):	Module::Build - budowanie i instalowanie modułów Perla
Name:		perl-Module-Build
Version:	0.4231
Release:	2
Epoch:		2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Module/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	066b193e461d7dfe1eca17a139353001
Patch0:		%{name}-startperl.patch
URL:		https://metacpan.org/release/Module-Build
BuildRequires:	perl(File::Spec) >= 0.82
BuildRequires:	perl(version) >= 0.87
BuildRequires:	perl-Module-Metadata >= 1.000002
BuildRequires:	perl-Perl-OSType >= 1.00
BuildRequires:	perl-devel >= 1:5.8.0
# perl-modules provides version's version without epoch, so use perl(version) dep
#BuildRequires:	perl-version >= 1:0.87
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-CPAN-Meta >= 2.142060
BuildRequires:	perl-CPAN-Meta-YAML >= 0.003
BuildRequires:	perl-ExtUtils-CBuilder >= 0.27
BuildRequires:	perl-ExtUtils-ParseXS >= 2.21
BuildRequires:	perl-File-Temp >= 0.15
BuildRequires:	perl-Parse-CPAN-Meta >= 1.4401
BuildRequires:	perl-Test-Harness >= 3.29
BuildRequires:	perl-Test-Simple >= 0.49
%endif
BuildConflicts:	perl(CPANPLUS::Dist::Build) < 0.08
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
%patch -P0 -p1

%build
%{__perl} Build.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Module/Build/*.pod
for s in Default MacOS VMS VOS Windows aix cygwin darwin os2 ; do
	%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Module/Build/Platform/${s}.pm
	%{__rm} $RPM_BUILD_ROOT%{_mandir}/man3/Module::Build::Platform::${s}.3pm
done

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
%{_mandir}/man3/Module::Build.3pm*
%{_mandir}/man3/Module::Build::[!P]*.3pm*
%{_mandir}/man3/Module::Build::PPMMaker.3pm*
%{_mandir}/man3/Module::Build::Platform::Unix.3pm*
