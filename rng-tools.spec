Summary:	Random number generator related utilities
Summary(pl.UTF-8):	Narzędzia do generatora liczb losowych
Name:		rng-tools
Version:	6.15
Release:	1
License:	GPL v2+
Group:		Base
Source0:	https://github.com/nhorman/rng-tools/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	75a5c1526fa98beccffbe0e691adfe75
Source1:	rngd.service
Source2:	rngd.sysconfig
URL:		https://github.com/nhorman/rng-tools/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	jansson-devel
BuildRequires:	jitterentropy-devel
BuildRequires:	libp11-devel
BuildRequires:	librtlsdr-devel
BuildRequires:	libxml2-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.671
Requires:	systemd-units >= 38
Suggests:	opensc
Obsoletes:	rng-utils < 1:2.0-4.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
Hardware random number generation tools.

%description -l pl.UTF-8
Narzędzia wspierające sprzętowe generowanie liczb losowych.

%prep
%setup -q

%{__sed} -i -e 's@PKCS11_ENGINE=.*@PKCS11_ENGINE=/usr/%{_lib}/opensc-pkcs11.so@' configure.ac

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-rtlsdr=yes
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{/etc/sysconfig,%{systemdunitdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{systemdunitdir}/rngd.service
cp -p %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/rngd

%clean
rm -rf $RPM_BUILD_ROOT

%post
%systemd_post rngd.service

%preun
%systemd_preun rngd.service

%postun
%systemd_reload

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README.md
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rngd
%attr(755,root,root) %{_bindir}/randstat
%attr(755,root,root) %{_bindir}/rngtest
%attr(755,root,root) %{_sbindir}/rngd
%{_mandir}/man1/rngtest.1*
%{_mandir}/man8/rngd.8*
%{systemdunitdir}/rngd.service
