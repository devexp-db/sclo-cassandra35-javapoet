Name:          javapoet
Version:       1.7.0
Release:       1%{?dist}
Summary:       A Java API for generating .java source files
License:       ASL 2.0
URL:           https://github.com/square/javapoet
Source0:       https://github.com/square/%{name}/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

%if 0
# test dependencies
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.eclipse.jdt.core.compiler:ecj:4.4.2)
BuildRequires: mvn(org.mockito:mockito-core:1.10.16)
# missing test dependencies
BuildRequires: mvn(com.google.jimfs:jimfs:1.0)
BuildRequires: mvn(com.google.testing.compile:compile-testing:0.6)
BuildRequires: mvn(com.google.truth:truth:0.25)
%endif

BuildArch:     noarch

%description
A utility class which aids in generating Java source files.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%pom_remove_plugin :maven-checkstyle-plugin

%mvn_file : %{name}

%build
# skip tests due to missing test dependencies
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc CHANGELOG.md README.md
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Tue Oct 25 2016 Tomas Repik <trepik@redhat.com> - 1.7.0-1
- initial rpm
