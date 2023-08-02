#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Class-MethodMaker
Version  : 2.24
Release  : 27
URL      : https://cpan.metacpan.org/authors/id/S/SC/SCHWIGON/class-methodmaker/Class-MethodMaker-2.24.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SC/SCHWIGON/class-methodmaker/Class-MethodMaker-2.24.tar.gz
Summary  : 'a module for creating generic methods'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Class-MethodMaker-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Perl Module Class::MethodMaker:
Easy building of Perl Classes
Description:
Modules & Classes:

%package dev
Summary: dev components for the perl-Class-MethodMaker package.
Group: Development
Provides: perl-Class-MethodMaker-devel = %{version}-%{release}
Requires: perl-Class-MethodMaker = %{version}-%{release}

%description dev
dev components for the perl-Class-MethodMaker package.


%package perl
Summary: perl components for the perl-Class-MethodMaker package.
Group: Default
Requires: perl-Class-MethodMaker = %{version}-%{release}

%description perl
perl components for the perl-Class-MethodMaker package.


%prep
%setup -q -n Class-MethodMaker-2.24
cd %{_builddir}/Class-MethodMaker-2.24

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Class::MethodMaker.3
/usr/share/man/man3/Class::MethodMaker::Constants.3
/usr/share/man/man3/Class::MethodMaker::Engine.3
/usr/share/man/man3/Class::MethodMaker::OptExt.3
/usr/share/man/man3/Class::MethodMaker::V1Compat.3
/usr/share/man/man3/Class::MethodMaker::array.3
/usr/share/man/man3/Class::MethodMaker::hash.3
/usr/share/man/man3/Class::MethodMaker::scalar.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
