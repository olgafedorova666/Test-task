Name:           raidix-task
Version:        1.0
Release:        1%{?dist}
Summary:        Raidix Task

License:        MIT License
URL:            https://github.com/olgafedorova666/Test-task
Source0:        raidix-task-1.0.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description


%prep
%setup -q
%global debug_package %{nil}


%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%license LICENSE
%{_bindir}/%{name}



%changelog
* Tue Mar 22 2022 rpmbuilder
- Example second item in the changelog for version-release 0.1-1
