#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	Telnet-Cisco
Summary:	Net::Telnet::Cisco Perl module
Summary(cs):	Modul Net::Telnet::Cisco pro Perl
Summary(da):	Perlmodul Net::Telnet::Cisco
Summary(de):	Net::Telnet::Cisco Perl Modul
Summary(es):	M�dulo de Perl Net::Telnet::Cisco
Summary(fr):	Module Perl Net::Telnet::Cisco
Summary(it):	Modulo di Perl Net::Telnet::Cisco
Summary(ja):	Net::Telnet::Cisco Perl �⥸�塼��
Summary(ko):	Net::Telnet::Cisco �� ����
Summary(no):	Perlmodul Net::Telnet::Cisco
Summary(pl):	Modu� Perla Net::Telnet::Cisco
Summary(pt):	M�dulo de Perl Net::Telnet::Cisco
Summary(pt_BR):	M�dulo Perl Net::Telnet::Cisco
Summary(ru):	������ ��� Perl Net::Telnet::Cisco
Summary(sv):	Net::Telnet::Cisco Perlmodul
Summary(uk):	������ ��� Perl Net::Telnet::Cisco
Summary(zh_CN):	Net::Telnet::Cisco Perl ģ��
Name:		perl-%{pdir}-%{pnam}
Version:	1.10
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-Net-Telnet
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Term-ReadKey
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Telnet::Cisco - interact with TELNET port on Cisco routers.

%description -l pl
Net::Telnet::Cisco - wsparcie dla protoko�u TELNET na urz�dzeniach
Cisco.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_sitelib}/Net/Telnet
%dir %{perl_sitelib}/auto/Net/Telnet
# empty autosplit.ix
#%dir %{perl_sitelib}/auto/Net/Telnet/Cisco
#%{perl_sitelib}/auto/Net/Telnet/Cisco/autosplit.ix
%{_mandir}/man3/*
