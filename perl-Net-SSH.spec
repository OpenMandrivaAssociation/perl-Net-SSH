%define upstream_name	 Net-SSH
%define upstream_version 0.09
Name:		perl-%{upstream_name}
Version:	2.14
Release:	1

Summary:	%{upstream_name} module for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Net-SSH
Source0:	https://cpan.metacpan.org/authors/id/I/IV/IVAN/Net-SSH-0.09.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Simple wrappers around ssh commands.

%prep
%setup -q -n Net-SSH-0.09

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


