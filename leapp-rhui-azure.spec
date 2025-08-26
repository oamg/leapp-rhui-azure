Name:           leapp-rhui-azure
Version:        1.0.0
Release:        17%{?dist}
Summary:        Support package for in-place upgrades using Leapp

%global leappfilespath        %{_datadir}/leapp-repository/repositories/system_upgrade/common/files/rhui
%global upgrade_gpg_keys_dir  %{_datadir}/leapp-repository/repositories/system_upgrade/common/files/distro/rhel/rpm-gpg/10

License:        LGPLv2+
URL:            http://redhat.com
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}

BuildArch:      noarch

%if 0%{?rhel} == 7
Requires:       python3
%endif

%if 0%{?rhel} == 8
Requires:       python39
%endif

%if 0%{?rhel} == 9
Requires:       python312
%endif

%description
Support files for in-place upgrade of pay-as-you-go RHEL images using Leapp on Azure

%package sap
Summary: Support package for in-place upgrades using Leapp
Group:   System Environment/Base

%if 0%{?rhel} == 7
Requires:       python3
%endif

%if 0%{?rhel} == 8
Requires:       python39
%endif

%if 0%{?rhel} == 9
Requires:       python312
%endif

%description sap
Support files for in-place upgrade of pay-as-you-go RHEL SAP images using Leapp on Azure

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT

%if 0%{?rhel} == 7
# Base RHEL
mkdir -p %{buildroot}%{leappfilespath}/azure
cp src/7to8/base/leapp-azure.repo  %{buildroot}/%{leappfilespath}/azure

# SAP HA
mkdir -p %{buildroot}%{leappfilespath}/azure-sap-ha
cp src/7to8/sap/leapp-azure-sap-ha.repo       %{buildroot}%{leappfilespath}/azure-sap-ha
cp src/7to8/sap/leapp-azure-base-sap-ha.repo  %{buildroot}%{leappfilespath}/azure-sap-ha

# SAP Apps
mkdir -p %{buildroot}%{leappfilespath}/azure-sap-apps
cp src/7to8/sap/leapp-azure-sap-apps.repo      %{buildroot}%{leappfilespath}/azure-sap-apps
cp src/7to8/sap/leapp-azure-base-sap-apps.repo %{buildroot}%{leappfilespath}/azure-sap-apps
%endif

%if 0%{?rhel} == 8
# Base RHEL
mkdir -p %{buildroot}%{leappfilespath}/azure
cp src/8to9/base/leapp-azure.repo %{buildroot}/%{leappfilespath}/azure

# SAP HA
mkdir -p %{buildroot}%{leappfilespath}/azure-sap-ha
cp src/8to9/sap/leapp-azure-sap-ha.repo %{buildroot}%{leappfilespath}/azure-sap-ha

# SAP Apps
mkdir -p %{buildroot}%{leappfilespath}/azure-sap-apps
cp src/8to9/sap/leapp-azure-sap-apps.repo %{buildroot}%{leappfilespath}/azure-sap-apps
%endif

%if 0%{?rhel} == 9

mkdir -p %{buildroot}%{leappfilespath}/azure
cp src/9to10/base/leapp-azure.repo                         %{buildroot}/%{leappfilespath}/azure
cp src/9to10/base/RPM-GPG-KEY-microsoft-azure-release-new  %{buildroot}/%{leappfilespath}/azure

mkdir -p %{buildroot}%{leappfilespath}/azure-sap-ha
cp src/9to10/sap/leapp-azure-sap-ha.repo            %{buildroot}/%{leappfilespath}/azure-sap-ha

mkdir -p %{buildroot}%{leappfilespath}/azure-sap-apps
cp src/9to10/sap/leapp-azure-sap-apps.repo          %{buildroot}/%{leappfilespath}/azure-sap-apps

# Same GPG key is used for all RHUI clients, take the one in /base
cp src/9to10/base/RPM-GPG-KEY-microsoft-azure-release-new  %{buildroot}/%{leappfilespath}/azure-sap-ha
cp src/9to10/base/RPM-GPG-KEY-microsoft-azure-release-new  %{buildroot}/%{leappfilespath}/azure-sap-apps
mkdir -p %{buildroot}/%{upgrade_gpg_keys_dir}
cp src/9to10/base/RPM-GPG-KEY-microsoft-azure-release-new  %{buildroot}/%{upgrade_gpg_keys_dir}

%endif

exit 0

%if 0%{?rhel} == 7
%files
%dir %{_datadir}/leapp-repository
%dir %{_datadir}/leapp-repository/repositories
%dir %{_datadir}/leapp-repository/repositories/system_upgrade
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files/rhui
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files/rhui/azure

/%{leappfilespath}/azure/leapp-azure.repo

%files sap
%dir %{_datadir}/leapp-repository
%dir %{_datadir}/leapp-repository/repositories
%dir %{_datadir}/leapp-repository/repositories/system_upgrade
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files/rhui
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files/rhui/azure-sap-ha
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files/rhui/azure-sap-apps

