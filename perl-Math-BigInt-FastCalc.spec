%define upstream_name    Math-BigInt-FastCalc
%define upstream_version 0.30

Name:       perl-%{upstream_name}
Version:    %perl_convert_version 0.30
Release:	1

Summary:    Math::BigInt::Calc with some XS for more speed
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Math/Math-BigInt-FastCalc-0.30.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl-Math-BigInt >= 1.991
BuildRequires: perl(Math::BigInt::Calc) >= 0.56
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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.290.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Mon Jul 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.290.0-1
+ Revision: 690284
- update to new version 0.29

* Sat Mar 12 2011 Funda Wang <fwang@mandriva.org> 0.280.0-1
+ Revision: 643952
- new version 0.28
- rebuild
- rebuild

* Sun Feb 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.260.0-1
+ Revision: 637635
- update to new version 0.26

* Tue Feb 08 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.251.0-1
+ Revision: 636794
- update to new version 0.251

* Sun Nov 14 2010 Jérôme Quelin <jquelin@mandriva.org> 0.240.0-1mdv2011.0
+ Revision: 597486
- update to 0.24

* Mon Sep 06 2010 Jérôme Quelin <jquelin@mandriva.org> 0.210.0-1mdv2011.0
+ Revision: 576338
- buildrequires: update
- update buildrequires:
- update to 0.21

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.190.0-2mdv2011.0
+ Revision: 556002
- rebuild for perl 5.12

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.190.0-1mdv2010.0
+ Revision: 401636
- rebuild using %%perl_convert_version
- fixed license field

* Mon May 11 2009 Jérôme Quelin <jquelin@mandriva.org> 0.19-1mdv2010.0
+ Revision: 374541
- import perl-Math-BigInt-FastCalc


* Mon May 11 2009 cpan2dist 0.19-1mdv
- initial mdv release, generated with cpan2dist


