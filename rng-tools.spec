Summary:	Random number generator related utilities
Name:		rng-tools
Version:	3
Release:	3
License:	GPL v2+
Group:		Base
URL:		http://sourceforge.net/projects/gkernel/
Source0:	http://downloads.sourceforge.net/gkernel/%{name}-%{version}.tar.gz
# Source0-md5:	fa305916ec101c85c0065aeceb81a38d
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext
BuildRequires:	groff
Obsoletes:	rng-utils < 1:2.0-4.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir /sbin

%description
Hardware random number generation tools.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/rngtest
%attr(755,root,root) %{_sbindir}/rngd
%{_mandir}/man1/rngtest.1.*
%{_mandir}/man8/rngd.8.*
