Summary:	A cross platform C99 library to get CPU features at runtime
Summary(pl.UTF-8):	Wieloplatformowa biblioteka C99 do sprawdzania funkcjonalności CPU w czasie działania
Name:		cpu_features
Version:	0.9.0
Release:	1
License:	Apache v2.0
Group:		Libraries
#Source0Download: https://github.com/google/cpu_features/releases
Source0:	https://github.com/google/cpu_features/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	383ee74871f1e85e625a32c7e72e7777
URL:		https://github.com/google/cpu_features
BuildRequires:	cmake >= 3.13
BuildRequires:	gcc >= 5:3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A cross-platform C library to retrieve CPU features (such as available
instructions) at runtime.

%description -l pl.UTF-8
Wieloplatformowa biblioteka C do odczytu funkcjonalności CPU (takiej
jak dostępne instrukcje) w czasie działania programu.

%package devel
Summary:	Header files for cpu_features library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki cpu_features
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for cpu_features library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki cpu_features.

%prep
%setup -q

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/list_cpu_features
%attr(755,root,root) %{_libdir}/libcpu_features.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/cpu_features
%{_libdir}/cmake/CpuFeatures
