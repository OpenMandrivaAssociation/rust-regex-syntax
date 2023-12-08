# Rust packages always list license files and docs
# inside the crate as well as the containing directory
%undefine _duplicate_files_terminate_build
%bcond_without check
%global debug_package %{nil}

%global crate regex-syntax

Name:           rust-regex-syntax
Version:        0.8.2
Release:        1
Summary:        Regular expression parser
Group:          Development/Rust

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/regex-syntax
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  rust >= 1.65

%global _description %{expand:
A regular expression parser.}

%description %{_description}

%package        devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(regex-syntax) = 0.8.2
Requires:       cargo
Requires:       rust >= 1.65

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%license %{crate_instdir}/src/unicode_tables/LICENSE-UNICODE
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(regex-syntax/default) = 0.8.2
Requires:       cargo
Requires:       crate(regex-syntax) = 0.8.2
Requires:       crate(regex-syntax/std) = 0.8.2
Requires:       crate(regex-syntax/unicode) = 0.8.2

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+arbitrary-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(regex-syntax/arbitrary) = 0.8.2
Requires:       (crate(arbitrary/default) >= 1.3.0 with crate(arbitrary/default) < 2.0.0~)
Requires:       (crate(arbitrary/derive) >= 1.3.0 with crate(arbitrary/derive) < 2.0.0~)
Requires:       cargo
Requires:       crate(regex-syntax) = 0.8.2

%description -n %{name}+arbitrary-devel %{_description}

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%files       -n %{name}+arbitrary-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(regex-syntax/std) = 0.8.2
Requires:       cargo
Requires:       crate(regex-syntax) = 0.8.2

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unicode-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(regex-syntax/unicode) = 0.8.2
Requires:       cargo
Requires:       crate(regex-syntax) = 0.8.2
Requires:       crate(regex-syntax/unicode-age) = 0.8.2
Requires:       crate(regex-syntax/unicode-bool) = 0.8.2
Requires:       crate(regex-syntax/unicode-case) = 0.8.2
Requires:       crate(regex-syntax/unicode-gencat) = 0.8.2
Requires:       crate(regex-syntax/unicode-perl) = 0.8.2
Requires:       crate(regex-syntax/unicode-script) = 0.8.2
Requires:       crate(regex-syntax/unicode-segment) = 0.8.2

%description -n %{name}+unicode-devel %{_description}

This package contains library source intended for building other packages which
use the "unicode" feature of the "%{crate}" crate.

%files       -n %{name}+unicode-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unicode-age-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(regex-syntax/unicode-age) = 0.8.2
Requires:       cargo
Requires:       crate(regex-syntax) = 0.8.2

%description -n %{name}+unicode-age-devel %{_description}

This package contains library source intended for building other packages which
use the "unicode-age" feature of the "%{crate}" crate.

%files       -n %{name}+unicode-age-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unicode-bool-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(regex-syntax/unicode-bool) = 0.8.2
Requires:       cargo
Requires:       crate(regex-syntax) = 0.8.2

%description -n %{name}+unicode-bool-devel %{_description}

This package contains library source intended for building other packages which
use the "unicode-bool" feature of the "%{crate}" crate.

%files       -n %{name}+unicode-bool-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unicode-case-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(regex-syntax/unicode-case) = 0.8.2
Requires:       cargo
Requires:       crate(regex-syntax) = 0.8.2

%description -n %{name}+unicode-case-devel %{_description}

This package contains library source intended for building other packages which
use the "unicode-case" feature of the "%{crate}" crate.

%files       -n %{name}+unicode-case-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unicode-gencat-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(regex-syntax/unicode-gencat) = 0.8.2
Requires:       cargo
Requires:       crate(regex-syntax) = 0.8.2

%description -n %{name}+unicode-gencat-devel %{_description}

This package contains library source intended for building other packages which
use the "unicode-gencat" feature of the "%{crate}" crate.

%files       -n %{name}+unicode-gencat-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unicode-perl-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(regex-syntax/unicode-perl) = 0.8.2
Requires:       cargo
Requires:       crate(regex-syntax) = 0.8.2

%description -n %{name}+unicode-perl-devel %{_description}

This package contains library source intended for building other packages which
use the "unicode-perl" feature of the "%{crate}" crate.

%files       -n %{name}+unicode-perl-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unicode-script-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(regex-syntax/unicode-script) = 0.8.2
Requires:       cargo
Requires:       crate(regex-syntax) = 0.8.2

%description -n %{name}+unicode-script-devel %{_description}

This package contains library source intended for building other packages which
use the "unicode-script" feature of the "%{crate}" crate.

%files       -n %{name}+unicode-script-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unicode-segment-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(regex-syntax/unicode-segment) = 0.8.2
Requires:       cargo
Requires:       crate(regex-syntax) = 0.8.2

%description -n %{name}+unicode-segment-devel %{_description}

This package contains library source intended for building other packages which
use the "unicode-segment" feature of the "%{crate}" crate.

%files       -n %{name}+unicode-segment-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
