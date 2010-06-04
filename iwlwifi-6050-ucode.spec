%define name iwlwifi-6050-ucode
%define version 9.201.4.1
%define release %mkrel 1

Summary: Intel PRO/Wireless 6250AGN microcode
Name:	 %{name}
Version: %{version}
Release: %{release}
Source0: http://www.intellinuxwireless.org/iwlwifi/downloads/%{name}-%{version}.tgz
License: Proprietary
Group:	 System/Kernel and hardware
Url:	 http://intellinuxwireless.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

%description
The file iwlwifi-6050-*.ucode provided in this package is required to be
present on your system in order for the Intel PRO/Wireless 6250AGN Network
Connection Adapter driver for Linux (iwlagn) to be able to operate on
your system.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}/lib/firmware
install -m644 *.ucode %{buildroot}/lib/firmware/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE.* README.*
/lib/firmware/*.ucode
