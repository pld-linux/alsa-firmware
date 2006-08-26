Summary:	Advanced Linux Sound Architecture - firmware data
Summary(pl):	Advanced Linux Sound Architecture - dane firmware
Name:		alsa-firmware
Version:	1.0.12
Release:	0.1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.alsa-project.org/pub/firmware/%{name}-%{version}.tar.bz2
# Source0-md5:	5228625d822e6995c96b80f8c3785db6
URL:		http://www.alsa-project.org/
BuildRequires:	automake
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautostrip	.*\.elf
%define		hotplugfwdir	/lib/firmware

%description
Firmware data for ALSA.

%description -l pl
Dane firmware dla ALSA.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%configure \
	--disable-buildfw \
	--with-hotplug-dir=%{hotplugfwdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -f hdsploader/README README.hdsploader
cp -f mixartloader/README README.mixartloader
cp -f pcxhrloader/README README.pcxhrloader
cp -f usx2yloader/README README.usx2yloader
cp -f vxloader/README README.vxloader

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* mixartloader/miXart.conf pcxhrloader/pcxhr.conf usx2yloader/us*.conf vxloader/vx*.conf
# -hotplug subpackage? (R: hotplug)
%{hotplugfwdir}/digiface_*.bin
%{hotplugfwdir}/multiface_*.bin
%{hotplugfwdir}/asihpi
%{hotplugfwdir}/ea
%{hotplugfwdir}/emu
%{hotplugfwdir}/mixart
%{hotplugfwdir}/pcxhr
%{hotplugfwdir}/vx
# -alsa subpackage? (R: alsa-tools, %{_datadir}/alsa dir)
%dir %{_datadir}/alsa/firmware
%{_datadir}/alsa/firmware/hdsploader
%{_datadir}/alsa/firmware/mixartloader
%{_datadir}/alsa/firmware/pcxhrloader
%{_datadir}/alsa/firmware/usx2yloader
%{_datadir}/alsa/firmware/vxloader
