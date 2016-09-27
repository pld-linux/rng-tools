Summary:	Random number generator related utilities
Summary(pl.UTF-8):	Narzędzia do generatora liczb losowych
Name:		rng-tools
Version:	5
Release:	2
License:	GPL v2+
Group:		Base
Source0:	http://downloads.sourceforge.net/gkernel/%{name}-%{version}.tar.gz
# Source0-md5:	6726cdc6fae1f5122463f24ae980dd68
Source1:	rngd.service
Source2:	rngd.sysconfig
URL:		http://sourceforge.net/projects/gkernel/
BuildRequires:	groff
BuildRequires:	libgcrypt-devel
BuildRequires:	rpmbuild(macros) >= 1.671
Requires:	systemd-units >= 38
Obsoletes:	rng-utils < 1:2.0-4.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
Hardware random number generation tools.

%description -l pl.UTF-8
Narzędzia wspierające sprzętowe generowanie liczb losowych.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{/etc/sysconfig,%{systemdunitdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{systemdunitdir}/rngd.service
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/rngd

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
%doc AUTHORS ChangeLog NEWS README
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rngd
%attr(755,root,root) %{_bindir}/rngtest
%attr(755,root,root) %{_sbindir}/rngd
%{_mandir}/man1/rngtest.1*
%{_mandir}/man8/rngd.8*
%{systemdunitdir}/rngd.service
