# Suppress most build root processing since we are just carrying binary data
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}
Name: fedora-iot
Version:	%{ostree_version}
Release:	1%{?dist}
Summary:	Image (rpm-ostree jigdo) for Fedora IoT
License:	MIT
#@@@rpmostree_jigdo_meta@@@

%description
%{summary}

%prep

%build

%install
mkdir -p %{buildroot}%{_prefix}/lib/ostree-jigdo/%{name}
for x in *; do mv ${x} %{buildroot}%{_prefix}/lib/ostree-jigdo/%{name}; done

%files
%{_prefix}/lib/ostree-jigdo/%{name}
