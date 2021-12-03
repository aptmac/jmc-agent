# JMC Agent Version
%global major 1
%global minor 0
%global patchlevel 1

# Revision
%global revnum 1
# set to 1 for snapshots, 0 for release
%global usesnapshot 0

# SNAPSHOT version
%global revhash 14d2f6ca7a404a71c8aa8676cfd301dcab647093
%global revdate 20211026

# JMC release version tag containing the agent code
%global jmc_version 8.1.1-ga
%global tarball_name jmc-%{jmc_version}

%if %{usesnapshot}
  %global releasestr %{revnum}.%{revdate}%{revhash}
%else
  %global releasestr %{revnum}
%endif

Name:     jmc-agent
Version:  %{major}.%{minor}.%{patchlevel}
Release:  %{releasestr}%{?dist}
Summary:  JDK Mission Control Agent
License:  UPL
URL:      http://openjdk.java.net/projects/jmc/agent/
Source0:  https://github.com/openjdk/jmc/archive/refs/tags/%{jmc_version}.tar.gz

BuildArch:  noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-commons)
BuildRequires:  mvn(org.ow2.asm:asm-util)

# On F35 onward, surefire requires Xmx1024m to avoid the VM from crashing during tests
Patch0:  0-increase-surefire-memory.patch

%description
The JMC agent allows users to add JFR instrumentation declaratively to a running program.
The agent can, for example, be used to add flight recorder events to third party code
for which the source is not available.

%package javadoc
Summary:  Javadoc for %{name}

%description javadoc
This package contains javadoc for %{summary}.

%prep
%setup -q -n %{tarball_name}/agent

%patch0 -p1

cp ./license/* ./

%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-failsafe-plugin
%pom_remove_plugin :maven-shade-plugin
%pom_remove_plugin :nexus-staging-maven-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt
%license THIRDPARTYREADME.txt
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt
%license THIRDPARTYREADME.txt
%doc README.md

%changelog
* Fri Dec 03 2021 Alex Macdonald <almacdon@redhat.com> - 1.0.1-1
- Initial package