/%{leappfilespath}/azure-sap-ha/leapp-azure-sap-ha.repo
/%{leappfilespath}/azure-sap-ha/leapp-azure-base-sap-ha.repo

/%{leappfilespath}/azure-sap-apps/leapp-azure-sap-apps.repo
/%{leappfilespath}/azure-sap-apps/leapp-azure-base-sap-apps.repo
%endif

%if 0%{?rhel} == 8
%files
%dir %{_datadir}/leapp-repository
%dir %{_datadir}/leapp-repository/repositories
%dir %{_datadir}/leapp-repository/repositories/system_upgrade
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files/rhui
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files/rhui/azure

/%{leappfilespath}/azure/leapp-azure.repo

%files sap
%dir %{_datadir}/leapp-repository
%dir %{_datadir}/leapp-repository/repositories
%dir %{_datadir}/leapp-repository/repositories/system_upgrade
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files/rhui
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files/rhui/azure-sap-ha
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files/rhui/azure-sap-apps

/%{leappfilespath}/azure-sap-ha/leapp-azure-sap-ha.repo

%{leappfilespath}/azure-sap-apps/leapp-azure-sap-apps.repo
%endif

%if 0%{?rhel} == 9
%files
%dir %{_datadir}/leapp-repository
%dir %{_datadir}/leapp-repository/repositories
%dir %{_datadir}/leapp-repository/repositories/system_upgrade
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files/rhui
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files/rhui/azure

/%{leappfilespath}/azure/leapp-azure.repo
/%{leappfilespath}/azure/RPM-GPG-KEY-microsoft-azure-release-new
/%{upgrade_gpg_keys_dir}/RPM-GPG-KEY-microsoft-azure-release-new

%files sap
%dir %{_datadir}/leapp-repository
%dir %{_datadir}/leapp-repository/repositories
%dir %{_datadir}/leapp-repository/repositories/system_upgrade
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files/rhui
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files/rhui/azure-sap-ha
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files/rhui/azure-sap-apps

/%{leappfilespath}/azure-sap-ha/leapp-azure-sap-ha.repo
/%{leappfilespath}/azure-sap-ha/RPM-GPG-KEY-microsoft-azure-release-new

/%{leappfilespath}/azure-sap-apps/leapp-azure-sap-apps.repo
/%{leappfilespath}/azure-sap-apps/RPM-GPG-KEY-microsoft-azure-release-new

/%{upgrade_gpg_keys_dir}/RPM-GPG-KEY-microsoft-azure-release-new

%endif

%changelog
* Tue Aug 26 2025 Michal Hecko <mhecko@redhat.com> 1.0.0-17
- add RHEL 9 packages for SAP Apps and SAP HA

* Sun Jun 15 2025 Michal Hecko <mhecko@redhat.com> 1.0.0-16
- add rhel9 package

* Thu May 30 2024 Michal Hecko <mhecko@redhat.com> 1.0.0-15
- add repofiles for 8.10 SAP

* Tue May 14 2024 Michal Hecko <mhecko@redhat.com> 1.0.0-14
- drop dependencies on leapp and leapp-upgrade-el{X}to{X+1}

* Thu Mar 07 2024 Michal Hecko <mhecko@redhat.com> 1.0.0-13
- migrate target client repo urls to RHUI4
- add dependency on python3

* Fri Jan 26 2024 Michal Hecko <mhecko@redhat.com> 1.0.0-12
- add dependencies on leapp to the leapp-rhui-*-sap packages

* Thu Aug 24 2023 Michal Hecko <mhecko@redhat.com> 1.0.0-11
- Do not include certs and keys, drop repositories

* Thu Jun 22 2023 Michal Hecko <mhecko@redhat.com> 1.0.0-10
- Update all certificates and keys

* Tue Jun 20 2023 Peter Mocary <pmocary@redhat.com> 1.0.0-9
- Bump for clarity reasons

* Thu Jun 01 2023 Michal Hecko <mhecko@redhat.com> 1.0.0-8
- Rename RHEL8 repoids and update certs

* Thu Mar 23 2023 Michal Hecko <mhecko@redhat.com> 1.0.0-7
- Rename keys and certificates for SAP systems
- Remove EUS keys and certificated for SAP Apps systems

* Wed Feb 15 2023 Michal Hecko <mhecko@redhat.com> 1.0.0-6
- Update RHUI certificates

* Mon Oct 10 2022 Michal Hecko <mhecko@redhat.com> 1.0.0-5
- Update repoids of RHUI repositories for 7to8 upgrade of SAP RHEL systems
- Fix missing EUS RHUI repoid when upgrading RHEL7 SAP Apps systems

* Fri Sep 02 2022 Michal Hecko <mhecko@redhat.com> 1.0.0-4
- Fix missing releasever in repo urls for 7to8 upgrade of base RHEL systems
