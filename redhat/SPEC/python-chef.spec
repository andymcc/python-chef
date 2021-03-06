%define ver 1

Name:       python-chef
Version:    0.2.1
Release:    %{ver}%{?dist}
Summary:	Python implementation of a Chef API client.

Group:		System
License:	None
URL:		https://github.com/rpedde/opencenter-agent
Source0:	python-chef-0.2.1.tgz

BuildRequires:  python-setuptools
Requires:	python >= 2.6

BuildArch: noarch


%description
Pluggable, modular host-based agent.  See the output and input
managers for docs on how to write plugins.

%prep
%setup -q -n %{name}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{python_sitelib}/chef*
%{python_sitelib}/PyChef*
%doc

%clean
rm -rf $RPM_BUILD_ROOT

%post

%changelog
* Mon Sep 10 2012 Joseph W. Breu (joseph.breu@rackspace.com) - 1.0
- Initial build
