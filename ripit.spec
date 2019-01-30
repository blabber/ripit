#
# spec file for package RipIT
#
%define	name	ripit
%define	version	3.9.0
%define	release	0

Name:		%{name}
Version:	%{version}
Release:	%{release}

Summary:	Perl script to create flac, ogg, mp3, m4a, als, mpc, wv and other files from an audio CD
License:	GPL
Group:		Applications/Multimedia
URL:		http://www.suwald.com/ripit/index.html

Source:		%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-buildroot
#BuildRoot:	%{_tmppath}/%{name}-%{version}-build
BuildArchitectures:	noarch
Requires:	cdparanoia vorbis-tools perl perl-CDDB_get
Packager:	Felix Suwald
Distribution:	SuSE 11.1

%description
This Perl script makes it a lot easier to create "mp3" files from an
audio CD. RipIT is a CLI script and supports Flac, Lame, Oggenc, Faac
(m4a), mp4als, Musepack, Wavpack and ffmpeg (to create lossless m4a and
other exotic formats). Artist and song titles are retrieved either with
the CDDB_get.pm from freedb.org or using WebService::MusicBrainz.pm from
MusicBrainz.org. It is possible to submit and edit CDDB entries at
freedb.org, submission of MusicBrainz data need a login. Sound files are
tagged and provided a converart picture tags are added.
Hidden tracks and ghost songs are detected and splitted into chunks of
sound, toc or inf files permit to burn the wavs with text and no gaps in
DAO mode. Different encoding formats or even the same format at
different qualities can be used at the same time and encoded into
different directories.



Authors:
--------
    Felix Suwald <ripit[_at_]suwald[_dot_]com>
    Mads Martin Joergenson <mmj@mmj.dk>
    Simon Quinn

%prep

%setup

%build

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

# Be sure to list all files needed or delete them before they are
# checked, else you get the "Installed (but unpackaged) file(s) found"
# error message!
%files

%defattr(-,root,root)
# TODO: do not use hardcoded paths.
# %{_bindir}/%{name}
# %{_mandir}/man1/%{name}.1.gz
# /etc/%{name}/config
/etc/ripit/config
/usr/local/bin/ripit
/usr/local/share/man/man1/ripit.1.gz

%config /etc/ripit/config

%doc README HISTORY LICENSE Makefile ripit.spec

%changelog