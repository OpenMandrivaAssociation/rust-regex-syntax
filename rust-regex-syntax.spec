%bcond_without check
%global debug_package %{nil}

%global crate regex-syntax

Name:           rust-%{crate}
Version:        0.6.23
Release:        1
Summary:        Regular expression parser

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/regex-syntax
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Regular expression parser.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unicode-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-devel %{_description}

This package contains library source intended for building other packages
which use "unicode" feature of "%{crate}" crate.

%files       -n %{name}+unicode-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unicode-age-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-age-devel %{_description}

This package contains library source intended for building other packages
which use "unicode-age" feature of "%{crate}" crate.

%files       -n %{name}+unicode-age-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unicode-bool-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-bool-devel %{_description}

This package contains library source intended for building other packages
which use "unicode-bool" feature of "%{crate}" crate.

%files       -n %{name}+unicode-bool-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unicode-case-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-case-devel %{_description}

This package contains library source intended for building other packages
which use "unicode-case" feature of "%{crate}" crate.

%files       -n %{name}+unicode-case-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unicode-gencat-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-gencat-devel %{_description}

This package contains library source intended for building other packages
which use "unicode-gencat" feature of "%{crate}" crate.

%files       -n %{name}+unicode-gencat-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unicode-perl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-perl-devel %{_description}

This package contains library source intended for building other packages
which use "unicode-perl" feature of "%{crate}" crate.

%files       -n %{name}+unicode-perl-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unicode-script-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-script-devel %{_description}

This package contains library source intended for building other packages
which use "unicode-script" feature of "%{crate}" crate.

%files       -n %{name}+unicode-script-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unicode-segment-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-segment-devel %{_description}

This package contains library source intended for building other packages
which use "unicode-segment" feature of "%{crate}" crate.

%files       -n %{name}+unicode-segment-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
