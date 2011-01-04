%define name iwlwifi-6050-ucode
%define version 41.28.5.1
%define version_api4 9.201.4.1
%define release %mkrel 2

Summary: Intel PRO/Wireless 6050AGN microcode
Name:	 %{name}
Version: %{version}
Release: %{release}
Source0: http://www.intellinuxwireless.org/iwlwifi/downloads/%{name}-%{version}.tgz
Source1: http://www.intellinuxwireless.org/iwlwifi/downloads/%{name}-%{version_api4}.tgz
License: Proprietary
Group:	 System/Kernel and hardware
Url:	 http://intellinuxwireless.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

%description
The file iwlwifi-6050-*.ucode provided in this package is required to be
present on your system in order for the Intel PRO/Wireless 6050AGN Network
Connection Adapter driver for Linux (iwlagn) to be able to operate on
your system.

%prep
%setup -q -a 1

# provide old firmware with ucode_api=4 for compatibility with older kernels
cp %{name}-%{version_api4}/iwlwifi-6050-4.ucode .
cp %{name}-%{version_api4}/README.iwlwifi-6050-ucode \
README.iwlwifi-6050-ucode-4
mv README.iwlwifi-6050-ucode README.iwlwifi-6050-ucode-5

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
