
%define probe_name xrootd-transfer-cms

Name:               gratia-probe-%{probe_name}
Summary:            Gratia probe for CMS xrootd-transfer accounting
Group:              Applications/System
Version:            1.09
Release:            1
License:            GPL
Group:              Applications/System
URL:                http://github.com/bbockelm/gratia-probe-xrootd-transfer-cms
Vendor:             The Open Science Grid <http://www.opensciencegrid.org/>

Requires:           gratia-probe-common >= 1.09

# Default ProbeName
%{!?meter_name: %global meter_name `hostname -f`}

%define customize_probeconfig(d:) sed -i "s#@PROBE_HOST@#%{meter_name}#" %{_sysconfdir}/gratia/%{-d*}/ProbeConfig

Source0:  %{name}-%{version}.tar.gz

# Build settings.
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description
Gratia probe for CMS xrootd-transfer accounting

# Build preparation.
%prep
%setup -q

%build

%configure

make

%install
# Setup
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post
sed -i "s#@PROBE_HOST@#%{meter_name}#" %{_sysconfdir}/gratia/%{probe_name}/ProbeConfig

%files
%defattr(-,root,root,-)
%{_datadir}/gratia/%{probe_name}/%{probe_name}
%{_sysconfdir}/init.d/gratia-probe-%{probe_name}
%config(noreplace) %{_sysconfdir}/gratia/%{probe_name}/SiteHostMapfile
%config(noreplace) %{_sysconfdir}/gratia/%{probe_name}/ProbeConfig

%changelog
