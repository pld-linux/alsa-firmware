Summary:	Advanced Linux Sound Architecture - firmware data
Summary(pl.UTF-8):	Advanced Linux Sound Architecture - dane firmware
Name:		alsa-firmware
Version:	1.0.19
Release:	1
License:	varies (GPL, BSD-like, distributable)
Group:		Libraries
Source0:	ftp://ftp.alsa-project.org/pub/firmware/%{name}-%{version}.tar.bz2
# Source0-md5:	bb93a1a58066bdb2308dc7b117df2b67
URL:		http://www.alsa-project.org/
BuildRequires:	automake
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautostrip	.*\.elf

%description
Firmware data for ALSA.

%description -l pl.UTF-8
Dane firmware dla ALSA.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%configure \
	--disable-buildfw \
	--with-hotplug-dir=/lib/firmware

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
cp -f aica/license.txt license.aica

# remove dead symlinks to /etc/sound/* (with sanity check)
for l in $RPM_BUILD_ROOT/lib/firmware/turtlebeach/*.bin ; do
	test -h $l || exit 1
	rm -f $l
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* mixartloader/miXart.conf pcxhrloader/pcxhr.conf usx2yloader/us*.conf vxloader/vx*.conf aica/Dreamcast_sound.txt license.aica
# loadable by hotplug/udev
/lib/firmware/aica_firmware.bin
/lib/firmware/digiface_*.bin
/lib/firmware/multiface_*.bin
/lib/firmware/asihpi
/lib/firmware/ea
/lib/firmware/emagic
/lib/firmware/emu
/lib/firmware/ess
/lib/firmware/korg
/lib/firmware/mixart
/lib/firmware/pcxhr
/lib/firmware/sb16
# just dead symlinks
#/lib/firmware/turtlebeach
/lib/firmware/vx
/lib/firmware/yamaha
# -alsa subpackage? loadable by alsa (R: alsa-tools, %{_datadir}/alsa dir)
%dir %{_datadir}/alsa/firmware
%{_datadir}/alsa/firmware/hdsploader
%{_datadir}/alsa/firmware/mixartloader
%{_datadir}/alsa/firmware/pcxhrloader
%{_datadir}/alsa/firmware/usx2yloader
%{_datadir}/alsa/firmware/vxloader
