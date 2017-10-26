Name:              torsocks
Version:           2.2.0
Release:           1%{?dist}

Summary:           Use SOCKS-friendly applications with Tor
Group:             Applications/Internet
License:           GPLv2+
URL:               https://gitweb.torproject.org/torsocks.git

Source0:           https://people.torproject.org/~dgoulet/torsocks/torsocks-%{version}.tar.xz
Source1:           https://people.torproject.org/~dgoulet/torsocks/torsocks-%{version}.tar.xz.asc

# Unit tests require /usr/bin/prove
BuildRequires:     perl(Test::Harness)


%description
Torsocks allows you to use most SOCKS-friendly applications in a safe way
with Tor. It ensures that DNS requests are handled safely and explicitly
rejects UDP traffic from the application you're using.


%prep
%setup -q -n %{name}-%{version}


%build
%configure --libdir=%{_libdir}
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

# Remove extraneous files.
rm -f %{buildroot}%{_libdir}/torsocks/libtorsocks.{a,la}*
rm -fr %{buildroot}%{_datadir}/doc/torsocks

# For bash completion.
install -p -D -m0644 extras/torsocks-bash_completion \
    %{buildroot}%{_sysconfdir}/bash_completion.d/torsocks


%check
pushd tests/
make check-am
popd


%files
%doc ChangeLog gpl-2.0.txt doc/notes/DEBUG doc/socks/socks-extensions.txt
%{_bindir}/torsocks
%{_mandir}/man1/torsocks.1.*
%{_mandir}/man5/torsocks.conf.5.*
%{_mandir}/man8/torsocks.8.*
%dir %{_libdir}/torsocks
# torsocks requires this file so it has not been placed in -devel subpackage
%{_libdir}/torsocks/libtorsocks.so
%{_libdir}/torsocks/libtorsocks.so.0*
%config(noreplace) %{_sysconfdir}/bash_completion.d/torsocks
%config(noreplace) %{_sysconfdir}/tor/torsocks.conf


%changelog
* Thu Oct 26 2017 Jajauma's Packages <jajauma@yandex.ru> - 2.2.0-1
- Update to latest upstream release
- Run all tests

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 28 2015 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.1.0-1
- update to upstream release 2.1.0
- run test suite

* Wed Apr 29 2015 Jon Ciesla <limburgher@gmail.com> - 2.0.0-3
- Updated to latest to fix syscall errors.

* Tue Nov 11 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.0.0-2
- remove extraneous files

* Tue Nov 11 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.0.0-1
- update to 2.0.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 23 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.3-1
- update to upstream release 1.3

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
