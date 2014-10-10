%define upstream_name	 Net-SSH
%define upstream_version 0.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	%{upstream_name} module for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Simple wrappers around ssh commands.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
make test

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Net
%{_mandir}/*/*


%changelog
* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.90.0-1mdv2010.0
+ Revision: 404246
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.09-2mdv2009.0
+ Revision: 268626
- rebuild early 2009.0 package (before pixel changes)

* Sat May 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-1mdv2009.0
+ Revision: 208357
- update to new version 0.09

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-7mdv2008.0
+ Revision: 86710
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-6mdv2007.0
- Rebuild

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.08-5mdk
- Fix SPEC according to Perl Policy
	- Source URL
- use mkrel

* Mon Jun 06 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-4mdk 
- better url
- drop useless empty directories
- spec cleanup
- make test in %%check

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.08-3mdk
- fix buildrequires in a backward compatible way

* Thu Jun 03 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.08-2mdk
- fix perms

* Wed Apr 21 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.08-1mdk
- new version
- rpmbuildupdate aware
- dir ownership
- no more explicit dependencies, let spec-helper do its job

