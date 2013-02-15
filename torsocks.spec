Name:              torsocks
Version:           1.2
Release:           3%{?dist}

Summary:           Use SOCKS-friendly applications with Tor
Group:             Applications/Internet
# COPYING file has incorrect FSF address
# https://code.google.com/p/torsocks/issues/detail?id=51
License:           GPLv2+
URL:               https://code.google.com/p/torsocks

Source0:           https://torsocks.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:           https://torsocks.googlecode.com/files/%{name}-%{version}.tar.gz.sig
Source2:           https://raw.github.com/adrelanos/Whonix/master/whonix_shared/usr/local/bin/uwt
Source3:           torsocks.bash_completion
# https://code.google.com/p/torsocks/issues/detail?id=50
Patch0:            torsocks-1.2-display-correct-error-message.patch
# https://code.google.com/p/torsocks/issues/detail?id=3
Patch1:            torsocks-1.2-symbol-not-found-try-prefix.patch

%description
Torsocks allows you to use most SOCKS-friendly applications in a safe way
with Tor. It ensures that DNS requests are handled safely and explicitly
rejects UDP traffic from the application you're using.


%prep
%setup -q
%patch0 -p1
%patch1 -p1


%build
%configure --libdir=%{_libdir}
make %{?_smp_mflags}

    
%install
make install DESTDIR=%{buildroot}

# Remove extraneous files.
rm -f %{buildroot}%{_libdir}/torsocks/libtorsocks.{a,la}*
rm -f %{buildroot}%{_datadir}/DEBUG
rm -f %{buildroot}%{_datadir}/README*
rm -f %{buildroot}%{_datadir}/SOCKS*
rm -f %{buildroot}%{_datadir}/*.sh
rm -f %{buildroot}%{_datadir}/*.txt
rm -f %{buildroot}%{_datadir}/*.patch

# Fix hardcoded library path.
sed -i -e 's|^LIBDIR=.*|LIBDIR="%{_libdir}/torsocks"|g' \
    %{buildroot}%{_bindir}/torsocks

# Include modified usewithtor to support setting proxy type, ip and port using
# cli parameters to prevent identity correlation through circuit sharing.
install -p -D -m 0755 %{SOURCE2} %{buildroot}%{_bindir}/uwt

# For bash completion.
install -p -D -m 0644 %{SOURCE3} \
    %{buildroot}%{_sysconfdir}/bash_completion.d/torsocks


%files
%doc ChangeLog COPYING README
%{_bindir}/torsocks
%{_bindir}/usewithtor
%{_bindir}/uwt
%{_mandir}/man1/torsocks.1.*
%{_mandir}/man1/usewithtor.1.*
%{_mandir}/man5/torsocks.conf.5.*
%{_mandir}/man8/torsocks.8.*
%dir %{_libdir}/torsocks
# torsocks requires this file so it has not been placed in -devel subpackage
%{_libdir}/torsocks/libtorsocks.so
%{_libdir}/torsocks/libtorsocks.so.1*
%config(noreplace) %{_sysconfdir}/bash_completion.d/torsocks
%config(noreplace) %{_sysconfdir}/torsocks.conf


%changelog
* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 23 2012 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.2-2
- add .sig file
- add links to upstream bug reports
- merge -devel package as torsocks requires libtorsocks.so
- fix directory ownership
- mark bash_completion file as a config file

* Sat Nov 17 2012 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.2-1
- initial package
