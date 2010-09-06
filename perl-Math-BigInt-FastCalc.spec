%define upstream_name    Math-BigInt-FastCalc
%define upstream_version 0.21

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Math::BigInt::Calc with some XS for more speed
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Math/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl-Math-BigInt >= 1.900.0
BuildRequires: perl(Test::More)

BuildRequires: perl-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}


%description
In order to allow for multiple big integer libraries, Math::BigInt was
rewritten to use library modules for core math routines. Any module which
follows the same API as this can be used instead by using the following:

	use Math::BigInt lib => 'libname';

'libname' is either the long name ('Math::BigInt::Pari'), or only the short
version like 'Pari'. To use this library:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README CHANGES META.yml
%{_mandir}/man3/*
%perl_vendorlib/*
