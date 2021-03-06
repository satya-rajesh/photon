Summary:        This project is an implementation of the TCG TPM 2.0 specification.
Name:           ibmtpm
Version:        1637
Release:        1%{?dist}
License:        BSD 2-Clause
URL:            https://sourceforge.net/projects/ibmswtpm2/files
Group:          System Environment/Security
Vendor:         VMware, Inc.
Distribution:   Photon
Source0:        %{name}%{version}.tar.gz
%define sha1 ibmtpm=ab4b94079e57a86996991e8a2b749ce063e4ad3e
BuildRequires:  openssl-devel curl-devel
Requires:       openssl curl
%description
This project is an implementation of the TCG TPM 2.0 specification.
It is based on the TPM specification Parts 3 and 4 source code donated by Microsoft,
with additional files to complete the implementation.

%prep
%setup -cqn %{name}-%{version}

%build
cd src
make %{?_smp_mflags}

%install
cd src
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}/lib/systemd/system
cat << EOF >> %{buildroot}/lib/systemd/system/ibmtpm_server.service
[Unit]
Description=ibmtpm_server

[Service]
Type=simple
ExecStart=/usr/bin/tpm_server
EOF

%files
%defattr(-,root,root)
%{_bindir}/*
/lib/systemd/system/ibmtpm_server.service

%changelog
*   Mon Jul 27 2020 Gerrit Photon <photon-checkins@vmware.com> 1637-1
-   Automatic Version Bump
*   Fri May 29 2020 Michelle Wang <michellew@vmware.com> 1628-1
-   Initial build. First version
