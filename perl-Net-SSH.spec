%define module	Net-SSH
%define name	perl-%{module}
%define version 0.09
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{module} module for perl
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif

%description
Simple wrappers around ssh commands.

%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%{makeinstall_std}

%check
make test

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Net
%{_mandir}/*/*

