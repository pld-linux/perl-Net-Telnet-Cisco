%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	Telnet-Cisco
Summary:	Net-Telnet-Cisco perl module
Summary(pl):	Modu³ perla Net-Telnet-Cisco
Name:		perl-%{pdir}-%{pnam}
Version:	1.08
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-Net-Telnet
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Term-ReadKey
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net-Telnet-Cisco - interact with TELNET port on Cisco routers.

%description -l pl
Net-Telnet - wsparcie dla protoko³u TELNET na urz±dzeniach Cisco.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Net/Telnet/Cisco.pm
%{_mandir}/man3/*
