Summary:	XMacro - mouse and keys event recorder
Name:		xmacro
Version:	0.3
%define		_snap	20000911
Release:	0.%{_snap}.1
License:	GPL v2+
Group:		Applications
Source0:	http://dl.sourceforge.net/xmacro/%{name}-pre%{version}-%{_snap}.tar.gz
# Source0-md5:	d2956b82f3d5380e58a75ccc721fb746
Patch0:		%{name}-Makefile.patch
BuildRequires:	XFree86-devel
URL:		http://xmacro.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The XMacro package contains two simple, C++ programs (xmacrorec and
xmacroplay) for recording and replaying keyboard and mouse events on
an X server. This functionality is achieved through the XTest extension.

%prep
%setup -q -n %{name}-pre%{version}-%{_snap}
%patch0 -p1

%build
%{__make} \
	CC="%{__cxx}" \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install xmacroplay xmacrorec xmacrorec2 $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README run example/*
%attr(755,root,root) %{_bindir}/*
