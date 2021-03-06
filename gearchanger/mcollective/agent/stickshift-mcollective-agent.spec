Summary:        M-Collective agent file for gearchanger-m-collective-plugin
Name:           stickshift-mcollective-agent
Version: 0.2.2
Release:        1%{?dist}
Group:          Development/Languages
License:        ASL 2.0
URL:            http://openshift.redhat.com
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       rubygems
Requires:       rubygem-open4
Requires:       rubygem-json
Requires:       rubygem-stickshift-node
Requires:       mcollective
Requires:       facter
BuildArch:      noarch

%description
mcollective communication plugin for amqp 1.0 enabled qpid broker

%prep
%setup -q

%clean
rm -rf %{buildroot}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/libexec/mcollective/mcollective/agent
mkdir -p %{buildroot}/usr/lib/ruby/site_ruby/1.8/facter
mkdir -p %{buildroot}/etc/cron.minutely
mkdir -p %{buildroot}/usr/libexec/mcollective

cp src/stickshift.rb %{buildroot}/usr/libexec/mcollective/mcollective/agent/
cp src/stickshift.ddl %{buildroot}/usr/libexec/mcollective/mcollective/agent/
cp facts/stickshift_facts.rb %{buildroot}/usr/lib/ruby/site_ruby/1.8/facter/
cp facts/stickshift-facts %{buildroot}/etc/cron.minutely/
cp facts/update_yaml.rb %{buildroot}/usr/libexec/mcollective/

%files
%defattr(-,root,root,-)
/usr/libexec/mcollective/mcollective/agent/stickshift.rb
/usr/libexec/mcollective/mcollective/agent/stickshift.ddl
/usr/lib/ruby/site_ruby/1.8/facter/stickshift_facts.rb
%attr(0700,-,-) /usr/libexec/mcollective/update_yaml.rb
%attr(0700,-,-) /etc/cron.minutely/stickshift-facts
/etc/cron.minutely/stickshift-facts


%changelog
* Thu Aug 16 2012 Adam Miller <admiller@redhat.com> 0.2.2-1
- adding rest api to fetch and update quota on gear group (abhgupta@redhat.com)

* Thu Aug 02 2012 Adam Miller <admiller@redhat.com> 0.2.1-1
- bump_minor_versions for sprint 16 (admiller@redhat.com)

* Wed Aug 01 2012 Adam Miller <admiller@redhat.com> 0.1.6-1
- Glob directories only once to calculate git repos and stopped apps.
  (mpatel@redhat.com)

* Mon Jul 30 2012 Dan McPherson <dmcphers@redhat.com> 0.1.5-1
- Merge pull request #288 from
  kraman/dev/kraman/features/remove_old_mcollective (mrunalp@gmail.com)
- Adding missed updates from when plugin was opensourced (kraman@gmail.com)

* Fri Jul 27 2012 Dan McPherson <dmcphers@redhat.com> 0.1.4-1
- Bug 843757 (dmcphers@redhat.com)
- Merge pull request #287 from mrunalp/bugs/841681 (rmillner@redhat.com)
- Fix for BZ841681. (mpatel@redhat.com)

* Thu Jul 26 2012 Dan McPherson <dmcphers@redhat.com> 0.1.3-1
- US2439: Add support for getting/setting quota. (mpatel@madagascar.(none))

* Tue Jul 24 2012 Adam Miller <admiller@redhat.com> 0.1.2-1
- Add pre and post destroy calls on gear destruction and move unobfuscate and
  stickshift-proxy out of cartridge hooks and into node. (rmillner@redhat.com)
- BROKE THE BUILD (admiller@redhat.com)
- BZ 841681: Make update_yaml single instance and use tmp file for
  generating/updating facts. (mpatel@redhat.com)

* Wed Jul 11 2012 Adam Miller <admiller@redhat.com> 0.1.1-1
- bump_minor_versions for sprint 15 (admiller@redhat.com)

* Wed Jul 11 2012 Adam Miller <admiller@redhat.com> 0.0.5-1
- Fix validation. (mpatel@redhat.com)
- Add missing method to DDL. (mpatel@redhat.com)

* Tue Jul 10 2012 Adam Miller <admiller@redhat.com> 0.0.4-1
- Merge pull request #211 from kraman/dev/kraman/bugs/835489
  (dmcphers@redhat.com)
- Fix to work around a bug in mcollective that doesn't convert string true into
  a boolean anymore. (mpatel@redhat.com)
- Fix stickshift DDL. (mpatel@redhat.com)
- Bugz 835489. Fixing location for district config file and adding in missing
  node_profile_enabled blocks (kraman@gmail.com)

* Mon Jul 09 2012 Dan McPherson <dmcphers@redhat.com> 0.0.3-1
- don't send stickshift logs to debug, instead use info (mmcgrath@redhat.com)

* Tue Jul 03 2012 Adam Miller <admiller@redhat.com> 0.0.2-1
- Automatic commit of package [stickshift-mcollective-agent] release [0.0.1-1].
  (kraman@gmail.com)
- Fix typo and remove dependency. (mpatel@redhat.com)
- MCollective updates - Added mcollective-qpid plugin - Added mcollective-
  gearchanger plugin - Added mcollective agent and facter plugins - Added
  option to support ignoring node profile - Added systemu dependency for
  mcollective-client (kraman@gmail.com)

* Fri Jun 29 2012 Krishna Raman <kraman@gmail.com> 0.0.1-1
- new package built with tito

