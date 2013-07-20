%global packname statnet.common
%global rlibdir %{_libdir}/R/library

Name:             R-%{packname}
Version:          3.1_0
Release:          1
Summary:          Common R Scripts and Utilities Used by the Statnet Project Software
Group:            Sciences/Mathematics
License:          GPLv3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_3.1-0.tar.gz
BuildArch:        noarch
Requires:         R-core 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex

%description
This package contains non-statistical utilities used by
the software developed by the Statnet Project. 
They may also be of use to others.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
