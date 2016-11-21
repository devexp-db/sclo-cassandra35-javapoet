%{?scl:%scl_package javapoet}
%{!?scl:%global pkg_name %{name}}

Name:		%{?scl_prefix}javapoet
Version:	1.7.0
Release:	2%{?dist}
Summary:	A Java API for generating .java source files
License:	ASL 2.0
URL:		https://github.com/square/javapoet
Source0:	https://github.com/square/%{pkg_name}/archive/%{pkg_name}-%{version}.tar.gz

BuildRequires:	%{?scl_prefix_maven}maven-local
BuildRequires:	%{?scl_prefix_maven}sonatype-oss-parent
%{?scl:Requires: %scl_runtime}

%if 0
# test dependencies
BuildRequires:	mvn(junit:junit)
BuildRequires:	mvn(org.eclipse.jdt.core.compiler:ecj:4.4.2)
BuildRequires:	mvn(org.mockito:mockito-core:1.10.16)
# missing test dependencies
BuildRequires:	mvn(com.google.jimfs:jimfs:1.0)
BuildRequires:	mvn(com.google.testing.compile:compile-testing:0.6)
BuildRequires:	mvn(com.google.truth:truth:0.25)
%endif

BuildArch:	noarch

%description
A utility class which aids in generating Java source files.

%package javadoc
Summary:	Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{pkg_name}-%{pkg_name}-%{version}

%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%pom_remove_plugin :maven-checkstyle-plugin

%mvn_file : %{pkg_name}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
# skip tests due to missing test dependencies
%mvn_build -f
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc CHANGELOG.md README.md
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Mon Nov 21 2016 Tomas Repik <trepik@redhat.com> - 1.7.0-2
- scl conversion

* Tue Oct 25 2016 Tomas Repik <trepik@redhat.com> - 1.7.0-1
- initial rpm
