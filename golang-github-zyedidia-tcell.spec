# Run tests in check section
%bcond_without check

%global goipath         github.com/zyedidia/tcell
%global commit          208b6e8f2f8d763a4accac33f3bdbd7dc9c71c01

%global common_description %{expand:
Alternate terminal package, similar to termbox.}

%gometa

Name:    %{goname}
Version: 0
Release: 0.5%{?dist}
Summary: Alternate terminal package, similar to termbox
License: ASL 2.0
URL:     %{gourl}
Source:  %{gosource}

BuildRequires: golang(github.com/gdamore/encoding)
BuildRequires: golang(github.com/lucasb-eyer/go-colorful)
BuildRequires: golang(github.com/mattn/go-runewidth)
BuildRequires: golang(golang.org/x/text/encoding)
BuildRequires: golang(golang.org/x/text/encoding/charmap)
BuildRequires: golang(golang.org/x/text/encoding/japanese)
BuildRequires: golang(golang.org/x/text/encoding/korean)
BuildRequires: golang(golang.org/x/text/encoding/simplifiedchinese)
BuildRequires: golang(golang.org/x/text/encoding/traditionalchinese)
BuildRequires: golang(golang.org/x/text/transform)

%if %{with check}
BuildRequires: golang(github.com/smartystreets/goconvey/convey)
%endif

%description
%{common_description}


%package    devel
Summary:    %{summary}
BuildArch:  noarch
 
%description devel
%{common_description}
 
This package contains the source code needed for building packages that import
the %{goipath} Go namespace.


%prep
%gosetup -q


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc TERMINALS.md README.md AUTHORS


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git208b6e8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 14 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20180314git208b6e8
- Fix BuildRequires

* Sat Mar 10 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20180314git208b6e8
- Update with the new Go packaging
- Upstream GIT revision 208b6e8

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20171129git869faf8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 07 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20171129git869faf8
- Upstream GIT revision 869faf8

* Fri Sep 29 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20170919git7095cc1
- First package for Fedora

